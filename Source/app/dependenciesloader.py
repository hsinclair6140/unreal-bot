import json
import os
import re
from app.package import Package
from .artifactrepo import ArtifactRepo


class DependenciesLoader:

    _num_dependencies:int = 0
    _data = {}
    _repo = None
    _dependencies_loaded = False

    def __init__(self, repo_config:str) -> None:
        self._exists(repo_config)
        self._repo = ArtifactRepo(repo_config)

    def load_metadata(self, path:str) -> None:
        """
        Loads a dependencies.json file. 

            Parameters:
                path (str): The full path with filename of the file to load.

            Raises:
                FileExistsError if the file does not exist.
        """

        self._exists(path)
        f = open(path)
        self._data = json.load(f)
        self._set_num_dependencies()
        f.close()
        self._dependencies_loaded = True

    def download(self):
        # NAME_OF_REPOSITORY = "nuget-hosted"
        # NEXUS_REMOTH_PATH = "AssetFactory.SFX.Ambient.Dark.Hostile/1.0.0"
        # LOCAL_PATH_TO_SAVE_FILE = r"C:\Users\hsinc\Downloads\AssetFactory.SFX.Ambient.Dark.Hostile.nupkg"
        for i in range(self._num_dependencies):
            package = self._data[f"Package{str(i)}"]
            self._repo.download(package["Repository"], package["ComponentName"], package["UnpackPath"])


    def count(self) -> int:
        if not self._dependencies_loaded:
            msg = "DependenciesLoader.load_dependencies(path:str) "
            msg += "must be called before calling DependenciesLoader.get_num_dependencies()."
            raise Exception(msg)
        return self._num_dependencies
    
    def _set_count(self) -> None:
        self._num_dependencies = 0
        for item in self._data: 
            mtch = re.search("Package(.*)", item)
            if mtch != None:
                package_num = mtch.group(1)
                self._num_dependencies += 1

    def _exists(self, path:str) -> str:
        """
        Checks if the file exists. If the path is absolute and does not exist, the 
        relative path will be checked. If the file is found from the relative path,
        the relative path will be converted to absolute and this new path will
        be returned.

        Raises:
            FileExistsError: if the file does not exist.
            
        Returns:
            If the file is found, returns the absolute path of the file.
        """
        if not os.path.exists(path):
            # if file does not exist, attempt to get relative path and see if that exists...
            path = os.path.join(os.getcwd(), path)
            # if the file still does not exist, throw error.
            raise FileExistsError(f"The file '{path}' does not exist.")
        return path

if __name__ == "__main__":

    
    dl = DependenciesLoader(r"C:\GameDevelopment\unreal-bot\Source\app\repo_config.ini")