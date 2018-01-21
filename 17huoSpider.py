# -*- coding: utf-8 -*-
"""
Created on 2017/11/20 10:02

@author: Carl
"""

from selenium import webdriver
import  time

browser=webdriver.Chrome()
browser.set_page_load_timeout(30)
browser.get('http://www.17huo.com/?mod=search&sq=2&keyword=%E7%BE%8A%E6%AF%9B&page=2')
page_info=browser.find_element_by_css_selector('body>div.wrap>div.pagem.product_list_pager>div.page_count')
print(page_info.text)
pages=int(page_info.text.split(' ')[1])

for page in range(pages):
    if page>1:break
    url='http://www.17huo.com/?mod=search&sq=2&keyword=%E7%BE%8A%E6%AF%9B&page='+str(page)
    browser.get(url)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    #goods=browser.find_element_by_css_selector("body>div.wrap>div>div.p_main>ul.item").find_elements_by_tag_name('li')
    goods = browser.find_elements_by_css_selector("body>div.wrap>div>div.p_main>ul.item>li")
    print('%d页有%d件商品' % ((page + 1), len(goods)),type(goods))
    for good in goods:
        try:
            name=good.find_element_by_css_selector('a>p.item_title').text
            price=good.find_element_by_css_selector('a>span.txt_nowprice').text
            print(name,price)
        except:
            print(good.text)