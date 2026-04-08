import queue
import blog_spider
import time
import random
import threading

def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    """
    爬虫线程执行的函数：
    1. 从 url_queue 中取出一个 url
    2. 调用 blog_spider.craw(url) 抓取网页源码
    3. 把抓到的 html 放入 html_queue
    4. 打印当前线程信息和队列状态
    """
    while True:
        # 从 url 队列中取出一个待爬取的网址
        # get() 默认是阻塞的，如果队列为空，线程会在这里等待
        url = url_queue.get()

        # 调用封装好的 craw 方法，获取该 url 对应的网页 HTML
        html = blog_spider.craw(url)

        # 将抓取到的网页源码放入 html_queue
        # 供后面的解析线程继续处理
        html_queue.put(html)

        # 打印当前线程名、正在爬取的 url，以及 url_queue 当前剩余数量
        print(
            threading.current_thread().name,
            f"craw {url}",
            "url_queue.size = ",
            url_queue.qsize()
        )

        # 让线程随机休眠 1~2 秒
        # 模拟人为访问节奏，避免请求过快
        time.sleep(random.randint(1, 2))


def do_parse(html_queue: queue.Queue, fout):
    """
    解析线程执行的函数：
    1. 从 html_queue 中取出网页源码
    2. 调用 blog_spider.parse(html) 解析网页内容
    3. 把解析结果写入文件
    4. 打印当前线程信息和解析结果数量
    """
    while True:
        # 从 html 队列中取出一个网页源码
        # 如果队列为空，同样会阻塞等待
        html = html_queue.get()

        # 调用封装好的 parse 方法，提取网页中的目标数据
        # results 一般是一个列表，例如 [(链接1, 标题1), (链接2, 标题2), ...]
        results = blog_spider.parse(html)

        # 遍历解析结果，并逐行写入输出文件
        for result in results:
            fout.write(str(result) + '\n')

        # 打印当前线程名、解析得到的结果数量，以及 html_queue 当前剩余数量
        print(
            threading.current_thread().name,
            f"result.size = {len(results)}",
            "html_queue.size = ",
            html_queue.qsize()
        )

        # 随机休眠 1~2 秒
        time.sleep(random.randint(1, 2))

if __name__ == "__main__":
    # 创建两个队列：
    # url_queue：存放待爬取的网页 url
    # html_queue：存放已经爬取到的网页源码 html
    url_queue = queue.Queue()
    html_queue = queue.Queue()

    # 把所有待爬取的 url 放入 url_queue
    # blog_spider.urls 一般是提前准备好的 url 列表
    for url in blog_spider.urls:
        url_queue.put(url)

    # 创建 3 个爬取线程
    # target=do_craw 表示线程执行 do_craw 函数
    # args=(url_queue, html_queue) 表示给 do_craw 传入这两个参数
    # name=f"craw{idx}" 是给线程起名字，方便调试时区分
    for idx in range(3):
        t = threading.Thread(
            target=do_craw,
            args=(url_queue, html_queue),
            name=f"craw{idx}"
        )
        t.start()   # 启动线程

    # 以写入模式打开文件，用来保存解析后的结果
    fout = open("02.data.txt", "w", encoding="utf-8")

    # 创建 3 个解析线程
    # target=do_parse 表示线程执行 do_parse 函数
    # args=(html_queue, fout) 表示给 do_parse 传入 html 队列和输出文件对象
    for idx in range(3):
        t = threading.Thread(
            target=do_parse,
            args=(html_queue, fout),
            name=f"parse{idx}"
        )
        t.start()   # 启动线程

