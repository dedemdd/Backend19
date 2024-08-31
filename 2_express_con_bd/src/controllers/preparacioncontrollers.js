import { prisma } from '../cliente.js';
import { PreparacionSerializer } from '../serializers/preparacionserializer.js'

export const crearPreparacion = async (req, res)=> {
    const {error, value} = PreparacionSerializer.validate(req.body);

    if(error) {
        return res.status(400).json({
            message: "Error al crear la preparacion",
            content: error.details
        });
    }

    //Buscar si ya existe una preparacion de la receeta
    //Select orden FROM preparaciones WHERE receta_id = '...' ORDER BY orden DESC;
    const prepacionExistente = await prisma.preparacion.findFirst({
        where: {recetaId: value.recetaId},
        orderBy: {orden: 'desc'},
        select: {orden: true}
    });
    //let nuevaPosicion;

    //if (prepacionExistente){
    //    nuevaPosicion = prepacionExistente.orden + 1;
    //} else {
    //    nuevaPosicion = 1;
   // }

    const nuevaPosicion = prepacionExistente
        ? prepacionExistente.orden + 1
        : 1;
    
    const nuevaPreparacion = await prisma.preparacion.create({
        data : {
            descripcion: value.descripcion,
            recetaId: value.recetaId,
            orden: nuevaPosicion
        }
    });

    return res.status(201).json({
        message: "Preparacion creada exitosamente",
        content: nuevaPreparacion
    });
};