from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render
from college.models import Person

# Create your views here.
# def home_page(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('first')
#         last_name = request.POST.get('last')
#         print(first_name)
#         print(last_name)
#         return HttpResponse("I am in django class")
#     return render(request, 'index.html')


def home_page(request):
    # obj = Person.objects.create(first_name='anil', last_name='deepak')
    result = Person.objects.all()
    for each in result:
        pass
        # print(each.first_name)
    first = Person.objects.first()
    # print(first.first_name)

    first_nm = Person.objects.filter(first_name='anil')
    # print(first_nm)

    update_last_name = Person.objects.filter(id=6).update(last_name='shilpa')
    # print(update_last_name)

    delete_3rd_record = Person.objects.filter(id=3).delete()
    print(delete_3rd_record)

    return HttpResponse(f"diplaying first element {first.first_name}")