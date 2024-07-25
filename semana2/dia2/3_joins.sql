
--INNER JOIN DEVUELVE LOS REGISTROS QUE TENGAN EN COMUN LA TABLA IZQ Y DERE
SELECT * FROM clientes INNER JOIN cuentas ON clientes.id = cuentas.cliente_id;


--EL LEFT JOIN DEVUELVE TODA LAS INFORMACIÓN (REGISTROS) DE LA TABLA DE LA IZQUIERA Y OPCIONALMENTE REGISTROS EN LA TABLA DE LA DERECHA
SELECT * FROM clientes LEFT JOIN cuentas ON clientes.id = cuentas.cliente_id;

--DEVOLVER LA INF DEL CLIENTE(nombre, correo, status y N° de cuenta, tipo_moneda)
SELECT clientes.nombre, clientes.correo, clientes.status, cuentas.numero_cuenta FROM clientes INNER JOIN cuentas ON clientes.id = cuentas.cliente_id;


--DEVOLVER LA INF DEL LOS CLIENTES QUE NO SEA EN SOLES
SELECT clientes.nombre, clientes.correo, clientes.status, cuentas.tipo_moneda FROM clientes INNER JOIN cuentas ON clientes.id = cuentas.cliente_id WHERE CUENTAS.tipo_moneda <> 'SOLES';



--DEVOLVER EL CLIENTE EL MANTENIMIENTO MAS ALTO Y EL TIPO DE MONEDA DE LA CUENTA
SELECT cuentas.mantenimiento, clientes.nombre FROM clientes INNER JOIN cuentas ON clientes.id = cuentas.cliente_id ORDER BY cuentas.mantenimiento DESC LIMIT 1;
SELECT cuentas.mantenimiento, clientes.nombre FROM clientes INNER JOIN cuentas ON clientes.id = cuentas.cliente_id ORDER BY cuentas.mantenimiento DESC LIMIT 1;


--CREAR TABLA
--id ai primary key not null
--cuenta_origen RELACION CON LA TABLA CUENTAS PUEDE SER NULL
--cuenta_destino RELACION CON LA TABLA CUENTAS NO PUEDE SER NULL
--monto float not null
--fecha_operacion timestamp la hora del servidor x defecto
CREATE TABLE movimientos (
    id SERIAL PRIMARY KEY NOT NULL,
    cuenta_origen INT,
    cuenta_destino INT NOT NULL,
    monto FLOAT NOT NULL,
    fecha_operacion TIMESTAMP DEFAULT NOW(),
    CONSTRAINT fk_cuenta_origen FOREIGN KEY (cuenta_origen) REFERENCES cuentas(id),
    CONSTRAINT fk_cuenta_destino FOREIGN KEY (cuenta_destino) REFERENCES cuentas(id)
);


ALTER TABLE movimientos ALTER COLUMN cuenta_destino DROP NOT NULL;





