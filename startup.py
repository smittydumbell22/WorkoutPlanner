import sqlite3

def create_cnn(file_name):
    # create database file by specifying location
    cnn = sqlite3.connect(file_name)

    return cnn

def create_tables(cnn):
    # initialize cursor object to interact with database
    cur = cnn.cursor()

    # create all necessary tables
    cur.execute("""CREATE TABLE if not exists workout
                (workout_id INTEGER PRIMARY KEY NOT NULL, 
                workout_name TEXT, 
                weight_type_id INTEGER,
                muscle_group_id INTEGER)""")

            

    cur.execute("""CREATE TABLE if not exists muscle_group
                (muscle_group_id INTEGER PRIMARY KEY NOT NULL,
                muscle_group TEXT)""")

    cur.execute("""CREATE TABLE if not exists weight_type
                (weight_type_id INTEGER PRIMARY KEY NOT NULL,
                weight_type TEXT)""")
    
    

    cnn.commit()

def insert_known_table_values(cnn):
    cur = cnn.cursor()

    cur.execute("""INSERT INTO muscle_group (muscle_group) VALUES ("legs"), ("back"), ("upper body"), ("core"), ("whole body")""")
    cur.execute("""INSERT INTO weight_type (weight_type) VALUES ("barbell"), ("dumbell"), ("bench press"), ("leg extension")""")

    cnn.commit()