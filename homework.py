from abc import ABC, abstractmethod
#1
#Можно написать в 10 раз короче, но мне было интересно

class Fibonacci:
    def __init__(self):
        self.instance = False
    def __call__(self, n=0):
        self.n = n
        self.instance = True
        return self
    def __iter__(self):
        if self.instance == False:
            self.__call__()
        self.counter = 0
        self.a = self.b = 1
        return self
    def __next__(self):
        if self.counter == 0 and self.n != 0:
            self.counter += 1
            return self.a
        elif self.counter < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.counter += 1
            return self.a
        else:
            raise StopIteration
fibbonacci = Fibonacci()
for i in fibbonacci(10):
    print(i)

#Вариант повеселее с генератором
def Fibonacci(n):
    a = 1
    b = 1
    counter = 0
    while counter < n:
        yield a
        a, b = b, a + b
        counter += 1
gen = Fibonacci(7)
for i in gen:
    print(i)

#2
def infinity(n):
    s = str()
    for i in range(1,n+1):
        s = s + str(i) + '-'
    for i in range(500):
        yield s
for i in infinity(10):
    print(i, end = '')
print()
#3 Очень занимательная штука
class AbstractBuilder(ABC):
    @abstractmethod
    def make_pizza(self):
        pass
    @abstractmethod
    def define_size(self):
        pass
    @abstractmethod
    def add_cheese(self):
        pass
    @abstractmethod
    def add_pepperoni(self):
        pass
    @abstractmethod
    def add_mushrooms(self):
        pass
    @abstractmethod
    def add_onions(self):
        pass
    @abstractmethod
    def add_becon(self):
        pass
class PizzaBuilder(AbstractBuilder):
    def __init__(self):
        self.make_pizza()

    def make_pizza(self):
        self.pizza = Pizza()

    def product(self):
        product = self.pizza
        self.make_pizza()
        return product

    def define_size(self, x = '30cm'):
        key = 'size'
        self.pizza.add(key, x)
    def add_cheese(self, x = ''):
        key = 'cheese'
        self.pizza.add(key, x)

    def add_pepperoni(self, x = ''):
        key = 'pepperoni'
        self.pizza.add(key, x)

    def add_mushrooms(self, x = ''):
        key = 'mushrooms'
        self.pizza.add(key, x)

    def add_onions(self, x = ''):
        key = 'onions'
        self.pizza.add(key, x)

    def add_becon(self, x = ''):
        key = 'becon'
        self.pizza.add(key, x)

class Pizza:
    def add(self,key, part):
        self.__dict__[key] = part

class PizzaDirector():
    def __init__(self):
        self.make_pizza()

    def make_pizza(self):
        self.builder = PizzaBuilder()
    def product(self):
        return self.builder.product()
    def type1_pizza(self):
        self.builder.define_size()
        self.builder.add_cheese('')
    def type2_pizza(self):
        self.builder.define_size()
        self.builder.add_cheese('')
        self.builder.add_pepperoni('')
        self.builder.add_mushrooms('')
    def type3_pizza(self):
        self.builder.define_size()
        self.builder.add_cheese('')
        self.builder.add_pepperoni('')
        self.builder.add_mushrooms('')
        self.builder.add_onions('')
        self.builder.add_becon('')


builder = PizzaDirector()
builder.type3_pizza()
a = builder.product()
print(a.__dict__)


#4


class AnimalFactory():
    def create_animal(self, i):
        if i.lower() == 'dog':
            a = Dog()
            a.speak()
            return a
        elif i.lower() == 'cat':
            a = Cat()
            a.speak()
            return a

        else:
            print(f'there is no {i} animal')



class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("Dog")
class Cat(Animal):
    def speak(self):
        print("Cat")


factory = AnimalFactory()
factory.create_animal('dog')
factory.create_animal('cat')
factory.create_animal('ct')

#5
class Strategy(ABC):
    @abstractmethod
    def execute(self,x,y):
        pass

class Calculator():
    def __init__(self,strategy: Strategy):
        self.strategy = strategy
    def set_strategy(self,strategy):
        self.strategy = strategy
        return self
    def calculate(self,x,y):
        a = self.strategy.execute(x,y)
        return a

class Addition(Strategy):
    def execute(self, x ,y):
        return x + y
class Subtraction(Strategy):
    def execute(self, x ,y):
        return x - y
class Multiplication(Strategy):
    def execute(self, x ,y):
        return x * y
class Division(Strategy):
    def execute(self, x ,y):
        return x / y

a = Calculator(Addition()).calculate(1,2)
b = Calculator(Subtraction()).calculate(1,2)
print(a)
print(b)
a = Calculator(Addition())
a.set_strategy(Division())
print(a.calculate(1,2))
