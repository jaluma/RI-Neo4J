import serializer
from datetime import datetime

def get_concursante_con_mayor_edad(db):
    results = db.run("MATCH (c:Concursante) "
                     "RETURN MAX(c.edad) AS Edad "
                     "LIMIT 100")

    for record in results:
        return int(record["Edad"])

def get_concursantes_alemanes(db):
    results = db.run("MATCH (c:Concursante) "
                     "WHERE c.pais='Alemania' "
                     "RETURN c as Concursante ")

    array = []
    [array.append(serializer.serialize_concursante(record["Concursante"])) for record in results]

    return array

def get_fecha_expulsion_dave(db):
    results = db.run("MATCH(c:Concursante)-[:EXPULSADO]-(g:Gala) "
                     "WHERE c.nombre = 'Dave' AND c.apellido = 'Zulueta' "
                     "RETURN g.fecha AS Fecha")

    for record in results:
        return record["Fecha"]

def get_concursantes_mas_colaboraciones(db):
    results = db.run("MATCH (c:Concursante)-[:CANTA_CON]-(colaboradores) "
                     "WITH c.nombre AS nombre, count(c) AS colaboraciones "
                     "return MAX(colaboraciones) as maximo")

    for record in results:
        maximo = int(record["maximo"])

    results = db.run("MATCH (c:Concursante)-[:CANTA_CON]-(colaboradores) "
                     "WITH c.nombre AS nombre, count(c) AS colaboraciones "
                     "WHERE colaboraciones = " + str(maximo) +
                     " RETURN nombre")

    array = []
    [array.append(record["nombre"]) for record in results]

    return array   

def get_concursante_canta_expulsados(db):
    results = db.run("MATCH (colaborador1:Concursante)-[:EXPULSADO]-(g1:Gala), (colaborador2:Concursante)-[:EXPULSADO]-(g2:Gala), "
                     "(colaborador1)-[:CANTA_CON]-(c:Concursante), "
                     "(colaborador2)-[:CANTA_CON]-(c) "
                     "WHERE g1.numero > 8 AND g2.numero > 8 AND colaborador1 <> colaborador2 "
                     "RETURN DISTINCT c")

    array = []
    [array.append(serializer.serialize_concursante(record["c"])) for record in results]

    return array

def get_concursantes_relacionados_ganador(db):
    results = db.run("MATCH (ganador:Concursante)-[:GANADOR]-(:Gala{nombre:'Gala final'}), "
                     "(expulsado:Concursante)-[:EXPULSADO]-(:Gala{nombre:'Gala final'}), "
                     "(ganador)-[:CANTA_CON*1..2]-(posible:Concursante), "
                     "(expulsado)-[:CANTA_CON]-(imposible:Concursante) "
                     "WHERE posible <> ganador "
                     "WITH collect(distinct posible) as posibles, collect(distinct imposible) as imposibles "
                     "MATCH (res:Concursante) "
                     "WHERE res IN posibles AND  NOT res IN imposibles "
                     "RETURN res ")

    array = []
    [array.append(serializer.serialize_concursante(record["res"])) for record in results]

    return array