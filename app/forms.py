from django import forms


class TaskForm(forms.Form):
    name = forms.CharField(max_length=200, label='タスク名')
    duration = forms.IntegerField(label="所要時間")
    sharing_rate = forms.IntegerField(label="分担率")
    wage = forms.IntegerField(label="賃金換算")