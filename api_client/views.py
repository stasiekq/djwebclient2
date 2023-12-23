from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
import requests

API_URL = "https://stasiekq.pythonanywhere.com/"

def index(request):
    return render(request, 'api_client/index.html')


def booking_delete(request, booking_id):
    response = requests.get(API_URL + 'api/' + str(booking_id) + '/')
    
    if response.status_code == 404:
        return HttpResponse('Booking not found')

    booking = response.json()

    if request.method == 'POST':
        try:
            response = requests.delete(API_URL + 'api/' + str(booking_id) + '/')
            response.raise_for_status()
            return redirect('/booking_list/')
        except requests.exceptions.RequestException as e:
            return HttpResponse(f'Error: {e}', status=500)

    context = {
        'booking': booking
    }

    return render(request, 'api_client/booking_delete.html', context)

def booking_list(request):
    response = requests.get(API_URL + 'api/')
    
    if response.status_code == 200:
        bookings = response.json()
        return render(request, 'api_client/booking_list.html', {'bookings': bookings})
    else:
        return HttpResponse('Error getting bookings')

def booking_details(request, booking_id):
    try:
        response = requests.get(API_URL + 'api/' + str(booking_id) + '/')
        response.raise_for_status()
        booking_data = response.json()
    except requests.exceptions.RequestException as e:
        return HttpResponse(f'Error: {e}', status=500)

    if not booking_data:
        return HttpResponse('Booking not found', status=404)

    context = {
        'booking': booking_data
    }
    return render(request, 'api_client/booking_details.html', context)

def booking_create(request):
    if request.method == 'POST':
        form = CreateBookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            room = form.cleaned_data['room']
            details = form.cleaned_data['details']

            # Sprawdź, czy numer pokoju jest większy niż 0
            if room < 1:
                return HttpResponse('Room number must be greater than or equal to 1', status=400)

            # Wyślij dane do API w celu utworzenia nowej rezerwacji
            try:
                response = requests.post(API_URL + 'api/', json={'name': name, 'room': room, 'details': details})
                response.raise_for_status()
                return redirect('/booking_list/')  # Przekieruj na stronę z listą rezerwacji po utworzeniu
            except requests.exceptions.RequestException as e:
                return HttpResponse(f'Error: {e}', status=500)
    else:
        form = CreateBookingForm()

    return render(request, 'api_client/booking_create.html', {'form': form})

def booking_update(request, booking_id):
    response = requests.get(API_URL + 'api/' + str(booking_id) + '/')
    
    if response.status_code == 404:
        return HttpResponse('Booking not found')

    booking = response.json()

    if request.method == 'POST':
        # Pobierz dane z formularza
        name = request.POST.get('name')
        room = request.POST.get('room')
        details = request.POST.get('details')

        # Wyślij dane do API w celu aktualizacji rezerwacji
        try:
            response = requests.put(API_URL + 'api/' + str(booking_id) + '/', json={'name': name, 'room': room, 'details': details})
            response.raise_for_status()
            return redirect('/booking_list/')
        except requests.exceptions.RequestException as e:
            return HttpResponse(f'Error: {e}', status=500)

    context = {
        'booking': booking
    }

    return render(request, 'api_client/booking_update.html', context)