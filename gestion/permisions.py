from rest_framework import permissions

class EsAdministrador(permissions.BasePermission):
    #Si queremos cambiar el mensaje en el caso no tenga los permitsos necesarios
    message = 'Lo sentimos pero aca solo pueden ingresar administradores'
    def has_permission(self, request, view):
        print(view)
        print(request.user)
        tipo_usuario = request.user.tipoUsuario
        print(tipo_usuario)

        if tipo_usuario == 'ADMIN':
            return True

        #Si retornamos True entonces significaria que cumple con los permisos validos
        #Si retornamos False no tiene los permisos sufficientes
        else:
            return False
        
class EsNovio(permissions.BasePermission):
    message = 'Acceso solo valido para los novios'

    def has_object_permission(self, request, view):
        tipo_usuario = request.user.tipoUsuario

        if tipo_usuario == 'NOVIO':
            return True
        else:
            return False