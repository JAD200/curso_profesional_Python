from datetime import datetime


def execution_time(func):
    # Those paraments are for diferent arguments that the function may have
    def wrapper(*args, **kwargs):#? "*args": arguemnts and "**kwargs": keyword arguments
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('Pasaron ' + str(time_elapsed.total_seconds()) + ' segundos')
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 1000000):# "_" it's an empty variable
        pass

@execution_time
def suma(a: int, b:int) -> int:
    return a + b

def run():
    suma(5 , 5)
    random_func()


if __name__ == '__main__':
    run()