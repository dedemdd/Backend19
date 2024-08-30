import express from 'express';

const servidor = express();
//Le estamos indicando a nuestro servidor que pueda entender y convertr la informacion provenientes del body 
servidor.use(express.json());

servidor.get('/', (req, res)=> {
    res.status(201).json({
        message: 'Bienvenido a mi API de express'});
});

servidor.post('/registro', (req, res)=> {
    console.log(req.body);
    //En express tenemos que indicarle que body va a poder recepcionar 
    //Si va a recepcionar json, xml txt, otros
    res.json({
        message: 'Registro completado exitosamente'
    });
})

servidor.listen(3000, ()=> {
    console.log('Servidor de express levantado existosamente');
});