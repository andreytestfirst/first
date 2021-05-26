from django.forms import ModelForm
from .models import PersonModel


class PersonForm(ModelForm):
    def save(self, commit=False):
        res = super().save(commit=False)
        res.set_password(self.cleaned_data['password'])
        res.save()
        return res

    class Meta:
        fields = ['email', 'first_name', 'username', 'last_name', 'password']
        model = PersonModel
#t
