def cambio_unidad(request):  
    
    socios = D_Personales.objects.all()
    
    date = datetime.datetime.now()
    date = int(date.strftime('%Y'))
    
    for s in socios:
        if (date - int(s.f_nacimiento.strftime('%Y')))  < 11 :
            s.seccion="Manada"
            
        if ((date - int(s.f_nacimiento.strftime('%Y'))  >= 11) and 
            (date - int(s.f_nacimiento.strftime('%Y'))  < 14)):
            s.seccion="Tropa"
            
        if ((date - int(s.f_nacimiento.strftime('%Y'))  >= 14) and 
            (date - int(s.f_nacimiento.strftime('%Y'))  < 17)):
            s.seccion="Esculta"
            
        if ((date - int(s.f_nacimiento.strftime('%Y'))  >= 17) and 
            (date - int(s.f_nacimiento.strftime('%Y'))  < 20)):
            s.seccion="Rover" 
            
        if (date - int(s.f_nacimiento.strftime('%Y')))  >= 20 :
            s.seccion="Scouter" 
        
        s.save()