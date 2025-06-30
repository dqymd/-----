# -*- coding: utf-8 -*-
"""
豆瓣电影Top250爬虫
-------------------
抓取豆瓣电影Top250的电影名称和评分，并保存为CSV文件。
"""

import requests  # 用于发送网络请求
from bs4 import BeautifulSoup  # 用于解析HTML页面
import csv  # 用于保存CSV文件
import time  # 用于延时，防止被封禁

# 豆瓣Top250页面的基础URL
BASE_URL = "https://movie.douban.com/top250"
# 请求头，伪装成浏览器，防止被反爬
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

def fetch_movies():
    """
    抓取豆瓣Top250所有电影的名称和评分
    返回：电影信息的列表，每个元素是字典{'title':..., 'rating':...}
    """
    movies = []
    # Top250分10页，每页25部电影
    for start in range(0, 250, 25):
        url = f"{BASE_URL}?start={start}"
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code != 200:
            print(f"获取第{start+1}页失败，状态码：{resp.status_code}")
            continue
        soup = BeautifulSoup(resp.text, 'html.parser')
        items = soup.find_all('div', class_='item')
        for item in items:
            # 电影标题
            title_tag = item.find('span', class_='title')
            title = title_tag.text.strip() if title_tag else 'N/A'
            # 电影评分
            rating_tag = item.find('span', class_='rating_num')
            rating = rating_tag.text.strip() if rating_tag else 'N/A'
            movies.append({'title': title, 'rating': rating})
        print(f"已抓取{start+25}部电影...")
        time.sleep(1)  # 每抓一页暂停1秒，防止被封禁
    return movies

def save_to_csv(movies, filename='douban_top250.csv'):
    """
    将电影信息保存到CSV文件
    movies: 电影信息列表
    filename: 保存的文件名
    """
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'rating'])
        writer.writeheader()
        writer.writerows(movies)
    print(f"已保存到 {filename}")

if __name__ == "__main__":
    # 主程序入口
    movies = fetch_movies()  # 抓取数据
    save_to_csv(movies)      # 保存数据 