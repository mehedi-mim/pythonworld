# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def square_numbers(nums):
    for i in nums:
        yield(i*i)

my_nums = square_numbers([1,2,3,4,5])

print(my_nums) #generator object
for x in my_nums:
    print (x)
#Generator don't hold the entire result in memory rather hold one result at a time
#In case of performance generator is good rather than list