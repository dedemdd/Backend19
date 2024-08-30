import { Router } from "express";
import { crearReceta } from "./controllers/recetacontrollers.js";

export const enrutador = Router();

enrutador.post('/recetas', crearReceta);

