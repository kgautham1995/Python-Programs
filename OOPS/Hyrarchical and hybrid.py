class one:
    def one_1(self):
        print("I am one")
class six():
    def six_6(self):
        print("I am six")
class two(one, six):
    def two_2(self):
        print("I am two")
class three(one):
    def three_3(self):
        print("I am three")
class four(two):
    def four_4(self):
        print("I am four")
class five(three):
    def five_5(self):
        print("I am five")
a=four()
b=five()
a.one_1()
a.two_2()
b.three_3()
a.four_4()
b.five_5()
a.six_6()