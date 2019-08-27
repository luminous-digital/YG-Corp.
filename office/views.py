from django.http import JsonResponse

from .models import Office


def json(request):
    offices = Office.objects.all()
    json = [{"lat": o.lat,
             'lng': o.lng,
             'isHeadquarter': o.is_headquarter,
             "region": o.region,
             "country": o.country,
             "city": o.city,
             "addressLine1": o.address_line_1,
             "addressLine2": o.address_line_2,
             "addressLine3": o.address_line_3,
             "tel": o.tel,
             "mail": o.mail,
             "web": o.web,
             "didYouKnow": o.did_you_know
             } for o in offices]
    return JsonResponse(json, safe=False)
