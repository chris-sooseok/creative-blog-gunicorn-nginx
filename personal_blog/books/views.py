from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import Book, Chapter
from .forms import ChapterForm, BookCreateForm
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = '4_books/book_list.html'

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = '4_books/book_detail.html'

class BookCreateView(LoginRequiredMixin,CreateView):
    model = Book
    template_name = "4_books/book_create.html"
    form_class = BookCreateForm
    login_url = 'account_login'
    success_url = reverse_lazy('book_list')

def BookDeleteFunction(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == "GET":
        return render(request, "4_books/book_delete.html", {"book":book})
    else:
        if request.user.is_authenticated:
            title = request.POST['title']
            if title == book.title:
                Book.objects.filter(id=pk).delete()
                return redirect("book_list")
            else:
                return render(request, "4_books/book_delete.html", {"book": book, "message": "The title didn't match"})
        else:
            return redirect("account_login")

class BookUpdateView(LoginRequiredMixin,UpdateView):
    model = Book
    fields = ['title',]
    login_url = 'account_login'
    template_name = "4_books/book_update.html"
    success_url = reverse_lazy('book_list')

def ChapterDetailFunction(request,book_pk,chapter_pk):
    book = Book.objects.get(id=book_pk)
    chapter = book.chapters.get(id=chapter_pk)
    return render(request, '4_books/chapter_detail.html', {'book':book, 'chapter':chapter})

def ChapterCreateFunction(request, pk):
    if request.user.is_authenticated:
        if request.method == "POST":   
            form = ChapterForm(request.POST)
            if form.is_valid():
                note_item = form.save(commit=False)
                note_item.book_id = pk
                note_item.save()
                return redirect('book_detail', pk=pk)
        
        else:
            form = ChapterForm()
            book = Book.objects.get(id=pk)
            return render(request, '4_books/chapter_create.html', {'book':book, 'form':form})
    else:
        return redirect('account_login')

def ChapterUpdateFunction(request, book_pk, chapter_pk):
    if request.user.is_authenticated:
        book = Book.objects.get(id=book_pk)
        if request.method == "POST":
            chapter_item = Chapter.objects.get(id=chapter_pk)
            chapter_item.chapter = request.POST['chapter']
            chapter_item.title = request.POST['title']
            chapter_item.content = request.POST['content']
            chapter_item.save()
            return redirect("chapter_detail", book_pk=book_pk, chapter_pk=chapter_pk)    
        else:
            chapter = Chapter.objects.get(id=chapter_pk)
            initial_data = {"title":chapter.title,'chapter':chapter.chapter, "content":chapter.content}
            form = ChapterForm(request.POST or None,initial=initial_data)
        return render(request, "4_books/chapter_update.html", {"book":book,"chapter":chapter, "form":form})
    else:
        return redirect('account_login')

def ChapterDeleteFunction(request, book_pk, chapter_pk):
    book = Book.objects.get(id=book_pk)
    chapter = Chapter.objects.get(id=chapter_pk)
    if request.method == "POST":
        if request.user.is_authenticated:
            if request.POST['title'] == chapter.title:
                chapter.delete()
                return redirect("topic_detail", pk=book_pk)
            else:
                return render(request, "4_books/chapter_delete.html", {"book":book, "chapter":chapter, "message": "The title didn't match"} )
        else:
            return redirect('account_login')
    else:
        return render(request, "4_books/chapter_delete.html", {"book":book, "chapter":chapter})
