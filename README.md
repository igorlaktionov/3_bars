# Ближайшие бары

Скрипт для нахождения:

-самого большого бара

-самого маленького бара

-ближайшего бара
# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```#!bash

$ python bars.py # possibly requires call of python3 executive instead of just python

Чтобы получить самый большой бар необходимо:
$ python bars.py -f=path/to/file --biggest

Чтобы получить самый маленький бар необходимо:
$ python bars.py -f=path/to/file --smallest

Чтобы получить ближайший бар необходимо:
$ python bars.py -f=path/to/file --closest -latitude=55.722531 -longitude=37.614595

Пример вывода:
Closest bar:  Бар«Пивная Библиотека»
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
