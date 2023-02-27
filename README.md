<h1> 2023-python <sup> co-made by <a href="https://github.com/Lyric-Meow/">Milly</a> </sup> </h1>
Лабораторные по курсу "Язык программирования Python", группы ИС-33, ИС-34

## Старт:
- Для работы необходим python 3.9 и выше.

### Библиотеки:

---

- numpy
- matplotlib
- tkinter

### Редактор любой. Из неплохих:

---

- IDLE (родной, идёт вместе с установщиком)
- Visual Studio Code, notepad++
- PyCharm
- vim (для любителей сначала страдать, потом наслаждаться)

## Полезное
<ul>
<Li>
Работа с блокнотами онлайн, с возможностью подключение удалённых мощностей гугла (GPU, TPU):
<a href="https://colab.research.google.com/">
<img src="https://img.shields.io/badge/Google%20Colab-2275be?logo=google&logoColor=fcec06" height="25" alt="Google colab Badge"/>
</a><br>
</Li>
<Li>
Презентация (будет обновляться в течение семестра): 
<a href="https://docs.google.com/presentation/d/1CqyrZYSh15dsVWt57eu14UDtm2-GFpSF5TD2_tVLaCc/edit?usp=sharing">
<img src="https://img.shields.io/badge/Google%20docs-2275be?logo=google&logoColor=fcec06" height="25" alt="Google Docs Badge"/>
</a><br>
</Li>
<Li>
Хорошая книга по python, очень простым языком и на понятных примерах: 
<a href="https://wombat.org.ua/AByteOfPython/AByteofPythonRussian-2.02.pdf">
<img src="https://img.shields.io/badge/Wombat-2275be?labelColor=fcec06" height="25" alt="Book Badge"/>
</a><br>
</Li>
<Li>
Сервер в Дискорд, где буду дублировать: 
<a href="https://discord.gg/MzPkCYf4Dh">
<img src="https://img.shields.io/badge/Discord-2275be?logo=discord&logoColor=fcec06" height="25" alt="Discord Badge"/>
</a><br>
</Li>
<Li>
Мой контакт:
<a href="mailto:nsmorozov@rf.unn.ru">
  <img src="https://img.shields.io/badge/E%E2%80%93mail-2275be?logo=gmail&logoColor=fcec06" height="25" alt="E–mail Badge"/>
</a>
</Ul>

## Предупреждения:
- В своей папке можете делать все что угодно, в чужие не залезать, в корневую тоже.
- Я буду ориентироваться на файлы, где в названии будет номер лабораторной.

## [1] Работа со структурами данных
	
### Исходные данные:

---

- свои ФИО, число, месяц, год рождения в виде кортежа;
- предметы в школьном аттестате (не меньше 14), как словарь из названия и оценки (можно мокать);
- имена (только) ближайших (до двоюродных включительно) родственников в списке;
- имя, которое вы бы дали своей домашней пушистой киве (строка).

### Действия:

---

<ol>
<Li> вывести среднюю оценку в аттестате;</Li>
<Li> вывести уникальные имена среди своих родственников (включая свое);</Li>
<Li> общая длина всех названий предметов;</Li>
<Li> уникальные буквы в названиях предметов;</Li>
<Li> имя вашей домашней пушистой кивы в бинарном виде;</Li>
<Li> отсортированный по алфавиту (в обратном порядке) список родственников;</Li>
<Li> количество дней от вашей даты рождения до текущей даты (должна быть всегда актуальной);</Li>
<Li> FIFO очередь, в которую можно добавлять предметы по вводимому с клавиатуры индексу (до команды остановки), после введения - вывести все;</Li>
<Li> по введеному индексу, поменять имя в отсортированном списке родственников на имя ацтекского правителя (<a href="https://en.wikipedia.org/wiki/List_of_rulers_of_Tenochtitlan"><img src="https://img.shields.io/badge/Wikipedia-2275be?logo=Wikipedia&logoColor=fcec06" height="25" alt="Wiki Badge"/></a>) под номером, получаемым из вашей даты рождения: number = (day + month**2 + year) % 21 + 1;</Li>
<Li> создать связный список, как словарь, где ключ - имя родственника, а значение - индекс следующего имени по исходному списку, упорядоченному по их (родственников) годам рождения, исходный список при этом должен остаться неизменным </Li>
<Li> написать функцию-генератор:
<ol type="1" start="0">
<li> аликвотной последовательности; </li> 
<li> последовательности Сильвестра; </li> 
<li> числа трибоначчи;</li> 
<li> числа Леонардо. Свой вариант определяется как number = len("ФИО") * len (family_names) % 4; </li> 
</ol>
</Li>

</ol>
