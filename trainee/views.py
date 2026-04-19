from django.shortcuts import render
from .models import Trainee
# Create your views here.
def trainee_list(request):
    trainees = Trainee.objects.all()
    context = {'trainees': trainees}
    return render(request, 'list.html', context)