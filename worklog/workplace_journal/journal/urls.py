from django.urls import path
from .views import add_entry, entry_list
from journal.views import add_entry, entry_list, profile_view



urlpatterns = [
    path('add/', add_entry, name='add_entry'),
    path('', entry_list, name='entry_list'),
    
]