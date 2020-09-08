from django.shortcuts import render

# Create your views here.
def index(request):
    """View function for home page of site."""
    trip_type = request.POST.get('trip_type', 'None')
    try:
        transp = request.POST['transp']
        no_people = request.POST['no_people']
        start = request.POST['start_date']
        end = request.POST['end_date']
        source_city = request.POST['soource_city']

    except (KeyError, Trip.DoesNotExist):
        #return render(request)
        return None


    #if request.method == 'POST':

    #trips_list = Trip.objects.orderby('-tripId')[:10]
    context = {'trip_type': trip_type,
                'transp': transp,
                'no_people': no_people,
                'start', start,
                'end': end,
                'source_city': source_city}

    return render(request, 'tripHome/index.html', context)
