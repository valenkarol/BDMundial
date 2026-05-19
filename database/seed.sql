USE mundial2026;

-- ============================================================
-- PAÍSES (equipos participantes + países sede)
-- ============================================================
INSERT INTO pais (nombre) VALUES
('México'),        -- 1  (país sede)
('USA'),           -- 2  (país sede)
('Canadá'),        -- 3  (país sede)
('Argentina'),     -- 4
('Brasil'),        -- 5
('Colombia'),      -- 6
('Uruguay'),       -- 7
('Ecuador'),       -- 8
('España'),        -- 9
('Francia'),       -- 10
('Alemania'),      -- 11
('Portugal'),      -- 12
('Inglaterra'),    -- 13
('Italia'),        -- 14
('Holanda'),       -- 15
('Marruecos'),     -- 16
('Senegal'),       -- 17
('Nigeria'),       -- 18
('Japón'),         -- 19
('Corea del Sur'), -- 20
('Arabia Saudita'),-- 21
('Irán'),          -- 22
('Australia'),     -- 23
('Nueva Zelanda'); -- 24

-- ============================================================
-- CIUDADES (solo en países sede: México, USA, Canadá)
-- ============================================================
INSERT INTO ciudad (nombre, pais_sede) VALUES
('Ciudad de México', 1),  -- 1
('Guadalajara',      1),  -- 2
('Monterrey',        1),  -- 3
('Nueva York',       2),  -- 4
('Los Ángeles',      2),  -- 5
('Dallas',           2),  -- 6
('Miami',            2),  -- 7
('Toronto',          3),  -- 8
('Vancouver',        3);  -- 9

-- ============================================================
-- ESTADIOS (en los países sede)
-- ============================================================
INSERT INTO estadio (nombre, capacidad, id_ciudad) VALUES
('Estadio Azteca',           87000, 1),  -- 1  México
('Estadio Akron',            49850, 2),  -- 2  Guadalajara
('Estadio BBVA',             53500, 3),  -- 3  Monterrey
('MetLife Stadium',          82500, 4),  -- 4  Nueva York
('SoFi Stadium',             70000, 5),  -- 5  Los Ángeles
('AT&T Stadium',             80000, 6),  -- 6  Dallas
('Hard Rock Stadium',        65326, 7),  -- 7  Miami
('BMO Field',                30000, 8),  -- 8  Toronto
('BC Place',                 54500, 9);  -- 9  Vancouver

-- ============================================================
-- CONFEDERACIONES
-- ============================================================
INSERT INTO confederacion (nombre) VALUES
('CONMEBOL'),   -- 1
('UEFA'),       -- 2
('CONCACAF'),   -- 3
('CAF'),        -- 4
('AFC'),        -- 5
('OFC');        -- 6

-- ============================================================
-- GRUPOS (12 grupos: A a L)
-- ============================================================
INSERT INTO grupo (nombre) VALUES
('A'),  -- 1
('B'),  -- 2
('C'),  -- 3
('D'),  -- 4
('E'),  -- 5
('F'),  -- 6
('G'),  -- 7
('H'),  -- 8
('I'),  -- 9
('J'),  -- 10
('K'),  -- 11
('L');  -- 12

-- ============================================================
-- DIRECTORES TÉCNICOS
-- ============================================================
INSERT INTO director_tecnico (nombre) VALUES
('Javier Aguirre'),       -- 1  México
('Mauricio Pochettino'),  -- 2  USA
('Jesse Marsch'),         -- 3  Canadá
('Lionel Scaloni'),       -- 4  Argentina
('Dorival Júnior'),       -- 5  Brasil
('Néstor Lorenzo'),       -- 6  Colombia
('Marcelo Bielsa'),       -- 7  Uruguay
('Sebastián Beccacece'),  -- 8  Ecuador
('Luis de la Fuente'),    -- 9  España
('Didier Deschamps'),     -- 10 Francia
('Julian Nagelsmann'),    -- 11 Alemania
('Roberto Martínez'),     -- 12 Portugal
('Gareth Southgate'),     -- 13 Inglaterra
('Luciano Spalletti'),    -- 14 Italia
('Ronald Koeman'),        -- 15 Holanda
('Walid Regragui'),       -- 16 Marruecos
('Aliou Cissé'),          -- 17 Senegal
('Eric Chelle'),          -- 18 Nigeria
('Hajime Moriyasu'),      -- 19 Japón
('Hong Myung-Bo'),        -- 20 Corea del Sur
('Roberto Mancini'),      -- 21 Arabia Saudita
('Amir Ghalenoei'),       -- 22 Irán
('Tony Popovic'),         -- 23 Australia
('Darren Bazeley');       -- 24 Nueva Zelanda

