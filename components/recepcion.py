from django.conf import settings

def options(opt):
    configs={}
    switcherpdf = {
        "1":{'page-size': 'Letter',
            'margin-top': '0.15in',
            'margin-right': '0.15in',
            'margin-bottom': '0.15in',
            'margin-left': '0.15in',
            'encoding': "UTF-8",
            'custom-header' : [
                ('Accept-Encoding', 'gzip')
            ],
            'cookie': [
                ('cookie-name1', 'cookie-value1'),
                ('cookie-name2', 'cookie-value2'),
            ],
            'no-outline': None
        },
        "2":{'page-size': 'Legal',
            'margin-top': '0.15in',
            'margin-right': '0.15in',
            'margin-bottom': '0.15in',
            'margin-left': '0.15in',
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
    }
    switcherhtml = {
        "1":{
            'stylepage':'width: 297mm;min-height: 380mm;max-height: 380mm;margin-top: 0px;margin-bottom:6px;',
            'header':'float:left;height:116px;padding:10px;margin-left:4%;margin-right:4%;width: 92%;border-bottom:3px #010101 solid;',
            'headercontainertitle':'width:70%;',
            'headertitle':'font-size:30px;font-weight:900;margin-top:50px',
            'headerimg':'width:240px;height:47px;position:relative;top: 50%;left: 50%;margin: -1% 0 0 -32%;',
            'headercontainerimg':'width:30%;height:100%;right:0;top:0;position:absolute',
            'footerpage':'margin-left:5%;margin-right:5%;width: 90%;height: 80px;margin-bottom:10px',
            'DOCtitle':'CARTA DE RENUNCIA A BENEFICIOS',
            'DOClogo':'images/FORD.png',
            'DOCpieR1':'Conserve el formulario completo en el distribuidor y proporcione una copia al cliente',
            'DOCpieR2':'FP- 2018PLAN',
            'footerR1':'width:100%;text-align:center;margin-bottom:20px;font-size:12px',
            'footerR2':'width:100%;',
            'allcontainer':'margin-left:4%;margin-right:4%;width: 92%;padding-left: 14px;padding-right: 14px;',
            'imgsign':'width:172px;height:36px;position:relative;'
        },
        "2":{
            'stylepage':'width: 297mm;min-height: 489.7mm;max-height: 489.7mm;margin-top: 0px;',
            'header':'float:left;height:116px;padding:10px;margin-left:4%;margin-right:4%;width: 92%;border-bottom:3px #010101 solid;',
            'headercontainertitle':'width:70%;',
            'headertitle':'font-size:30px;font-weight:900;margin-top:50px',
            'headerimg':'width:240px;height:47px;position:relative;top: 50%;left: 50%;margin: -5% 0 0 -32%;',
            'headercontainerimg':'width:30%;height:100%;right:0;top:0;position:absolute',
            'footerpage':'margin-left:4%;margin-right:4%;width: 92%;height: 100px;margin-bottom:10px',
            'DOCtitle':'CARTA DE RENUNCIA A BENEFICIOS',
            'DOClogo':'images/FORD.png',
            'DOCpieR1':'Conserve el formulario completo en el distribuidor y proporcione una copia al cliente',
            'DOCpieR2':'FP- 2018PLAN',
            'footerR1':'width:100%;text-align:center;margin-bottom:20px;font-size:12px',
            'footerR2':'width:100%;',
            'allcontainer':'margin-left:4%;margin-right:4%;width: 92%;padding-left: 14px;padding-right: 14px;',
            'imgsign':'width:172px;height:36px;position:relative;'
        }
    }
    configs["pdf"] = switcherpdf.get(opt,"Opción no encontrada")
    configs["html"] = switcherhtml.get(opt,"Opción no encontrada")
    return configs

def WRACRN001(conf,vin,firma):
    doc="<div class='all-container' style='"+conf["allcontainer"]+"'>"
    doc+="""
        <div class="container">
            <div style="display:-webkit-box;Roboto, 'Segoe UI', Tahoma, sans-serif;margin-top:10px">
                <div style="width: 39.666667%;padding: 5px;display: block;padding-top:10px;">
                    <p style="font-size:16px">Número de identificación del vehículo (VIN)</p>
                </div>
                <div style="display:-webkit-box;width: 60.333333%;padding-right: 5px;padding-left: 5px;">
                    <div class="cell">-</div>
                    <div class="cell-right">
                    """
    doc+=str(vin)[0,1]
    doc+="""</div>
                    <div class="cell-right">
                    """
    doc+=str(vin)[0,1]
    doc+="""</div>
                    <div class="cell-right">-</div>
                    <div class="cell-right">-</div>
                    <div class="cell-right">-</div>
                    <div class="cell-right">-</div>
                    <div class="cell-right">-</div>
                    <div class="cell-right">-</div>
                    <div class="cell-right">-</div>
                    <div class="cell-right">-</div>
                    <div class="cell-right">-</div>
                    <div class="cell-right">-</div>
                    <div class="cell-right">-</div>
                    <div class="cell-right">-</div>
                    <div class="cell-right">-</div>
                    <div class="cell-right">-</div>
                </div>
            </div>
            <div style="display:-webkit-box;Roboto, 'Segoe UI', Tahoma, sans-serif;margin-top:10px">
                <div style="width: 100%;padding:5px;display: block;text-align:center;">
                    <p style="font-size:18px;font-weight:900;padding:0px;margin:2px;">El único plan de extensión de garantía respaldado por Ford Motor</p>
                    <p style="font-size:20px;font-weight:900;padding:0px;margin:2px;">Company</p>
                    <p style="font-size:20px;font-weight:900;padding:0px;margin:2px;">Protegiendo tu tranquilidad</p>
                    <br>
                    <br>
                    <p style="font-size:26px;font-weight:900;padding:0px;margin:2px;">Lista de características y beneficios de la garantía</p>
                    <p style="font-size:26px;font-weight:900;padding:0px;margin:2px;">extendida</p>
                    <div style="width: 80%;margin-left:10%;margin-right:10%;margin-bottom:18px;height:495px;padding:15px;text-align:left;border:1px #010101 solid;">
                        <div style="display:-webkit-box;">
                            <div style="width: 5.666667%;padding: 5px;display: block;">
                                <i class="far fa-check-square" style="font-size:28px"></i>
                            </div>
                            <div style="width: 94.333333%;padding-top:8px;display: block;font-size:22px">
                                Plazo adicional de la cobertura
                            </div>
                        </div>
                        <div style="display:-webkit-box;">
                            <div style="width: 5.666667%;padding: 5px;display: block;">
                                <i class="far fa-check-square" style="font-size:28px"></i>
                            </div>
                            <div style="width: 94.333333%;padding-top:8px;display: block;font-size:22px">
                                Cobertura Nacional
                            </div>
                        </div>
                        <div style="display:-webkit-box;">
                            <div style="width: 5.666667%;padding: 5px;display: block;">
                                <i class="far fa-check-square" style="font-size:28px"></i>
                            </div>
                            <div style="width: 94.333333%;padding-top:8px;display: block;font-size:22px">
                                Amplia cobertura en componentes
                            </div>
                        </div>
                        <div style="display:-webkit-box;">
                            <div style="width: 5.666667%;padding: 5px;display: block;">
                                <i class="far fa-check-square" style="font-size:28px"></i>
                            </div>
                            <div style="width: 94.333333%;padding-top:8px;display: block;font-size:22px">
                                Asistencia Vial 24 horas
                            </div>
                        </div>
                        <div style="display:-webkit-box;">
                            <div style="width: 5.666667%;padding: 5px;display: block;">
                                <i class="far fa-check-square" style="font-size:28px"></i>
                            </div>
                            <div style="width: 94.333333%;padding-top:8px;display: block;font-size:22px">
                                Sin gastos adicionales
                            </div>
                        </div>
                        <div style="display:-webkit-box;">
                            <div style="width: 5.666667%;padding: 5px;display: block;">
                                <i class="far fa-check-square" style="font-size:28px"></i>
                            </div>
                            <div style="width: 94.333333%;padding-top:8px;display: block;font-size:22px">
                                Transferible a otro propietario
                            </div>
                        </div>
                        <div style="display:-webkit-box;">
                            <div style="width: 5.666667%;padding: 5px;display: block;">
                                <i class="far fa-check-square" style="font-size:28px"></i>
                            </div>
                            <div style="width: 94.333333%;padding-top:8px;display: block;font-size:22px">
                                Beneficio de movilidad ante cualquier imprevisto
                            </div>
                        </div>
                        <div style="display:-webkit-box;">
                            <div style="width: 5.666667%;padding: 5px;display: block;">
                                <i class="far fa-check-square" style="font-size:28px"></i>
                            </div>
                            <div style="width: 94.333333%;padding-top:8px;display: block;font-size:22px">
                                Facilidad de Financiamiento
                            </div>
                        </div>
                        <div style="display:-webkit-box;">
                            <div style="width: 5.666667%;padding: 5px;display: block;">
                                <i class="far fa-check-square" style="font-size:28px"></i>
                            </div>
                            <div style="width: 94.333333%;padding-top:8px;display: block;font-size:22px">
                                Meses sin intereses disponibles
                            </div>
                        </div>
                        <div style="display:-webkit-box;">
                            <div style="width: 5.666667%;padding: 5px;display: block;">
                                <i class="far fa-check-square" style="font-size:28px"></i>
                            </div>
                            <div style="width: 94.333333%;padding-top:8px;display: block;font-size:22px">
                                Cero deducible
                            </div>
                        </div>
                        <div style="display:-webkit-box;">
                            <div style="width: 5.666667%;padding: 5px;display: block;">
                                <i class="far fa-check-square" style="font-size:28px"></i>
                            </div>
                            <div style="width: 94.333333%;padding-top:8px;display: block;font-size:22px">
                                Tranquilidad ante reparaciones imprevistas
                            </div>
                        </div>
                    </div>
                    <p style="font-size:20px;font-weight:regular;padding:0px;margin:8px;font-style: italic;">Reconozco que he revisado las características y los beneficios del plan</p>
                    <p style="font-size:20px;font-weight:regular;padding:0px;margin:8px;font-style: italic;">de extensión de garantía de Ford Protect y he decidido que no deseo</p>
                    <p style="font-size:20px;font-weight:regular;padding:0px;margin:8px;font-style: italic;">adquirirlo en este momento</p>
                    <div style="width: 74%;margin-left:13%;margin-right:13%;margin-top:45px;height:88px;padding:5px;display: block;text-align:left;">
                        <div style="width: 100%;height:46px;padding:5px;display:-webkit-box;text-align:left;border-bottom:1px #010101 solid;">
                            <div style="width: 25.333333%;display: block;text-align:center">
    """
    doc+="<img src='"+firma+"' style='"+str(conf["imgsign"])+"'>"
    doc+="""                
                            </div>
                            <div style="width: 54.333333%;padding-top:18px;display: block;text-align:center">
    """
    doc+="Nombre de cliente completo"
    doc+="""
                            </div>
                            <div style="width: 20.333333%;padding-top:18px;display: block;text-align:center">
    """
    doc+="11/11/2020"
    doc+="""
                            </div>
                        </div>
                        <div style="width: 100%;height:40px;padding:5px;display:-webkit-box;text-align:left;">
                            <div style="width: 25.333333%;display: block;text-align:center">
    """
    doc+="FIRMA DEL CLIENTE"
    doc+="""                
                            </div>
                            <div style="width: 54.333333%;display: block;text-align:center">
    """
    doc+="NOMBRE DEL CLIENTE"
    doc+="""
                            </div>
                            <div style="width: 20.333333%;display: block;text-align:center">
    """
    doc+="FECHA"
    doc+="""
                            </div>
                        </div>
                    </div>
                    <div style="width: 74%;margin-left:13%;margin-right:13%;margin-top:3px;height:88px;padding:5px;display: block;text-align:left;">
                        <div style="width: 100%;height:46px;padding:5px;display:-webkit-box;text-align:left;border-bottom:1px #010101 solid;">
                            <div style="width: 25.333333%;display: block;text-align:center">
    """
    doc+="<img src='"+firma+"' style='"+str(conf["imgsign"])+"'>"
    doc+="""                
                            </div>
                            <div style="width: 54.333333%;padding-top:18px;display: block;text-align:center">
    """
    doc+=""
    doc+="""
                            </div>
                            <div style="width: 20.333333%;padding-top:18px;display: block;text-align:center">
    """
    doc+="11/11/2020"
    doc+="""
                            </div>
                        </div>
                        <div style="width: 100%;height:40px;padding:5px;display:-webkit-box;text-align:left;">
                            <div style="width: 25.333333%;display: block;text-align:center">
    """
    doc+=""
    doc+="""                
                            </div>
                            <div style="width: 54.333333%;display: block;text-align:center">
    """
    doc+=""
    doc+="""
                            </div>
                            <div style="width: 20.333333%;display: block;text-align:center">
    """
    doc+="FECHA"
    doc+="""
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    """
    doc+="</div>"
    return doc

def JAVASCRIPTWRACRN001():
    doc=""
    return doc