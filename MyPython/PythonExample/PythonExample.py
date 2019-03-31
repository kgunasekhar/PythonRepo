from   selenium import webdriver


  
browser = webdriver.Chrome()
browser.set_window_size("1024", "768")
browser.maximize_window()
browser.get("http://www.facebook.com")
  
username = browser.find_element_by_name("email")
password = browser.find_element_by_name("pass")
submit   = browser.find_element_by_id("u_0_2")
  
username.send_keys("9494747492")
password.send_keys("9494747492")
  
submit.click()
  
browser.quit()