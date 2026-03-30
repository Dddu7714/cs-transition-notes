import threading
import time

lock = threading.Lock()

class Account:
    def __init__(self, balance):
        self.balance = balance
    
def draw(account, amount):
    ## 给这段代码加互斥锁，保证同一时刻只有一个线程能进入这段取钱逻辑
    with lock:
        # 如果余额大于取钱数目
        if account.balance >= amount:
            time.sleep(0.1)  #加这一句会把问题显现出来，因为sleep会造成当前线程的阻塞，进而切换线程
            print(threading.current_thread().name, 
                "取钱成功")
            account.balance -= amount
            print(threading.current_thread().name,
                "余额", account.balance )
        else:
            print(threading.current_thread().name, 
                "取钱失败，余额不足")
        
if __name__ == "__main__":
    account = Account(1000)
    ta = threading.Thread(name="ta", target=draw, args=(account, 800))
    tb = threading.Thread(name="tb", target=draw, args=(account, 800))

    ta.start()
    tb.start()






