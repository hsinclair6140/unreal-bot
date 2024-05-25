from nexus import Nexus
import configparser

class ArtifactRepo:
    """
    Abstract artifact repository class that provides basic repo functionality, 
    such as upload/download of artifacts.

    Parameters:
        repo_config_path (str) : The full path of the repo config file to load.
    """
    _repo = None

    def __init__(self, repo_config_path:str) -> None:
        config.read(repo_config_path)
        config = configparser.ConfigParser()
        url = config['repo']['url']
        un = config['repo']['un']
        pw = config['repo']['pw']

        self._repo = Nexus(url, un, pw)

    def download(self, repo:str, remote_path:str, download_path:str):
        """
        Download an artifact from the repo. 

        Parameters:
            repo (str) : The name of the repo, such as 'nuget-hosted'.
            remote_path (str) : The path of the artifact, such as 
            'AssetFactory.SFX.Ambient.Dark.Hostile/1.0.0'.
            download_path (str) : The local path to download the artifact 
            to. This should include the package name and extension.
        """
        self._repo.download(repo, remote_path, download_path)
