CREATE TYPE enum_tipo_moneda AS ENUM ('SOLES', 'DOLARES', 'EUROS');

CREATE TABLE cuentas (
    id SERIAL PRIMARY KEY NOT NULL,
    numero_cuenta TEXT NOT NULL UNIQUE,
    tipo_moneda enum_tipo_moneda NOT NULL,
    fecha_creacion DATE DEFAULT NOW(),
    mantenimiento FLOAT NULL,
    cliente_id INT NOT NULL,
    CONSTRAINT fk_clientes FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);