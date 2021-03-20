from django.shortcuts import render
from .models import QuesAns
def add_show(request):
    ques_data = QuesAns.all()
    return render(request,'forms.html' ,{'QuesAns':ques_data})

# Create your views here.
