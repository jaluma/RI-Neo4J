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