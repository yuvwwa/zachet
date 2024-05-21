#1 задача
class Singleton:

    __id = None
    __name = None
    __adress = None 
    __mail_index = None

    def __new__(cls, *args, **kwargs):
        if cls.__instances is None:
            cls.__instances = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instances

    @property
    def id(self) -> int:
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id  = id


    @property 
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def adress(self) -> str:
        return self.__adress
    @adress.setter
    def adress(self, adress: str):
        self.__adress = adress


    @property
    def mail_index(self) -> int:
        return self.__mail_index
    @mail_index.setter
    def mail_index(self, mail_index: int):
        self.__mail_index = mail_index
