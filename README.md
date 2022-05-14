# План урока-туторила для группы "Питон на четверых" :)

### API
(Application programming interface) — это контракт, который предоставляет программа. «Ко мне можно обращаться так и так, я обязуюсь делать то и это».
### Query string
Допустим, есть URL следующего вида:
- `https://api.duckduckgo.com/?q=search_text&format=json`
- `query_params` = `{'q': search_text, 'format': 'json' }`
- `https` - протокол
- `api.duckduckgo.com` - хост
- `?` - начало параметров запроса
- `q` -имя параметра
- `search_text` -значение параметра
- `&` - разделитель параметров

### Requests 
Библиотеке python, можно установить командой: 
```shell
pip install requests
```
Это - основной инструмент для работы с API, которым придется пользоваться на первых порах.
```python
import requests

def fetch_duckduckgo_data(search_text):
    query_params = {
        'q': search_text,
        'format': 'json'
    }
    response = requests.get('https://api.duckduckgo.com/', params=query_params)
    response.raise_for_status()
    # response.text
    # response.content

    return response.json()
```
- `response.raise_for_status()` - для случаев, когда ответ не 20*
- `return response.json()` - вернуть JSON 

### JSON

- JSON (англ. JavaScript Object Notation) — текстовый формат обмена данными, основанный на JavaScript. Но при этом формат независим от JS и может использоваться в любом языке программирования.
- Неупорядоченное множество пар "ключ:значение"
```json
{
  "Abstract": "",
  "AbstractSource": "Wikipedia",
  "AbstractText": "",
  "AbstractURL": "https://en.wikipedia.org/wiki/123",
  "ImageWidth": 0,
  "IsBool": true,
  "":  "",
  "RelatedTopics": [
    {"FirstURL": "https://duckduckgo.com/Japan_Airlines_Flight_123"}, 
    {"": ""}
  ]
}

```
### Декораторы
- Функция, которая в качестве первого позиционного аргумента принимает другую функцию и как-то изменяет ее поведение, не меняя код изначальной функции.
```python
def guardian(func):
    def inner(*args, **kwargs):
        neighbors = ["Иван", "Алекей"]
        if args[0] in neighbors:
            func(*args, **kwargs)
        else:
            print("тебе сюда нельзя, гав-гав")
    return inner


@guardian
def say_hello(visitor):
    print(f"Привет, {visitor}")


if __name__ == '__main__':
    visitors = ["коля", "Иван", "Николай", "Глеб"]
    for visitor in visitors:
        say_hello(visitor)

```
### Класс

- Класс — тип, описывающий устройство объектов. Объект — это экземпляр класса. Класс можно сравнить с чертежом, по которому создаются объекты.

```python
class User:
    def __init__(self, name, age, work):
        self.name = name
        self.age = age
        self.work = work

    def say_hello(self):
        return f"hello, my name is {self.name}"


user1 = User('Egor', '28', 'python')


class Child(User):
    def __init__(self, name, age, work, music):
        super().__init__(name, age, work)
        self.music = music

    def say_music(self):
        return f"hello, my name is {self.name}, i'm listening to {self.music}"


child1 = Child('Ivan', '13', 'python', 'Bah')

```
### FastAPI

Установка:
```shell
pip insatll fastapi uvicorn jinja2
```
```python
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from modules import fetch_duckduckgo_data


app = FastAPI() #  создаем экземпляр объекта
app.mount("/static", StaticFiles(directory="templates"), name="templates") #  "монтируем" директорию с шаблонами
templates = Jinja2Templates(directory="templates")  #  в качестве языка шаблонов будем использовать Jinja2


@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/search", response_class=HTMLResponse)
def search_page(request: Request):
    search_question = request.query_params.get('search_question')

    answer_data = fetch_duckduckgo_data(search_question)
    url = answer_data.get('AbstractURL')
    source = answer_data.get('AbstractSource')

    return templates.TemplateResponse("index.html", {"request": request,
                                                     "url": url,
                                                     "source": source})

```