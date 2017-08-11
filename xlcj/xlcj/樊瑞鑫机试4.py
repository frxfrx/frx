from selenium import webdriver
from bs4 import BeautifulSoup
import pymongo


# 获取页面
def get_html(url, driver):
    driver.get(url)
    driver.implicitly_wait(10)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    parse_html(soup)


# 获取所有信息
def parse_html(soup):
    info = soup.find_all('div', class_='col2_right j_threadlist_li_right ')
    print('正在存入数据。。。')
    for i in info:
        author = i.find('div', class_='threadlist_title pull_left j_th_tit ').get_text().strip()
        try:
            content = i.find('div', class_='threadlist_abs threadlist_abs_onlyline ').get_text().strip()
            save_db(author, content)
        except:
            save_db(author, '该用户暂时未发表任何回复！')
    print('数据存入成功！')


# 存数据到mongodb
def save_db(author, content):
    client = pymongo.MongoClient('localhost', 27017)
    db_set = client.tb_db.db_set
    db_set.insert({'用户名': author, '内容': content})


if __name__ == '__main__':
    url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E7%B2%BE%E5%93%81%E8%B4%B4'
    driver = webdriver.PhantomJS()
    get_html(url, driver)