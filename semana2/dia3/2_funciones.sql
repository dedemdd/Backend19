CREATE TABLE demostracion_triggers (
    id SERIAL PRIMARY KEY NOT NULL,
    contador INT
);

--En postgres se pueden instalar extensiones para generar UUID
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

--PARA GENERAR EL UUID DE MANERA ALEATORIA
SELECT uuid_generate_v4();


--FUNCION
CREATE OR REPLACE FUNCTION insertar_clientes_con_cuenta(nombre_cliente TEXT, 
        correo_cliente TEXT, 
        status_cliente enum_status, 
        activo_cliente BOOLEAN,
        tipo_moneda enum_tipo_moneda
        )
RETURNS VOID AS $$
-- JUSTO ANTES DE EMPEZAR LA FUNCION DECLARO LAS VARIABLES A UTILIZAR EN LA FUNCION
DECLARE
    nuevo_cliente_id INT;
BEGIN
    -- RETURNING retorna informacion si es un INSERT, UPDATE o DELETE
    INSERT INTO clientes (nombre, correo, status, activo) VALUES (nombre_cliente, correo_cliente, status_cliente, activo_cliente) RETURNING id INTO nuevo_cliente_id;

    INSERT INTO cuentas (numero_cuenta, tipo_moneda, cliente_id) VALUES (uuid_generate_v4(), tipo_moneda, nuevo_cliente_id);
END;
$$ LANGUAGE plpgsql;

--EJECUTAR LA FUNCION
SELECT insertar_clientes_con_cuenta('Shrek', 'shrek@dreamworks.com', 'TIPO_B', true, 'SOLES');


--CREAR UN TRIGGER
CREATE OR REPLACE FUNCTION incrementador()