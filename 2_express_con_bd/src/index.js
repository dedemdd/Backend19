import express from 'express';
import {config} from 'dotenv';
import { enrutador } from './router.js';

config();

const servidor = express();

//Pueden entender la informacion proveniente del body en formato json
servidor.use(express.json());

const PUERTO = process.env.PORT;


//Estamos agregando todas las rutas de nuestro servidor a nuestro proyecto de express
servidor.use(enrutador);

servidor.listen(PUERTO, ()=> {
    console.log(`Servidor corriendo exitosamente en el puerto ${PUERTO}`);
});

