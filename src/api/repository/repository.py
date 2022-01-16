from abc import abstractmethod

class Repository():
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
