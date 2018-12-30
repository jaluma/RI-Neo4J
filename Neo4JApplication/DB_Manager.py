#from flask import Flask, g, Response, request
#from neo4j.v1 import GraphDatabase, basic_auth

#import flask
#import neo4j.v1

import os

class DB_Manager:

    def __init(self):
        self.app = flask.Flask(__name__, static_url_path='/static/')

        password = os.getenv("NEO4J_PASSWORD")
        self._driver = neo4j.v1.GraphDatabase.driver('bolt://localhost',auth=basic_auth("neo4j", password))

        self.app.run(port=8080)

    def get_db(self):
        if not hasattr(flask.g, 'neo4j_db'):
            flask.g.neo4j_db = self._driver.session()
        return flask.g.neo4j_db

    #@self.app.teardown_appcontext
    def close_db(self,error):
        if hasattr(flask.g, 'neo4j_db'):
            flask.g.neo4j_db.close()

    #@self.app.route("/")
    def get_index(self):
        return self.app.send_static_file('index.html')


