from django.contrib import admin
from .models import *
@admin.register(Patient)
@admin.register(Answer)
@admin.register(QuesAns)
@admin.register(Results)
class UserAdmin(admin.ModelAdmin):
    list_display=('Pid','name','age')

class UserAdmin(admin.ModelAdmin):
    list_display = ('P_id', 'Ansid')

class UserAdmin(admin.ModelAdmin):
    list_display=('Qid','Question')

class UserAdmin(admin.ModelAdmin):
    list_display = ('Q_id', 'Ansid', 'Answers')


# Register your models here.
