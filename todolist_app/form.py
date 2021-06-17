

from django import forms

from todolist_app.models import Tasklist

class TaskForm(forms.Form):
    class Meta:
        model = Tasklist
        fields = ('tasks','done')

