import concurrent.futures
import blog_spider

# craw
# 创建一个线程池并命名pool，with表示这段代码执行完后，线程池会自动关闭和回收资源
with concurrent.futures.ThreadPoolExecutor() as pool:
    # 把urls交给函数craw
    htmls = pool.map(blog_spider.craw, blog_spider.urls)
    # zip把一一对应的url和html捆绑打包为元组，再用list变成列表[(url1, html1), (url2, html2)..]
    htmls = list(zip(blog_spider.urls, htmls))
    for url, html in htmls:
        print(url, len(html))

print("craw over")

# parse
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        # 任务提交给线程池后，任务不一定立刻完成，线程池先返回一个 future 对象
        # submit一次提交一个对象
        future = pool.submit(blog_spider.parse, html)
        futures[future] = url
    
    # 按任务提交顺序取结果
    #for future, url in futures.items():
        # 取出这个任务最终执行完成后的返回值，如果任务还没执行完，程序会在这里等待，直到任务完成
    #    print(url, future.result())

    # 按完成顺序处理
    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        print(url, future.result())













