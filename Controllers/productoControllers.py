from instancias import conexion
from models import ProductoModel
from flask_restful import Resource, request
from serializers import ProductoSerializer
from marshmallow.exceptions import ValidationError
from utilitarios import serializadorPaginacion

class ProductosController(Resource):
    def post(self):
        data = request.get_json()
        serializador = ProductoSerializer()
        try:
            dataSerializada = serializador.load(data)
            nuevoProducto = ProductoModel(**dataSerializada)
            conexion.session.add(nuevoProducto)
            conexion.session.commit()

            resultado = serializador.dump(nuevoProducto)
            return {
                'message': 'Producto creado exitosamente',
                'content': resultado
            }
        except ValidationError as error:
            return {
                'message': 'Error al crear producto',
                'errors': error.args
            }, 400
        
    def get(self):
        
        #Devolver todos los productos usando el serializador          
        #Para la paginanacion es necesario saber paginas que vamos a ubicarnos cuantos elementos por pagina quiere el frontend
        queryParams = request.args
        page = int(queryParams.get('page', 1))
        perPage = int(queryParams.get('perPage', 5))

        #El offset es la cantidad de elementos que se tiene que saltar
        offset = (int(page) - 1) * int(perPage)
        limit = perPage
        
        totalProductos = conexion.session.query(ProductoModel).count()
        productos = conexion.session.query(ProductoModel).offset(offset).limit(limit).all()

        informacionPaginacion = serializadorPaginacion (total = totalProductos, pagina=page, porPagina=perPage)
        serializador = ProductoSerializer()

        respuesta = serializador.dump(productos, many = True)
        return {
            'content': respuesta,
            'pagination': informacionPaginacion
        }
