from django.http import Http404

from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation


def get_schoolkid(full_name, class_letter, study_year):
    try:
        return Schoolkid.objects.get(
            full_name__contains=full_name,
            group_letter=class_letter.upper(),
            year_of_study=study_year
        )
    except Schoolkid.DoesNotExist:
        print('No matches in the db')
        return None
    except Schoolkid.MultipleObjectsReturned:
        print('Find more that one schoolkid')
        return None


def fix_marks(schoolkid, bad_mark_threshold):
    bad_marks = Mark.objects.filter(
        schoolkid=schoolkid, points__lte=bad_mark_threshold)
    for mark in bad_marks:
        mark.points = 5
        mark.save()


def fix_chastisement(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def create_commendation(schoolkid, subject, commendation_text):
    lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter.upper(),
        subject__title=subject
    ).last()

    Commendation.objects.create(
        schoolkid=schoolkid,
        teacher=lesson.teacher,
        subject=lesson.subject,
        created=lesson.date,
        text=commendation_text
    )
