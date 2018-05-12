import xml.etree.ElementTree as ET
from .models import museos

tree = ET.parse('museos.xml')
root = tree.getroot()

#Creamos diccionario para guardar los parámetros de museo en museo
#y lo guardamos de uno en uno en la base de dato.

def create_BD (museos_BD):
    aux  = [False,False,False,False,False,False,False,False,False,False,False,False,
            False,False,False,False,False,False,False,False,False,False,False,False]
    if not museos_BD:
        for child in root:
            if child.tag == 'infoDataset':
                pass
            else:
                for contenido in child:
                    for atributo in contenido:
                        #Posibles campos para Entidad
                        if atributo.attrib['nombre'] == 'NOMBRE':
                            aux[0] = atributo.text

                        elif atributo.attrib['nombre'] == 'ID-ENTIDAD':
                            aux[1] = atributo.text
      
                        elif atributo.attrib['nombre'] == 'DESCRIPCION':
                            aux[2] = atributo.text

                        elif atributo.attrib['nombre'] == 'HORARIO':
                            aux[3] = atributo.text

                        elif atributo.attrib['nombre'] == 'TRANSPORTE':
                            aux[4] = atributo.text

                        elif atributo.attrib['nombre'] == 'ACCESIBILIDAD':
                            aux[5] = atributo.text

                        elif atributo.attrib['nombre'] == 'CONTENT-URL':
                            aux[6] = atributo.text                      

                        #Posibles Campos para Localización
                        elif atributo.attrib['nombre'] == 'LOCALIZACION':
                            for localizacion in atributo:
                                if localizacion.attrib['nombre'] == 'NOMBRE-VIA':
                                    aux[7] = localizacion.text

                                elif localizacion.attrib['nombre'] == 'CLASE-VIAL': 
                                    aux[8] = localizacion.text
                           
                                elif localizacion.attrib['nombre'] == 'TIPO-NUM':
                                    aux[9] = localizacion.text

                                elif localizacion.attrib['nombre'] == 'NUM':
                                    aux[10] = localizacion.text

                                elif localizacion.attrib['nombre'] == 'LOCALIDAD':
                                    aux[11] = localizacion.text
  
                                elif localizacion.attrib['nombre'] == 'PROVINCIA':
                                    aux[12] = localizacion.text

                                elif localizacion.attrib['nombre'] == 'CODIGO-POSTAL':
                                    aux[13] = localizacion.text

                                elif localizacion.attrib['nombre'] == 'BARRIO':
                                    aux[14] = localizacion.text

                                elif localizacion.attrib['nombre'] == 'DISTRITO':
                                    aux[15] = localizacion.text

                                elif localizacion.attrib['nombre'] == 'COORDENADA-X':
                                    aux[16] = localizacion.text

                                elif localizacion.attrib['nombre'] == 'COORDENADA-Y':
                                    aux[17] = localizacion.text

                                elif localizacion.attrib['nombre'] == 'LATITUD':
                                    aux[18] = localizacion.text

                                elif localizacion.attrib['nombre'] == 'LONGITUD':
                                    aux[19] = localizacion.text


                        #Posibles Campos para Datos de contacto     
                        elif atributo.attrib['nombre'] == 'DATOSCONTACTOS':
                            for datoscontactos in atributo:

                                if datoscontactos.attrib['nombre'] == 'TELEFONO':
                                    aux[20] = datoscontactos.text

                                elif datoscontactos.attrib['nombre'] == 'FAX':
                                    aux[21] = datoscontactos.text

                                elif datoscontactos.attrib['nombre'] == 'EMAIL':
                                    aux[22] = datoscontactos.text


                        elif atributo.attrib['nombre'] == 'DESCRIPCION-ENTIDAD':
                            aux[23] = atributo.text



                for i in range(0,24):
                    atrib = aux[i]
                    if atrib == False:
                        aux[i] = 'No hay información'


                import_museo = museos(museo=aux[0] , id_entidad = aux[1], descripcion = aux[2], 
                    horario = aux[3], transporte = aux[4], accesibilidad = aux[5], 
                    content_url = aux[6], nombre_via = aux[7], clase_vial = aux[8],
                    tipo_num = aux[9], num = aux[10], localidad = aux[11], provincia = aux[12],
                    codigo_postal = aux[13], barrio = aux[14], distrito = aux[15],
                    coordenada_x = aux[16], coordenada_y = aux[17], latitud = aux[18],
                    longitud = aux[19], telefono = aux[20], fax = aux[21], email = aux[22], descripcion_entidad = aux[23])
                import_museo.save()

                aux  = [False,False,False,False,False,False,False,False,False,False,False,False,
                        False,False,False,False,False,False,False,False,False,False,False,False]


if __name__ == "__main__":
    create_BD(museos_BD)