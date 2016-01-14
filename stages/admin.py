from django.contrib import admin


from stages.models import Contact
from stages.models import Entreprise
from stages.models import Pays
from stages.models import GestionDeTaxe
from stages.models import VillesDeFrance


class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'libelle', 'email','telephone')
	
	
class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ('nom', 'adresse', 'codePostal','ville','pays', 'telephone','latitude', 'longitude')
	

class PaysAdmin(admin.ModelAdmin):
    list_display = ('nom_fr_fr','nom_en_gb','code', 'alpha2', 'alpha3')

	
class VillesDeFranceAdmin(admin.ModelAdmin):
    list_display = ('nom_reel', 'code_postal', 'surface','longitude_grd','latitude_grd')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Entreprise, EntrepriseAdmin)
admin.site.register(Pays, PaysAdmin)
admin.site.register(VillesDeFrance, VillesDeFranceAdmin)



@admin.register(GestionDeTaxe)
class GestionDeTaxeAdmin(admin.ModelAdmin):
    list_display=('entreprise','taxePaye','dateTaxe','dateContact', 'contact','modalite')

