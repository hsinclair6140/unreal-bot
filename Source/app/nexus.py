from nexuscli.nexus_config import NexusConfig
from nexuscli.nexus_client import NexusClient
from nexuscli.nexus_http import NexusHttp
from nexuscli.api.repository.base_models.repository import Repository

class Nexus:
    """
    Class wrapper for nexuscli that provides an abstract layer for basic
    interactions with the Nexus artifact repo. 

    Parameters:
        url (str) : The URL of the Nexus repo, such as "http://localhost:8081".
        un (str) : The username to the Nexus repo.
        pw (str) : The password to the Nexus repo.
    """

    _nexus_repository:Repository = None
    _nexus_client:NexusClient = None
    _nexus_http:NexusHttp = None

    def __init__(self, url:str, un:str, pw:str) -> None:
        nexus_config = NexusConfig(url=url, username=un, password=pw)
        self._nexus_client = NexusClient(nexus_config)
        self._nexus_http = NexusHttp(nexus_config)

    def download(self, repo:str, remote_path:str, download_path:str):
        """
        Download an artifact from the Nexus repo. 

        Parameters:
            repo (str) : The name of the repo, such as 'nuget-hosted'.
            remote_path (str) : The path of the artifact, such as 
            'AssetFactory.SFX.Ambient.Dark.Hostile/1.0.0'.
            download_path (str) : The local path to download the artifact 
            to. This should include the package name and extension.
        """
        self._nexus_repository=Repository(name=repo,nexus_client=self._nexus_client, nexus_http=self._nexus_http)
        self._nexus_repository.download(remote_path, download_path, flatten=True)
