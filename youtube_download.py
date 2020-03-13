#! /usr/bin/env python3
# author: Qi Shao

########### load packages ############
from selenium import webdriver
import time
from bs4 import BeautifulSoup


########### 打开hrome ############
driver = webdriver.Chrome(executable_path="/home/sensetime/Desktop/code/anet_dataset/chromedriver")#用chrome浏览器打开
driver.get("https://www.youtube.com/")


########### 窗口最大化 ############
driver.maximize_window()
time.sleep(1)
driver.refresh()


########### 获取cookie ############
cookie = driver.get_cookies()


########### 查询query ############
for query in ['cat', 'dog']:

    ########### 查询query，限制video时长在4分钟以内 ############
    url = 'https://www.youtube.com/results?search_query=' + query + '&sp=EgQQARgB'
    driver.get(url)
    print(query)

    def execute_times(times):
        for i in range(times + 1):
            ########### 解析html ############
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')
            zzr = soup.find_all('a', id="thumbnail")

            ########### 获取video_id ############
            for item in zzr:
                video = item.get("href")
                if video is not None and "/watch?v=" in video:
                    video_id = video.replace('/watch?v=', '')
                    print(video_id)

            ########### 模拟鼠标向下滑动 ############
            js = "var q=document.documentElement.scrollTop=100000000000"
            driver.execute_script(js)
            time.sleep(3)  # 等待页面刷新

    ########### 模拟鼠标向下滑动3次 ############
    execute_times(3)
    time.sleep(1)

########### 退出Chrome ############
driver.quit()