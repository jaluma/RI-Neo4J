from util import install_and_import

#configuracion de la conexion
url = 'bolt://localhost:7687'
username = "neo4j"
password = "neo4j"

class db_manager():

    def __init__(self):
        self.install_dependencies()
        import flask
        import neo4j.v1

        self._app = flask.Flask(__name__, static_url_path='/static/')

        self._driver = neo4j.v1.GraphDatabase.driver(url, auth=neo4j.v1.basic_auth(username, password))
        self._app.app_context().push()

    def get_db(self):
        import flask
        import neo4j.v1

        if not hasattr(flask.g, 'neo4j_db'):
            flask.g.neo4j_db = self._driver.session()
        return flask.g.neo4j_db

    def close_db(self,error):
        self.import_libraries()

        if hasattr(flask.g, 'neo4j_db'):
            flask.g.neo4j_db.close()

    def query(self,f):
        import flask
        import neo4j.v1

        db = self.get_db()
        with self._app.app_context():
            r = f(db)

        return r

    def install_dependencies(self):
        install_and_import("flask")

        install_and_import("neo4j-driver", "neo4j.v1")
