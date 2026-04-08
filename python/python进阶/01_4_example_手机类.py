'''
案例： 定义手机类，能开机、关机、拍照
'''

# 1.定义手机类
class Phone:
    # 属性

    # 1.1 开机
    def open(self):
        print(f'{self}手机开机')
    # 1.2 关机
    def close(self):
        print(f'{self}手机关机')
    # 1.3 拍照
    def take_photo(self):
        print(f'{self}手机拍照')

# 2. 创建手机类
p1 = Phone()
print(f'p1对象:{p1}')
p1.open()
p1.take_photo()
p1.close()

print('-' * 34)

# 3. 继续创建手机类
p2 = Phone()
print(f'p2对象:{p2}')
p2.open()
p2.take_photo()
p2.close()

