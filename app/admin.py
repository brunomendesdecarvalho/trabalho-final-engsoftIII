from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import ModelForm
from .models import User, Turma, Disciplina


class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ('estudante', 'professor')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    add_form = UserCreationForm
    list_display = ("username",)
    ordering = ("username",)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active',
                       'estudante', 'professor')}
         ),
    )

    filter_horizontal = ()


admin.site.register(User, CustomUserAdmin)
admin.site.register(Turma)
admin.site.register(Disciplina)
