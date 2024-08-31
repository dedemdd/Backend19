import express from 'express';
import {config} from 'dotenv';
import { enrutador } from './router.js';

config();

const servidor = express();

//Pueden entender la informacion proveniente del body en formato json
servidor.use(express.json());

const PUERTO = process.env.PORT;

//un middleware > es un intermediario en el cual se va a gestionar los errores emititdos por prisma o por otros factores
const errorHandler = (error, req, res, next) => {
    console.error(error);

    let mensajePersonalizado;
    let status;

    switch (error.message) {
        case "No Receta found":
            mensajePersonalizado = 'Receta no existe';
            status = 404;
            break;

        case "No Preparacion found":
            mensajePersonalizado = 'Preparacion no existe';
            status = 404;
            break;
        
        case "No Ingrediente found":
            mensajePersonalizado = 'Ingrediente no existe';
            status = 404;
            break;

        default:
            mensajePersonalizado = error.message;
            status = 400;
            
    }

    res.status(500).json({
        message: 'Error al hacer la operacion',
        content: mensajePersonalizado,
    });
};

//ahora agregamos la funcion como middleware


//Estamos agregando todas las rutas de nuestro servidor a nuestro proyecto de express
servidor.use(enrutador);


//Ahora agregamos la funcion como middleware
//Una vez que el error ha sido emitido en el controlador lo vamos a recibir en el middleware antes de retirnar la informacion al usuario
servidor.use(errorHandler);
servidor.listen(PUERTO, ()=> {
    console.log(`Servidor corriendo exitosamente en el puerto ${PUERTO}`);
});

