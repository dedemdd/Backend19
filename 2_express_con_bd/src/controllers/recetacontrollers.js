import { prisma } from '../cliente.js';
import { RecetaSerializer } from '../serializers/recetaserializer.js'

//async >
export async function crearReceta(req, rest) {
    const body = req.body; // {nombre: "Tres leches de vainnilla"}
    const resultado = await prisma.receta.create({
        data: {
            nombre: body.nombre,
            descripcion: body.descripcion
        },
    });

    //resultado.
    return rest.json({
        message: 'Receta creada con exitosamente',
        content: resultado,
    });
}

export const listarRecetas = async (req, res) => {
    const resultado = await prisma.receta.findMany();

    return res.json({
        content: resultado,
    });
};

export const actualizarReceta = async (req, res) => {
    const body = req.body;

    //receta/:id
    const id = req.params.id
    //const { id} = req.params;

    const { error, value } = RecetaSerializer.validate(body);

    if (error) {
        return res.status(400).json({
            message: "Error al actualizar la receta",
            content: error.details,
        })
    }

    //SELECT id FROM receta WHERE id = '....';
    const recetaEncontrada = await prisma.receta.findUniqueOrThrow({
        
        where: { id: +id }, //{id:id}
        select: {id: true}
    });

    const recetaActualizada = await prisma.receta.update({
        where: { id: recetaEncontrada.id },
        data: {
            nombre: value.nombre,
            descripcion: value.descripcion,
            habilitado: value.habilitado,

        }
    });

    return res.json({
        message: "Receta actualizada con exito",
        content: recetaActualizada,
    });
};
