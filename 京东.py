from selenium import webdriver
from bs4 import BeautifulSoup
import requests, re
from urllib.parse import quote
import json


# 获取商品最大页
def get_max_page(str_goods):
    url = 'https://gou.jd.com/search?keyword={}&enc=utf-8'.format(str_goods)
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    max_page = soup.select('.f-pager .fp-text i')[0].string
    get_goods_url(max_page, driver, str_goods)


# 获取所有商品的url
def get_goods_url(max_page, driver, str_goods):
    for page in range(1, int(max_page) + 1):
        page_url = 'https://gou.jd.com/search?keyword={}&page={}'.format(str_goods, str(page))
        driver.get(page_url)
        driver.implicitly_wait(10)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        div = soup.select('.pic a')
        for d in div:
            goods_url = 'https://item.jd.com/' + d['href'].split('%2F')[3].split('&')[0]
            get_comment_api_text(goods_url)


# 获取评论接口内容
def get_comment_api_text(goods_url):
    num = goods_url.split('/')[-1].split('.')[0]
    api = 'https://club.jd.com/comment/productPageComments.action?productId={}&score=0&sortType=5&page=0&pageSize=10'.format(
        num)
    res = requests.get(api)
    if not re.match(r'^<!DOCTYPE HTML>', res.text):
        text = res.text
        json_text = json.loads(text)
        get_comment_max_page(json_text, num)


# 获取评论最大页
def get_comment_max_page(text, num):
    sum_comment = text['productCommentSummary']['commentCount']
    sum_page = str(sum_comment / 10).split('.')
    one = int(sum_page[0])
    two = int(sum_page[1])
    if two != 0:
        one = int(sum_page[0]) + 1
        for page in range(0, one + 1):
            api = 'https://club.jd.com/comment/productPageComments.action?productId={}&score=0&sortType=5&page={}&pageSize=10'.format(
                num, str(page))
            get_comment(api)
    else:
        for page in range(0, one + 1):
            api = 'https://club.jd.com/comment/productPageComments.action?productId={}&score=0&sortType=5&page={}&pageSize=10'.format(
                num, str(page))
            get_comment(api)


# 获取评论信息
def get_comment(api):
    res = requests.get(api)
    json_text = json.loads(res.text)
    list = json_text['comments']
    for l in list:
        content = l['content']
        time = l['creationTime']
        nickname = l['nickname']
        level_name = l['userLevelName']
        vote_count = l['usefulVoteCount']
        print(nickname + '---' + level_name + '---' + str(vote_count) + '---' + time + '---' + content)


if __name__ == '__main__':
    goods = input('请输入要查询的商品:')
    str_goods = quote(goods)
    get_max_page(str_goods)
