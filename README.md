# db_hack

Script uses for import in shell to correct the django project information in DB

## Install 

Copy and add script.py near manage.py in the django project

## Get started

Python3 and the django project must be installed with requirements, script is useless without this stuff.

Use this comand to start django-shell:
```
python3 manage.py shell
```
Copy and inter all script code into django-shell.
Then you get possibilities to use script func in django-shell.

## Funcs and args

- `name_part` - string, part name of schoolkid you want to fix ifromation, like: 'Пупкин Василий'
- `year_of_study` - integer, class year of this person
- `letter_upper` - upper case string char of person group, like: 'A'
- `point` - integer, mark in db 
- `subject` - string, subject, like: 'Математика'
- `text` - string, commendation, like: 'Хвалю!'
- `lesson_number` - integer, number of specific lesson, default = None, then func will choose random lesson.

`fix_marks(name_part, year_of_study, letter_upper, point)`

Fix all bad marks less or equal point arg to best grade (default - 5) for one schoolkid.

`fix_chastisement(name_part, year_of_study, letter_upper)`

Delete chastisements for schoolkid.

`show_lessons_count(year_of_study, letter_upper, subject)`

Show count number of subject for schoolkid.

`create_commendation(part_name, year_of_study, letter_upper, subject, text, lesson_number)`

Create commendation for schoolkid.

## Project goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).