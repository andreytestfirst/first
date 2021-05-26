
from django.urls import path, include
from django.views.generic import ListView,CreateView
from .models import PersonModel
from .views import ShowPerson, ShowPer,SavePerson
from .forms import PersonForm
app_name = 'main'

urlpatterns = [
    path('', ShowPerson.as_view(), name = 'show_person'),
    path('2/', ShowPer.as_view(), name = 'shwper'),
    path('3/', SavePerson.as_view(), name = 'shwper2'),
    path('4/', ListView.as_view(model=PersonModel, template_name='main/personmodel_list.html'), name = 'show4'),
 ]

