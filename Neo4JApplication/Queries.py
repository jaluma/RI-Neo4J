import serializer

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