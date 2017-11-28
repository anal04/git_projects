'''
Declaring import statements:
-----------------------------
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



'''
Opening the web page:
----------------------
'''

driver = webdriver.Chrome()
a = driver.get("http://www.python.org")



'''
Maximizing the web page:
-------------------------
'''
driver.set_window_size(1024, 600)
driver.maximize_window()



#Wait for 5 secs
driver.implicitly_wait(5)
assert "Python" in driver.title



'''
For Clicking "Python" and "PSF" tab:
--------------------------------------
For accessing "<a href="/" title="The Python Programming Language" class="current_item selectedcurrent_branch selected">Python</a>",
use "find_element_by_partial_link_text('Python')" or "find_element_by_link_text('Python')" or "find_element_by_xpath(u'//a[text()="Python"]')"------>The third type is mainly used for string hyperlink
'''

Python = driver.find_element_by_partial_link_text('Python').send_keys(Keys.RETURN);
time.sleep(2)
PSF = driver.find_element_by_partial_link_text('PSF').send_keys(Keys.RETURN);
time.sleep(2)
'''
To Click the search box:
---------------------------
For accessing "<input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="pycon" tabindex="1">",
use "find_element_by_id("id-search-field")"------>For id access
"find_element_by_name("q")----->For class access
'''

elem = driver.find_element_by_id("id-search-field")
elem.clear()

'''
Searching the string "pycon" in the search tab
-----------------------------------------------
'''

elem.send_keys("pycon")
time.sleep(2)

#For pressing "Enter" key
elem.send_keys(Keys.RETURN)
driver.implicitly_wait(5)

assert "No results found." not in driver.page_source

p = driver.find_element_by_xpath(u'//a[text()="PyCon Pakistan"]').send_keys(Keys.RETURN);
driver.implicitly_wait(5)

#To go to the previous page in a browser
driver.back()
time.sleep(2)

#To go to the next page in a browser
driver.forward()
time.sleep(2)


M=3
for i in range(M):
    driver.back()
time.sleep(2)


learn_more = driver.find_element_by_link_text('Learn More').send_keys(Keys.RETURN);
time.sleep(2)



beginner_guide = driver.find_element_by_link_text('Beginner’s Guide').send_keys(Keys.RETURN);
time.sleep(2)
driver.back()


python_periodicals = driver.find_element_by_link_text('Python Periodicals').send_keys(Keys.RETURN);
time.sleep(2)
driver.back()


python_packaging_user = driver.find_element_by_partial_link_text("Python Packaging User").send_keys(Keys.RETURN);
time.sleep(2)
driver.back()
 

pep_index = driver.find_element_by_link_text('PEP Index').send_keys(Keys.RETURN);
time.sleep(2)
driver.back()


'''
Minimizing the window size:
-----------------------------
'''
driver.set_window_size(700,450)
time.sleep(2)

driver.close()

