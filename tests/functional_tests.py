from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://0.0.0.0:5050")
assert "Django" in browser.title