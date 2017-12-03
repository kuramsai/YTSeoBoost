from random import randint
from TorCtl import TorCtl
import urllib2
from selenium import webdriver
import selenium
import time
import random

lines = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
         "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
         "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5",
         "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
         "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5",
         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"]
user_agent =random.choice(lines)
print user_agent

xyz = '' 
def request(url1):
	try:
		fp = webdriver.FirefoxProfile()
		# Direct = 0, Manual = 1, PAC = 2, AUTODETECT = 4, SYSTEM = 5
		fp.set_preference("network.proxy.type", 1)
		fp.set_preference("network.proxy.socks","127.0.0.1")
		fp.set_preference("network.proxy.socks_port",int("9150"))
		fp.set_preference("general.useragent.override",user_agent)
		fp.update_preferences()
		browser = webdriver.Firefox(firefox_profile=fp)
		#profile=webdriver.FirefoxProfile()
		#profile.set_preference('network.proxy.type', 1)
		#profile.set_preference('network.proxy.socks', '127.0.0.1')
		#profile.set_preference('network.proxy.socks_port', 9150)
		#proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8118"})
		#opener = urllib2.build_opener(proxy_support)
		#urllib2.install_opener(opener)
		#_set_urlproxy()
		#request=urllib2.Request(url, None, headers)
		#browser=webdriver.Firefox(profile)
		print "profile loaded"
		url = 'http://www.youtube.com'
		browser.get(url)
		browser.maximize_window()
		print "loaded url"
		time.sleep(2)
		inputElement = browser.find_element_by_id("masthead-search-term")
		inputElement.send_keys('araku roadtrip')
		browser.find_element_by_xpath("//button[@class='yt-uix-button yt-uix-button-size-default yt-uix-button-default search-btn-component search-button']").click()
		time.sleep(5)
		if not browser.find_element_by_xpath('//a[@href="'+url1+'"]'):
			while True:
			     scrollDown()
			     if browser.find_element_by_xpath('//a[@href="'+url1+'"]'):
				     break
		browser.find_element_by_xpath('//a[@href="'+url1+'"]').click()
		xyz = browser.page_source    	
		time.sleep(randint(20,50))
		browser.quit()
	except Exception as e1:
		print "Inner",e1
	 
def renew_connection():
    conn = TorCtl.connect(controlAddr="localhost", controlPort=9151, passphrase="password")
    conn.send_signal("NEWNYM")
    conn.close()

def scrollDown():
	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
 
for i in range(0, 1000):
	try:
		print "Start"
		renew_connection()
		print "Renew success"
		print request("/watch?v=e27Os6lmc6M")
		print "Request success"
	except Exception as e:
		print e
