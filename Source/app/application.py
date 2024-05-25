from app.dependenciesloader import DependenciesLoader

class Application:
    
    def setup(dependencies:str):
        dl = DependenciesLoader()
        dl.load_dependencies(dependencies)
        num_dependencies = dl.get_num_dependencies()
        print(f"{num_dependencies} dependencies loaded from {dependencies}.")
