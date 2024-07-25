CREATE DATABASE ELearning;

--CREANDO LAS TABLAS
CREATE TABLE categoria (
    id SERIAL PRIMARY KEY,
    nombre TEXT UNIQUE NOT NULL
);

-- Crear la tabla cursos
CREATE TABLE cursos (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    categoria_id INT NOT NULL,
    CONSTRAINT fk_categoria FOREIGN KEY (categoria_id) REFERENCES categoria(id)
);
CREATE TABLE estudiantes (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    correo TEXT UNIQUE NOT NULL
);

-- Crear la tabla inscripciones
CREATE TABLE inscripciones (
    id SERIAL PRIMARY KEY,
    curso_id INT NOT NULL,
    CONSTRAINT fk_curso FOREIGN KEY (curso_id) REFERENCES cursos(id),
    estudiante_id INT NOT NULL,
    CONSTRAINT fk_estudiante FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
    fecha_inscripcion TIMESTAMP NOT NULL    
);

-- Crear la tabla evaluaciones
CREATE TABLE evaluaciones (
    id SERIAL PRIMARY KEY,
    inscripcion_id INT NOT NULL,
    CONSTRAINT fk_inscripcion FOREIGN KEY (inscripcion_id) REFERENCES inscripciones(id),
    nota FLOAT NOT NULL,
    fecha_evaluacion TIMESTAMP NOT NULL    
);

------INSERTANDO DATOS A LA TABLA
--ISERTANDO DATOS A LA TABLA CATEGORIA

INSERT INTO categoria (nombre) VALUES
('Cursos generales'),
('Cursos específicos');

-- INSERTANDO DATOS A LA TABLA CURSOS

INSERT INTO cursos (nombre, categoria_id) VALUES
('MATEMATICA I',1),
('MATEMATICA II',1),
('LITERATURA',1),
('CALCULO I',1),
('CALCULO II',1),
('APLICACIONES WEB',2),
('FUNDAMENTOS DE REDES',2),
('SEMINARIO DE TESIS',1),
('CIENCIA DE DATOS',2),
('BASE DE DATOS I',2),
('BASE DE DATOS II',2);

-- INSERTANDO DATOS A LA TABLA ESTUDIANTES

INSERT INTO estudiantes (nombre, correo) VALUES
 ('Lucy Silva','lsilva@gmail.com'),
 ('Alberto Peralta','aperalta@hotmail.com'),
 ('Víctor Jaramillo','vjaramillo@gmail.com'),
 ('Franck Peralta','fperalta@hotmail.com'),
 ('Oled Sanchez','osanchez@gmail.com'),
 ('Ricardo Perez','rperez@gmail.com'),
 ('Maria Ruiz','mruiz@gmail.com'),
 ('Isabel Bardales','ibardales@gmail.com'),
 ('Tula Peralta','tperalta@hotmail.com'),
 ('Alessandro Motta','amotta@gmail.com'),
 ('Eugenia Fernandez','efernandez@gmail.com');

--INSERTANDO DATOS A LA TABLA DE INSCRIPCIONES
INSERT INTO inscripciones VALUES 
(1,'1','1','2024-01-08T10:05'),
(2,'3','1','2024-01-08T15:05'),
(3,'6','1','2024-01-08T20:15'),
(4,'8','1','2024-01-08T10:25'),
(5,'4','2','2024-01-11T14:00'),
(6,'5','2','2024-01-11T14:15'),
(7,'6','2','2024-01-11T14:25'),
(8,'10','2','2024-01-11T14:35'),
(9,'1','3','2024-01-13T10:20'),
(10,'2','3','2024-01-13T10:22'),
(11,'4','3','2024-01-13T10:25'),
(12,'6','4','2024-01-14T09:05'),
(13,'7','4','2024-01-14T09:10'),
(14,'10','4','2024-01-14T09:14'),
(15,'11','4','2024-01-14T09:20'),
(16,'2','5','2024-01-14T10:00'),
(17,'3','5','2024-01-14T10:05'),
(18,'5','5','2024-01-14T10:25'),
(19,'2','6','2024-01-15T08:00'),
(20,'9','6','2024-01-15T08:05'),
(21,'10','6','2024-01-15T08:10'),
(22,'11','6','2024-01-15T08:15'),
(23,'6','7','2024-01-15T09:00'),
(24,'8','7','2024-01-15T09:03'),
(25,'10','7','2024-01-15T09:05'),
(26,'3','8','2024-01-15T09:20'),
(27,'6','8','2024-01-15T09:22'),
(28,'10','8','2024-01-15T09:25'),
(29,'8','9','2024-01-16T08:05'),
(30,'9','9','2024-01-16T08:15'),
(31,'6','10','2024-01-16T08:20'),
(32,'10','10','2024-01-16T08:25'),
(33,'11','10','2024-01-16T08:30'),
(34,'5','11','2024-01-17T10:05'),
(35,'7','11','2024-01-17T10:10'),
(36,'11','11','2024-01-17T10:15');

