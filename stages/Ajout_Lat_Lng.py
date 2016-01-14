from django.http import HttpResponse
import urllib.request
import json
import urllib.parse
from stages.models import Entreprise


def ajout(request):
    for e in Entreprise.objects.all():

        a=e.adresse
        v=e.ville
        c=e.codePostal
        p=e.pays


        param={'address':a+','+v+','+c+','+p}
        params = urllib.parse.urlencode(param)
        url="https://maps.googleapis.com/maps/api/geocode/json?%s" % params

        response = urllib.request.urlopen(url)
        jsongeocode = response.read()
        code=jsongeocode.decode('utf-8')

        dic=json.loads(code)
        if  dic['results']:
            e.latitude=dic['results'][0]['geometry']['location']['lat']
            e.longitude=dic['results'][0]['geometry']['location']['lng']
            e.save()



    return HttpResponse('hello')






