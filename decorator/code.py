import time

def timer(func):
    def wrapper(*args):
        before = time.time()
        func()
        print("Function took:",time.time() - before,"seconds")
    
    return wrapper

@timer
def run():
    time.sleep(2)

run()

