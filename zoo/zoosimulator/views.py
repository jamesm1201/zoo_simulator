from django.shortcuts import render, redirect
from django.http import JsonResponse
from .zoosim import Zoo

#I use a global variable here due to time contstraints 
zoo = Zoo()

def zoo_home(request):
    """Render the home page with the current zoo status."""
    zoo_status = zoo.get_zoo_status()
    return render(request, 'home.html', {'zoo': zoo})

def pass_time(request):
    """Simulate the passing of 1 hour in the zoo."""
    zoo.add_hour()
    return redirect('zoo_home')

def feed_zoo(request):
    """Feed the animals and improve their health."""
    zoo.feed()
    return redirect('zoo_home')



