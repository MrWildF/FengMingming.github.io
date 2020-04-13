from selenium import webdriver
import time
import re
import pandas as pd
driver=webdriver.Chrome()#√
option = webdriver.ChromeOptions()#可以不要
option.add_argument("--user-data-dir="+r"C:/Users/Mr.Gent/AppData/Local/Google/Chrome/User Data/")#可以不要
driver = webdriver.Chrome(chrome_options=option) #加载chrome的插件，括号里的不要
driver.get("https://www.tianyancha.com/company/3018009943")
time.sleep(10)#留给登录的时间
with open (r'D:\python\重组网\公司信息\宣告破产cq.txt','r',encoding='utf-8') as f:
    #encoding='gbk'
    lines = f.readlines()
    tags0 = []
    money0 = []
    time0 = []
    type0 = []
    profession0 = []
    staffs0 = []
    range0 = []
    line0 = []
    for line in lines:
        try:
            driver.switch_to.window(driver.window_handles[0])
            element = driver.find_element_by_id("header-company-search")
            element.clear()
            element.send_keys(line)
            #sreach_window=driver.current_window_handle
            driver.find_element_by_css_selector('#web-content > div > div.container-left > div.search-block.header-block-container > div.result-list.sv-search-container > div:nth-child(1) > div > div.content > div.header > a').click()
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(3)
            tags1 = driver.find_element_by_css_selector('#company_web_top > div.box.-company-box > div.content > div.tag-list-content').text
            money = driver.find_element_by_css_selector('#_container_baseInfo > table.table.-striped-col.-border-top-none.-breakall > tbody > tr:nth-child(1) > td:nth-child(2) > div').text
            time1 = driver.find_element_by_css_selector('#_container_baseInfo > table.table.-striped-col.-border-top-none.-breakall > tbody > tr:nth-child(2) > td:nth-child(2) > div').text
            type1 = driver.find_element_by_css_selector('#_container_baseInfo > table.table.-striped-col.-border-top-none.-breakall > tbody > tr:nth-child(5) > td:nth-child(2)').text
            profession1 = driver.find_element_by_css_selector('#_container_baseInfo > table.table.-striped-col.-border-top-none.-breakall > tbody > tr:nth-child(5) > td:nth-child(4)').text
            staffs = driver.find_element_by_css_selector('#_container_baseInfo > table.table.-striped-col.-border-top-none.-breakall > tbody > tr:nth-child(8) > td:nth-child(2)').text
            range1 = driver.find_element_by_css_selector('#_container_baseInfo > table.table.-striped-col.-border-top-none.-breakall > tbody > tr:nth-child(11) > td:nth-child(2)').text
            tags0.append(tags1)
            money0.append(money)
            time0.append(time1)
            type0.append(type1)
            profession0.append(profession1)
            staffs0.append(staffs)
            range0.append(range1)
            line0.append(line)
            driver.close()
        except Exception as e :
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(3)
            tags0.append(0)
            money0.append(0)
            time0.append(0)
            type0.append(0)
            profession0.append(0)
            staffs0.append(0)
            range0.append(0)
            line0.append(line)
            driver.close()
        continue
df = pd.DataFrame({'公司':line0,'标签':tags0,'类型':type0,'行业':profession0,'资金':money0,'成立时间':time0,'员工数':staffs0,'范围':range0})
df.to_excel(r'D:\python\重组网\公司信息\宣告破产cq1.xlsx')
driver.close()