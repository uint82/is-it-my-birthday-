from django.shortcuts import render
import datetime

def is_birthday(request):
    sekarang =  datetime.datetime.now()
    return render(request, 'birthday/index.html', {
        "ulangtahun": sekarang.day == 4 and sekarang.month == 7
    })
    

