from django.shortcuts import render, redirect
from .forms import AttendanceForm

def attend_conference(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = AttendanceForm()
    
    context = {'form': form}
    return render(request, 'attend.html', context)
