import { Router } from "express";
import { crearEquipo, listarEquipos } from "./controllers/equiposcontrollers.js";
import {
  registroUsuario,
  login,
  perfilUsuario,
} from "./controllers/usuariocontrollers.js";
import { generarUrlFirmada, crearImagen, devolverImagen } from "./controllers/imagencontrollers.js";
import asyncHandler from "express-async-handler";
import { validarToken, validarAdmin } from "./utils.js";



export const rutas = Router();

rutas
  .route("/equipos")
  .post(
    //asyncHandler(validarToken),
    //asyncHandler(validarAdmin),
    asyncHandler(crearEquipo)
  )
  .get(asyncHandler(listarEquipos));

rutas.route("/registro").post(asyncHandler(registroUsuario));

rutas.route("/login").post(asyncHandler(login));

rutas
  .route("/perfil")
  .get(asyncHandler(validarToken), asyncHandler(perfilUsuario));

rutas.route("/generar-url").post(asyncHandler(generarUrlFirmada));

rutas.route("/imagen").post(asyncHandler(crearImagen));

rutas.route("/imagen/:id").post(asyncHandler(devolverImagen));


