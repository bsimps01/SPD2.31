# By Kami Bigdely
# PEP8 - whitespaces and variable names.
class pizza:
    def __init__ (self, my_bread_type,cheese_type,meat_type,
                    toppings,size):
        self.my_bread_type= my_bread_type
        self.cheese_type = cheese_type
        self.meat_type= meat_type
        self.toppings = toppings
        self.size = size

    @classmethod
    def Create_ChicagoPizza (my_bread_type, cheese_type, meat_type, 
                            toppings, size):
        my_bread_type = 'deep-dish bread'
        cheese_type = 'mozzarella cheese'
        meat_type = 'Italian sausage'
        toppings = ['green bell pepper','mushroom', 'chunky tomato sauce', 'onion']
        return pizza(my_bread_type, cheese_type, meat_type, toppings, size) 

    @classmethod
    def createCalifornia_pizza(my_bread_type, cheese_type, meat_type, 
                                toppings, size):
        my_bread_type = 'thin crust'
        cheese_type = 'feta cheese'
        meat_type = 'roasted chicken'
        toppings = ['garlic', 'spinach', 'broccoli', 'olives', 'red onion', 'red bell pepper' ]
        return pizza(my_bread_type, cheese_type, meat_type, toppings, size) 

    def printInfo(self):
        print('bread type is: ', self.my_bread_type)
        print('cheese type is: ', self.cheese_type)
        print('meat type is: ', self.meat_type)
        print('Toppings are: ', end='')
        print(', '.join(map(str, self.toppings)))

    
myPizza = pizza.createCalifornia_pizza('deep dish', 'mozzarella', 'chicken', 'large')
myPizza.printInfo()