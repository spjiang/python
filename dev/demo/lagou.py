##以python岗位为例，运用selenium+Chrome()爬取岗位信息
# coding=UTF-8
from lxml import etree
from selenium import webdriver
import time
import csv

browser = webdriver.Chrome()
browser.get('https://www.lagou.com/jobs/list_PYTHON?px=default&city=%E5%85%A8%E5%9B%BD#filterBox')
browser.implicitly_wait(10)

def get_dates(selector):
        items = selector.xpath('//*[@id="s_position_list"]/ul/li')
        for item in items:
            yield {
                'Name': item.xpath('div[1]/div[1]/div[1]/a/h3/text()')[0],
                'Company': item.xpath('div[1]/div[2]/div[1]/a/text()')[0],
                'Salary': item.xpath('div[1]/div[1]/div[2]/div/span/text()')[0],
                'Education': item.xpath('div[1]/div[1]/div[2]/div//text()')[3].strip(),
                'Size': item.xpath('div[1]/div[2]/div[2]/text()')[0].strip(),
                'Welfare': item.xpath('div[2]/div[2]/text()')[0]
            }
def main():
    i = 0
    for i in range(30):
        selector = etree.HTML(browser.page_source)
        browser.find_element_by_xpath('//*[@id="order"]/li/div[4]/div[2]').click()
        time.sleep(5)
        print('第{}页抓取完毕'.format(i+1))
        for item in get_dates(selector):
            print(item)
        with open('Py.csv', 'a', newline='') as csvfile:  ##Py.csv是文件的保存路径，这里默认保存在工作目录
            fieldnames = ['Name', 'Company', 'Salary', 'Education', 'Size', 'Welfare']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for item in get_dates(selector):
                writer.writerow(item)
        time.sleep(5)
    browser.close()
if __name__=='__main__':
    main()