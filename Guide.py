class MainClass:
    # This is a constructor for MainClass
    def __init__(self, para1, para2, para3):
        self.p1 = para1
        self.p2 = para2
        self.p3 = para3

    # defining a method necessarily needs a self parameter within a class so that the interpreter knows which object's
    # method you're referring to
    def change_para(self, new_para):
        self.p1 = new_para


# Note that when creating an object of the class, with parameters, the "self" is ignored and the first parameter is the
# first value that is taken
u1 = MainClass(1, 2, 3)
u1.change_para(5)
print(f"{u1.p1}")
print(u1.p2)
print(u1.p3)
