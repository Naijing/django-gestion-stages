 # -*- coding: utf-8 -*-

from django.shortcuts import render_to_response,RequestContext
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django import forms
import geocoder
from geopy.distance import great_circle
from django.http import HttpResponse

from stages.models import Entreprise
import json

class Form(forms.Form):
    adresse = forms.CharField(label='Adresse', max_length=256)
    ville = forms.CharField(label='Ville', max_length=256)
    pays = forms.CharField(label='Pays', max_length=256)
    rayon= forms.IntegerField(label='Rayon (Mètres)')


def get_location(request):
    if request.method == "POST":
        form=Form(request.POST)
        if form.is_valid():

            a=request.POST['adresse']
            v=request.POST['ville']
            p=request.POST['pays']
            r=float(request.POST['rayon'])

            g = geocoder.google(a+','+v+','+p)
            res=g.latlng
            point_d=(res[0], res[1])


            entreprises = Entreprise.objects.all()
            list=[]

            for e in entreprises:
                point_e=(e.latitude, e.longitude)
                distance=great_circle(point_d, point_e).meters

                if distance <=r :
                    list.append(e)




            return render_to_response('buffer.html', {'res':res, 'rayon':r, 'entreprises': entreprises, 'adresse':a, 'ville':v, 'pays':p, 'rayon':r, 'list_entreprises':list}, context_instance=RequestContext(request))
    else:
        form = Form()
        e = Entreprise.objects.values()
    return render_to_response('formulaire_buffer.html', {'form':form,'entreprises': e},context_instance=RequestContext(request))


def localisation(request):

	e = Entreprise.objects.values()

	return render_to_response('geo.html', {'entreprises': e},context_instance=RequestContext(request))
