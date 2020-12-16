# coding:utf-8
from key import EMAIL,PASSWORD
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import chromedriver_binary

url = input("starをつける記事のurlを入力 : ")
starNum = int(input("starをつける個数を入力 : "))
username = EMAIL
password = PASSWORD

driver = webdriver.Chrome()

#ログインページを開く
loginUrl= "https://www.hatena.ne.jp/login"
driver.get(loginUrl)

#ログイン
loginUserName = driver.find_element_by_xpath("//*[@id='login-name']")
loginUserName.send_keys(username)

loginPassword = driver.find_element_by_xpath("//*[@id='container']/div/form/div/div[2]/div/input")
loginPassword.send_keys(password)

submitButton = driver.find_element_by_class_name("submit-button")
submitButton.click()
sleep(5)

#入力されたはてなブログのページにとぶ
driver.get(url)
starButton = driver.find_element_by_class_name("hatena-star-add-button")

#入力された回数クリック
for i in range(starNum):
  starButton.click()

sleep(5)