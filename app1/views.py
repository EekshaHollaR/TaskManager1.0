from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def IndexView(request):
    user = {"name": "Eeksha"}
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return render(request, 'tasks/index.html', {'user': user, 'days': days})

def rootPageView(request):
    return render(request,'rootPage.html')

def dayView(request,day):
    days=['Monday', 'Tuesday', 'Wednesday', 
            'Thursday', 'Friday', 'Saturday','Sunday']
    tasks = [{'text': 'a'}, {'text': 'b'}, {'text': 'c'}]
    return render(request,'tasks/day.html',{
        'days':days,
        'tasks':tasks,
        'day':day
})
