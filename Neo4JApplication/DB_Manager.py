#from flask import Flask, g, Response, request
#from neo4j.v1 import GraphDatabase, basic_auth

import flask
import neo4j.v1

app = flask.Flask(__name__, static_url_path='/static/')

_driver = neo4j.v1.GraphDatabase.driver('bolt://localhost:7687', auth=neo4j.v1.basic_auth("neo4j", "neo4j"))
app.app_context().push()
#app.run(port=8080)

def get_db():
    if not hasattr(flask.g, 'neo4j_db'):
        flask.g.neo4j_db = _driver.session()
    return flask.g.neo4j_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(flask.g, 'neo4j_db'):
        flask.g.neo4j_db.close()

@app.route("/")
def get_index():
    return app.send_static_file('html/index.html')

def query(f):
    db = get_db()
    with app.app_context():
        f(db)

