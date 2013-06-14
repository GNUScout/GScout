def economicos_socio(request, n_asociado):
    try:
        socio = Socio.objects.get(n_asociado=n_asociado)
    except:
        return  HttpResponseRedirect('/socios/search')
    
    economicos = D_Economicos.objects.get(socio_id=socio)
    
    return render_to_response('socios/datos_economicos.html', 
                              {'economicos': economicos })


