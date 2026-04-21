from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import TraineeForm
from .models import Trainee


def trainee_list(request):
    trainees = Trainee.objects.all()
    context = {'trainees': trainees}
    return render(request, 'trainee/list.html', context)


def trainee_detail(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    context = {'trainee': trainee}
    return render(request, 'trainee/traineedetail.html', context)


class TraineeCreateView(CreateView):
    model = Trainee
    form_class = TraineeForm
    template_name = 'trainee/addtrainee.html'
    success_url = reverse_lazy('trainee_list')


class TraineeUpdateView(UpdateView):
    model = Trainee
    form_class = TraineeForm
    template_name = 'trainee/update.html'
    success_url = reverse_lazy('trainee_list')


class TraineeDelete(DeleteView):
    model = Trainee
    template_name = 'trainee/delete.html'
    success_url = reverse_lazy('trainee_list')
