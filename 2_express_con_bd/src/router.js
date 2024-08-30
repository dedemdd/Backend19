import { Router } from "express";
import { crearReceta, listarRecetas, actualizarReceta } from "./controllers/recetacontrollers.js";

export const enrutador = Router();

//cuando utulizamos el mismo endpoint para dos o mas controladores, se recomienda agruaprlos
//enrutador.post('/recetas', crearReceta);
//enrutador.get('/recetas', listarRecetas);
enrutador.route('/recetas').post(crearReceta).get(listarRecetas);
enrutador.route('/receta/:id').put(actualizarReceta);




