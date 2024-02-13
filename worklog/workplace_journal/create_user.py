# Importuj konfigurację Django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "workplace_journal.settings")

# Załaduj aplikację Django
import django
django.setup()

# Teraz możesz tworzyć użytkowników
from django.contrib.auth.models import User

# Tworzenie użytkownika
user = User.objects.create_user('user1', 'user1@example.com', 'user1233')

# Ustawienie atrybutu is_staff na False, co oznacza, że użytkownik nie jest administratorem
user.is_staff = False

# Zapisanie zmian
user.save()

print("Utworzono użytkownika 'user' z hasłem 'user123'.")