-- ============================================================
-- EQUIPOS  (nombre, id_confederacion, id_grupo, id_director, id_pais)
-- ============================================================
INSERT INTO equipo (nombre, id_confederacion, id_grupo, id_director, id_pais) VALUES
-- GRUPO A
('México',         3, 1,  1,  1),
('USA',            3, 1,  2,  2),
('Canadá',         3, 1,  3,  3),
('Uruguay',        1, 1,  7,  7),

-- GRUPO B
('Argentina',      1, 2,  4,  4),
('Brasil',         1, 2,  5,  5),
('Colombia',       1, 2,  6,  6),
('Ecuador',        1, 2,  8,  8),

-- GRUPO C
('España',         2, 3,  9,  9),
('Francia',        2, 3, 10, 10),
('Alemania',       2, 3, 11, 11),
('Portugal',       2, 3, 12, 12),

-- GRUPO D
('Inglaterra',     2, 4, 13, 13),
('Italia',         2, 4, 14, 14),
('Holanda',        2, 4, 15, 15),
('Marruecos',      4, 4, 16, 16),

-- GRUPO E
('Senegal',        4, 5, 17, 17),
('Nigeria',        4, 5, 18, 18),
('Japón',          5, 5, 19, 19),
('Corea del Sur',  5, 5, 20, 20),

-- GRUPO F
('Arabia Saudita', 5, 6, 21, 21),
('Irán',           5, 6, 22, 22),
('Australia',      5, 6, 23, 23),
('Nueva Zelanda',  6, 6, 24, 24);

-- ============================================================
-- JUGADORES (nombre, posicion, numero, valor, edad, peso, estatura, id_equipo)
-- ============================================================
INSERT INTO jugador (nombre, posicion, numero, valor, edad, peso, estatura, id_equipo) VALUES
-- México (id_equipo 1)
('Guillermo Ochoa',   'Portero',    1,  5000000, 39, 80, 1.83, 1),
('Edson Álvarez',     'Mediocampista', 4, 30000000, 26, 79, 1.90, 1),
('Santiago Giménez',  'Delantero',  9, 40000000, 23, 80, 1.84, 1),
('Hirving Lozano',    'Extremo',    22, 20000000, 20, 72, 1.73, 1),

-- USA (id_equipo 2)
('Matt Turner',       'Portero',    1,  6000000, 30, 87, 1.93, 2),
('Christian Pulisic', 'Mediocampista', 10, 45000000, 26, 70, 1.77, 2),
('Gio Reyna',         'Extremo',    7, 20000000, 22, 69, 1.80, 2),
('Ricardo Pepi',      'Delantero',  9, 15000000, 21, 79, 1.88, 2),

-- Canadá (id_equipo 3)
('Milan Borjan',      'Portero',    18, 3000000, 36, 91, 1.94, 3),
('Alphonso Davies',   'Lateral',    19, 70000000, 24, 76, 1.80, 3),
('Jonathan David',    'Delantero',  9, 55000000, 24, 75, 1.81, 3),
('Tajon Buchanan',    'Extremo',    11, 10000000, 25, 72, 1.79, 3),

-- Uruguay (id_equipo 4)
('Sergio Rochet',     'Portero',    1,  4000000, 29, 84, 1.92, 4),
('Federico Valverde', 'Mediocampista', 8, 80000000, 26, 78, 1.82, 4),
('Darwin Núñez',      'Delantero',  9, 75000000, 25, 81, 1.87, 4),
('Luis Suárez',       'Delantero',  10, 5000000, 37, 86, 1.82, 4),

-- Argentina (id_equipo 5)
('Emiliano Martínez', 'Portero',    23, 25000000, 32, 86, 1.95, 5),
('Lionel Messi',      'Delantero',  10, 35000000, 37, 72, 1.70, 5),
('Julián Álvarez',    'Delantero',  9, 80000000, 24, 73, 1.70, 5),
('Enzo Fernández',    'Mediocampista', 24, 90000000, 24, 73, 1.78, 5),

