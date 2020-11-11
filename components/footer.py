#R1 para especificar que queremos una sola fila o 1 row
#C1 para especificar que queremos una sola columna o 1 col
def footerR2C1(conf):
    obj = "<div class='futer' style='"+str(conf["footerpage"])+"'>"
    obj += "<div style='"+str(conf["footerR1"])+"'>"
    obj +=str(conf["DOCpieR1"])
    obj +="</div>"
    obj += "<div style='"+str(conf["footerR2"])+"'>"
    obj +=str(conf["DOCpieR2"])
    obj +="</div>"
    obj +="</div>"
    return str(obj)
