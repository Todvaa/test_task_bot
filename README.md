# test_task_bot
## Description
Test task, building a price chart with indicators according to the specified parameters.
The code is structured, has an extensible architecture. It is possible to add any indicators,
multiple indicators per chart. Added tests
## Installation
1. Download the project from this repository
2. Install dependencies
<br><pre>pip install -r requirements.txt</pre><br>
## Run tests
1. Run the following command from the project directory
<br><pre>python -m unittest</pre><br>
## Data
The repository contains a test file prices.csv. The file contains two columns TS and PRICE.
The CsvInputAdapter class casts it to pandas.DataFrame, an OHLC structure. The code implements the ability to add other adapters.
To process user files, the column structure must be identical to prices.csv, when starting, specify the absolute path to the user file.
See Examples of using.
#### Arguments
Mandatory
- "input" (String. Link or path to a file with extension, the possibility of adding a link to data in the future is taken into account)
- "interval_minutes" (Integer. Time interval for chart element)

Optional
- "(-e | --ema) + int" (Adds the EMA indicator to the chart with the specified period)
## Examples of using
This command builds an hourly candlestick chart with the EMA(14) indicator
<br><pre>python main.py prices.csv 60 -e 14</pre><br>
Result:
![image](https://github.com/Todvaa/test_task_bot/assets/109280151/0205609a-390a-476d-9a66-cccc0a799844)

This chart plots a two-hour candlestick chart with the EMA(100) indicator
<br><pre>python main.py prices.csv 120 -e 100</pre><br>
Result:
![image](https://github.com/Todvaa/test_task_bot/assets/109280151/bd867ef0-9b22-4ac4-95d4-1d9077955b89)

This chart builds a fifteen-minute chart without an indicator.
<br><pre>python main.py prices.csv 15</pre><br>
Result:
![image](https://github.com/Todvaa/test_task_bot/assets/109280151/61972126-ecb3-4dde-aaa6-de71a9668beb)

*** To get acquainted with the available functionality, run the following command from the project directory
<br><pre>python main.py -h</pre><br>

## Описание
Тестовое задание, построение графка цены с индикаторами по заданным параметрам. 
Код структурирован, имеет расширяемую архитектуру. Предусмотрена возможность добавления любых индикаторов,
нескольких индикаторов на график. Добавлены тесты
## Установка
1. Скачайте проект из данного репозитория
2. Установите зависимости
<br><pre>pip install -r requirements.txt</pre><br>
## Запуск тестов
1. Выполните следующую команду из директории проекта
<br><pre>python -m unittest</pre><br>
## Данные
В репозитории представлен тестовый файл prices.csv. Файл содержит две колонки TS и PRICE.
Класс CsvInputAdapter приводит его к типу pandas.DataFrame, структура OHLC. В коде реализована возможность добавления иных адаптеров.
Для обработки пользовательских файлов структура колонок должна быть идентичной prices.csv, при запуске указывать абсолютный путь до пользовательского файла.
См. Примеры использования. 
#### Аргументы
Обязательные
- "input" (Строка. Ссылка или путь к файлу с расширением, учтена возможность добавления ссылки на данные в будущем)
- "interval_minutes" (Целое число. Временной интервал для элемента графика)

Необязательные
- "(-e | --ema) + int" (Добавляет индикатор EMA на график с указанным периодом)

## Примеры использования
Данная команда построит часовой свечной график с индикатором EMA(14)
<br><pre>python main.py prices.csv 60 -e 14</pre><br>
Результат: 
![image](https://github.com/Todvaa/test_task_bot/assets/109280151/0205609a-390a-476d-9a66-cccc0a799844)

Данная команда построит двух часовой свечной график с индикатором EMA(100)
<br><pre>python main.py prices.csv 120 -e 100</pre><br>
Результат: 
![image](https://github.com/Todvaa/test_task_bot/assets/109280151/bd867ef0-9b22-4ac4-95d4-1d9077955b89)

Данная команда построит пятнадцатиминутный график без индикатора
<br><pre>python main.py prices.csv 15</pre><br>
Результат: 
![image](https://github.com/Todvaa/test_task_bot/assets/109280151/61972126-ecb3-4dde-aaa6-de71a9668beb)


*** Для ознакомления с доступным функционалом выполните следующую команду из директории проекта
<br><pre>python main.py -h</pre><br>
