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

### 6 Добуваємо quotes та authors

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
Знаючи як добувати дані із окремої цитати, організуємо прохід по всім цитатам на сторінці:
```python
for quote in response.css("div.quote"):
    text = quote.css("span.text::text").get()
    author = quote.css("small.author::text").get()
    tags = quote.css("div.tags a.tag::text").getall()
    print(dict(text=text, author=author, tags=tags))

{'text': '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”', 'author': 'Albert Einstein', 'tags': ['change', 'deep-thoughts', 'thinking', 'world']}
{'text': '“It is our choices, Harry, that show what we truly are, far more than our abilities.”', 'author': 'J.K. Rowling', 'tags': ['abilities', 'choices']}
```

### 7 Організуємо добування даних за допомогою паука
Паук зазвичай створює багато словників, що містять дані добуті із сторінки. Організуємо видачу даних за допомогою генератора
[quotes_scrapy.py](https://github.com/jenja-pa/PythonLearningProjects/blob/65ba26e04ec9e0bbec20dcaa81e9b28d4671a738/scrapy/tutorial/tutorial/spiders/quotes_scrapy.py)

при запуску проекта ми можемо спостерігати, що в лог видаються добуті нами дані.

### 8 Збереження добутих даних
Сами простий спосіб зберегти це скористатися такою командою:
```Batchfile
scrapy crawl quotes -O quotes.json
```
Буде згенеровано файл quotes.json, що буде містити добуті дані сериалізовані у JSON.

команда -O перекриває будь-який існуючий файл
команда -o додає контент у існуючий файл
Однак, додавання уJSON файл робить його інвалідним JSON. 
тому треба використати інший формат серилізації, такий як JSON Lines:
```Batchfile
scrapy crawl quotes -o quotes.jsonl
```
Формат JSON Lines чудово підходить для таких цілей бо підтримує додавання нових записів. 
Кожен запис розміщується на окремому рядку, тому ви можете обробляти великі файли без наявності великої кількості пам'яті, є інструменти такі як [JQ](https://stedolan.github.io/jq) що допоможуть із цим.

В малих проектах, таких я це, виконаної роботи уже достатньо. 
Однак якщо вам потрібні більш складні речі для скрапінга - ви можете написати [Item Pipeline](https://docs.scrapy.org/en/latest/topics/item-pipeline.html#topics-item-pipeline)

Приклад такого проекта існує в ***tutorial/pipelines.py***
Але зараз нам це не потрібно.

### 9 Перехід по лінкам
Отже замість того щоб добувати дані із 2х сторінок із https://quotes.toscrape.com, ми хочемо отримати всі дані із сайта.

Для цього нам потрібно знати як переходити по лінкам.

Перше нам потрібно добути лінк на сторінку яка нам потрібна.

Перевіряючи сторінку ми бачимо, що існує тег <a ...> який веде на наступну сторінку:
```html
<ul class="pager">
    <li class="next">
        <a href="/page/2/">Next <span aria-hidden="true">&rarr;</span></a>
    </li>
</ul>
```
ми можемо добути цей елемент в shell:
```Batchfile
response.css('li.next a').get()
'<a href="/page/2/">Next <span aria-hidden="true">→</span></a>'
```
Отримаємо елемент anchor, але нам потрібний його атрибут href. 
Для цих цілей Scrapy підтримує CSS розширення що дає змогу вибирати значення атрибутів:
```Batchfile
response.css('li.next a::attr(href)').get()
'/page/2/'
```

Модифікуємо наш паук, щоб він міг рекурсивно переходити на наступну сторінку, щоб добути дані і із неї:
[quotes_scrapy.py](https://github.com/jenja-pa/PythonLearningProjects/blob/6eb17820e9428c4f4e40eb2fb42668bd562f022c/scrapy/tutorial/tutorial/spiders/quotes_scrapy.py)

Зараз після добування даних, матод parse() шукає лінка на наступну сторінку, будує повний абсолютний шлях за допомогою vtnjlf urljoin(), бо лінк може бути відносний та генераторно створює новий запит до наступної сторінки, реєструючи себе як callback для обробки докування даних наступної сторінки і продовжує цей шлях просуваючись по всіх сторінках.

Як ми бачимо механізм Scrapy такий:
 - слідуючи за лінком коли ми визиваєм Request то Scrapy планує що буде наступгний запит і реєструє для його обробки цей же метод який зараз працює, щоб визвати його як тільки цей метод закінчиться

використовуючи це ви можете побудувати складний засіб що буде слідувати лінкам відповідно до правил та добувати різного роду дані відповідно від того яка є відвідана сторінка

В нашому прикладі, було створено один із видів циклу що слідує за лінком на наступну сторінку доки такого лінка не буде знайдено, це хороший приклад обробки набору сторінок із пагінацією  
 
 
 
