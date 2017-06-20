#!/usr/bin/env python3
# Autores: Elizabeth Gonzales Romero y Brandon Estiven Moran Rojas
# Programa: API-Wikipedia.py
# Fecha: Sat junio 17 08:29:18 COT 2017
# Descripcion: esta API consulta en la pagina de wikipedia y realiza un resumen del significado de de la palabra que buscamos  

#para instalar la libreria de wikipedia ejecutamos en la consola de comando pip install wikipedia 
import wikipedia 

#especificamos el idioma que deseamos utilizar en este caso es español 
wikipedia.set_lang("es")
#pedimos al usuario que ingrese la palabra que desea buscar 
s = input('digite su busqueda:')
#imprimimos el resumen del significado de la palabra que buscamos 
print (wikipedia.summary(str(s)))