from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


import csv
import pandas as pd
driver = webdriver.Firefox()

# driver = webdriver.Chrome(ChromeDriverManager().install())
import pandas as pd
import time
import os
driver.get('https://www.google.com/search?q=ludhiana+mobile+shop&biw=1301&bih=670&sz=0&tbm=lcl&ei=hjcfYofLG4iF4t4Pp86BuAQ&oq=ludhiana+mobile+shop&gs_l=psy-ab.12...0.0.0.57988.0.0.0.0.0.0.0.0..0.0....0...1c..64.psy-ab..0.0.0....0._ymsZQLQXCM#rlfi=hd:;si:;mv:[[30.927806899999997,75.8587285],[30.895273999999993,75.83704900000001]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:10')

names = []
phone=[]
#
# # for s in p:
# #     names.append(s.text)
# #     s.click()
#     # time.sleep(5)
batch=driver.find_elements(By.CLASS_NAME,'cXedhc')
# # for batches in batch:
# #     batches.click()
# #     time.sleep(5)
p = driver.find_elements(By.CLASS_NAME, 'dbg0pd')
print(len(p))
for ps in p:
    print(ps.text)
    time.sleep(5)
    names.append(ps.text)
for batches in batch:
    batches.click()
    time.sleep(5)
    no = driver.find_elements(By.XPATH,"//div[@class='Z1hOCe']/div[@class='zloOqf PZPZlf']//span[@class='LrzXr zdqRlf kno-fv']/span[@data-dtype='d3ph']")

    for nom in no:
        print(nom.text)
        time.sleep(5)
        phone.append(nom.text)


fields = ['name', 'phone']
with open('new_data1.csv', 'w') as f:
        # using csv.writer method from CSV package
    write = csv.writer(f)
    data=[names,phone]
#
    # write.writerow(fields)
    write.writerows(data)
df = pd.read_csv("new_data1.csv", header=None)
# print(df)
list=df.loc[1]
# print(list)
# list.drop()
c=df.dropna(axis=1)
# print(c)
l=c.loc[1]
import re
new =l.tolist()

new1=[]
for i in new:


    res = re.sub(' +','', i)

    res="+91"+res[1:]

    new1.append(res)


print(new1)
message = "questo è il messaggio"

for i in new1:
    url = "https://web.whatsapp.com/send?phone="+ i + "&text=" + message + "&app_absent=1"
    time.sleep(5)

    # Load Whatsapp Web page
    driver.get(url)
    # time.sleep(5)

    # Wait for the page be loaded
    time.sleep(10)

    enter_action = ActionChains(driver)
    time.sleep(5)
    enter_action.send_keys(Keys.ENTER)
    time.sleep(5)

# Send message
    enter_action.perform()
    time.sleep(5)

# Close browser
driver.close()
