from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import validate
from models import UsuarioModel, TipoUsuario
from marshmallow_enum import EnumField
from marshmallow import Schema, fields

class RegistroSerializer(SQLAlchemyAutoSchema):
    #Las columnas que usan Enum masrchmallow_sqlalchemy no sabe como convertirlas cuando son deserializadas
    tipoUsuario = EnumField(TipoUsuario)
    #xxxxx@xxxx.xxx
    #aparte de las validaciones que nos brinda marshmellow_sqlalchemy le estamos agreggando validar que se un correo
    correo = auto_field(validate=validate.Email(error='El correo no cumple con el formato correcto'))

    #Load_only > solo se usará este field paa la serializacion  mas no para la deserializacion
    #dump_only = solo se usara para la desealilizacion mas no para la serializacion
    password = auto_field(load_only=True)
    class Meta:
        model = UsuarioModel

#Este un serializador creado desde 0 sin modelo
class LoginSerializer(Schema):
    correo = fields.Email(required = True)
    password = fields.String(required = True)


class ActualizarUsuarioSerializer(Schema):
    nombre = fields.String(required = True)

class CambiarPasswordSerializer(Schema):
    passwordAntigua = fields.String(required = True)
    passwordNueva = fields.String(required = True, validate=validate.Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&?!])[A-Za-z\d@#$%^&?!]{6,}$'))

class ResetearPasswordSerializer(Schema):
    correo = fields.Email(required=True)

class ConfirmarResetTokenSerializer(Schema):
    token = fields.String(required=True)
    
class ConfirmarResetPasswordSerializer(Schema):    
    token = fields.String(required=True)
    passwordNueva = fields.String(required = True, validate=validate.Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&?!])[A-Za-z\d@#$%^&?!]{6,}$'))