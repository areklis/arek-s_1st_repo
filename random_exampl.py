Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> random.randint(-15000,321897301)
299637842
>>> random.randint()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    random.randint()
TypeError: randint() missing 2 required positional arguments: 'a' and 'b'
>>> random.random()
0.22615434861371375
>>> random.uniform(5,7)
5.671876014713549
>>> items=['ena','duo','tria','tessera']
>>> random.shuffle(items)
>>> items
['ena', 'duo', 'tria', 'tessera']
>>> random.shuffle(items)
>>> items
['tria', 'tessera', 'ena', 'duo']
>>> 