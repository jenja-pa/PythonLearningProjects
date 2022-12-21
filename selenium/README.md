# Матеріали вивчення можливостей Selenium

## Створюємо нове віртуальне оточення під проекти на Selenium
(Лінк)[] на приклад створення вірт.оточення

## Встановлення модуля selenium та перевірка
```
pip install selenium
```
перевірка:
```
>>> import selenium
```
> якщо помилок немає - все добре

## Завантаження та встановлення Chrome Driver (сам GoogleGhrome - повинен бути встановлений)
Chrome Driver [link](https://sites.google.com/chromium.org/driver/?pli=1)
 1. Перейти за посиланням
 2. Визначити поточну версію вашого встановленого браузера
 > click (три верт. точки) / Help / About Google chrome
 > (моя: Version 108.0.5359.125 (Official Build) (64-bit))
 3. Скачуємо WebDriver - версії, що найбільше підходить нам 
 > (для мене: ChromeDriver 108.0.5359.71 / chromedriver_win32.zip)
 > в папку (Download)
 4. Витягуємо файл .exe із архіва в папку Program Files (x86)/
 > для копіювання файла можуть знадобитися права адміністратора
 5. Драйвер встановлено

## Перевірка роботи драйвера
 1. створюємо файл techwithtim/tutorial1.py 
 ```Python
from selenium import webdriver


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://techwithtim.net")

print(driver.title)
driver.close() # Закрити відкриту процесом вкладку
# driver.quit() # Закрити весь браузер
```

