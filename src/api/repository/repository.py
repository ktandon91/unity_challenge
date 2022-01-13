from abc import abstractmethod
from typing import List

from api.models import Game, OID


class Repository(object):
    @property
    def client(self):
        raise NotImplementedError

    @property
    def db(self):
        raise NotImplementedError

    @abstractmethod
    async def connect(self, path: str):
        pass

    @abstractmethod
    async def close(self):
        pass

    @abstractmethod
    async def get_games(self) -> List[Game]:
        pass

    @abstractmethod
    async def get_game(self, game_id: OID) -> Game:
        pass

    @abstractmethod
    async def add_game(self, game: Game):
        pass

    @abstractmethod
    async def update_game(self, game_id: OID, game: Game):
        pass

    @abstractmethod
    async def delete_game(self, game_id: OID):
        pass
