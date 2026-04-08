import flask
from concurrent.futures import ProcessPoolExecutor
import math
import json


app = flask.Flask(__name__)

PRIMES = [112272535095293] * 50

# 模拟cpu密集型计算
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

@app.route("/is_prime/<numbers>")
def api_is_prime(numbers):
    number_list = [int(x) for x in numbers.split(",")]
    results = process_pool.map(is_prime, number_list)
    return json.dumps(dict(zip(number_list, results)))

if __name__ == "__main__":
    process_pool = ProcessPoolExecutor()
    app.run()