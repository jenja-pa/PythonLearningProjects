# Scrapy Tutorial

В цьому керівництві ми ознайомимось із базовими знаннями про **scrappy**

### 1. Створення початкового шаблона застосунка
```Bathfile
scrapt startproject tutorial
```
### 2. Написання першого [паука](https://github.com/jenja-pa/PythonLearningProjects/blob/9803ca349c9c20e9642c5d5f9c184f3adee90046/scrapy/tutorial/tutorial/spiders/quotes_scrapy.py)

### 3. Запуск проекта, із папки проекта виконати команду:
```Bathfile
scrapy crawl quotes
```
в папці проекта з'являться 2 html файла

### 4. Якщо початкові файли мають наперед задані лінки можна обійтися без функції start_requests(), а замість неї використати атрибут start_urls де списком указати перелік лінків [паук](https://github.com/jenja-pa/PythonLearningProjects/blob/fe61127e2a8599107a52a788dd109907edd953db/scrapy/tutorial/tutorial/spiders/quotes_scrapy.py)

### 5. Отримання даних із HTML
Кращий шлях познайомитись із витягненням даних це попробувати використати селектори за допомогою інструмента Scrapy shell. Виконайте:

*linux*:
```Bathfile
scrapy shell 'https://quotes.toscrape.com/page/1/'
```
*windows*:
```Bathfile
scrapy shell "https://quotes.toscrape.com/page/1/"
```
> не забувайте брати адресу в лапки '..'(linux), або у подвійні лапки ".."(windows), бо інакше запит може не працювати.

#### 5.1 CSS запити
Результати виконання різних типів запитів із даної консолі:
```python
response.css('title')
[<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]

response.css('title::text').getall()
['Quotes to Scrape']

response.css('title').getall()
['<title>Quotes to Scrape</title>']

response.css('title::text').get()
'Quotes to Scrape'

response.css('title::text')[0].get()
'Quotes to Scrape'

response.css('noelement')[0].get()
Traceback (most recent call last):
...
IndexError: list index out of range
...
'''

response.css("noelement").get()
```
> .getall() - повертає список знайдених елементів

> .get() - повертає перший знайдений елемент

також можна застосувати регулярні вирази для отримання даних:
```python
response.css('title::text').re(r'Quotes.*')
['Quotes to Scrape']

response.css('title::text').re(r'Q\w+')
['Quotes']

response.css('title::text').re(r'(\w+) to (\w+)')
['Quotes', 'Scrape']
```

#### 5.2 XPath запити
Scrapy також підтримує XPath вирази, приклад запиту:
```python
response.xpath('//title')
[<Selector xpath='//title' data='<title>Quotes to Scrape</title>'>]
response.xpath('//title/text()').get()
'Quotes to Scrape'
```
> XPath вирази це основа scrapy і навіть CSS селектори конвертуються в XPath.

### 6 XPath запити
Добуваємо quotes та authors

Отже оскільки ми знаємо як вибирати дані добудемо на сторінці цитату та автора.

Розглянемо як виглядає сторінка та будуємо запити із консолі запитів
```python
response.css("div.quote")
[<Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
 <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
 ...]
 ```
 
 ```python
 response.css("div.quote")
[<Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
 <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
 ...]
```
Кожен селектор повертає всю інформацію про цитату і пізніше ми зможеио добути із неї потрібну інформацію, для цього назначимо результат у змінну і робитимемо запити із неї:
```python
quote = response.css("div.quote")[0]

text = quote.css("span.text::text").get()
text -> '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”'
author = quote.css("small.author::text").get()
author -> 'Albert Einstein'
```
теги ми отримаємо як список рядків за допомогою .getall():
```python
tags = quote.css("div.tags a.tag::text").getall()
tags -> ['change', 'deep-thoughts', 'thinking', 'world']
```
