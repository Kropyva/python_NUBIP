# task-4

# @CoronaStatEuroBot - бот для виведення статистики країн Європи, щодо COVID-19
@CoronaStatEuroBot

# Підготовка.
Cкачуємо пакети для бота.

![Screenshot_1](https://user-images.githubusercontent.com/65035716/123501118-51e84580-d64b-11eb-95a1-8bbb0dff8b95.jpg)


Знаходимо в BotFather в телеграмі й "просимо" дозволу на створення бота.

![Screenshot_2](https://user-images.githubusercontent.com/65035716/123501122-5ad91700-d64b-11eb-8d56-eb79d112e762.jpg)

Далі пишемо код.

# Бот у ділі.
Старт бота.

![Screenshot_3](https://user-images.githubusercontent.com/65035716/123501128-64fb1580-d64b-11eb-82b2-2c1882e25c2d.jpg)

Натискаємо кнопку "Show information", щоб побачити список країн.

![Screenshot_4](https://user-images.githubusercontent.com/65035716/123501138-780de580-d64b-11eb-9d89-2ebb31d24fa9.jpg)

![Screenshot_5](https://user-images.githubusercontent.com/65035716/123501177-a2f83980-d64b-11eb-971b-ee73b6473a7a.jpg)

Можемо гортати список.

![Screenshot_6](https://user-images.githubusercontent.com/65035716/123501182-aa1f4780-d64b-11eb-8cfa-1a5ea951e27c.jpg)

Можна ввести країну самостійно, якщо така є в списку, то бот виведе щодо неї інформацію.

Усі країни потрібно вводити англійською та з великої букви.

Якщо це не європейська країна, або такої не існує, то бот про це напише.

![Screenshot_8](https://user-images.githubusercontent.com/65035716/123501190-bacfbd80-d64b-11eb-9052-15059e861ffe.jpg)

# Попередження.
Щоб запустити бота - потрібен config.py файл з токеном в середині.

Є деякі країни винятки, де потрібно писати два слова з великої букви.
Такі як: "Bosnia and Herzegovina", "North Macedonia", "San Marino", "Channel Islands", "Isle of Man", "Faeroe Islands", "Vatican City" або "UK".

Якщо кількість країн в списку не ділиться на 9, то при переході від однієї сторінки до іншої - можуть бути повтори з минулої.

![Screenshot_9](https://user-images.githubusercontent.com/65035716/123501194-c4592580-d64b-11eb-8b5a-133bcfd3bbba.jpg)

![Screenshot_10](https://user-images.githubusercontent.com/65035716/123501196-cc18ca00-d64b-11eb-9a25-b888323147f9.jpg)

# Updated.

Added /statistics_txt command - Get a 'file'.txt wist statistics.

![Screenshot_11](https://user-images.githubusercontent.com/65035716/123504294-f628b700-d660-11eb-8c03-3acf1a0bde46.jpg)