from math import ceil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from os import environ

def serializadorPaginacion(total:int, pagina:int, porPagina:int):
    #Operador ternario
    #                VAL_VERDADERO IF CONDICIONAL  ELSE VALOR_FALSO
    itemsPorPagina = porPagina if total >= porPagina else total

    # Forma antigua de hacerlo
    # if total >= perPage:
    #     itemsPorPagina = perPage
    # else:
    #     itemsPorPagina = total

    totalPaginas = ceil(total / itemsPorPagina) if itemsPorPagina > 0 else None
    paginaPrevia = pagina - 1 if pagina > 1 and pagina <= totalPaginas else None
    paginaSiguiente = pagina + 1 if totalPaginas > 1 and pagina < totalPaginas else None

    return {
            'itemsPorPagina': itemsPorPagina, 
            'totalPaginas': totalPaginas,
            'total': total,
            'paginaPrevia': paginaPrevia,
            'paginaSiguiente': paginaSiguiente,
            'porPagina' : porPagina,
            'pagina': pagina
            }

def enviarCorreo(destinatario, titulo, texto, html):
    if not destinatario:
        print('Es necesario el correo')
        return
    
    emailEmisor =  environ.get('CORREO_EMISOR')
    passwordEmisor = environ.get('PASSWORD_CORREO_EMISOR')

    #creamos el cuerpo de nuestro email
    cuerpo = MIMEText(texto, 'plain')
    cuerpoHtml = MIMEText(html, 'html')

    #Ahora comenzamos a crear la confirguracion de nuestro emaial
    correo = MIMEMultipart('alternative')
    #Configuramos el titulo
    correo['Subject'] = titulo
    
    correo['To'] = destinatario

    #Adjuntamos el cuerpo de nuestro correo
    correo.attach(cuerpo)
    correo.attach(cuerpoHtml)

    #creamos la conexion que se encargara de realizar el envio del correo 
    #587 es el puerto estandar para los servidores de correo
    emisor = SMTP(environ.get('CORREO_HOST'), 587)
    emisor.starttls()

    emisor.login(emailEmisor, passwordEmisor)
    
    emisor.sendmail(from_addr=emailEmisor, to_addrs=destinatario, msg=correo.as_string())

    emisor.quit()
    
    print('Correo enviado existosamente')
    
    
