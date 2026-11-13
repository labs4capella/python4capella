"""Exercise EASE's import hook without an Eclipse runtime."""
import importlib
import sys
import unittest
from pathlib import Path
from unittest.mock import Mock


class EASEImporterTests(unittest.TestCase):
    def setUp(self):
        self.saved_modules = {name: module for name, module in sys.modules.copy().items()
                              if name == 'eclipse' or name.startswith('eclipse.')}
        for name in self.saved_modules:
            del sys.modules[name]
        self.saved_meta_path = sys.meta_path[:]
        self.addCleanup(self.restore_imports)
        source = Path(__file__).resolve().parents[2] / 'plugins/org.eclipse.ease.lang.python/pysrc/pep302.py'
        namespace = {}
        exec(compile(source.read_text(), str(source), 'exec'), namespace)
        self.finder = sys.meta_path[-1]
        self.finder.is_module_path = Mock(side_effect=lambda name: name in ('eclipse', 'eclipse.tools'))
        self.code = {'eclipse.unittest': 'value = 42',
                     'eclipse.tools.example': 'from eclipse.unittest import value'}
        self.finder.is_module = Mock(side_effect=lambda name: name in self.code)
        self.finder.get_code = Mock(side_effect=lambda name: self.code[name])

    def restore_imports(self):
        sys.meta_path[:] = self.saved_meta_path
        for name in list(sys.modules):
            if name == 'eclipse' or name.startswith('eclipse.'):
                del sys.modules[name]
        sys.modules.update(self.saved_modules)

    def test_test_runner_import(self):
        namespace = {}
        exec('import eclipse.unittest as easeunit', namespace)
        module = namespace['easeunit']
        self.assertEqual(42, module.value)
        self.assertEqual('eclipse', module.__package__)
        self.assertEqual('eclipse.unittest', module.__spec__.name)
        self.assertIs(self.finder, module.__loader__)
        self.assertIs(module, sys.modules['eclipse'].unittest)
        self.assertEqual([], sys.modules['eclipse'].__path__)
        self.assertIsNotNone(sys.modules['eclipse'].__spec__.submodule_search_locations)

    def test_nested_package_and_relative_import(self):
        self.code['eclipse.tools.example'] = 'from ..unittest import value'
        module = importlib.import_module('eclipse.tools.example')
        self.assertEqual(42, module.value)
        self.assertEqual('eclipse.tools', module.__package__)

    def test_cached_import_and_reload(self):
        module = importlib.import_module('eclipse.unittest')
        self.assertIs(module, importlib.import_module('eclipse.unittest'))
        self.finder.get_code.assert_called_once_with('eclipse.unittest')
        self.code['eclipse.unittest'] = 'value = 43'
        self.assertIs(module, importlib.reload(module))
        self.assertEqual(43, module.value)

    def test_missing_module_is_not_cached(self):
        with self.assertRaises(ModuleNotFoundError):
            importlib.import_module('eclipse.missing')
        self.assertNotIn('eclipse.missing', sys.modules)

    def test_failed_module_is_removed_and_can_be_retried(self):
        self.code['eclipse.unittest'] = 'raise RuntimeError("module failed")'
        with self.assertRaisesRegex(RuntimeError, 'module failed'):
            importlib.import_module('eclipse.unittest')
        self.assertNotIn('eclipse.unittest', sys.modules)
        self.code['eclipse.unittest'] = 'value = 44'
        self.assertEqual(44, importlib.import_module('eclipse.unittest').value)

    def test_non_ease_import_is_not_claimed(self):
        self.assertIsNone(self.finder.find_spec('json'))
        self.finder.is_module_path.assert_not_called()
        self.finder.is_module.assert_not_called()

    def test_legacy_loader_remains_available(self):
        self.assertIs(self.finder, self.finder.find_module('eclipse'))
        package = self.finder.load_module('eclipse')
        module = self.finder.load_module('eclipse.unittest')
        self.assertEqual([], package.__path__)
        self.assertEqual(42, module.value)


if __name__ == '__main__':
    unittest.main()
