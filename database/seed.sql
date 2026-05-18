USE mundial2026;

-- PAISES
INSERT INTO pais(nombre)
VALUES
('Colombia'),
('Brasil'),
('Argentina'),
('España'),
('Francia');

-- CIUDADES
INSERT INTO ciudad(nombre, pais_sede)
VALUES
('Bogotá', 1),
('Medellín', 1),
('Río de Janeiro', 2),
('Buenos Aires', 3),
('Madrid', 4);

-- ESTADIOS
INSERT INTO estadio(nombre, capacidad, id_ciudad)
VALUES
('Metropolitano', 50000, 1),
('Maracaná', 78000, 3),
('Monumental', 70000, 4);

-- CONFEDERACIONES
INSERT INTO confederacion(nombre)
VALUES
('CONMEBOL'),
('UEFA'),
('CONCACAF');

-- GRUPOS
INSERT INTO grupo(nombre)
VALUES
('A'),
('B'),
('C'),
('D');

-- DIRECTORES
INSERT INTO director_tecnico(nombre)
VALUES
('Néstor Lorenzo'),
('Scaloni'),
('Didier Deschamps');

-- EQUIPOS
INSERT INTO equipo(
nombre,
id_confederacion,
id_grupo,
id_director
)
VALUES
('Colombia', 1, 1, 1),
('Argentina', 1, 2, 2),
('Francia', 2, 3, 3);

-- JUGADORES
INSERT INTO jugador(
nombre,
posicion,
numero,
valor,
edad,
peso,
estatura,
id_equipo
)
VALUES
(
'Luis Díaz',
'Extremo',
7,
85000000,
27,
65,
1.80,
1
),

(
'Messi',
'Delantero',
10,
50000000,
37,
72,
1.70,
2
),

(
'Mbappé',
'Delantero',
9,
180000000,
25,
75,
1.78,
3
);

-- PARTIDOS
INSERT INTO partido(
fecha,
id_estadio,
id_equipo_local
)
VALUES
('2026-06-11', 1, 1),
('2026-06-12', 2, 2),
('2026-06-13', 3, 3);