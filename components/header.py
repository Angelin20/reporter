from django.conf import settings
#R1 para especificar que queremos una sola fila o 1 row
#C1 para especificar que queremos una sola columna o 1 col
def headerR1C1(content):
    obj = "<div class='headerPage'>"
    obj +=str(content)
    obj +="</div>"
    return str(obj)

def headerR1C2(content,src_icon,conf):
    obj = "<div class='headerPage' style='"+str(conf["header"])+"'>"
    obj +="<div style='"+str(conf["headercontainertitle"])+"'>"
    obj +="<h1 style='"+str(conf["headertitle"])+"'>"+str(content)+"</h1>"
    obj +="</div>"
    obj +="<div style='"+str(conf["headercontainerimg"])+"'>"
    obj +="<img src='"+settings.STATIC_URL+src_icon+"' style='"+str(conf["headerimg"])+"'>"
    obj +="</div>"
    obj +="</div>"
    return str(obj)
