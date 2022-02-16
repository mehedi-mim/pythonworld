# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def my_func(mimi,*args,mim = None,**kwargs):
    print("Arguments: ",mimi,args,mim,kwargs)

my_func("abc","sim",abc = 12,mim = "sim")

def my_random_django_view(request,**kwargs):
    print(request)
    print(kwargs.get('id'))
my_random_django_view("request",id='some_id')

# Good practice positional arguments,keyord arguments