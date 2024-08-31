import { Router } from "express";
import { crearReceta, listarRecetas, actualizarReceta, eliminarReceta, listarRecetaPorId } from "./controllers/recetacontrollers.js";
import { crearIngrediente } from "./controllers/ingredientecontrollers.js";
import { crearPreparacion } from "./controllers/preparacioncontrollers.js";
import asyncHandler from "express-async-handler";



export const enrutador = Router();

//cuando utulizamos el mismo endpoint para dos o mas controladores, se recomienda agruaprlos
//enrutador.post('/recetas', crearReceta);
//enrutador.get('/recetas', listarRecetas);
enrutador
    .route('/recetas')
    .post(asyncHandler(crearReceta))
    .get(asyncHandler(listarRecetas));
enrutador
    .route('/receta/:id')
    .put(asyncHandler(actualizarReceta))
    .delete(asyncHandler(eliminarReceta))
    .get(asyncHandler(listarRecetaPorId));

enrutador.route('/ingredientes').post(asyncHandler(crearIngrediente)); 
enrutador.route('/preparaciones').post(asyncHandler(crearPreparacion)); 



