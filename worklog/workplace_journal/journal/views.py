from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Entry
from .forms import EntryForm

@login_required
def add_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.save()
            return redirect('entry_list')
    else:
        form = EntryForm()
    return render(request, 'journal/add_entry.html', {'form': form})

@login_required
def entry_list(request):
    if request.user.is_superuser:
        # Jeśli użytkownik jest administratorem, pobierz wszystkie wpisy
        entries = Entry.objects.all()
    else:
        # W przeciwnym razie pobierz tylko wpisy dodane przez użytkownika
        entries = Entry.objects.filter(author=request.user)
    return render(request, 'journal/entry_list.html', {'entries': entries})

def profile_view(request):
    return render(request, 'journal/profile.html')
