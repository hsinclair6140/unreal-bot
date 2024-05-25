class Package:
  
    def __init__(self, 
                repository = "", 
                format = "", 
                component_name = "", 
                component_version = "", 
                unpack_path = ""):
        self.repository = repository
        self.format = format
        self.component_name = component_name
        self.component_version = component_version
        self.unpack_path = unpack_path

    def set_repository(self, repository):
        self.repository = repository

    def set_format(self, format):
        self.format = format

    def set_component_name(self, component_name):
        self.component_name = component_name

    def set_component_version(self, component_version):
        self.component_version = component_version

    def set_unpack_path(self, unpack_path):
        self.unpack_path = unpack_path