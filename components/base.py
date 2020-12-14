from django.conf import settings
def body(header,container,footer,opt,style):
    obj = """
        <!doctype html>
        <html>
        """
    obj+= str(header)
    if opt == 1:
        obj+= """
            <body class="gray-bg" style="overflow-x: auto;" cz-shortcut-listen="true">
                <div class="book" >
        """
        obj+= "<div class='page' id='firstpage' style='"+str(style["stylepage"])+"'>"
        obj+= str(container)
        #obj+= "</div><div class='page' id='firstpage' style='"+str(style["stylepage"])+"'>"
        #obj+= str(container)
        obj+= """
                    </div>
                </div>
            </body>
        </html>
        """
    else:
        obj+= """
            <body style="background:#fff">
        """
        obj+= "<div class='pageprint' style='"+str(style["stylepage"])+"'>"
                            
        obj+= str(container)
        #obj+= "</div><div class='pageprint' style='"+str(style["stylepage"])+"'>"
        #obj+= str(container)
        obj+= """
                </div>
            </body>
        </html>
        """
    return str(obj)

def header(titulo,css):
    obj = """
        <head>
            <meta charset="utf-8">
        """
    obj+="<title>"+titulo+"</title>\n"
    obj+="<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css' integrity='sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS' crossorigin='anonymous' >"
    obj+="<link rel='stylesheet' href='https://pro.fontawesome.com/releases/v5.10.0/css/all.css' integrity='sha384-AYmEC3Yw5cVb3ZcuHtOA93w35dYTsvhLPVnYs9eStHfGJvOvKxVfELGroGkvsg+p' crossorigin='anonymous'/>"
    obj+= "<link rel='icon' href='"+settings.STATIC_URL +"images/icon.png'>\n"
    obj+= "<link rel='apple-touch-icon' href='"+settings.STATIC_URL +"images/icon_round.png'>\n"
    for element in css:
        obj+= "<link rel='stylesheet' href='"+settings.STATIC_URL +element+"'>\n"
    obj+= """
        </head>
        """
    return str(obj)

def footer(scripts):
    obj = "<script type='text/javascript'>"+str(scripts)+"</script>"
    return obj

def page(head,container,foot):
    obj = "<div id='page-wrapper'>"
    obj +=str(head)
    obj +=str(container)
    obj +=str(foot)
    obj +="</div>"
    return str(obj)

