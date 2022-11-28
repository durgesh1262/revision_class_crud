from django.shortcuts import render, redirect
from .forms import Studentregistration
from .models import Student
from django.views.generic.base import View


class Add(View):
    def get(self, request):
        form = Studentregistration()
        return render(request, 'add.html', {'form': form})
    
    def post(self, request):
        if request.method == 'POST':
            form =  Studentregistration(request.POST)
            if form.is_valid():
                form.save()
                return redirect('show')
            
class Show(View):
    def get(self, request):
        form = Student.objects.all()
        return render(request, 'show.html', {'form': form})  
             

class Edit(View):
    def get(self, request, id):
        fm = Student.objects.get(pk = id)
        form = Studentregistration( instance = fm)       
        return render(request, 'edit.html', {'form': form})
    
    
    def post(self, request, id):
        fm = Student.objects.get(pk = id)
        form = Studentregistration(request.POST, instance = fm)
        if form.is_valid():
            form.save()
            return redirect('show')
                     
class Delete(View):
     def get(self, request, id):
        fm = Student.objects.get(pk = id)
        fm.delete()   
        return redirect('show')
                 
            
    

# Create your views here.
