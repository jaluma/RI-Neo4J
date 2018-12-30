import serializer
import flask
import json

def get_concursante_con_mayor_edad(db):
    results = db.run("MATCH (c:Concursante) "
                     "RETURN MAX(c.edad) AS Edad "
                     "LIMIT 100")


    return flask.Response(json.dumps([record['Edad'] for record in results]), mimetype="application/json")