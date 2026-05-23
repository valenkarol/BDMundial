-- ============================================================
-- RESET COMPLETO — borra y recrea la base de datos desde cero
-- Ejecutar en HeidiSQL, DBeaver, o en la terminal de MariaDB
-- ============================================================
--solo para emergencias 

DROP DATABASE IF EXISTS mundial2026;
CREATE DATABASE mundial2026 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE mundial2026;

-- ============================================================
-- TABLAS
-- ============================================================

CREATE TABLE pais (
    id_pais INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE ciudad (
    id_ciudad INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    pais_sede INT NOT NULL,
    FOREIGN KEY (pais_sede) REFERENCES pais(id_pais)
);

CREATE TABLE estadio (
    id_estadio INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    capacidad INT NOT NULL,
    id_ciudad INT NOT NULL,
    FOREIGN KEY (id_ciudad) REFERENCES ciudad(id_ciudad)
);

CREATE TABLE confederacion (
    id_confederacion INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE grupo (
    id_grupo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(10) NOT NULL
);

CREATE TABLE director_tecnico (
    id_director INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE equipo (
    id_equipo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_confederacion INT NOT NULL,
    id_grupo INT NOT NULL,
    id_director INT UNIQUE,
    id_pais INT NOT NULL,
    FOREIGN KEY (id_confederacion) REFERENCES confederacion(id_confederacion),
    FOREIGN KEY (id_grupo)         REFERENCES grupo(id_grupo),
    FOREIGN KEY (id_director)      REFERENCES director_tecnico(id_director),
    FOREIGN KEY (id_pais)          REFERENCES pais(id_pais)
);

CREATE TABLE jugador (
    id_jugador INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    posicion VARCHAR(50),
    numero INT,
    valor DECIMAL(15,2),
    edad INT,
    peso DECIMAL(5,2),
    estatura DECIMAL(5,2),
    id_equipo INT NOT NULL,
    FOREIGN KEY (id_equipo) REFERENCES equipo(id_equipo)
);

CREATE TABLE partido (
    id_partido INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    id_estadio INT NOT NULL,
    id_equipo_local INT NOT NULL,
    id_equipo_visitante INT NOT NULL,
    FOREIGN KEY (id_estadio)          REFERENCES estadio(id_estadio),
    FOREIGN KEY (id_equipo_local)     REFERENCES equipo(id_equipo),
    FOREIGN KEY (id_equipo_visitante) REFERENCES equipo(id_equipo)
);

CREATE TABLE usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombreUsuario VARCHAR(100) UNIQUE NOT NULL,
    contrasena VARCHAR(100) NOT NULL,
    rol ENUM('ADMIN','TRADICIONAL','ESPORADICO') NOT NULL
);

CREATE TABLE bitacora (
    id_bitacora INT AUTO_INCREMENT PRIMARY KEY,
    accion VARCHAR(100),
    fecha_ingreso DATE,
    fecha_salida DATE,
    hora_ingreso TIME,
    hora_salida TIME,
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);

-- ============================================================
-- DATOS
-- ============================================================

-- PAÍSES
INSERT INTO pais (nombre) VALUES
('México'),('USA'),('Canadá'),('Argentina'),('Brasil'),
('Colombia'),('Uruguay'),('Ecuador'),('España'),('Francia'),
('Alemania'),('Portugal'),('Inglaterra'),('Italia'),('Holanda'),
('Marruecos'),('Senegal'),('Nigeria'),('Japón'),('Corea del Sur'),
('Arabia Saudita'),('Irán'),('Australia'),('Nueva Zelanda');

-- CIUDADES (solo países sede)
INSERT INTO ciudad (nombre, pais_sede) VALUES
('Ciudad de México',1),('Guadalajara',1),('Monterrey',1),
('Nueva York',2),('Los Ángeles',2),('Dallas',2),('Miami',2),
('Toronto',3),('Vancouver',3);

-- ESTADIOS
INSERT INTO estadio (nombre, capacidad, id_ciudad) VALUES
('Estadio Azteca',   87000, 1),
('Estadio Akron',    49850, 2),
('Estadio BBVA',     53500, 3),
('MetLife Stadium',  82500, 4),
('SoFi Stadium',     70000, 5),
('AT&T Stadium',     80000, 6),
('Hard Rock Stadium',65326, 7),
('BMO Field',        30000, 8),
('BC Place',         54500, 9);

-- CONFEDERACIONES
INSERT INTO confederacion (nombre) VALUES
('CONMEBOL'),('UEFA'),('CONCACAF'),('CAF'),('AFC'),('OFC');

-- GRUPOS
INSERT INTO grupo (nombre) VALUES
('A'),('B'),('C'),('D'),('E'),('F'),('G'),('H'),('I'),('J'),('K'),('L');

-- DIRECTORES TÉCNICOS
INSERT INTO director_tecnico (nombre) VALUES
('Javier Aguirre'),('Mauricio Pochettino'),('Jesse Marsch'),
('Lionel Scaloni'),('Dorival Júnior'),('Néstor Lorenzo'),
('Marcelo Bielsa'),('Sebastián Beccacece'),('Luis de la Fuente'),
('Didier Deschamps'),('Julian Nagelsmann'),('Roberto Martínez'),
('Gareth Southgate'),('Luciano Spalletti'),('Ronald Koeman'),
('Walid Regragui'),('Aliou Cissé'),('Eric Chelle'),
('Hajime Moriyasu'),('Hong Myung-Bo'),('Roberto Mancini'),
('Amir Ghalenoei'),('Tony Popovic'),('Darren Bazeley');

-- EQUIPOS (nombre, id_confederacion, id_grupo, id_director, id_pais)
INSERT INTO equipo (nombre, id_confederacion, id_grupo, id_director, id_pais) VALUES
-- GRUPO A
('México',        3,1, 1, 1),('USA',           3,1, 2, 2),
('Canadá',        3,1, 3, 3),('Uruguay',        1,1, 7, 7),
-- GRUPO B
('Argentina',     1,2, 4, 4),('Brasil',         1,2, 5, 5),
('Colombia',      1,2, 6, 6),('Ecuador',        1,2, 8, 8),
-- GRUPO C
('España',        2,3, 9, 9),('Francia',        2,3,10,10),
('Alemania',      2,3,11,11),('Portugal',       2,3,12,12),
-- GRUPO D
('Inglaterra',    2,4,13,13),('Italia',         2,4,14,14),
('Holanda',       2,4,15,15),('Marruecos',      4,4,16,16),
-- GRUPO E
('Senegal',       4,5,17,17),('Nigeria',        4,5,18,18),
('Japón',         5,5,19,19),('Corea del Sur',  5,5,20,20),
-- GRUPO F
('Arabia Saudita',5,6,21,21),('Irán',           5,6,22,22),
('Australia',     5,6,23,23),('Nueva Zelanda',  6,6,24,24);

-- JUGADORES (nombre, posicion, numero, valor, edad, peso, estatura, id_equipo)
INSERT INTO jugador (nombre, posicion, numero, valor, edad, peso, estatura, id_equipo) VALUES
-- México (1)
('Guillermo Ochoa','Portero',1,5000000,39,80,1.83,1),
('Edson Álvarez','Mediocampista',4,30000000,26,79,1.90,1),
('Santiago Giménez','Delantero',9,40000000,23,80,1.84,1),
('Hirving Lozano','Extremo',22,20000000,20,72,1.73,1),
-- USA (2)
('Matt Turner','Portero',1,6000000,30,87,1.93,2),
('Christian Pulisic','Mediocampista',10,45000000,26,70,1.77,2),
('Gio Reyna','Extremo',7,20000000,22,69,1.80,2),
('Ricardo Pepi','Delantero',9,15000000,21,79,1.88,2),
-- Canadá (3)
('Milan Borjan','Portero',18,3000000,36,91,1.94,3),
('Alphonso Davies','Lateral',19,70000000,24,76,1.80,3),
('Jonathan David','Delantero',9,55000000,24,75,1.81,3),
('Tajon Buchanan','Extremo',11,10000000,25,72,1.79,3),
-- Uruguay (4)
('Sergio Rochet','Portero',1,4000000,29,84,1.92,4),
('Federico Valverde','Mediocampista',8,80000000,26,78,1.82,4),
('Darwin Núñez','Delantero',9,75000000,25,81,1.87,4),
('Luis Suárez','Delantero',10,5000000,37,86,1.82,4),
-- Argentina (5)
('Emiliano Martínez','Portero',23,25000000,32,86,1.95,5),
('Lionel Messi','Delantero',10,35000000,37,72,1.70,5),
('Julián Álvarez','Delantero',9,80000000,24,73,1.70,5),
('Enzo Fernández','Mediocampista',24,90000000,24,73,1.78,5),
-- Brasil (6)
('Alisson Becker','Portero',1,30000000,32,91,1.93,6),
('Vinícius Jr.','Extremo',7,200000000,24,73,1.76,6),
('Rodrygo','Extremo',11,90000000,24,68,1.74,6),
('Endrick','Delantero',9,60000000,18,68,1.73,6),
-- Colombia (7)
('Camilo Vargas','Portero',1,3000000,33,80,1.89,7),
('Luis Díaz','Extremo',7,85000000,27,65,1.80,7),
('James Rodríguez','Mediocampista',10,10000000,33,78,1.80,7),
('Jhon Córdoba','Delantero',9,12000000,31,82,1.92,7),
-- Ecuador (8)
('Hernán Galíndez','Portero',1,2000000,35,82,1.90,8),
('Moisés Caicedo','Mediocampista',10,90000000,23,73,1.80,8),
('Enner Valencia','Delantero',13,5000000,35,77,1.76,8),
('Gonzalo Plata','Extremo',20,15000000,23,70,1.77,8),
-- España (9)
('Unai Simón','Portero',1,20000000,27,84,1.90,9),
('Pedri','Mediocampista',26,120000000,22,63,1.74,9),
('Lamine Yamal','Extremo',19,150000000,17,65,1.76,9),
('Álvaro Morata','Delantero',7,20000000,32,82,1.87,9),
-- Francia (10)
('Mike Maignan','Portero',16,35000000,29,86,1.91,10),
('Kylian Mbappé','Delantero',10,180000000,26,78,1.78,10),
('Antoine Griezmann','Mediocampista',7,30000000,33,73,1.76,10),
('Aurélien Tchouaméni','Mediocampista',8,80000000,24,85,1.87,10),
-- Alemania (11)
('Manuel Neuer','Portero',1,10000000,38,92,1.93,11),
('Florian Wirtz','Mediocampista',10,130000000,21,70,1.76,11),
('Jamal Musiala','Mediocampista',14,110000000,21,70,1.80,11),
('Kai Havertz','Delantero',9,70000000,25,82,1.89,11),
-- Portugal (12)
('Diogo Costa','Portero',1,30000000,25,84,1.90,12),
('Cristiano Ronaldo','Delantero',7,25000000,39,85,1.87,12),
('Rafael Leão','Extremo',17,80000000,25,82,1.88,12),
('Vitinha','Mediocampista',16,70000000,24,67,1.74,12),
-- Inglaterra (13)
('Jordan Pickford','Portero',1,20000000,30,74,1.85,13),
('Jude Bellingham','Mediocampista',10,180000000,21,75,1.86,13),
('Harry Kane','Delantero',9,100000000,31,86,1.88,13),
('Phil Foden','Mediocampista',47,150000000,24,69,1.71,13),
-- Italia (14)
('Gianluigi Donnarumma','Portero',1,50000000,26,90,1.96,14),
('Nicolò Barella','Mediocampista',18,80000000,27,77,1.77,14),
('Federico Chiesa','Extremo',14,35000000,27,75,1.75,14),
('Mateo Retegui','Delantero',9,30000000,25,79,1.87,14),
-- Holanda (15)
('Bart Verbruggen','Portero',22,20000000,22,84,1.97,15),
('Virgil van Dijk','Defensa',4,25000000,33,93,1.95,15),
('Xavi Simons','Mediocampista',10,80000000,21,65,1.81,15),
('Memphis Depay','Delantero',10,10000000,30,78,1.76,15),
-- Marruecos (16)
('Yassine Bounou','Portero',1,20000000,33,84,1.91,16),
('Achraf Hakimi','Lateral',2,65000000,26,73,1.81,16),
('Hakim Ziyech','Mediocampista',7,15000000,31,65,1.80,16),
('Youssef En-Nesyri','Delantero',9,25000000,27,82,1.89,16),
-- Senegal (17)
('Édouard Mendy','Portero',16,15000000,32,81,1.97,17),
('Sadio Mané','Extremo',10,25000000,32,69,1.75,17),
('Idrissa Gueye','Mediocampista',15,10000000,34,66,1.75,17),
('Boulaye Dia','Delantero',9,22000000,27,78,1.84,17),
-- Nigeria (18)
('Francis Uzoho','Portero',16,5000000,26,82,1.90,18),
('Victor Osimhen','Delantero',9,100000000,25,78,1.86,18),
('Wilfred Ndidi','Mediocampista',4,20000000,27,77,1.82,18),
('Alex Iwobi','Mediocampista',17,20000000,28,75,1.78,18),
-- Japón (19)
('Shuichi Gonda','Portero',12,2000000,34,79,1.82,19),
('Takefusa Kubo','Mediocampista',8,35000000,23,65,1.73,19),
('Junya Ito','Extremo',14,10000000,31,69,1.76,19),
('Kaoru Mitoma','Extremo',9,45000000,27,69,1.78,19),
-- Corea del Sur (20)
('Kim Seung-gyu','Portero',18,3000000,34,82,1.89,20),
('Son Heung-min','Delantero',7,35000000,32,78,1.83,20),
('Lee Kang-in','Mediocampista',10,30000000,23,68,1.73,20),
('Hwang Hee-chan','Extremo',9,25000000,28,72,1.76,20),
-- Arabia Saudita (21)
('Mohammed Al-Owais','Portero',21,3000000,32,80,1.88,21),
('Salem Al-Dawsari','Extremo',11,4000000,32,68,1.71,21),
('Firas Al-Buraikan','Delantero',9,5000000,24,75,1.80,21),
('Sami Al-Najei','Defensa',5,1000000,33,80,1.87,21),
-- Irán (22)
('Alireza Beiranvand','Portero',1,2000000,32,88,1.96,22),
('Mehdi Taremi','Delantero',9,18000000,32,83,1.87,22),
('Sardar Azmoun','Delantero',7,10000000,29,84,1.90,22),
('Ali Karimi','Mediocampista',14,3000000,20,69,1.77,22),
-- Australia (23)
('Mat Ryan','Portero',1,3000000,32,78,1.84,23),
('Martin Boyle','Extremo',20,4000000,31,70,1.71,23),
('Mathew Leckie','Extremo',7,3000000,33,73,1.80,23),
('Mitchell Duke','Delantero',9,2000000,33,80,1.83,23),
-- Nueva Zelanda (24)
('Max Crocombe','Portero',1,500000,31,84,1.88,24),
('Chris Wood','Delantero',9,5000000,32,87,1.90,24),
('Clayton Lewis','Mediocampista',14,2000000,26,73,1.77,24),
('Joe Bell','Mediocampista',6,1000000,24,75,1.82,24);

-- PARTIDOS
INSERT INTO partido (fecha, id_estadio, id_equipo_local, id_equipo_visitante) VALUES
-- Grupo A
('2026-06-11',1,1,2),('2026-06-12',8,3,4),('2026-06-15',4,1,3),
('2026-06-15',5,2,4),('2026-06-19',6,1,4),('2026-06-19',7,2,3),
-- Grupo B
('2026-06-13',4,5,6),('2026-06-13',1,7,8),('2026-06-17',5,5,7),
('2026-06-17',6,6,8),('2026-06-21',7,5,8),('2026-06-21',8,6,7),
-- Grupo C
('2026-06-14',4,9,10),('2026-06-14',9,11,12),('2026-06-18',5,9,11),
('2026-06-18',6,10,12),('2026-06-22',1,9,12),('2026-06-22',3,10,11),
-- Grupo D
('2026-06-15',4,13,14),('2026-06-15',9,15,16),('2026-06-19',2,13,15),
('2026-06-19',3,14,16),('2026-06-23',1,13,16),('2026-06-23',8,14,15),
-- Grupo E
('2026-06-16',6,17,18),('2026-06-16',9,19,20),('2026-06-20',7,17,19),
('2026-06-20',8,18,20),('2026-06-24',4,17,20),('2026-06-24',5,18,19),
-- Grupo F
('2026-06-16',1,21,22),('2026-06-16',2,23,24),('2026-06-20',3,21,23),
('2026-06-20',6,22,24),('2026-06-24',7,21,24),('2026-06-24',9,22,23);

-- USUARIO ADMIN
INSERT INTO usuario (nombreUsuario, contrasena, rol) VALUES
('admin','admin123','ADMIN');