from django.shortcuts import render
from  .models import room
from .forms import roomform

# Create your views here.

def home(request):
    rooms=room.objects.all()
    return render(request,'home.html',{'room':rooms})
def name(request,pk):
    rooms=room.objects.get(id=pk)
    context={'room':rooms}
    return render(request,'name.html',context)
def createroom(request):
    form=roomform()
    return render(request,'room_form.html',context)

    