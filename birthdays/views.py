from django.shortcuts import render
from django.http import Http404, JsonResponse, HttpResponse, QueryDict
from datetime import date
from django.views.decorators.csrf import csrf_exempt

from .models import Person, Present


def index(request):
    birthdays_today = []
    #get all people with birthday today
    for p in Person.objects.all():
        if p.isBirthdayToday():
            birthdays_today.append(p)

    #get and format today's date
    today = date.today()
    suffix = _getSuffix(today)
    today_date = '{}{} {}'.format(today.day, suffix, today.strftime("%B"))

    #return template plus context
    context = {
        'birthdays_today': birthdays_today,
        'today_date': today_date,
    }
    return render(request, 'birthdays/index.html', context)

@csrf_exempt
def detail(request, person_id):
    response = {}
    if request.method == 'GET':
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            raise Http404("Person does not exist")
        try:
            present = Present.objects.get(recipient=person)
        except Present.DoesNotExist:
            present = None
        context = {
                'person' : person,
                'present' : present,
            }
        return render(request, 'birthdays/detail.html', context)
    if request.method == 'PUT':
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            raise Http404("Person does not exist")
        data = QueryDict(request.body)
        try:
            already = Present.objects.get(recipient=person)
        except Present.DoesNotExist:
            try:
                if data['present-what']!="":
                    present = Present(what=data['present-what'], price=data['present-price'], recipient=person)
                    present.save()
                response['data'] = "OK"
                return JsonResponse(response)
            except Exception as e:
                response['data'] = "Oh no! Something went wrong: "+str(e)
                return JsonResponse(response)
        response['data'] = "This person already has a present!"
        return JsonResponse(response)
    if request.method == 'DELETE':
        try:
            person = Person.objects.get(id=person_id)
            person.delete()
        except Person.DoesNotExist:
            raise Http404("Person does not exist")
        response['data'] = "OK"
        print(response)
        return JsonResponse(response)


def all(request):
    people = {}
    for person in Person.objects.all():
        people[int(person.id)-1] = { 'id' : person.id, 'name' : person.name, 'picture' : person.picture }
    return JsonResponse(people)


@csrf_exempt
def new(request):
    response = {}
    if request.method == 'GET':
        return render(request, 'birthdays/add.html')
    if request.method == 'POST':
        try:
            data = QueryDict(request.body)
            person = Person(name=data['name'], birth_date=data['birthday'], picture=data['picture'], fun_fact=data['fun_fact'])
            person.save()
            id = person.id
            if data['present-what']!="":
                present = Present(what=data['present-what'], price=data['present-price'], recipient=person)
                present.save()
            response['id'] = str(id)
            return JsonResponse(resonse)
        except Exception as e:
            response['error'] = "Oh no! Something went wrong: "+str(e)
            return JsonResponse(response)




#-------------------------------------------------------
#HELPER METHODS BELOW
#-------------------------------------------------------
def _getSuffix(day):
    if 4 <= day.day <= 20 or 24 <= day.day <= 30:
        return "th"
    else:
        return ["st", "nd", "rd"][day.day % 10 - 1]
