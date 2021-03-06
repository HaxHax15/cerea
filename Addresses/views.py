from django.shortcuts import render,get_object_or_404,get_list_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect

@login_required
def countries(request, id, title, prefix):
    if prefix=='countries':
        if not id:
            objects_list = Country.objects.all()
        else:
            objects_list = get_list_or_404(Country,pk=id)
    elif prefix=='regions':
        if not id:
            objects_list = Region.objects.all()
        else:
            objects_list = get_list_or_404(Region,pk=id)
    elif prefix=='cities':
        if not id:
            objects_list = City.objects.all()
        else:
            objects_list = get_list_or_404(City,pk=id)
    elif prefix=='streets':
        if not id:
            objects_list = Street.objects.all()
        else:
            objects_list = get_list_or_404(Street,pk=id)


    context = {'objects_list':objects_list, 'title':title, 'prefix':prefix}
    return render(request, "tpl/countries.html",context)

@login_required
def places(request, place_id):
    places_list = Place.objects.all()
    context = {'places_list':places_list}
    return render(request, "tpl/places.html",context)

@login_required
def houses(request, house_id):
    houses_list = House.objects.all()
    context = {'houses_list':houses_list}
    return render(request, "tpl/houses.html",context)


def editcountry(request,country_id, title):
    country = get_object_or_404(Country, pk = country_id)
    if request.method == 'POST':
        form = CountryForm(request.POST,instance=country)
        if form.is_valid():
            country = form.save()
            return HttpResponseRedirect('/adminka/locations/countries')
    else:
        form = CountryForm(instance=country)
    return render(request, 'tpl/forms/AddressEditForm.html', {'form': form, 'title':title})


def editplace(request,place_id, title):
    place = get_object_or_404(Place, pk = place_id)
    if request.method == 'POST':
        form = PlaceForm(request.POST,instance=place)
        if form.is_valid():
            place = form.save()
            return HttpResponseRedirect('/adminka/locations/places')
    else:
        form = PlaceForm(instance=place)
    return render(request, 'tpl/forms/AddressEditForm.html', {'form': form, 'title':title})


def editregion(request,region_id, title):
    region = get_object_or_404(Region, pk = region_id)
    if request.method == 'POST':
        form = RegionForm(request.POST,instance=region)
        if form.is_valid():
            region = form.save()
            return HttpResponseRedirect('/adminka/locations/regions')
    else:
        form = RegionForm(instance=region)
    return render(request, 'tpl/forms/AddressEditForm.html', {'form': form, 'title':title})


def editcity(request,city_id, title):
    city = get_object_or_404(City, pk = city_id)
    if request.method == 'POST':
        form = CityForm(request.POST,instance=city)
        if form.is_valid():
            city = form.save()
            return HttpResponseRedirect('/adminka/locations/cities')
    else:
        form = CityForm(instance=city)
    return render(request, 'tpl/forms/AddressEditForm.html', {'form': form, 'title':title})

def editstreet(request,street_id, title):
    street = get_object_or_404(Street, pk = street_id)
    if request.method == 'POST':
        form = StreetForm(request.POST,instance=street)
        if form.is_valid():
            street = form.save()
            return HttpResponseRedirect('/adminka/locations/streets')
    else:
        form = StreetForm(instance=street)
    return render(request, 'tpl/forms/AddressEditForm.html', {'form': form, 'title':title})

def edithouse(request,house_id, title):
    house = get_object_or_404(House, pk = house_id)
    if request.method == 'POST':
        form = HouseForm(request.POST,instance=house)
        if form.is_valid():
            house = form.save()
            return HttpResponseRedirect('/adminka/locations/houses')
    else:
        form = HouseForm(instance=house)
    return render(request, 'tpl/forms/AddressEditForm.html', {'form': form, 'title':title})