import configparser
import psycopg2


class DataBase:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("../settings.ini")
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
            self.cursor.execute("INSERT INTO days(day, day_num) VALUES ('Понедельник', 1);"
                                "INSERT INTO days(day, day_num) VALUES ('Вторник', 2);"
                                "INSERT INTO days(day, day_num) VALUES ('Среда', 3);"
                                "INSERT INTO days(day, day_num) VALUES ('Четверг', 4);"
                                "INSERT INTO days(day, day_num) VALUES ('Пятница', 5);"
                                "INSERT INTO days(day, day_num) VALUES ('Суббота', 6);"
                                "INSERT INTO days(day, day_num) VALUES ('Воскресенье', 7);")

    def add_server(self):
        with self.connection:
            self.cursor.execute(
                "INSERT INTO servers(name, mode, time, level) VALUES ('💎 Rockford', 'capture', '15:00-23:00', 2);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('💎 Rockford', 'bizwar', '15:00-23:00', 2);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('🏰 VineWood', 'capture', '15:00-23:00', 5);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('🏰 VineWood', 'bizwar', '15:00-23:00', 5);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('🌵 LaMesa', 'capture', '15:00-23:00', 4);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('🌵 LaMesa', 'bizwar', '15:00-23:00', 4);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('🌘 Eclipse', 'capture', '15:00-23:00', 2);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('🌘 Eclipse', 'bizwar', '15:00-23:00', 2);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('🍀 Alta', 'capture', '15:00-23:00', 5);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('🍀 Alta', 'bizwar', '15:00-23:00', 5);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('🍇 BlackBerry', 'capture', '15:00-23:00', 2);"
                "INSERT INTO servers(name, mode, time, level) VALUES ('🍇 BlackBerry', 'bizwar', '15:00-23:00', 2);")
    def add_new_server(self, name, mode, time, level):
        with self.connection:
            self.cursor.execute("INSERT INTO servers(name, mode, time, level) VALUES (%s, %s, %s, %s);", (name, mode, time, level,))
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
                "INSERT INTO server_days VALUES (12, 2), (12, 3), (12, 5), (12, 6);")  # bb biz

    def add_invite(self, fruction, discord, server_id):
        with self.connection:
            self.cursor.execute(
                "INSERT INTO invites(fruction, discord, server_id) VALUES (%s, %s, %s);", (fruction, discord, server_id))

    def get_today_invites(self):
        with self.connection:
            self.cursor.execute(
                "SELECT fruction, discord, s.name, s.time, s.level FROM invites "
                "LEFT JOIN servers s ON s.id=invites.server_id WHERE s.id IN (SELECT server_id FROM server_days WHERE day_id=EXTRACT(dow FROM now()));")
            return self.cursor.fetchall()
