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
     