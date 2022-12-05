from django.contrib.auth import get_user_model
list(get_user_model().objects.filter(is_superuser=True).values_list('username', flat=True))
