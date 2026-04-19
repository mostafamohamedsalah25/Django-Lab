from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TraineeForm
import trainee
from .models import Trainee
# Create your views here.
def trainee_list(request):
    trainees = Trainee.objects.all()
    context = {'trainees': trainees}
    return render(request, 'trainee/list.html', context)

def add_trainee(request):
    if request.method == 'POST':
        form = TraineeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('trainee_list')
    else:
        form = TraineeForm()

    context = {'form': form}
    return render(request, 'trainee/addtrainee.html', context)


def update_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)

    if request.method == 'POST':
        form = TraineeForm(request.POST, instance=trainee)
        if form.is_valid():
            form.save()
            return redirect('trainee_list')
    else:
        form = TraineeForm(instance=trainee)

    context = {'form': form, 'trainee': trainee}
    return render(request, 'trainee/update.html', context)


def trainee_detail(request, id):
    trainee = get_object_or_404(Trainee, id=id)

    context = {'trainee': trainee}
    return render(request, 'trainee/traineedetail.html', context)