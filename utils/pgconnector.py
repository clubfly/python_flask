import os
import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
class PgConnector:
    engine = {}
    Session = {}
    def __init__(self, service):
        if service not in PgConnector.engine:
            path = os.getcwd()
            with open(os.path.join(path, "conf", "default.conf")) as default_config_file:
                config = json.load(default_config_file)
            env = config["env"]
            with open(os.path.join(path, "conf", config["project_name"], config[env]["pgsql_setting"])) as pgsql_config_file:
                pgsql_config = json.load(pgsql_config_file)
            pgsql_uri = self.__compose_uri(pgsql_config[env][service])
            engine = create_engine(pgsql_uri,client_encoding='utf8')
            PgConnector.engine[service] = engine
            PgConnector.Session[service] = sessionmaker(bind=engine)

        connection = PgConnector.engine[service].connect()
        self.session = PgConnector.Session[service](bind=connection)

    def get_session(self):
        return self.session

    def query(self, *entities, **kwargs):
        return self.session.query(*entities, **kwargs)

    def execute_raw_sql(self, sql_statment):
        return self.session.execute(sql_statment)

    def __compose_uri(self, config):
        host = config["PGSQL_HOST"]
        port = config["PGSQL_PORT"]
        if port:
            host = "{}:{}".format(host, port)
        
        user = config["PGSQL_USER"]
        password = config["PGSQL_PASSWORD"]
        if password:
            user = "{}:{}".format(user, password)
        
        return "postgresql+psycopg2://{}@{}/{}".format(user, host, config["PGSQL_DB"])