-- Brasil (id_equipo 6)
('Alisson Becker',    'Portero',    1, 30000000, 32, 91, 1.93, 6),
('Vinícius Jr.',      'Extremo',    7, 200000000, 24, 73, 1.76, 6),
('Rodrygo',           'Extremo',    11, 90000000, 24, 68, 1.74, 6),
('Endrick',           'Delantero',  9, 60000000, 18, 68, 1.73, 6),

-- Colombia (id_equipo 7)
('Camilo Vargas',     'Portero',    1,  3000000, 33, 80, 1.89, 7),
('Luis Díaz',         'Extremo',    7, 85000000, 27, 65, 1.80, 7),
('James Rodríguez',   'Mediocampista', 10, 10000000, 33, 78, 1.80, 7),
('Jhon Córdoba',      'Delantero',  9, 12000000, 31, 82, 1.92, 7),

-- Ecuador (id_equipo 8)
('Hernán Galíndez',   'Portero',    1,  2000000, 35, 82, 1.90, 8),
('Moisés Caicedo',    'Mediocampista', 10, 90000000, 23, 73, 1.80, 8),
('Enner Valencia',    'Delantero',  13, 5000000, 35, 77, 1.76, 8),
('Gonzalo Plata',     'Extremo',    20, 15000000, 23, 70, 1.77, 8),

-- España (id_equipo 9)
('Unai Simón',        'Portero',    1, 20000000, 27, 84, 1.90, 9),
('Pedri',             'Mediocampista', 26, 120000000, 22, 63, 1.74, 9),
('Lamine Yamal',      'Extremo',    19, 150000000, 17, 65, 1.76, 9),
('Álvaro Morata',     'Delantero',  7, 20000000, 32, 82, 1.87, 9),

-- Francia (id_equipo 10)
('Mike Maignan',      'Portero',    16, 35000000, 29, 86, 1.91, 10),
('Kylian Mbappé',     'Delantero',  10, 180000000, 26, 78, 1.78, 10),
('Antoine Griezmann', 'Mediocampista', 7, 30000000, 33, 73, 1.76, 10),
('Aurélien Tchouaméni','Mediocampista', 8, 80000000, 24, 85, 1.87, 10),

-- Alemania (id_equipo 11)
('Manuel Neuer',      'Portero',    1, 10000000, 38, 92, 1.93, 11),
('Florian Wirtz',     'Mediocampista', 10, 130000000, 21, 70, 1.76, 11),
('Jamal Musiala',     'Mediocampista', 14, 110000000, 21, 70, 1.80, 11),
('Kai Havertz',       'Delantero',  9, 70000000, 25, 82, 1.89, 11),

-- Portugal (id_equipo 12)
('Diogo Costa',       'Portero',    1, 30000000, 25, 84, 1.90, 12),
('Cristiano Ronaldo', 'Delantero',  7, 25000000, 39, 85, 1.87, 12),
('Rafael Leão',       'Extremo',    17, 80000000, 25, 82, 1.88, 12),
('Vitinha',           'Mediocampista', 16, 70000000, 24, 67, 1.74, 12),

-- Inglaterra (id_equipo 13)
('Jordan Pickford',   'Portero',    1, 20000000, 30, 74, 1.85, 13),
('Jude Bellingham',   'Mediocampista', 10, 180000000, 21, 75, 1.86, 13),
('Harry Kane',        'Delantero',  9, 100000000, 31, 86, 1.88, 13),
('Phil Foden',        'Mediocampista', 47, 150000000, 24, 69, 1.71, 13),

-- Italia (id_equipo 14)
('Gianluigi Donnarumma', 'Portero', 1, 50000000, 26, 90, 1.96, 14),
('Nicolò Barella',    'Mediocampista', 18, 80000000, 27, 77, 1.77, 14),
('Federico Chiesa',   'Extremo',    14, 35000000, 27, 75, 1.75, 14),
('Mateo Retegui',     'Delantero',  9, 30000000, 25, 79, 1.87, 14),

-- Holanda (id_equipo 15)
('Bart Verbruggen',   'Portero',    22, 20000000, 22, 84, 1.97, 15),
('Virgil van Dijk',   'Defensa',    4, 25000000, 33, 93, 1.95, 15),
('Xavi Simons',       'Mediocampista', 10, 80000000, 21, 65, 1.81, 15),
('Memphis Depay',     'Delantero',  10, 10000000, 30, 78, 1.76, 15),

