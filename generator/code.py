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


from pkg_resources import yield_lines
import mem_profile
import random
import time

names = ['A','B','C','D']
majors = ['Math','Bangla','English']

print ('Memory (Bofore): Mb'.format(mem_profile.meory_usage_resource()))


def people_list(num_people):
    result = []
    for i in xrange(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result

def people_generator(num_people):
    for i in xrange(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield(person)

t1 = time.clock()
people = people_list(1000000)
t2 = time.clock()

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()

print('Memeory (After) : {} Mb'.format(mem_profile.meory_usage_resource()))
print('Took {} Seconds'.format(t2-t1))