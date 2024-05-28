import json
import os
import re
import shutil
import zipfile
from app.package import Package
from app.artifactrepo import ArtifactRepo


class DependenciesLoader:

    _num_dependencies:int = 0
    _data = {}
    _repo = None
    _dependencies_loaded = False
    _dependencies_json_path = ""

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
        self._set_count()
        f.close()
        self._dependencies_loaded = True
        
        # for printing the correct spelling to the console
        msg_dependencies_word = "dependencies"
        if self._num_dependencies == 1:
            msg_dependencies_word = "dependency"

        self._dependencies_json_path = path

        print(f"{self._num_dependencies} {msg_dependencies_word} loaded from '{path}'.")

    def download(self, repo:str, component_name:str, component_version:str, format:str, download_path:str):
        """
        Downloads an asset from the repo.

            Parameters:
                repo (str): The repo to download from, such as 'nuget-hosted'.
                component_name (str): The name of the package, such as 'AssetFactory.SFX.Ambient.Dark.Hostile'.
                component_version (str): The version of the package, such as '1.0.0'.
                format (str): The format of the package, such as 'nuget'.
                download_path (str): The full path (dir + filename + file extension) of where to save the package locally.
        """

        remote_path = component_name + "/" + component_version
        package_filename = f"{component_name}.{format}"
        self._repo.download(repo, remote_path, download_path)

    def count(self) -> int:
        """
        Returns the total number of packages loaded when calling 'load_metadata()'.

            Raises:
                Exception: in the event that 'load_metadata()' has not been called yet.
        """
        if not self._dependencies_loaded:
            msg = "DependenciesLoader.load_dependencies(path:str) "
            msg += "must be called before calling DependenciesLoader.get_num_dependencies()."
            raise Exception(msg)
        return self._num_dependencies
    
    def _create_unpack_path(self, unpack_path:str) -> str:
        dependencies_json_dir = os.path.dirname(self._dependencies_json_path)
        dependencies_json_dir = os.path.normpath(dependencies_json_dir)
        relative_download_path:str = unpack_path
        if relative_download_path.startswith('.\/'):
            relative_download_path = relative_download_path.lstrip('.')
        relative_download_path = relative_download_path.lstrip('//')
        relative_download_path = os.path.normpath(relative_download_path)
        return os.path.join(dependencies_json_dir, relative_download_path)
    
    def unpack(self, nuget_package_path:str, unpack_dir:str) -> None:
        """
        Unpacks a nuget packaged (.nupkg) by unzipping the package and deleting the 
        _rels/package folders and the [Content_Types].xml file.

            Parameters:
                nuget_package_path (str): the full file path of the nuget package to unpack.
                unpack_dir (str): the directory to unpack the package at.
        """
        with zipfile.ZipFile(nuget_package_path, 'r') as zip_ref:
            zip_ref.extractall(unpack_dir)
        shutil.rmtree(os.path.join(unpack_dir, "_rels"))
        shutil.rmtree(os.path.join(unpack_dir, "package"))
        os.remove(os.path.join(unpack_dir, "[Content_Types].xml"))
    
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

    # for i in range(self._num_dependencies):
    # package = self._data[f"Package{str(i)}"]
    # repo = package["Repository"]
    # remote_path = package["ComponentName"] + "/" + package["ComponentVersion"]

    dl = DependenciesLoader(r"C:\GameDevelopment\unreal-bot\Source\app\repo_config.ini")
    dl.load_metadata(r"C:\GameDevelopment\asset-factory\dependencies.json")
    download_path = os.path.join(os.getcwd(), "tmp", "AssetFactory.SFX.Ambient.Dark.Hostile.nuget",)
    dl.download("nuget-hosted", 
                "AssetFactory.SFX.Ambient.Dark.Hostile",
                "1.0.0",
                "nuget",
                download_path)
    dl.unpack(download_path, r"C:\GameDevelopment\asset-factory\Source\AssetFactory\Content\AssetFactory\SFX\Ambient\Dark")
