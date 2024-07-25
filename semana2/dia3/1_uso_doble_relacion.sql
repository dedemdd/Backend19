INSERT INTO movimientos (cuenta_origen, cuenta_destino, monto, fecha_operacion) VALUES
(null, 1, 100.10, '2024-07-01T14:15:17'),
(null, 2, 500.20, '2024-07-06T09:30:15'),
(null, 3, 650.00, '2024-07-06T15:29:18'),
(null, 4, 456.00, '2024-07-08T10:15:17'),
(null, 5, 500.00, '2024-07-10T17:18:24'),
(null, 6, 1050.24, '2024-07-04T12:12:12'),
(null, 7, 984.78, '2024-07-09TT11:06:49'),
(1,2, 40.30, '2024-07-10T10:10:10'),
(4,7, 350.00, '2024-07-16T20:15:35'),
(3, null, 50.00, '2024-07-16T22:15:10'),
(5, null, 100.00, '2024-07-17T10:19:25'),
(6, null, 350.28, '2024-07-18T14:15:16');

--OBTENER EL SALDO DE LAS CUENTAS
SELECT *, 
CASE
    WHEN cuenta_origen IS NULL AND cuenta_destino IS NOT NULL THEN 'DEPOSITO'
    WHEN cuenta_origen IS NOT NULL AND cuenta_destino IS NULL THEN 'RETIRO'
    WHEN cuenta_origen IS NOT NULL AND cuenta_destino IS NOT NULL THEN 'TRANSFERENCIA'
    ELSE 'MOVIMIENTO DESCONOCIDO'
END AS tipo_movimiento 
FROM movimientos;

--------
-- En base al correo de los clientes hacer lo siguiente 
-- Si el dominio es gmail indicar 'ES JOVEN' si es yahoo indicar 'ES UN DINOSAURIO' y si es HOTMAIL indicar 'ES ADULTO' caso contrario indicar 'DOMINIO DESCONOCIDO'

SELECT *,
    CASE 
        WHEN correo like '%gmail.com' THEN 'ES JOVEN'
        WHEN correo like '%yahoo.com' THEN 'ES UN DINOSAURIO'
        WHEN correo like '%hotmail.com' THEN 'ES ADULTO'
        ELSE 'DOMINIO DESCONOCIDO'
    END AS tipo_correo
FROM clientes;
------------------------------------

--OBTENEMOS LOS DEBITOS DE TODAS LAS CUENTAS (LO QUE SALE)
SELECT cuenta_origen AS cuenta, SUM(monto) as debito
FROM movimientos
WHERE cuenta_origen IS NOT NULL
GROUP BY cuenta_origen;

--OBTENEMOS LOS CREDITOS DE TODAS LAS CUENTAS (LO QUE ENTRA)
SELECT cuenta_destino AS cuenta, SUM(monto) as credito
FROM movimientos
WHERE cuenta_destino IS NOT NULL
GROUP BY cuenta_destino;

--COMBINANMOS LAS DOS CONSULTAS
WITH debitos AS (
  SELECT cuenta_origen AS cuenta, SUM(monto) AS debitos
  FROM movimientos
  WHERE cuenta_origen IS NOT NULL
  GROUP BY cuenta_origen
),
creditos AS (
  SELECT cuenta_destino AS cuenta, SUM(monto) AS creditos
  FROM movimientos
  WHERE cuenta_destino IS NOT NULL
  GROUP BY cuenta_destino
)

-- COALESCE es una funcion que acepta una lista de argumentos y retorna el primero elemento no nulo de la lista
SELECT  COALESCE(debitos.cuenta, creditos.cuenta) AS cuenta, COALESCE(creditos.creditos, 0) - COALESCE(debitos.debitos, 0)
FROM debitos
FULL OUTER JOIN creditos ON debitos.cuenta = creditos.cuenta
ORDER BY cuenta;

-----