--INSERTANDO DATOS A LA TABLA DE EVALUACIONES

INSERT INTO evaluaciones VALUES
(1,'1','18','2024-07-01T10:15'),
(2,'1','16','2024-07-02T10:15'),
(3,'2','19','2024-07-02T10:15'),
(4,'2','20','2024-07-03T10:15'),
(5,'2','18','2024-07-03T10:50'),
(6,'3','17','2024-07-03T10:55'),
(7,'3','14','2024-07-04T11:15'),
(8,'4','15','2024-07-04T11:15'),
(9,'4','11','2024-07-04T11:25'),
(10,'4','13','2024-07-04T11:35'),
(11,'5','20','2024-07-05T08:15'),
(12,'5','16','2024-07-05T08:15'),
(13,'6','17','2024-07-05T09:00'),
(14,'6','13','2024-07-05T09:05'),
(15,'7','14','2024-07-05T09:15'),
(16,'7','16','2024-07-05T09:20'),
(17,'7','15','2024-07-05T09:35'),
(18,'8','16','2024-07-06T08:00'),
(19,'8','17','2024-07-06T08:10'),
(20,'9','11','2024-07-06T08:15'),
(21,'9','12','2024-07-06T09:15'),
(22,'10','13','2024-07-07T09:00'),
(23,'10','15','2024-07-07T09:05'),
(24,'10','14','2024-07-07T09:08'),
(25,'11','16','2024-07-07T10:15'),
(26,'11','17','2024-07-07T10:25'),
(27,'12','16','2024-07-08T08:00'),
(28,'12','14','2024-07-08T08:00'),
(29,'12','16','2024-07-08T08:35'),
(30,'13','17','2024-07-08T09:15'),
(31,'13','14','2024-07-08T09:25'),
(32,'13','16','2024-07-08T10:45'),
(33,'14','9','2024-07-09T08:15'),
(34,'14','16','2024-07-09T08:25'),
(35,'14','15','2024-07-09T08:45'),
(36,'15','14','2024-07-09T08:50'),
(37,'15','20','2024-07-09T10:15'),
(38,'16','16','2024-07-09T10:25'),
(39,'16','15','2024-07-09T10:35'),
(40,'16','13','2024-07-09T10:45'),
(41,'17','16','2024-07-10T09:00'),
(42,'17','17','2024-07-10T09:15'),
(43,'18','15','2024-07-10T10:15'),
(44,'18','13','2024-07-10T10:25'),
(45,'18','16','2024-07-10T10:35'),
(46,'19','17','2024-07-10T10:45'),
(47,'19','19','2024-07-10T10:55'),
(48,'19','20','2024-07-10T11:15');

--DEVOLVER TODOS LOS ESTUDIANTES Y LOS CURSOS QUE ESTAN INSCRITOS
SELECT est.nombre, cur.nombre FROM inscripciones
INNER JOIN estudiantes est ON est.id = inscripciones.estudiante_id
INNER JOIN cursos cur ON cur.id = inscripciones.curso_id; 

--MOSTRAR TODOS LOS CURSOS Y LOS ESTUDIANTES QUE ESTAN INSCRITOS EN ELLOS (TENER EN CUENTA QUE PUEDE HABER CURSOS SIN ESTUDIANTES)
--OBTENER EL PROMEDIO DE NOTAS POR CURSO
SELECT  cursos.nombre AS curso,
    AVG(evaluaciones.nota) AS promedio_nota
FROM  cursos
JOIN inscripciones ON cursos.id = inscripciones.curso_id
JOIN evaluaciones ON inscripciones.id = evaluaciones.inscripcion_id
GROUP BY 
--LISTAR LOS ESTUDIANTES CON SU NOMBRE Y SU PROMEDIO DE NOTAS (GROUP BY)












