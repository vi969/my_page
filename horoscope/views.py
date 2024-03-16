from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - <i>пятый знак зодиака</i>, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

def index(request):
    zodiac_list = list(zodiac_dict)
    sign_li = ''
    for sign in zodiac_list:
        link = reverse('zodiac', args=(sign,))
        sign_li += f'<li><a href={link}>{sign.title()}</a></li>'
    ul_list = f'<ul>{sign_li}</ul>'
    return HttpResponse(ul_list)


def get_ifo_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    if description:
        return HttpResponse(f'<h2>Information about sign of zodiac "{sign_zodiac}:"<p>{description}</p>')
    else:
        return HttpResponseNotFound(f'<h4>Sign {sign_zodiac} is not exists</h4>')


def get_ifo_sign_zodiac_by_num(request, num_zodiac:int):
    zodiac_list = list(zodiac_dict)

    if num_zodiac > len(zodiac_list):
        return HttpResponseNotFound(f'<h3>Wrong sign zodiac:{num_zodiac}</h3>')
    else:
        name_zodiac = zodiac_list[num_zodiac -1]
        redirect_url = reverse('zodiac', args=(name_zodiac, ))
        return HttpResponseRedirect(redirect_url)
