
import json
from pathlib import Path


class BackendBase:
    def init():
        raise Exception("expected overridden function init...")


class Backend:
    def __init__(self, backend: str=None, local_test: bool=None) -> None:
        self._local_test = local_test
        self._config = self.get_config(local_test)
        if backend in self.backends.keys():
            self._backend : BackendBase = self.backends[backend]()
        else:
            raise Exception("Error... backend requested not found..")
        pass
        self._backend

    @property
    def backends(self) -> dict:
        return {
            "sqllite": self._sqllite,
            "todotxt": self._todotxt
        }
    
    @backends.setter
    def backends(self, val):
        raise Exception("Error... Can't set backends...")
    
    def _sqllite(self):
        pass

    def _todotxt(self):
        pass

    def init(self):
        self._backend.init()
        
        # config["db"] = db
        # config["access_token"] = access_token
        # if refresh_token:
        #     config["refresh_token"] = refresh_token
        
        # connection = sqlite3.connect(config["db"])
        # slack_client = WebClient(
        #     token=access_token
        # )

        # write_config(local_test, config)

    def get_config_file(self, is_local: bool = False):
        if is_local:
            Path('.local_env').mkdir(parents=True, exist_ok=True)
            config_file = open('.local_env/config.json', 'w+')
        else:
            Path('~/.slack_todo').mkdir(parents=True, exist_ok=True)
            config_file = open('~/.slack_todo/config.json', 'w+')
        return config_file

    def get_config(self, is_local: bool = False):
        
        config_file = self.get_config_file(is_local)
        config = config_file.readlines()
        if len(config) > 0:
            config = json.loads(config)
        else:
            config = dict()

        config_file.close()
        return config

    def write_config(self, is_local: bool = False, config: dict = None):
        config_file = self.get_config_file(is_local)
        config_file.write(json.dumps(config))
        config_file.close()