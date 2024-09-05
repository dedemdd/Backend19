import express from 'express';
import morgan from 'morgan';


const servidor = express();
const PORT =process.env.PORT

//Agregamos logger de las request de nuestro servidor
servidor.use(morgan('common'));

servidor.listen(PORT, ()=> {
    console.log(`Servidor de express levantado en el puerto ${PORT}`);
});

