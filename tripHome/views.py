from django.shortcuts import render

# Create your views here.
def index(request):
    """View function for home page of site."""

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
