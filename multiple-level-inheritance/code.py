class Father:
    def __init__(self):
        print("Father")
    def showF(self):
        print("Father Class Method")
class Son(Father):
    def __init__(self):
        print("Son")
    def shows(self):
        print("Son Class Method")

class GrandSon(Son):
    def __init__(self):
        super().__init__()
        print("GrandSon")
    def showG(self):
        print("GrandSon Class Method")

g = GrandSon()