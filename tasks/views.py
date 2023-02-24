from django.shortcuts import render, HttpResponseRedirect
from .forms import TaskList
from .models import User

# Create your views here.
# This function will add new Item and Show All Item
def add_show(request):
    if request.method == 'POST':
        fm = TaskList(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['title']
            #em = fm.cleaned_data['email']
            ds = fm.cleaned_data['description']
            reg = User(title=nm, description=ds)
            reg.save()
            fm = TaskList()
    else:
        fm = TaskList()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})


#This function will Update/Edit

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = TaskList(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = TaskList(instance = pi)

    return render(request, 'enroll/updatestudent.html', {'form': fm})


# This function will delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

