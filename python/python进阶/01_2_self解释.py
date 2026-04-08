'''
案例：self关键字介绍
需求：定义汽车类，创建多个该类的函数，看打印结果
'''
# 1. 定义汽车类.
class Car:
      # 属性
  
      # 行为, 跑
      def run(self):
          print('汽车会跑!...')
          print(f'我是run函数, self的值是: {self}')

# 2.创建汽车类的对象.
c1 = Car()
print(f'c1对象:{c1}')   # 和{self}一致    
# 输出：<__main__.Car object at 0x000002025FFDF1F0> 
# __main__.Car → 类名   0x000002025FFDF1F0 → 对象在内存中的地址（十六进制）
print(f'c1对象: {id(c1)}')
# 输出：2209223668208
# 对象在内存中的地址对应的整数（十进制），每次运行可能都不同
# 调用Car#run()
c1.run()
print('-' * 34)

# 3.继续创建汽车类的对象.
c2 = Car()
print(f'c2对象: {c2}')
# 输出：<__main__.Car object at 0x000002025FFDF250>
# 调用Car#run()
c2.run()