import dbcreds
import mariadb

def get_animal():
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM animals")
        animals = cursor.fetchall()
        return animals

    except mariadb.ProgrammingError:
        print("You need lessons.")
    except mariadb.OperationalError:
        print("There seems to be something wrong with the connection.")
    finally:
        if(cursor != None):
            cursor.close()
        if(conn != None):
            conn.rollback()
            conn.close()

def add_animal(animalAdd):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO animals(name) VALUES (?)", [animalAdd])
        conn.commit()
        if(cursor.rowcount == 1):
            return True
        else:
            return False

    except mariadb.ProgrammingError:
        print("You need lessons.")
    except mariadb.OperationalError:
        print("There seems to be something wrong with the connection.")
    finally:
        if(cursor != None):
            cursor.close()
        if(conn != None):
            conn.rollback()
            conn.close()

def edit_animal(oldAnimal, newAnimal):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
        cursor = conn.cursor()
        cursor.execute("UPDATE animals SET name=? WHERE name=?", [newAnimal, oldAnimal])
        conn.commit()
        if(cursor.rowcount == 1):
            return True
        else:
            return False

    except mariadb.ProgrammingError:
        print("You need lessons.")
    except mariadb.OperationalError:
        print("There seems to be something wrong with the connection.")
    finally:
        if(cursor != None):
            cursor.close()
        if(conn != None):
            conn.rollback()
            conn.close()

def delete_animal(animalDelete):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM animals WHERE name =?", [animalDelete])
        conn.commit()
        if(cursor.rowcount == 1):
            return True
        else:
            return False

    except mariadb.ProgrammingError:
        print("You need lessons.")
    except mariadb.OperationalError:
        print("There seems to be something wrong with the connection.")
    finally:
        if(cursor != None):
            cursor.close()
        if(conn != None):
            conn.rollback()
            conn.close()