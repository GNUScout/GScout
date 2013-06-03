#Indicamos la fecha de elaboracion del fichero
now = datetime.datetime.now()
now = now.strftime("%d-%m-%Y")
# "datos" almacena el contenido en formato string de todos los datos
# incluidas las comas y los retornos de carro, para facilitar la creacion del fichero csv
datos="ID, Titular, NIF Titular, Banco, Nombre Socio, Apellidos Socio, DNI Socio\n"
for d in range(len(lista)):
    datos += str(socios[lista[d]]['socio_id_id']) + "," + unicodedata.normalize('NFKD',economicos[lista[d]]['titular']).encode('ascii','ignore') + "," + str(economicos[lista[d]]['nif_titular']) + "," + str(economicos[lista[d]]['banco']) + "," + unicodedata.normalize('NFKD',socios[lista[d]]['nombre']).encode('ascii','ignore') + "," + unicodedata.normalize('NFKD',socios[lista[d]]['apellidos']).encode('ascii','ignore') + "," + str(socios[lista[d]]['dni']) + "\n"
             
# media_body preparará el contenido de datos para transformarlo al formato csv 
# gracias a la funcion MediaIoBaseUpload, es importante poner la resumable=False
# para evitar problemas de carga y de formato.
media_body = MediaIoBaseUpload(StringIO.StringIO(datos), 'text/csv', resumable=False)

# body almacenara el titulo del fichero, la descripcion y el tipo de fichero.
body = {
  'title': 'Datos_Economicos_'+now+'',
  'description': 'A test document',
  'mimeType': "text/csv"
}

# Finalmente se llama al servicio de drive_service al cual le pasamos por parametros body, mediabody
# que tendra el contenido y convert=True para obligar la conversion del fichero.
file = drive_service.files().insert(body=body, media_body=media_body, convert="true").execute()
pprint.pprint(file) 