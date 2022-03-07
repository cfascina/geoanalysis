import folium

from django.shortcuts import render
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .forms import MeasurementModelForm
from .utils import get_location, get_center_coords, get_zoom


def view_calc_distance(request):
    form = MeasurementModelForm(request.POST or None)
    geolocator = Nominatim(user_agent = 'measurements')
    destination = None
    distance = None
    
    ip = '191.251.56.14'
    location_ = get_location(ip)
    location = geolocator.geocode(location_)
    point_from = (location.latitude, location.longitude)

    m = folium.Map(
        location = get_center_coords(location.latitude, location.longitude), 
        width = 800, 
        height = 500,
        zoom_start = 8
    )

    folium.Marker(
        [location.latitude, location.longitude], 
        tooltip = 'Click here', 
        popup = location.address,
        icon = folium.Icon(color = 'green')
    ).add_to(m)
    

    if form.is_valid():
        instance = form.save(commit = False)

        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)
        point_to = (destination.latitude, destination.longitude)
        distance = round(geodesic(point_from, point_to).km, 2)        
     
        m = folium.Map(
            location = \
                get_center_coords(
                    location.latitude, 
                    location.longitude, 
                    destination.latitude, 
                    destination.longitude
                ), 
            width = 800, 
            height = 500,
            zoom_start = get_zoom(distance)
        )

        folium.Marker(
            [location.latitude, location.longitude], 
            tooltip = 'Click here', 
            popup = location.address,
            icon = folium.Icon(color = 'green')
        ).add_to(m)

        folium.Marker(
            [destination.latitude, destination.longitude], 
            tooltip = 'Click here', 
            popup = destination.address,
            icon = folium.Icon(color = 'blue')
        ).add_to(m)

        line = folium.PolyLine(
            locations = [point_from, point_to],
            width = 5,
            color = 'blue' 
        ).add_to(m)

        instance.location = location
        instance.point_from = point_from
        instance.destination = destination
        instance.point_to = point_to
        instance.distance = distance
        instance.save()
    
    m = m._repr_html_()

    context = {
        'form': form,
        'map': m,
        'destination': destination,
        'distance': distance,
    }

    return render(request, 'main.html', context)