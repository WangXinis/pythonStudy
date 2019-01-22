from selenium import webdriver
browser = webdriver.Chrome()# executable_path后面跟的是chromedriver的绝对路径
# url="http://www.baidu.com"
url='http://www.zhihu.com/settings/account'
browser.get(url)
print(browser.page_source)
# browser.close()





# from selenium import webdriver
# browser = webdriver.Chrome()# executable_path后面跟的是chromedriver的绝对路径
# browser.get("http://www.taobao.com")
# input_first = browser.find_element_by_id("q")
# input_second = browser.find_element_by_css_selector("#q")
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first)
# print(input_second)
# print(input_third)
# browser.close()


# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)