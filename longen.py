import undetected_chromedriver as uc
driver=uc.Chrome()
import time
driver.implicitly_wait(10)
driver.get('https://www.jd.com')
driver.get('https://item.jd.com/10083857953496.html')
# driver.find_element('xpath',"//img[@width='220' and @data-img='1']").c

time.sleep(10)
title_id=[]
title=driver.find_element('xpath',"//div[@class='sku-name']")
title_id.append(title.text)
price_id=[]
price=driver.find_element('xpath',"//span[@class='p-price']")
price_id.append(price.text)
color_id=[]
color=driver.find_elements('xpath',"//div[@id='choose-attr-1']/div/div")
for item in color:
    color_id.append(item.text)
size_id=[]
size=driver.find_elements('xpath',"//div[@id='choose-attr-2']/div/div")
for item in size:
    size_id.append(item.text)
time.sleep(10)
sku_id=[]
sku=driver.find_element('xpath',"//li[@title='猎豹1.0']")

sku_id.append(sku.text)
detail_id=[]
detail=driver.find_element('xpath',"//div[@class='detail']")

detail_id.append(detail.text)
img_url_id=[]
img_url=driver.find_element('xpath',"//p/img[1]")
img_url_id.append(img_url)
all=[]
t=zip(title_id,price_id,color_id,size_id,sku_id,detail_id,img_url_id)
for item in t:
    all.append(item)
import json

with open('data.json','w') as f:
    f.write(json.dumps(all))
# 2.算法
import random
target=random.randint(-109,109)
print(target)
nums=[]
for i in range(5):
    nums.append(random.randint(2,104))
print(nums)
if nums[0]+nums[1]==target:
    print([0,1])
#2elt测试文件
import pandas as pd
df=pd.read_csv(r'C:\Users\zhanghao\Desktop\__MACOSX\item\._column_mapping.propties',encoding='utf-8')
print(df)
df1=pd.read_csv(r'C:\Users\zhanghao\Desktop\__MACOSX\item\._JD_00001_导出SPU_2023_09_12_0.csv',encoding='utf-8')
print(df1)


