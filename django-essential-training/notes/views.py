from django.shortcuts import render
# from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView

from .forms import NotesForm
from .models import Notes

# CLASS-BASED VIEWS

class NotesCreateView(CreateView):
    model = Notes # endpoint knows what it's regarding to
    # fields = ['title', 'text'] # what fields are used
    success_url = '/smart/notes' # redirect user to see the notes they created

    # pass this instead of the fields
    form_class = NotesForm

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

# NON-CLASSBASED VIEWS

# def list(request):
#     all_notes = Notes.objects.all()  # stores all notes
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         # return a 404 page
#         return render(request, 'notes/404.html')
#         # if don't return 404 page can use Http404 response
#         # raise Http404("Note doesn't exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})
