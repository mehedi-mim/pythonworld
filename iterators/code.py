nums =  [1,2,3]
# print(dir(nums))
i_nums = iter(nums)
print(next(i_nums))
while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break

        
class Test:
 
    # Constructor
    def __init__(self, limit):
        self.limit = limit
 
    # Creates iterator object
    # Called when iteration is initialized
    def __iter__(self):
        self.x = 10
        return self
 
    # To move to next element. In Python 3,
    # we should replace next with __next__
    def __next__(self):
 
        # Store current value ofx
        x = self.x
 
        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration
 
        # Else increment and return old value
        self.x = x + 1;
        return x
 
# Prints numbers from 10 to 15
for i in Test(15):
    print(i)
 
# Prints nothing
for i in Test(5):
    print(i)
