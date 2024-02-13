from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from journal.views import entry_list
from journal.views import add_entry, entry_list, profile_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', entry_list, name='home'),
    path('journal/', include('journal.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/profile/', profile_view, name='profile')
]