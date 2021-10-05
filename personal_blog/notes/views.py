from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import Topic, Note
from .forms import NoteForm, TopicCreateForm
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class TopicListView(LoginRequiredMixin, ListView):
    model = Topic
    context_object_name = 'topic_list'
    template_name = '2_notes/topic_list.html'

    def get_context_data(self, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)
        topic_list =  Topic.objects.filter(user=self.request.user).all()
        context.update({'topic_list':topic_list})
        return context

class TopicDetailView(LoginRequiredMixin, DetailView):
    model = Topic
    context_object_name = 'topic'
    template_name = '2_notes/topic_detail.html'


class TopicCreateView(LoginRequiredMixin,CreateView):
    model = Topic
    template_name = "2_notes/topic_create.html"
    form_class = TopicCreateForm
    login_url = 'account_login'
    success_url = reverse_lazy('notes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
def TopicDeleteFunction(request, pk):
    topic = Topic.objects.get(user=request.user, id=pk)
    if request.method == "GET":
        return render(request, "2_notes/topic_delete.html", {"topic":topic})
    else:
        if request.user.is_authenticated:
            title = request.POST['title']
            if title == topic.topic:
                Topic.objects.filter(user=request.user,id=pk).delete()
                return redirect("notes")
            else:
                return render(request, "2_notes/topic_delete.html", {"topic": topic, "message": "The title didn't match"})
        else:
            return redirect("account_login")

class TopicUpdateView(LoginRequiredMixin,UpdateView):
    model = Topic
    fields = ['topic',]
    login_url = 'account_login'
    template_name = "2_notes/topic_update.html"
    success_url = reverse_lazy('notes')

@login_required
def NoteDetailFunction(request,topic_pk,note_pk):
    topic = Topic.objects.get(user=request.user,id=topic_pk)
    note = topic.notes.get(user=request.user, uuid=note_pk)
    return render(request, '2_notes/note_detail.html', {'topic':topic, 'note':note})

@login_required
def NoteCreateFunction(request, pk):
    if request.user.is_authenticated:
        if request.method == "POST":   
            form = NoteForm(request.POST)
            if form.is_valid():
                note_item = form.save(commit=False)
                note_item.user = request.user
                note_item.topic_id = pk
                note_item.save()
                return redirect('topic_detail', pk=pk)
            else:
                return redirect('topic_detail', pk=pk)
        else:
            form = NoteForm()
            topic = Topic.objects.get(user=request.user, id=pk)
            num = topic.notes.count()
            form.fields['order'].initial = num + 1
            return render(request, '2_notes/note_create.html', {'topic':topic, 'form':form})
    else:
        return redirect('account_login')

@login_required
def NoteUpdateFunction(request, topic_pk, note_pk):
    if request.user.is_authenticated:
        topic = Topic.objects.get(user=request.user, id=topic_pk)
        if request.method == "POST":
            note_item = Note.objects.get(uuid=note_pk)
            note_item.title = request.POST['title']
            note_item.order = request.POST['order']
            note_item.summary = request.POST['summary']
            note_item.content = request.POST['content']
            note_item.save()
            return redirect("note_detail", topic_pk=topic_pk, note_pk=note_pk)    
        else:
            note = Note.objects.get(user=request.user, uuid=note_pk)
            initial_data = {"title":note.title,'order':note.order, "summary": note.summary, "content":note.content}
            form = NoteForm(request.POST or None,initial=initial_data)
        return render(request, "2_notes/note_update.html", {"topic":topic,"note":note, "form":form})
    else:
        return redirect('account_login')

@login_required
def NoteDeleteFunction(request, topic_pk, note_pk):
    topic = Topic.objects.get(user=request.user, id=topic_pk)
    note = Note.objects.get(user=request.user, uuid=note_pk)
    if request.method == "POST":
        if request.user.is_authenticated:
            if request.POST['title'] == note.title:
                note.delete()
                return redirect("topic_detail", pk=topic_pk)
            else:
                return render(request, "2_notes/note_delete.html", {"topic":topic, "note":note, "message": "The title didn't match"} )
        else:
            return redirect('account_login')
    else:
        return render(request, "2_notes/note_delete.html", {"topic":topic, "note":note})

#def FileCleanFunction(request):
#    if request.user.is_superuser:
#        all_imgs = []
#        file_del = 0
#        dir_del = 0
#        note_list = Note.objects.all()
#        for note in note_list:
#            soup = BeautifulSoup(note.content, "lxml")
#            all_img = soup.findAll('img')
#            for img in all_img:
#                all_imgs.append(img.get("src")[1::])
#
#        path = "media/uploads"
#        for subdir, dirs, files in os.walk(path):
#            try:
#                os.rmdir(subdir)
#                dir_del += 0
#            except:
#                continue
#            for filename in files:
#                filepath = subdir + os.sep + filename
#                if not filepath  in all_imgs:
#                    os.remove(filepath)
#                    file_del += 1
#
#        print("number of files deleted are ", file_del)
#        print("number of dir deleted are ", dir_del)
#        return redirect('topic_list')
#    else:
#        return redirect('account_login')
#