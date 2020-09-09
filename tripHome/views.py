from django.shortcuts import render
from . models import Trip
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def postData(request):
    if request.is_ajax():
        #do something
        request_data = request.POST
        return HttpResponse("OK")

        try:
            transp = request.POST['transp']
            no_people = request.POST['no_people']
            start = request.POST['start_date']
            end = request.POST['end_date']
            source_city = request.POST['soource_city']

        except (KeyError, Trip.DoesNotExist):
        #return render(request)
            return None


def index(request):

    if request.is_ajax():
        #do something
        request_data = request.POST
        return HttpResponse("OK")

    """View function for home page of site."""
    # trip_type = request.POST.get('trip_type', 'None')
    # try:
    #     transp = request.POST['transp']
    #     no_people = request.POST['no_people']
    #     start = request.POST['start_date']
    #     end = request.POST['end_date']
    #     source_city = request.POST['soource_city']

    # except (KeyError, Trip.DoesNotExist):
    #     #return render(request)
    #     return None


    # #if request.method == 'POST':

    # #trips_list = Trip.objects.orderby('-tripId')[:10]
    # context = {'trip_type': trip_type,
    #             'transp': transp,
    #             'no_people': no_people,
    #             'start': start,
    #             'end': end,
    #             'source_city': source_city}
    # Generate counts of some of the main objects
    num_books = 5
    num_instances = 5
    
    # Available books (status = 'a')
    num_instances_available = 5
    
    # The 'all()' is implied by default.    
    num_authors = 5
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


    # return render(request, 'tripHome/index.html')
