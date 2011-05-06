# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from models import Enquete, Opcao

def enquetes(request):

    enquetes = Enquete.objects.all()
    
    c = {
        'enquetes': enquetes,
    }

    return render_to_response('enquetes.html', c)

def votar(request, id_enquete=None):
    
    try:
        enquete = Enquete.objects.get(pk=id_enquete)
        enquetes_session = request.session.get('enquetes', False)
        
        if enquete.id in enquetes_session:
            return HttpResponseRedirect('/enquetes/%d/resultado/' % enquete.id)
    except:
        return HttpResponseRedirect('/enquetes/')

    if request.method == 'POST':
        try:
            opcao_id = request.POST.get('opcao', None)
            opcao = Opcao.objects.get(pk=opcao_id)
            opcao.total_votos += 1
            opcao.save()
            if request.session.get('enquetes', False):
                request.session['enquetes'].append(enquete.id)
            else:
                request.session['enquetes'] = [enquete.id,]
            request.session.modified = True
            return HttpResponseRedirect('/enquetes/%d/resultado/' % enquete.id)
        except:
            pass
    
    c = {
        'enquete': enquete,
    }

    return render_to_response('votar.html', c, context_instance=RequestContext(request))

def resultado(request, id_enquete=None):
    try:
        enquete = Enquete.objects.get(pk=id_enquete)
    except:
        return HttpResponseRedirect('/enquetes/')

    
    c = {
        'enquete': enquete,
    }

    return render_to_response('resultado.html', c)

