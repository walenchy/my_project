

# Create your views here.
import requests
from django.http import JsonResponse

def hello(request):
    visitor_name = request.GET.get('visitor_name', 'Guest')
    client_ip = request.META.get('REMOTE_ADDR', '102.88.69.52')

   
    location = "lagos"  
    temperature = 11  

    response_data = {
        'client_ip': client_ip,
        'location': location,
        'greeting': f'Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}'
    }
    return JsonResponse(response_data)
