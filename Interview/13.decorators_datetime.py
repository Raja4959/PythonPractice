import time
from datetime import datetime


def param_dec(thr: int):
    def dec(func):
        def wrapper(*args, **kwargs):
            st = datetime.now()
            func()
            ed = datetime.now()
            diff = ed-st
            if diff > thr:  # and func.__name__ = :
                print("time taken to execute the function ", diff)
            return
        return wrapper
    return dec


@param_dec(thr=5000)
def action():
    for i in range(10000):
        time.sleep(0.00001)
        continue


@param_dec(thr=10000)
def sec_act():
    time.sleep(2)
    return
