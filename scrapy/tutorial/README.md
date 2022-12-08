# Scrapy Tutorial

В цьому керівництві ми ознайомимось із базовими знаннями про **scrappy**

1. Створення початкового шаблона застосунка
```Bathfile
scrapt startproject tutorial
```
2. Написання першого [паука](https://github.com/jenja-pa/PythonLearningProjects/blob/9803ca349c9c20e9642c5d5f9c184f3adee90046/scrapy/tutorial/tutorial/spiders/quotes_scrapy.py)

3. Запуск проекта, із папки проекта виконати команду:
```Bathfile
scrapy crawl quotes
```
в папці проекта з'являться 2 html файла

4. Якщо початкові файли мають наперед задані лінки можна обійтися без функції start_requests(), а замість неї використати атрибут start_urls де списком указати перелік лінків [паук](https://github.com/jenja-pa/PythonLearningProjects/blob/fe61127e2a8599107a52a788dd109907edd953db/scrapy/tutorial/tutorial/spiders/quotes_scrapy.py)

