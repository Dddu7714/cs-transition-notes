"""
案例: 演示通过 self关键字实现 在类内访问其它函数.
需求: 定义汽车类, 类内有run()函数, 并在work()中调用run()函数, 创建该类对象, 调用上述的函数.
"""

# 1. 定义汽车类.
class Car:
    # 属性(名词)

    # 行为(动词)
    # 1.1 run()函数
    def run(self):
        print(f'{self} 汽车在跑...')

    # 1.2 work()函数, 在其内部调用run()
    def work(self):
        print(f'我是work函数, 我的self值: {self}')
        self.run()      # self = 本类当前对象的引用.

# 2.在类外访问Car类的行为(函数)
c1 = Car()
print(f'c1对象: {c1}')
c1.run()        # c1在跑
print('-' * 34)
c1.work()       # c1在work, c1在跑
print('=' * 34) # 分割线

# 3.再次创建对象.
c2 = Car()
print(f'c2对象: {c2}')
c2.run()
print('-' * 34)
c2.work()

# c1对象: <__main__.Car object at 0x00000163CC0DF190>
# <__main__.Car object at 0x00000163CC0DF190> 汽车在跑...
# ----------------------------------
# 我是work函数, 我的self值: <__main__.Car object at 0x00000163CC0DF190>
# <__main__.Car object at 0x00000163CC0DF190> 汽车在跑...
# ==================================
# c2对象: <__main__.Car object at 0x00000163CC0DF1F0>
# <__main__.Car object at 0x00000163CC0DF1F0> 汽车在跑...
# ----------------------------------
# 我是work函数, 我的self值: <__main__.Car object at 0x00000163CC0DF1F0>
# <__main__.Car object at 0x00000163CC0DF1F0> 汽车在跑...