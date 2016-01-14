__author__ = 'jinjin'

from django.conf.urls import patterns,url
from . import views
from . import Ajout_Lat_Lng
from . import geolocalisation

urlpatterns=patterns(' ',url(r'^$',views.entreprise, name='entreprise'),
                        url(r'ajout/$',Ajout_Lat_Lng.ajout, name='ajout' ),
                        url(r'localisation/$',geolocalisation.localisation, name='localisation' ),
                        url(r'getlocation/$',geolocalisation.get_location, name='get_location' ),
                      url(r'publipostage/$',views.publipostage, name='publipostage' ),
                     url(r'publipostage/(\d+)/$',views.pdf, name='pdf' ),
                     url(r'publipostage2/(\d+)/$',views.pdf2, name='pdf2' ),
                    # url(r'fasong/$',views.fasong, name='fasong' ),


                     )
