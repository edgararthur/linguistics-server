from django.shortcuts import render, redirect
from .forms import AttendanceForm
from django.http import HttpResponse

def attend_conference(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return HttpResponse("Success")  # Redirect to a success page
    else:
        form = AttendanceForm()
    
    context = {'form': form}
    return render(request, 'app/index.html', context)
# 