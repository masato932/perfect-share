from django.views.generic import View
from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/index.html', {
        })

class AddView(View):
    def get(self, request, *args, **kwargs):
        year = self.kwargs['year']
        month = self.kwargs['month']
        day = self.kwargs['day']
        task_data = Task.objects.all()
        return render(request, 'app/add.html', {
            'task_data':task_data,
            'year':year,
            'month':month,
            'day':day,
        })

class TaskEditView(View):
    def get(self, request, *args, **kwargs):
        year = self.kwargs['year']
        month = self.kwargs['month']
        day = self.kwargs['day']
        task_data = Task.objects.get(id=self.kwargs['pk'])
        form = TaskForm(
            request.POST or None,
            initial={
                'name': task_data.name,
                'duration': task_data.duration,
                'sharing_rate': task_data.sharing_rate,
                'wage': task_data.wage,
            }
        )

        return render(request, 'app/task_form.html', {
            'form': form,
            'year':year,
            'month':month,
            'day':day,
        })
    
    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST or None)
        year = self.kwargs['year']
        print(year)

        if form.is_valid():
            task_data = Task.objects.get(id=self.kwargs['pk'])
            task_data.name = form.cleaned_data['name']
            task_data.duration = form.cleaned_data['duration']
            task_data.sharing_rate = form.cleaned_data['sharing_rate']
            task_data.wage = form.cleaned_data['wage']
            task_data.save()
            # return redirect('index')
            print(form)
            year=int(form.cleaned_data['year'])
            month=int(form.cleaned_data['month'])
            day=int(form.cleaned_data['day'])
            return redirect('add', year, month, day)

        return render(request, 'app/task_form.html', {
            'form': form
        })