-- Marruecos (id_equipo 16)
('Yassine Bounou',    'Portero',    1, 20000000, 33, 84, 1.91, 16),
('Achraf Hakimi',     'Lateral',    2, 65000000, 26, 73, 1.81, 16),
('Hakim Ziyech',      'Mediocampista', 7, 15000000, 31, 65, 1.80, 16),
('Youssef En-Nesyri', 'Delantero',  9, 25000000, 27, 82, 1.89, 16),

-- Senegal (id_equipo 17)
('Édouard Mendy',     'Portero',    16, 15000000, 32, 81, 1.97, 17),
('Sadio Mané',        'Extremo',    10, 25000000, 32, 69, 1.75, 17),
('Idrissa Gueye',     'Mediocampista', 15, 10000000, 34, 66, 1.75, 17),
('Boulaye Dia',       'Delantero',  9, 22000000, 27, 78, 1.84, 17),

-- Nigeria (id_equipo 18)
('Francis Uzoho',     'Portero',    16, 5000000, 26, 82, 1.90, 18),
('Victor Osimhen',    'Delantero',  9, 100000000, 25, 78, 1.86, 18),
('Wilfred Ndidi',     'Mediocampista', 4, 20000000, 27, 77, 1.82, 18),
('Alex Iwobi',        'Mediocampista', 17, 20000000, 28, 75, 1.78, 18),

-- Japón (id_equipo 19)
('Shuichi Gonda',     'Portero',    12, 2000000, 34, 79, 1.82, 19),
('Takefusa Kubo',     'Mediocampista', 8, 35000000, 23, 65, 1.73, 19),
('Junya Ito',         'Extremo',    14, 10000000, 31, 69, 1.76, 19),
('Kaoru Mitoma',      'Extremo',    9, 45000000, 27, 69, 1.78, 19),

-- Corea del Sur (id_equipo 20)
('Kim Seung-gyu',     'Portero',    18, 3000000, 34, 82, 1.89, 20),
('Son Heung-min',     'Delantero',  7, 35000000, 32, 78, 1.83, 20),
('Lee Kang-in',       'Mediocampista', 10, 30000000, 23, 68, 1.73, 20),
('Hwang Hee-chan',    'Extremo',    9, 25000000, 28, 72, 1.76, 20),

-- Arabia Saudita (id_equipo 21)
('Mohammed Al-Owais', 'Portero',    21, 3000000, 32, 80, 1.88, 21),
('Salem Al-Dawsari',  'Extremo',    11, 4000000, 32, 68, 1.71, 21),
('Firas Al-Buraikan', 'Delantero',  9, 5000000, 24, 75, 1.80, 21),
('Sami Al-Najei',     'Defensa',    5, 1000000, 33, 80, 1.87, 21),

-- Irán (id_equipo 22)
('Alireza Beiranvand', 'Portero',   1, 2000000, 32, 88, 1.96, 22),
('Mehdi Taremi',      'Delantero',  9, 18000000, 32, 83, 1.87, 22),
('Sardar Azmoun',     'Delantero',  7, 10000000, 29, 84, 1.90, 22),
('Ali Karimi',        'Mediocampista', 14, 3000000, 20, 69, 1.77, 22),

-- Australia (id_equipo 23)
('Mat Ryan',          'Portero',    1, 3000000, 32, 78, 1.84, 23),
('Martin Boyle',      'Extremo',    20, 4000000, 31, 70, 1.71, 23),
('Mathew Leckie',     'Extremo',    7, 3000000, 33, 73, 1.80, 23),
('Mitchell Duke',     'Delantero',  9, 2000000, 33, 80, 1.83, 23),

-- Nueva Zelanda (id_equipo 24)
('Max Crocombe',      'Portero',    1, 500000, 31, 84, 1.88, 24),
('Chris Wood',        'Delantero',  9, 5000000, 32, 87, 1.90, 24),
('Clayton Lewis',     'Mediocampista', 14, 2000000, 26, 73, 1.77, 24),
('Joe Bell',          'Mediocampista', 6, 1000000, 24, 75, 1.82, 24);

