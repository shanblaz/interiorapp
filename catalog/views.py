from django.shortcuts import render

# Create your views here.
from catalog.models import bedroom, kitchen




def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_bedroom = bedroom.objects.all().count()
    num_kitchen = kitchen.objects.all().count()
    
    # Available books (status = 'a')
  
    
    context = {
        'num_bedroom': num_bedroom,
        'num_kitchen': num_kitchen,

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

    