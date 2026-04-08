import blog_spider
import threading
import time
## 单线程
def single_thread():
    print("single_thread begin")
    for url in blog_spider.urls:
        blog_spider.craw(url)
        print("single_thread end")
## 多线程
def multi_thread():
    print("multi_thread begin")
    threads = []
    for url in blog_spider.urls:
        # 创建一个线程对象，用来让某个函数在新的线程里并发执行。
        threads.append(
            threading.Thread(target = blog_spider.craw, args = (url, ))
        )
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print("multi_thread begin")
if __name__ == "__main__":
    start = time.time()
    single_thread()
    end = time.time()
    print("single thread cost:", end - start, "seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi thread cost:", end - start, "seconds")
