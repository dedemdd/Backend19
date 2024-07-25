CREATE DATABASE finanzas;

CREATE TYPE enum_status AS ENUM ('TIPO_A', 'TIPO_B', 'TIPO_C');

CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    correo TEXT UNIQUE NOT NULL,
    status enum_status NOT NULL DEFAULT 'TIPO_A',
    activo BOOLEAN DEFAULT true,
    fecha_creacion DATE DEFAULT NOW()
);

--id autoincrementable primary key
--numero_cuenta text not null unico,
--tipo_moneda SOLES | DOLARES | EUROS NOT NULL
--mantenimiento float null


-- Cuantas cuentas hay en soles, dolares y euros

-- Mostrar los numeros de cuenta y su tipo de moneda ordenados por la fecha de creacion del mas nuevo al mas viejo

-- Cual es la cuenta con mayor mantenimiento 

-- Que cliente tiene mas cuentas

INSERT INTO clientes (nombre, correo, status, activo) VALUES
('Eduardo de Rivero Manrique', 'ederivero@gmail.com', 'TIPO_B', true);

SELECT COUNT(*), tipo_moneda FROM cuentas GROUP BY tipo_moneda ORDER BY COUNT(*);
SELECT numero_cuenta, tipo_moneda,fecha_creacion FROM cuentas ORDER BY fecha_creacion DESC;
SELECT MAX(numero_cuenta) FROM cuentas;
