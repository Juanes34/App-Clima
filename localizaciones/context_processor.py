from .models import locations

def get_locations(request):
    localizaciones = locations.objects.values('nombre','code','pais').order_by('nombre')
    return{
        'localizaciones':localizaciones
    }