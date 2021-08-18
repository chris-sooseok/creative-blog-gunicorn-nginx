from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Date, Todo
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .forms import TodoUpdateForm, DateCreateForm
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

class DateListView(LoginRequiredMixin, ListView):
    model = Date
    template_name = '1_todos/date_list.html'
    login_url = 'account_login'
    def get_context_data(self, **kwargs):
        context = super(DateListView, self).get_context_data(**kwargs)
        date_list = Date.objects.filter(user=self.request.user).all()
        page = self.request.GET.get('page')
        paginator = Paginator(date_list, 11)
        page_obj = paginator.get_page(page)
        context.update({'page_obj':page_obj})
        return context
  
class DateDetailView(LoginRequiredMixin, DetailView):
    model = Date
    context_object_name = 'date'
    template_name = '1_todos/date_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DateDetailView, self).get_context_data(**kwargs)
        page = self.request.GET.get('page')
        paginator = Paginator(Date.objects.all(), 11)
        page_obj = paginator.get_page(page)
        context.update({'page_obj':page_obj})
        return context


class DateCreateView(LoginRequiredMixin, CreateView):
    model = Date
    template_name = '1_todos/date_create.html'
    form_class = DateCreateForm
    login_url = 'account_login'
    success_url = reverse_lazy('date_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(DateCreateView, self).get_context_data(**kwargs)
        date_list = Date.objects.filter(user=self.request.user).all()
        page = self.request.GET.get('page')
        paginator = Paginator(date_list, 11)
        page_obj = paginator.get_page(page)
        context.update({'page_obj':page_obj})
        return context


class DateDeleteView(LoginRequiredMixin, DeleteView):
    model = Date
    template_name = '1_todos/date_delete.html'
    login_url = 'account_login'
    success_url = reverse_lazy('date_list')

    def get_context_data(self, **kwargs):
        context = super(DateDeleteView, self).get_context_data(**kwargs)
        page = self.request.GET.get('page')
        paginator = Paginator(Date.objects.all(), 11)
        page_obj = paginator.get_page(page)
        context.update({'page_obj':page_obj})
        return context

@login_required
def TodoCreateFunction(request,pk):
    date = Date.objects.get(id=pk)

    date_list = Date.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(date_list, 11)
    page_obj = paginator.page(page)

    if request.method == "GET":
        return render(request, '1_todos/todo_create.html', {'date':date, 'page_obj':page_obj})
    elif request.method == "POST":
        if request.user.is_authenticated:
            user = request.user
            title = request.POST['title']
            start_time = request.POST['start_time']
            end_time = request.POST['end_time']
            task = request.POST['task']
            Todo(user=user,title=title,start_time=start_time,end_time=end_time,task=task,date=date).save()

            return redirect('date_detail', pk=pk)
        else:
            return redirect('account_login')

@login_required
def TodoDeleteFunction(request,date_pk,todo_pk):
    if request.method == "GET":
        date_list = Date.objects.filter(user=request.user).all()
        page = request.GET.get('page', 1)
        paginator = Paginator(date_list, 11)
        page_obj = paginator.page(page)
        date = Date.objects.get(user=request.user,id=date_pk)
        todo_item = Todo.objects.get(user=request.user,id=todo_pk)
        return render(request, '1_todos/todo_delete.html', {'date':date, 'todo':todo_item, 'page_obj':page_obj})
    
    elif request.method == "POST":
        if request.user.is_authenticated:
            todo_item = Todo.objects.get(user=request.user,id=todo_pk)
            todo_item.delete()
            return redirect('date_detail', pk=date_pk)
        else:
            return redirect('account_login')

@login_required
def TodoUpdateFunction(request, date_pk, todo_pk ):

    if request.method == "POST":
        if request.user.is_authenticated:
            todo_item = Todo.objects.get(user=request.user,id=todo_pk)
            todo_item.title = request.POST['title']
            todo_item.start_time = request.POST['start_time']
            todo_item.end_time = request.POST['end_time']
            todo_item.task = request.POST['task']
            todo_item.save()
            return redirect("date_detail", pk=date_pk)
        else:
            return redirect('account_login')
    else:
        date_list = Date.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(date_list, 11)
        page_obj = paginator.page(page)
        date = Date.objects.get(pk=date_pk)
        todo = Todo.objects.get(id=todo_pk)
        initial_data = {"title":todo.title, "task":todo.task}
        time = {'start_time': todo.start_time.strftime("%H:%M:%S"), 'end_time': todo.end_time.strftime("%H:%M:%S")}
        form = TodoUpdateForm(request.POST or None, initial=initial_data)
        return render(request, "1_todos/todo_update.html", {"date":date, "todo":todo, "form":form, "time":time, "page_obj":page_obj})
