import random
from datacenter.models import Schoolkid, Lesson, Commendation, Mark, Chastisement


def fix_marks(full_name):
    """Исправляет плохие оценки на 4 и 5"""
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=full_name.title())
        kidsmarks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4)
        for mark in kidsmarks:
            mark.points = random.randint(4, 5)
            mark.save()
    except Schoolkid.DoesNotExist:
        print('<ученик не найден, проверьте ввод>')
    except Schoolkid.MultipleObjectsReturned:
        print('<найдено более одного ученика, уточните ввод>')


def create_commendation(full_name, subject):
    """Создаёт положительный отзыв в указанном предмете"""
    try:
        kid = Schoolkid.objects.get(full_name__contains=full_name.title())
        lessons = Lesson.objects.filter(year_of_study=kid.year_of_study,
                                        group_letter=kid.group_letter,
                                        subject__title=subject.title())
        lesson = random.choice(lessons)
        Commendation.objects.create(text="Ты молодец!", created=lesson.date,
                                    schoolkid=kid, subject=lesson.subject,
                                    teacher=lesson.teacher)
    except Schoolkid.DoesNotExist:
        print('<ученик не найден, проверьте ввод>')
    except Schoolkid.MultipleObjectsReturned:
        print('<найдено более одного ученика, уточните ввод>')
    except IndexError:
        print('<не найдено название предмета, проверьте ввод>')


def remove_chastisements(full_name):
    """Удаляет плохие отзывы"""
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=full_name.title())
        chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
        for chastisement in chastisements:
            chastisement.delete()
    except Schoolkid.DoesNotExist:
        print('<ученик не найден, проверьте ввод>')
    except Schoolkid.MultipleObjectsReturned:
        print('<найдено более одного ученика, уточните ввод>')


print('<скрипты импортированы>')
