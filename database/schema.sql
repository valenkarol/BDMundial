CREATE DATABASE IF NOT EXISTS mundial2026;

USE mundial2026;

CREATE TABLE pais (
    id_pais INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE ciudad (
    id_ciudad INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    pais_sede INT NOT NULL,

    FOREIGN KEY (pais_sede)
    REFERENCES pais(id_pais)
);

CREATE TABLE estadio (
    id_estadio INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    capacidad INT NOT NULL,
    id_ciudad INT NOT NULL,

    FOREIGN KEY (id_ciudad)
    REFERENCES ciudad(id_ciudad)
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

CREATE TABLE IF NOT EXISTS equipo (

    id_equipo INT AUTO_INCREMENT PRIMARY KEY,

    nombre VARCHAR(100) NOT NULL,

    id_confederacion INT NOT NULL,

    id_grupo INT NOT NULL,

    id_director INT UNIQUE,

    id_pais INT NOT NULL,

    FOREIGN KEY (id_confederacion)
    REFERENCES confederacion(id_confederacion),

    FOREIGN KEY (id_grupo)
    REFERENCES grupo(id_grupo),

    FOREIGN KEY (id_director)
    REFERENCES director_tecnico(id_director),

    FOREIGN KEY (id_pais)
    REFERENCES pais(id_pais)
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

    FOREIGN KEY (id_equipo)
    REFERENCES equipo(id_equipo)
);

CREATE TABLE IF NOT EXISTS partido (

    id_partido INT AUTO_INCREMENT PRIMARY KEY,

    fecha DATE NOT NULL,

    id_estadio INT NOT NULL,

    id_equipo_local INT NOT NULL,

    id_equipo_visitante INT NOT NULL,

    FOREIGN KEY (id_estadio)
    REFERENCES estadio(id_estadio),

    FOREIGN KEY (id_equipo_local)
    REFERENCES equipo(id_equipo),

    FOREIGN KEY (id_equipo_visitante)
    REFERENCES equipo(id_equipo)
);

CREATE TABLE usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,

    nombreUsuario VARCHAR(100) UNIQUE NOT NULL,
    contrasena VARCHAR(100) NOT NULL,

    rol ENUM(
        'ADMIN',
        'TRADICIONAL',
        'ESPORADICO'
    ) NOT NULL
);

CREATE TABLE bitacora (
    id_bitacora INT AUTO_INCREMENT PRIMARY KEY,

    accion VARCHAR(100),

    fecha_ingreso DATE,
    fecha_salida DATE,

    hora_ingreso TIME,
    hora_salida TIME,

    id_usuario INT NOT NULL,

    FOREIGN KEY (id_usuario)
    REFERENCES usuario(id_usuario)
);