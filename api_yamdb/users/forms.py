from django.contrib.auth import get_user_model

from django.forms import ModelForm

User = get_user_model()


class UserForm(ModelForm):
    """Форма для модели CustomUser."""

    model = User
