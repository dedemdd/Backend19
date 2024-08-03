from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import ProductoModel


class ProductoSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = ProductoModel
        #Para que haga la validacion a las llaves foraneas y tambien las tome en cuenta
        include_fk = True