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
        settings = {}
        if "name" in request.GET:
            settings["name"]=request.GET["name"]
        if "dwn" in request.GET:
            settings["dwn"]=request.GET["dwn"]
        if "opt" in request.GET:
            settings["opt"]=request.GET["opt"]
        if "path" in request.GET:
            settings["path"]=request.GET["path"]
        #definir perfil de impresión para formato en el cual por defecto esta en tamaño carta con margenes amplios
        options = {}
        if settings["name"][0:3] == "WRA":
            options = recepcion.options(settings["opt"])
            container=getattr(recepcion, settings["name"])(options["html"])    
        #definir variables de estilo para importarlos desde la ruta por defecto de archivos estaticos
        css = ['css/base.css']
        csspdf = ['static/css/base.css']
        #impresión fisica
        t = Template(
            base.body(
                base.header(settings["name"],css),
                base.page(
                    str(header.headerR1C2(options["html"]["DOCtitle"],options["html"]["DOClogo"],options["html"])),
                    container,
                    str(footer.footerR2C1(options["html"]))
                ),
                base.footer,
                1,
                options["html"]
            )
        )
        #Impresión del archivo en pdf
        pdfkit.from_string(
            base.body(
                base.header(settings["name"],{}),
                base.page(
                    str(header.headerR1C2(options["html"]["DOCtitle"],options["html"]["DOClogo"],options["html"])),
                    container,
                    str(footer.footerR2C1(options["html"]))
                ),
                base.footer,
                0,
                options["html"]
            ), settings["name"]+'.pdf', options=options["pdf"],css=csspdf)
        
        #Presentar previsualización del formato
        c = Context({'message': 'Your message'})
        html = t.render(c)
        return HttpResponse(html)
    
    @action(detail=True, methods=['POST']) 
    def post(self, request, format=None):
        response = {}
        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'custom-header' : [
                ('Accept-Encoding', 'gzip')
            ],
            'cookie': [
                ('cookie-name1', 'cookie-value1'),
                ('cookie-name2', 'cookie-value2'),
            ],
            'no-outline': None
        }
        css = ['static/css/style.css', 'static/css/swiper.css']
        pdfkit.from_file('templates/email.html', 'out.pdf', options=options, css=css)
        return Response("Test de correo enviado Satisfactoriamente",status=status.HTTP_200_OK)