from django.shortcuts import render
# from django.http import Http404
from django.views.generic import DetailView, ListView

from .models import Notes

# class-based view


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

# Non class-based views

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
