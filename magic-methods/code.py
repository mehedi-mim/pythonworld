# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Weight:
    def __init__(self,kilos):
        self.kilos = kilos
    def __add__(self,other):
        if type(other) == int:
            return Weight(self.kilos + other)
        return Weight(self.kilos + other.kilos)
    def __radd__(self,other):
        if type(other) == int:
            return Weight(self.kilos + other)
        return Weight(self.kilos + other.kilos)

w1 = Weight(50)
wr = w1 + 10
rw = 10 + w1

print(wr.kilos)
print(rw.kilos)
