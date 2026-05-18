

SELECT 
c.nombre AS confederacion,
j.nombre AS jugador,
MAX(j.valor) AS valor
FROM jugador j
INNER JOIN equipo e
ON j.id_equipo = e.id_equipo
INNER JOIN confederacion c
ON e.id_confederacion = c.id_confederacion
GROUP BY c.nombre;

SELECT
e.nombre,
COUNT(p.id_partido) AS partidos
FROM partido p
INNER JOIN estadio e
ON p.id_estadio = e.id_estadio
GROUP BY e.nombre;

SELECT
j.nombre,
j.edad,
e.nombre
FROM jugador j
INNER JOIN equipo e
ON j.id_equipo = e.id_equipo
WHERE j.edad < 21;