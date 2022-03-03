from django.shortcuts import render, get_object_or_404
from .models import Measurements
from .forms import MeasurementModelForm


def view_calc_distance(request):
    obj = get_object_or_404(Measurements, id = 1)
    form = MeasurementModelForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit = False)

        instance.location = 'San Francisco'
        instance.destionation = form.cleaned_data.get('destination')
        instance.distance = 5000

        instance.save()
    
    context = {
        'distance': obj,
        'form': form,
    }

    return render(request, 'index.html', context)