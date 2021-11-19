import random

from django.http import Http404
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation


def get_schoolkid(full_name, class_letter, study_year):
    try:
        return Schoolkid.objects.get(
            full_name__contains=full_name,
            group_letter=class_letter.upper(),
            year_of_study=study_year
        )
    except ObjectDoesNotExist:
        raise Http404('No matches in the db')
    except MultipleObjectsReturned:
        raise Http404('Find more than one schoolkid')


def fix_marks(schoolkid, bad_mark):
    bad_marks = Mark.objects.filter(
        schoolkid=schoolkid, points__lte=bad_mark)
    for mark in bad_marks:
        mark.points = 5
        mark.save()


def fix_chastisement(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def show_lessons_count(schoolkid, subject):
    lessons = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter.upper(),
        subject__title=subject
    ).order_by('date')

    print(lessons.count())


def create_commendation(schoolkid, subject, commendation_text):
    lessons = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter.upper(),
        subject__title=subject
    ).order_by('date')

    lesson = random.choice(lessons)

    Commendation.objects.create(
        schoolkid=schoolkid,
        teacher=lesson.teacher,
        subject=lesson.subject,
        created=lesson.date,
        text=commendation_text
    )
