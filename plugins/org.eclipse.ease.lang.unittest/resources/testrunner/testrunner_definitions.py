import functools

class timeout(object):

    def __init__(self, timeout):
        self.timeout = timeout        

    def __call__(self, fn):
        @functools.wraps(fn)
        def decorated(*args, **kwargs):
            MOD_org_eclipse_ease_lang_unittest_UnitTestModule.setTestTimeout(self.timeout)
            fn(*args, **kwargs)
            
        return decorated

__name__ = "__ease_unittest__"   
