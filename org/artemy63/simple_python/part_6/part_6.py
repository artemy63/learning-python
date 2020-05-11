class Base:
    def __init__(self):
        print("I do not do anything useful")


class SubBase(Base):
    def __init__(self, private_property_value):
        super().__init__()
        print("I have more power than base class")
        self.__private_property = private_property_value

    @property
    def private_property(self):
        print("Inside @property")
        return self.__private_property


bc = Base()
sc = SubBase('top secret')
print(sc.private_property)
print(sc._SubBase__private_property)


class ThreeTypesOfMethods:
    number_of_instances = 0

    def __init__(self):
        print('Init ThreeTypesOfMethods')
        ThreeTypesOfMethods.number_of_instances += 1

    def method_of_instance(self):
        print('Usual method, has "self" reference in signature')
        self.__class__

    @classmethod
    def method_of_class(cls):
        print('method of whole class, has "cls" reference in signature')
        return cls.number_of_instances

    @staticmethod
    def method_without_dependencies():
        print("I'm a static method")


types_of_methods = ThreeTypesOfMethods()
types_of_methods.method_of_class()
types_of_methods.method_of_instance()
ThreeTypesOfMethods.method_without_dependencies()


class Element():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def dump(self):
        print('Current state: name = {} symbol = {} number = {}'
              .format(self.name, self.symbol, self.number))

    def __str__(self):
        'overrides standard behavior of print() function, similar to toString() in Java'
        return 'Element class, current state is :\n name = {} symbol = {} number = {}'\
            .format(self.name, self.symbol, self.number)


init_dict = {'name': 'Hidrogenium', 'symbol': 'H', 'number': 1}
hidrogenium = Element(**init_dict)
hidrogenium.dump()
print(hidrogenium.name)
print(hidrogenium)
