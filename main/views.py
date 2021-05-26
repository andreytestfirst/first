from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from .forms import *


class ShowPerson(generic.ListView):
    model = PersonModel
    # context_object_name = 'person'       указываем как будет называться имя в контексте для вывода в html


class ShowPer(generic.View):
    def get(self, request, **kwargs):
        data = PersonModel.objects.all()
        form = PersonForm
        context = {'personmodel_list': data, 'form':form}
        return render(request, 'main/personmodel_list.html', context)

    def post(self, request, **kwargs):
        form = PersonForm(request.POST)
        if form.is_valid():
            res = form.save(commit=False)
            res.set_password(form.cleaned_data['password'])
            print(res.password)
            res.save()
        else:
            return render(request, 'main/personmodel_list.html')
        return render(request,'main/personmodel_list.html', {'ответ': 'Данные сохранены'})


class SavePerson(generic.CreateView):
    model = PersonModel
    form_class = PersonForm
    template_name = 'main/personmodel_list.html'
    success_url = reverse_lazy('main:shwper')
    # fields= ['email','first_name','username','last_name','password']