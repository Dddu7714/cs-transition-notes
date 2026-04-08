import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}, cost {end - start} seconds")
        return result
    return wrapper

PRIMES = [112272535095293] * 50

# 判断一个数是否是素数
def is_prime(n):
    if n < 2:
        return False
    if n ==2:
        return True
    if n % 2 == 0:
        return False
    # 求n的平方根并向下取整
    sqrt_n = int(math.floor(math.sqrt(n)))
    # 非质数一定能写成两数乘积，且一个比平方根大一个比平方根小
    # step为2，因为前面已经检查过偶数了
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

## 单线程
@timer
def single_thread():
    for number in PRIMES:
        is_prime(number)

## 多线程
@timer
def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)

## 多进程
@timer
def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


'''
if __name__ == "__main__":
    start = time.time()
    single_thread()
    end = time.time()
    print("single_thread, cost", end - start, "seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi_thread, cost", end - start, "seconds")

    start = time.time()
    multi_process()
    end = time.time()
    print("multi_process, cost", end - start, "seconds")
'''
if __name__ == "__main__":
    single_thread()
    multi_thread()
    multi_process()
