import configparser
import psycopg2


class DataBase:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("../settings1.ini")
        host = config["settings"]["host"]
        user = config["settings"]["user"]
        password = config["settings"]["password"]
        db_name = config["settings"]["db_name"]
        try:
            self.connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name,
            )
        except:
            print('err')
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def create_servers(self):
        with self.connection:
            self.cursor.execute("CREATE TABLE servers("
                                "id serial PRIMARY KEY,"
                                "name varchar(50) NOT NULL,"
                                "mode varchar(50) NOT NULL,"
                                "time varchar(50) NOT NULL,"
                                "level varchar(50) NOT NULL);")

    def create_invites(self):
        with self.connection:
            self.cursor.execute("CREATE TABLE invites("
                                "id serial PRIMARY KEY,"
                                "fruction varchar(50),"
                                "discord varchar(150),"
                                "fk_invite_server int REFERENCES servers(id));")

    def create_famq(self):
        with self.connection:
            self.cursor.execute("CREATE TABLE families("
                                "id serial PRIMARY KEY,"
                                "name varchar(50) NOT NULL,"
                                "hook varchar(150) NOT NULL);")

    def create_days(self):
        with self.connection:
            self.cursor.execute("CREATE TABLE days(id serial PRIMARY KEY,day varchar(50), day_num integer);")

    def create_server_days(self):
        with self.connection:
            self.cursor.execute("CREATE TABLE server_days("
                                "	server_id int REFERENCES servers(id),"
                                "	day_id int REFERENCES days(id),"
                                "	CONSTRAINT day_server PRIMARY KEY (server_id, day_id))")

    def add_days(self):
        with self.connection:
            self.cursor.execute("INSERT INTO days(day, day_num) VALUES ('??????????????????????', 1);"
                                "INSERT INTO days(day, day_num) VALUES ('??????????????', 2);"
                                "INSERT INTO days(day, day_num) VALUES ('??????????', 3);"
                                "INSERT INTO days(day, day_num) VALUES ('??????????????', 4);"
                                "INSERT INTO days(day, day_num) VALUES ('??????????????', 5);"
                                "INSERT INTO days(day, day_num) VALUES ('??????????????', 6);"
                                "INSERT INTO days(day, day_num) VALUES ('??????????????????????', 7);")

    def add_server(self):
        with self.connection:
            self.cursor.execute(
                "INSERT INTO servers(name, mode, time, level) VALUES ('???? Rockford', 'capture', '15:00-23:00', 2);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('???? Rockford', 'bizwar', '15:00-23:00', 2);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('???? VineWood', 'capture', '15:00-23:00', 5);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('???? VineWood', 'bizwar', '15:00-23:00', 5);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('???? LaMesa', 'capture', '15:00-23:00', 4);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('???? LaMesa', 'bizwar', '15:00-23:00', 4);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('???? Eclipse', 'capture', '15:00-23:00', 2);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('???? Eclipse', 'bizwar', '15:00-23:00', 2);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('???? Alta', 'capture', '15:00-23:00', 5);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('???? Alta', 'bizwar', '15:00-23:00', 5);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('???? BlackBerry', 'capture', '15:00-23:00', 2);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('???? BlackBerry', 'bizwar', '15:00-23:00', 2);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('???? Burton', 'capture', '15:00-23:00', 5);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('???? Burton', 'bizwar', '14:00-23:00', 5);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('???? Richman', 'bizwar', '14:00-23:00', 2);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('???? Richman', 'capture', '13:00-23:00', 2);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('???? Sunrise', 'capture', '13:00-23:00', 5);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('???? Sunrise', 'bizwar', '13:00-23:00', 5);"
            )

    def add_new_server(self, name, mode, time, level):
        with self.connection:
            self.cursor.execute("INSERT INTO servers(name, mode, time, level) VALUES (%s, %s, %s, %s);",
                                (name, mode, time, level,))

    def add_server_days(self):
        with self.connection:
            self.cursor.execute(
                "INSERT INTO server_days VALUES (1, 1), (1, 3), (1, 5), (1, 7);"  # rockford cpt
                "INSERT INTO server_days VALUES (2, 1), (2, 2), (2, 4), (2, 6);"  # rockford biz
                "INSERT INTO server_days VALUES (3, 1), (3, 3), (3, 5), (3, 7);"  # vv cpt
                "INSERT INTO server_days VALUES (4, 2), (4, 4), (4, 5), (4, 7);"  # vv biz
                "INSERT INTO server_days VALUES (5, 1), (5, 3), (5, 5), (5, 7);"  # lamesa cpt
                "INSERT INTO server_days VALUES (6, 1), (6, 2), (6, 4), (6, 6);"  # lamesa biz
                "INSERT INTO server_days VALUES (7, 1), (7, 3), (7, 5), (7, 7);"  # eclipse cpt
                "INSERT INTO server_days VALUES (8, 1), (8, 2), (8, 4), (8, 6);"  # eclipse biz
                "INSERT INTO server_days VALUES (9, 1), (9, 3), (9, 5), (9, 7);"  # alta cpt
                "INSERT INTO server_days VALUES (10, 2), (10, 4), (10, 6), (10, 7);"  # alta biz
                "INSERT INTO server_days VALUES (11, 2), (11, 4), (11, 6), (11, 7);"  # bb cpt
                "INSERT INTO server_days VALUES (12, 2), (12, 3), (12, 5), (12, 6);"  # bb biz
                "INSERT INTO server_days VALUES (17, 1), (17, 3), (17, 5), (17, 7)"  # sr cpt
                "INSERT INTO server_days VALUES (18, 2), (18, 4), (18, 6), (18, 7)"  # sr biz
            )  # bb biz

    def add_family(self, famq, hook):
        with self.connection:
            self.cursor.execute(
                "INSERT INTO families(name, hook) VALUES (%s, %s);", (famq, hook))

    def add_invite(self, fruction, discord, mode, server, family):

        with self.connection:
            self.cursor.execute(
                f"SELECT id FROM servers WHERE mode = '{mode}' AND LOWER(name) Like LOWER('%{server}');")
            server_id = self.cursor.fetchone()[0]
            self.cursor.execute(f"SELECT id FROM families WHERE name = '{family}'")
            family_id = self.cursor.fetchone()[0]
            self.cursor.execute(
                "INSERT INTO invites(fruction, discord, server_id, family) VALUES (%s, %s, %s, %s);",
                (fruction, discord, server_id, family_id))

    def get_today_invites(self, family):
        with self.connection:
            self.cursor.execute(f"SELECT id FROM families WHERE name = '{family}'")
            family_id = self.cursor.fetchone()[0]
            self.cursor.execute(
                "SELECT fruction, discord, s.name, s.time, s.level FROM invites "
                f"LEFT JOIN servers s ON s.id=invites.server_id AND invites.family={family_id} WHERE s.id IN (SELECT server_id FROM server_days WHERE day_id=EXTRACT(dow FROM now()));")
            return self.cursor.fetchall()

    def get_famq_invites(self, family):
        with self.connection:
            self.cursor.execute(f"SELECT id FROM families WHERE name = '{family}'")
            family_id = self.cursor.fetchone()[0]
            self.cursor.execute(
                f"SELECT fruction, (select name from servers where id=i.server_id ) FROM invites i where family = {family_id}"
                )
            return self.cursor.fetchall()
    def get_all(self):
        with self.connection:
            self.cursor.execute("SELECT id, name, hook FROM families")
        return self.cursor.fetchall()
