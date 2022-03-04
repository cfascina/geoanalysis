from django.shortcuts import render, get_object_or_404
from .models import Measurements
from .forms import MeasurementModelForm
from geopy.geocoders import Nominatim
from .utils import get_location
from geopy.distance import geodesic


def view_calc_distance(request):
    obj = get_object_or_404(Measurements)
    form = MeasurementModelForm(request.POST or None)
    geolocator = Nominatim(user_agent = 'measurements')
    
    ip = '191.251.56.14'
    location_ = get_location(ip)
    location = geolocator.geocode(location_)
    point_from = (location.latitude, location.longitude)

    if form.is_valid():
        instance = form.save(commit = False)

        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)
        point_to = (destination.latitude, destination.longitude)
        distance = round(geodesic(point_from, point_to).km, 2)        
        
        instance.location = location
        instance.point_from = point_from
        instance.destination = destination
        instance.point_to = point_to
        instance.distance = distance

        instance.save()
    
    context = {
        'distance': obj,
        'form': form,
    }

    return render(request, 'main.html', context)