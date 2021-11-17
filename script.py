import random

from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation


def fix_marks(name_part, year_of_study, letter_upper, point):
    schoolkid = Schoolkid.objects.get(
        full_name__contains=name_part, group_letter=letter_upper, year_of_study=year_of_study)
    bad_marks = Mark.objects.filter(
        schoolkid=schoolkid, points__lte=point)
    for mark in bad_marks:
        mark.points = 5
        mark.save()


def fix_chastisement(name_part, year_of_study, letter_upper):
    schoolkid = Schoolkid.objects.get(
        full_name__contains=name_part, group_letter=letter_upper, year_of_study=year_of_study)
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def show_lessons_count(year_of_study, letter_upper, subject):
    lessons = Lesson.objects.filter(
        year_of_study=year_of_study, group_letter=letter_upper, subject__title=subject).order_by('date')
    print(lessons.count())


def create_commendation(part_name, year_of_study, letter_upper, subject, text, lesson_number=None):
    schoolkid = Schoolkid.objects.get(
        full_name__contains=part_name, year_of_study=year_of_study, group_letter=letter_upper)
    lessons = Lesson.objects.filter(
        year_of_study=year_of_study, group_letter=letter_upper, subject__title=subject).order_by('date')

    if lesson_number:
        lesson = lessons[lesson_number]
    else:
        lesson = random.choice(lessons)

    teacher = lesson.teacher
    subject = lesson.subject
    date = lesson.date

    Commendation.objects.create(
        schoolkid=schoolkid, teacher=teacher, subject=subject, created=date, text=text)
