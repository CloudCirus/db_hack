# db_hack

The script is used to run in django-shell. Using functions from the script you can change some of the data in the database.

## Install 

Copy and add script.py near manage.py in the django project

## Get started

Python3 and the django project must be installed with requirements, script is useless without this stuff.
Move script.py near managept in the django project.

Use this comand to start django-shell:
```
python3 manage.py shell
```
Import script funcs in django-shell:
```
from script.py import *
```
Then you get possibilities to use script func in django-shell.

You need to define the variable like, kid, it will contain the instance of the Schoolkid class, example:
```
schoolkid = get_schoolkid('Василий Пупкин', 'Б', 8)
```
Then you can use other functions.

## Funcs and args

- `schoolkid` - the instance of the Schoolkid class, that contains in the variable you create befor. 
- `full_name` - string, part name of schoolkid you want to fix ifromation, like: 'Пупкин Василий'
- `study_year` - integer, class year of this person
- `class_letter` - upper case string char of person group, like: 'A'
- `bad_mark` - integer, mark in db 
- `subject` - string, subject, like: 'Математика'
- `commendation_text` - string, like: 'Хвалю!'
- `lesson_number` - integer, number of specific lesson, default = None, then func will choose random lesson.

Fix all bad marks less or equal `bad_mark` arg to best grade (default = 5) for one schoolkid:
```
fix_marks(schoolkid, bad_mark)
```

Delete chastisements for schoolkid:
```
fix_chastisement(schoolkid)
```

Show count number of subject for schoolkid:
```
show_lessons_count(schoolkid, subject)
```

Create commendation for schoolkid:
```
create_commendation(schoolkid, subject, commendation_text, lesson_number)
```

If you whant to overrite the variable that you define before, use:
```
schoolkid = get_schoolkid(full_name, class_letter, study_year)
```

## Project goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).