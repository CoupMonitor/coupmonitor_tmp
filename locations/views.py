from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import csrf
#from jquery_locationpicker.forms import JqueryLocationPicker
from .models import Location
from .forms import LocationFormArabic,LocationFormEnglish

def list_locations(request,
		   template_name='locations/list.html',
                   page_count=25):

    #language = request.GET.get('language', 'en')
    language = request.LANGUAGE_CODE
    locations_list = Location.objects.language(language).all()
    paginator = Paginator(locations_list, page_count)

    page = request.GET.get('page')
    try:
      locations = paginator.page(page)
    except PageNotAnInteger:
      # If page is not an integer, deliver first page
      locations = paginator.page(1)
    except EmptyPage:
      # If page is out of range deliver last page of results
      locations = paginator.page(paginator.num_pages)


    return render_to_response(template_name, {"locations": locations})


def location_detail(request, lid):
    pass

def add_location(request, template_name='locations/add.html', page_count=25, language='en'):
    form_ar = LocationFormArabic(request.POST or None)
    form_en = LocationFormEnglish(request.POST or None)
    # loc_picker = JqueryLocationPicker(request.POST or None)
    context = {}
    context.update(csrf(request))
    context.update({"formen": form_en, "formar": form_ar})

    if form_ar.is_valid() and form_en.is_valid() and loc_picker.is_valid():
        new_location = form.save(commit=False)
        print new_location
        new_location.save()
        loc_picker.latitiude
        loc_picker.longitude

    return render_to_response( template_name, context )


def update_location(request, lid):
    pass

def delete_location(request, lid):
    pass




