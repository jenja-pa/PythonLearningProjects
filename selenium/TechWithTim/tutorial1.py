# tutorial1.py
from selenium import webdriver


PATH = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://techwithtim.net")

print(driver.title)
driver.close()  # Закрити відкриту процесом вкладку
# driver.quit()  # Закрити весь браузер
