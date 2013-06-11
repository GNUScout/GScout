################ Vista #######################

def economicos_socio(request, n_asociado):
    try:
        socio = Socio.objects.get(n_asociado=n_asociado)
    except:
        return  HttpResponseRedirect('/socios/search')
    
    economicos = D_Economicos.objects.get(socio_id=socio)
    
    return render_to_response('socios/datos_economicos.html', 
                              {'economicos': economicos })

################ Template #######################

{% block form %}
    <p><strong>Titular de la cuenta: </strong> {{economicos.titular}}</p>
    <p><strong>N.I.F. del Titular: </strong> {{economicos.nif_titular}}</p>
    <p><strong>Banco: </strong> {{economicos.banco}}</p>
    <p><strong>Sucursal: </strong> {{economicos.sucursal}}</p>
    <p><strong>Localidad: </strong> <time>{{economicos.localidad}}</time></p>
    <p> 
        <strong>Datos de la cuenta: </strong> {{economicos.d_banco}}-
        {{economicos.d_sucursal}}-{{economicos.dc}}-{{economicos.n_cuenta}}
    </p>
    <a class="btn btn-large btn-primary" 
        href="/socios/{{ economicos.socio_id.n_asociado }}/edit_economicos">
        Editar
    </a>    
{% endblock %}