-- ============================================================
-- PARTIDOS (fase de grupos — un partido por par de equipos)
-- Estadios: 1-3 México | 4-7 USA | 8-9 Canadá
-- ============================================================
INSERT INTO partido (fecha, id_estadio, id_equipo_local, id_equipo_visitante) VALUES
-- Grupo A  (México, USA, Canadá, Uruguay)
('2026-06-11', 1, 1, 2),   -- México vs USA       (Azteca)
('2026-06-12', 8, 3, 4),   -- Canadá vs Uruguay   (BMO Field)
('2026-06-15', 4, 1, 3),   -- México vs Canadá    (MetLife)
('2026-06-15', 5, 2, 4),   -- USA vs Uruguay      (SoFi)
('2026-06-19', 6, 1, 4),   -- México vs Uruguay   (AT&T)
('2026-06-19', 7, 2, 3),   -- USA vs Canadá       (Hard Rock)

-- Grupo B  (Argentina, Brasil, Colombia, Ecuador)
('2026-06-13', 4, 5, 6),   -- Argentina vs Brasil (MetLife)
('2026-06-13', 1, 7, 8),   -- Colombia vs Ecuador (Azteca)
('2026-06-17', 5, 5, 7),   -- Argentina vs Colombia (SoFi)
('2026-06-17', 6, 6, 8),   -- Brasil vs Ecuador   (AT&T)
('2026-06-21', 7, 5, 8),   -- Argentina vs Ecuador (Hard Rock)
('2026-06-21', 8, 6, 7),   -- Brasil vs Colombia  (BMO)

-- Grupo C  (España, Francia, Alemania, Portugal)
('2026-06-14', 4, 9, 10),  -- España vs Francia   (MetLife)
('2026-06-14', 9, 11, 12), -- Alemania vs Portugal (BC Place)
('2026-06-18', 5, 9, 11),  -- España vs Alemania  (SoFi)
('2026-06-18', 6, 10, 12), -- Francia vs Portugal (AT&T)
('2026-06-22', 1, 9, 12),  -- España vs Portugal  (Azteca)
('2026-06-22', 3, 10, 11), -- Francia vs Alemania (BBVA)

-- Grupo D  (Inglaterra, Italia, Holanda, Marruecos)
('2026-06-15', 4, 13, 14), -- Inglaterra vs Italia (MetLife)
('2026-06-15', 9, 15, 16), -- Holanda vs Marruecos (BC Place)
('2026-06-19', 2, 13, 15), -- Inglaterra vs Holanda (Akron)
('2026-06-19', 3, 14, 16), -- Italia vs Marruecos  (BBVA)
('2026-06-23', 1, 13, 16), -- Inglaterra vs Marruecos (Azteca)
('2026-06-23', 8, 14, 15), -- Italia vs Holanda   (BMO)

-- Grupo E  (Senegal, Nigeria, Japón, Corea del Sur)
('2026-06-16', 6, 17, 18), -- Senegal vs Nigeria  (AT&T)
('2026-06-16', 9, 19, 20), -- Japón vs Corea Sur  (BC Place)
('2026-06-20', 7, 17, 19), -- Senegal vs Japón    (Hard Rock)
('2026-06-20', 8, 18, 20), -- Nigeria vs Corea Sur (BMO)
('2026-06-24', 4, 17, 20), -- Senegal vs Corea Sur (MetLife)
('2026-06-24', 5, 18, 19), -- Nigeria vs Japón    (SoFi)

-- Grupo F  (Arabia Saudita, Irán, Australia, Nueva Zelanda)
('2026-06-16', 1, 21, 22), -- Arabia vs Irán      (Azteca)
('2026-06-16', 2, 23, 24), -- Australia vs N.Zelanda (Akron)
('2026-06-20', 3, 21, 23), -- Arabia vs Australia (BBVA)
('2026-06-20', 6, 22, 24), -- Irán vs N.Zelanda   (AT&T)
('2026-06-24', 7, 21, 24), -- Arabia vs N.Zelanda (Hard Rock)
('2026-06-24', 9, 22, 23); -- Irán vs Australia   (BC Place)

-- ============================================================
-- USUARIO ADMIN por defecto
-- ============================================================
INSERT INTO usuario (nombreUsuario, contrasena, rol) VALUES
('admin', 'admin123', 'ADMIN');