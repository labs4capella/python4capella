include('workspace://Python4Capella/simplified_api/sirius.py')
if False:
    from simplified_api.sirius import *
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *


class CapellaModel():
    def __init__(self, aird_path):
        self.session = load_sirius_session(aird_path)
    def get_system_engineering(self):
        if self.session is None:
            return None
        else:
            return SystemEngineering(getEngineering(self.session))
