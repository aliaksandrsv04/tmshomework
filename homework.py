from dataclasses import dataclass

#1
class Good:
    def __init__(self, productname='', shopname='', price=0):
        self.productname = productname
        self.shopname = shopname
        self.price = price
    def __repr__(self):
        return f'-{ self.productname},{ self.shopname},{self.price}-'
product1 = Good('bee','shop1',40)
product2 = Good('apple','shop2',10)
product3 = Good('peer','shop3',20)
product4 = Good('queen','shop4',20)
class Storage:
    def __init__(self, *args):
        self.mylist = []
        for i in args:
            self.mylist.append(i)
    def __repr__(self):
        return f'{self.mylist}'
    def __getitem__(self, item):
        return self.mylist[item]
    def info_by_name(self,name):
        for i in self.mylist:
            if i.productname == name:
                print(i.shopname,  i.price)
                break
    def sort_by (self, method:str):
        if method == 'name':
            for i in range(len(self.mylist)-1):
                for k in range(1,len(self.mylist)-i):
                    if self.mylist[k].productname < self.mylist[k-1].productname:
                        self.mylist[k-1], self.mylist[k] = self.mylist[k], self.mylist[k-1]
            for i in self.mylist:
                print(i)
        elif method == 'shop':
            for i in range(len(self.mylist)-1):
                for k in range(1,len(self.mylist)-i):
                    if self.mylist[k].shopname < self.mylist[k-1].shopname:
                        self.mylist[k-1], self.mylist[k] = self.mylist[k], self.mylist[k-1]
            for i in self.mylist:
                print(i)
        elif method == 'price':
            for i in range(len(self.mylist)-1):
                for k in range(1,len(self.mylist)-i):
                    if self.mylist[k].price < self.mylist[k-1].price:
                        self.mylist[k-1], self.mylist[k] = self.mylist[k], self.mylist[k-1]
            for i in self.mylist:
                print(i)
    def __add__(self, other):
        mylist = []
        if len(self.mylist) == len(other.mylist):
            for i in range(len(self.mylist)):
                mylist.append(self.mylist[i].price + other.mylist[i].price)
        else:
            raise ValueError
        return mylist
storage = Storage(product2,product1,product4, product3)
storage.info_by_name('2')
storage.sort_by('price')
storage2 = Storage(product1,product2,product3,product4)
print(storage + storage2)
print(storage)

#2

class EleBeeError(Exception):
    def __init__(self):
        print('EleBzzzz Error')
@dataclass
class BeePhant:
    bee: int
    elephant: int
    @staticmethod
    def number(bee,elephant):
        if not 0<=bee<=100 or not 0<=elephant<=100:
            raise EleBeeError
    def fly(self):
        if self.bee >= self.elephant:
            return True
        else:
            return  False
    def trumpet(self):
       if self.bee <= self.elephant:
           return 'tu-tu-doo-doo'
       else:
           return 'wzzzz'
    def eat(self, meal, value):
        approve = ['nectar', 'grass']
        if meal not in approve:
            raise EleBeeError
        elif meal == approve[0]:
            self.elephant -= value
            self.bee += value
        else:
            self.elephant += value
            self.bee -= value
        if BeePhant.number(self.bee,self.elephant):
            raise EleBeeError
    def __post_init__(self):
        BeePhant.number(self.bee,self.elephant)

beeel = BeePhant(0,0)
beeel.eat('nectar',200)
print(beeel.elephant)

#3
from dataclasses import dataclass, field
class IvanovError(Exception):
    pass
surnames = [
    "Иванов",
    "Петров",
    "Сидоров",
    "Смирнов",
    "Кузнецов",
    "Попов",
    "Васильев",
    "Соколов",
    "Михайлов",
    "Новиков"
]

dict_surnames = {i+1: surnames[i] for i in range(len(surnames))}
print(dict_surnames)

@dataclass
class Bus:
    speed: int = 80
    max_place: int = 10
    surnames_list: list = field(default_factory = lambda: surnames.copy())
    any_free_places: bool = False
    dict_places: dict = field(default_factory = lambda: dict_surnames.copy())
    def boarding(self,surnames:list,operator: str):
        try:
            if operator == '-' and len(self.surnames_list) >= len(surnames):
                surnames_copy = surnames.copy()
                for i in surnames:
                    try:
                        self.surnames_list.remove(i)
                    except:
                        pass
                for i,k in self.dict_places.items():
                    if k in surnames_copy:
                        self.dict_places[i] = None
                        surnames_copy.remove(k)
                if len(self.surnames_list) != self.max_place:
                    self.any_free_places = True
                else:
                    self.any_free_places = False
            elif operator == '+' and self.any_free_places == True and self.max_place - len(self.surnames_list) >= len(surnames):
                surnames_copy = surnames.copy()
                for i in surnames:
                    try:
                        self.surnames_list.append(i)
                    except:
                        pass
                for i,k in self.dict_places.items():
                    if k == None and surnames_copy != []:
                        self.dict_places[i] = surnames_copy[0]
                        surnames_copy.pop(0)
                if len(self.surnames_list) != self.max_place:
                    self.any_free_places = True
                else:
                    self.any_free_places = False
            else:
                raise IvanovError
        except:
            raise IvanovError
        finally:
            print(self)
    def speedlimit(self, value, str1: str):
        if str1 == '+':
            self.speed +=value
        elif str1 == '-':
            self.speed -= value
        else:
            raise IvanovError
    def __contains__(self, item):
        return item in self.surnames_list
    def __iadd__(self, other:str):
        if len(self.surnames_list) != self.max_place:
            self.surnames_list.append(other)
            if len(self.surnames_list) == self.max_place:
                self.any_free_places = False
            else:
                self.any_free_places = True
            for i, k in self.dict_places.items():
                if k == None:
                    self.dict_places[i] = other
                    break
            return self
        else:
            raise IvanovError
    def __isub__(self, other:str):
        if len(self.surnames_list) != []:
            try:
                self.surnames_list.remove(other)
            except:
                raise IvanovError
            if len(self.surnames_list) == self.max_place:
                self.any_free_places = False
            else:
                self.any_free_places = True
            for i, k in self.dict_places.items():
                if k == other:
                    self.dict_places[i] = None
                    break
            return self
        else:
            raise IvanovError

happybus = Bus()
happybus.boarding(["Иванов","Петров","Сидоров","Смирнов","Кузнецов","Попов","Васильев","Соколов","Михайлов","Новиков"], '-')
happybus.boarding(['Иванов',"Петров","Сидоров","Смирнов","Кузнецов","Попов","Васильев","Соколов"],'+')
happybus += 'Свиридов'
print(happybus)
happybus -= 'Свиридов'
print(happybus)
print('hello')