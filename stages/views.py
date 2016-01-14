from django.shortcuts import render_to_response, RequestContext
from stages.models import Entreprise, GestionDeTaxe
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django import forms
from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import ugettext_lazy as _




def entreprise(request):
    entreprises=Entreprise.objects.all()
    page_size=10
    after_range_num = 5
    before_range_num = 4
    try:
        page = int(request.GET.get("page",1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    paginator = Paginator(entreprises,page_size)
    try:
        entreprises = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        entreprises = paginator.page(1)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+before_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+before_range_num]

   # entreprises = Entreprise.objects.values()
   # return render_to_response('entreprise_list.html', {'entreprises':entreprises})




    return render_to_response('entreprise_list.html', {'page_objects':entreprises,'page_range':page_range})


class TaxeIsPay(ModelForm):

    class Meta:
        model = GestionDeTaxe
        fields = ('taxePaye',)
        labels = {
            "taxePaye": _("Paiement effectué"),
        }
        



def publipostage(request):
    if request.method == "POST":
        form=TaxeIsPay(request.POST)
        if form.is_valid():

            arrayEntreprise=[]

            taxe=request.POST['taxePaye']
            if taxe=='NON':

                g=GestionDeTaxe.objects.filter(taxePaye=taxe)

                for e in g:
                    arrayEntreprise.append(e.entreprise)

                return render_to_response('postage_process.html', {'entreprises':arrayEntreprise}, context_instance=RequestContext(request))
            elif taxe=='OUI':
                g=GestionDeTaxe.objects.filter(taxePaye=taxe)

                for e in g:
                    arrayEntreprise.append(e.entreprise)

                return render_to_response('postage_process2.html', {'entreprises':arrayEntreprise}, context_instance=RequestContext(request))

    else:
        form = TaxeIsPay()

        return render_to_response('formulaire_publipostage.html', {'form':form,},context_instance=RequestContext(request))








def pdf(request,a):

    e=Entreprise.objects.get(pk=a)

    nom=e.nom
    adresse=e.adresse
    codePostal=e.codePostal
    ville=e.ville
    pays=e.pays


    g=GestionDeTaxe.objects.get(entreprise__pk=a)
    contact=g.contact
    email=contact.email
    dateContact=g.dateContact
    modalite=g.modalite

    htmly     = get_template('pdf.html')

    d = Context({'nom':nom, 'adresse':adresse,
                                           'codePostal':codePostal,'ville':ville,
                                           'pays':pays,'contact':contact,
                                           'dateContact':dateContact,
                                           'modalite':modalite
                                           })

    subject, from_email, to = "Demande de taxe d'apprentissage", 'naijing.wang88@gmail.com', email

    html_content = htmly.render(d)
    msg = EmailMessage(subject, html_content, from_email, [to])
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()

    return HttpResponse('Email envoyé ')


def pdf2(request,a):

    e=Entreprise.objects.get(pk=a)

    nom=e.nom
    adresse=e.adresse
    codePostal=e.codePostal
    ville=e.ville
    pays=e.pays


    g=GestionDeTaxe.objects.get(entreprise__pk=a)
    contact=g.contact
    email=contact.email
    dateContact=g.dateContact
    modalite=g.modalite

    htmly     = get_template('pdf2.html')

    d = Context({'nom':nom, 'adresse':adresse,
                                           'codePostal':codePostal,'ville':ville,
                                           'pays':pays,'contact':contact,
                                           'dateContact':dateContact,
                                           'modalite':modalite
                                           })

    subject, from_email, to = "Taxe d'apprentissage", 'naijing.wang88@gmail.com', email

    html_content = htmly.render(d)
    msg = EmailMessage(subject, html_content, from_email, [to])
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()

    return HttpResponse('Email envoyé ')


#def fasong(request):
    #send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER,
    #['wangxiao8808@hotmail.com'], fail_silently=False)

   # return HttpResponse('email send')
