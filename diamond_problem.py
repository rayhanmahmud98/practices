class Grandma:
    def make_cake(self):
        print("grandmas cake")
        
class Mom(Grandma):
    def make_cake(self):
        print("moms chocolate cake")
        super().make_cake()
        
class Dad(Grandma):
    def make_cake(self):
        print("Dads vanilla cake")
        super().make_cake()
        
class You(Mom,Dad):
    def make_cake(self):
        print("you are making cake")
        super().make_cake()
        
you = You()
you.make_cake()