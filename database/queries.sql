-- CONSULTA 1
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


-- CONSULTA 2
SELECT
p.fecha,
es.nombre,
el.nombre,
ev.nombre
FROM partido p
INNER JOIN estadio es
ON p.id_estadio = es.id_estadio
INNER JOIN equipo el
ON p.id_equipo_local = el.id_equipo
INNER JOIN equipo ev
ON p.id_equipo_visitante = ev.id_equipo
WHERE es.nombre = 'Maracaná';


-- CONSULTA 3
SELECT
pa.nombre,
e.nombre,
SUM(j.valor) AS valor_total
FROM jugador j
INNER JOIN equipo e
ON j.id_equipo = e.id_equipo
INNER JOIN pais pa
ON e.id_pais = pa.id_pais
GROUP BY e.nombre
ORDER BY valor_total DESC;


-- CONSULTA 4
SELECT
e.nombre,
COUNT(j.id_jugador) AS menores_21
FROM jugador j
INNER JOIN equipo e
ON j.id_equipo = e.id_equipo
WHERE j.edad < 21
GROUP BY e.nombre;