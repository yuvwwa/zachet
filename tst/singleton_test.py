from singletonnn import Singleton
import unittest

class singleton_test(unittest.TestCase):
  
    #проверка на соответствие 
    
    def test_id_similar(self):

        id1 = Singleton()
        id2 = Singleton()

        print(id1.__id)
        print(id2.__id)

        assert id1.__id == id2.__id

    def test_name_similar(self):
        name1 = Singleton()
        name2 = Singleton()

        print(name1.__name)
        print(name2.__name)

        assert name1.__name == name2.__name

    def test_adress_similar(self):
        adress1 = Singleton()
        adress2 = Singleton()

        print(adress1.__adress)
        print(adress2.__adress)

        assert adress1.__adress == adress2.__adress

    def test_mail_index_similar(self):
        mail1 = Singleton()
        mail2 = Singleton()

        print(mail1.__mail_index)
        print(mail2.__mail_index)

        assert mail1.__mail_index == mail2.__mail_index

