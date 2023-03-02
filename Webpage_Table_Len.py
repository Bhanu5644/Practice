from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ser_obj = Service("C:/Users/BHANU/Documents/chromedriver_win32.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://demo.guru99.com/test/web-table-element.php")
Row = len(driver.find_elements(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr"))
Colume = len(driver.find_elements(By.XPATH,'//*[@id="leftcontainer"]/table/tbody/tr[1]/td'))

print(Row)
print(Colume)
for r in range(2,Row+1):
    for c in range(1,Colume+1):
        Value = driver.find_element(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(Value,end='')
    print()
driver.close()