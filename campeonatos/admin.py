# campeonatos/admin.py

from django.contrib import admin
from .models import Campeonato, Time, Jogo
from django import forms

class TimeAdminForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.current_user
        if not user.is_superuser:
            self.fields['campeonato'].queryset = Campeonato.objects.filter(users=user)

class TimeAdmin(admin.ModelAdmin):
    form = TimeAdminForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.current_user = request.user
        return form

class JogoAdminForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.current_user
        if not user.is_superuser:
            self.fields['campeonato'].queryset = Campeonato.objects.filter(users=user)

class JogoAdmin(admin.ModelAdmin):
    form = JogoAdminForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.current_user = request.user
        return form

class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio', 'data_fim', 'tipo')
    filter_horizontal = ('users',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(users=request.user)

admin.site.register(Campeonato, CampeonatoAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(Jogo, JogoAdmin)
