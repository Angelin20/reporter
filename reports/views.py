from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.conf import settings
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.db.models import F,Q
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from requests.exceptions import ConnectionError
from requests.exceptions import HTTPError
from django.db import connections
from datetime import datetime
import json
import unidecode
from components import recepcion
import os

#paquetes necesarios para realizar los pdfs
import pdfkit
from components import base,header,footer
from django.template import Context, Template

class getPDF(APIView):
    @action(detail=True, methods=['GET']) 
    def get(self, request, format=None):
        #inicializar variable de settings para obtener parametros en request
        #var name con el valor del reporte en especifico que se requiere
        #var dwn con valor en 1 para descargar y 0 para solo visualizar
        #var opt con valor numerico para obtener el perfil de configuración de la impresión y visualización
        #var path con el valor de la ruta en la que queremos que se guarde 0 no guarda
        settingspdf = {}
        if "name" in request.GET:
            settingspdf["name"]=request.GET["name"]
        if "dwn" in request.GET:
            settingspdf["dwn"]=request.GET["dwn"]
        if "opt" in request.GET:
            settingspdf["opt"]=request.GET["opt"]
        if "path" in request.GET:
            settingspdf["path"]=request.GET["path"]
        #definir perfil de impresión para formato en el cual por defecto esta en tamaño carta con margenes amplios
        options = {}
        if settingspdf["name"][0:3] == "WRA":
            options = recepcion.options(settingspdf["opt"])
            container=getattr(recepcion, settingspdf["name"])(options["html"])
            javascript=getattr(recepcion, "JAVASCRIPT"+settingspdf["name"])()
        #definir variables de estilo para importarlos desde la ruta por defecto de archivos estaticos
        css = ['css/base.css']
        csspdf = ['static/css/base.css']
        
        #Evalua parametro path para saber si se tiene que guardar el archivo y se asigna la carpeta donde se guardara
        if settingspdf["path"] != "None":
            try:
                os.makedirs(settingspdf["path"])
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
            pdfkit.from_string(
                base.body(
                    base.header(settingspdf["name"],{}),
                    base.page(
                        str(header.headerR1C2(options["html"]["DOCtitle"],options["html"]["DOClogo"],options["html"])),
                        container,
                        str(footer.footerR2C1(options["html"]))
                    ),
                    base.footer(""),
                    0,
                    options["html"]
                ), settingspdf["path"]+"/"+settingspdf["name"]+'.pdf', options=options["pdf"],css=csspdf)
        
        #Validar la variable dwn para saber si viene 1 para visualizar y 0 u otro caracter para descargar
        if settingspdf["dwn"] == "1":
            t = Template(
                base.body(
                    base.header(settingspdf["name"],css),
                    base.page(
                        str(header.headerR1C2(options["html"]["DOCtitle"],options["html"]["DOClogo"],options["html"])),
                        container,
                        str(footer.footerR2C1(options["html"]))
                    ),
                    base.footer(javascript),
                    1,
                    options["html"]
                )
            )
            #Presentar previsualización del formato
            c = Context({'message': 'Your message'})
            html = t.render(c)
            return HttpResponse(html)
        else:
            configkit = pdfkit.configuration(wkhtmltopdf='C:/wkhtmltopdf/bin/wkhtmltopdf.exe')
            filepdf=pdfkit.from_string(
                base.body(
                    base.header(settingspdf["name"],{}),
                    base.page(
                        str(header.headerR1C2(options["html"]["DOCtitle"],options["html"]["DOClogo"],options["html"])),
                        container,
                        str(footer.footerR2C1(options["html"]))
                    ),
                    base.footer(""),
                    0,
                    options["html"]
                ), False, options=options["pdf"],css=csspdf, configuration=configkit)
            response = HttpResponse(filepdf,content_type='application/pdf')
            response['Content-Disposition'] = "attachment; filename=" + settingspdf["name"]+".pdf"
            return response

    @action(detail=True, methods=['POST']) 
    def post(self, request, format=None):
        settingspdf = {}
        if "name" in request.data:
            settingspdf["name"]=request.data["name"]
        if "dwn" in request.data:
            settingspdf["dwn"]=request.data["dwn"]
        if "opt" in request.data:
            settingspdf["opt"]=request.data["opt"]
        if "path" in request.data:
            settingspdf["path"]=request.data["path"]
        options = {}
        if settingspdf["name"][0:3] == "WRA":
            options = recepcion.options(settingspdf["opt"])
            container=getattr(recepcion, settingspdf["name"])(options["html"],request.data["vin"],request.data["garantia"]) #En esta linea se obtiene la funcion constructora
            javascript=getattr(recepcion, "JAVASCRIPT"+settingspdf["name"])()
        css = ['css/base.css']
        csspdf = ['static/css/base.css']
        if settingspdf["path"] != "None":
            try:
                os.makedirs(settingspdf["path"])
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
            configkit = pdfkit.configuration(wkhtmltopdf='C:/wkhtmltopdf/bin/wkhtmltopdf.exe')
            pdfkit.from_string(
                base.body(
                    base.header(settingspdf["name"],{}),
                    base.page(
                        str(header.headerR1C2(options["html"]["DOCtitle"],options["html"]["DOClogo"],options["html"])),
                        container,
                        str(footer.footerR2C1(options["html"]))
                    ),
                    base.footer(""),
                    0,
                    options["html"]
                ), settingspdf["path"]+"/"+settingspdf["name"]+'.pdf', options=options["pdf"],css=csspdf, configuration=configkit)
        
        #Validar la variable dwn para saber si viene 1 para visualizar y 0 u otro caracter para descargar
        if settingspdf["dwn"] == "1":
            t = Template(
                base.body(
                    base.header(settingspdf["name"],css),
                    base.page(
                        str(header.headerR1C2(options["html"]["DOCtitle"],options["html"]["DOClogo"],options["html"])),
                        container,
                        str(footer.footerR2C1(options["html"]))
                    ),
                    base.footer(javascript),
                    1,
                    options["html"]
                )
            )
            #Presentar previsualización del formato
            c = Context({'message': 'Your message'})
            html = t.render(c)
            return HttpResponse(html)
        else:
            configkit = pdfkit.configuration(wkhtmltopdf='C:/wkhtmltopdf/bin/wkhtmltopdf.exe')
            filepdf=pdfkit.from_string(
                base.body(
                    base.header(settingspdf["name"],{}),
                    base.page(
                        str(header.headerR1C2(options["html"]["DOCtitle"],options["html"]["DOClogo"],options["html"])),
                        container,
                        str(footer.footerR2C1(options["html"]))
                    ),
                    base.footer(""),
                    0,
                    options["html"]
                ), False, options=options["pdf"],css=csspdf, configuration=configkit)
            response = HttpResponse(filepdf,content_type='application/pdf')
            response['Content-Disposition'] = "attachment; filename=" + settingspdf["name"]+".pdf"
            return response