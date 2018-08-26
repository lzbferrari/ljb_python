'''
关于类的分类可以打印出长颈鹿会干什么
'''
class Things:
    pass
class Inanimate(Things):
    pass
class Animate(Things):
    pass
class Sidewalks(Inanimate):
    pass
class Animals(Animate):
    def breathe(self):
        print('breathing')
    def move(self):
        print('moving')
    def eat_food(self):
        print('eating food')
class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')
    pass
class Giraffes(Mammals):
    def dance(self):
        self.lefe_Foot_Forward()
        self.left_Foot_Back()
        self.right_Foot_Forward()
        self.right_Foot_Back()
        self.left_Foot_Back()
        self.right_Foot_Back()
        self.right_Foot_Forward()
        self.left_Foot_Forward()
    def eat_leaves_from_trees(self):
        print('eating leabes')
    def lefe_Foot_Forward(self):
        print('left foot forward')
    def left_Foot_Back(self):
        print('left foot back')
    def right_Foot_Forward(self):
        print('right foot forward')
    def right_Foot_Back(self):
        print('right foot back')
    def left_Foot_Back(self):
        print('left foot back')
    def right_Foot_Back(self):
        print('right foot back')
    def right_Foot_Forward(self):
        print('right foot forward')
    def left_Foot_Forward(self):
        print('left foot forward')
    pass

class ThisIsmMyClass:
    def this_is_a_class_function(self):
        print('I an a class function')
    def this_is_also_a_class_function(self):
        print('I am also a class function. See?')
reginald = Giraffes()
harold = Giraffes()

reginald.dance()

a = Giraffes()
a.eat_food()