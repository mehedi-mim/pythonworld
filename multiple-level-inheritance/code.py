class Father:
    def showF(self):
        print("Father Class Method")
class Son(Father):
    def shows(self):
        print("Son Class Method")

class GrandSon(Son):
    def showG(self):
        print("GrandSon Class Method")
