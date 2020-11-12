from flask import Flask, request, Response
import mariadb
import json
import dbcreds
import random
# import functions

app = Flask(__name__)

@app.route("/animals", methods=["GET", "POST", "PATCH", "DELETE"])
def animalpage():
    if request.method == 'GET':
        conn = None
        cursor = None
        animals = None
        try:
            conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM animals")
            animals = cursor.fetchall()

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
            if(animals != None):
                animal_number = random.randrange(len(animals))
                return Response(json.dumps(animals[animal_number][0], default=str), mimetype="application/json", status=200)
        
    elif request.method == 'POST':
        conn = None
        cursor = None
        animalAdd = request.json.get('name')
        rows = None
        try:
            conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO animals(name) VALUES (?)", [animalAdd])
            conn.commit()
            rows = cursor.rowcount
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
            if(rows == 1):
                return Response(animalAdd + " has been successfully added to the list!", mimetype="text/html", status=201)
            else:
                return Response("Something went wrong!", mimetype="text/html", status=500)
           
    elif request.method == 'PATCH':
        conn = None
        cursor = None
        oldAnimal = request.json.get('change')
        newAnimal = request.json.get('name')
        rows = None
        try:
            conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
            cursor = conn.cursor()
            cursor.execute("UPDATE animals SET name=? WHERE name=?", [newAnimal, oldAnimal])
            conn.commit()
            rows = cursor.rowcount

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
            if(rows == 1):
                return Response(oldAnimal + " has been changed to " + newAnimal + "!", mimetype="text/html", status=201)
            else:
                return Response("Something went wrong!", mimetype="text/html", status=500)

    elif request.method == 'DELETE':
        conn = None
        cursor = None
        animalDelete = request.json.get('name')
        rows = None
        try:
            conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM animals WHERE name =?", [animalDelete])
            conn.commit()
            rows = cursor.rowcount

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
            if(rows == 1):
                return Response(animalDelete + " has been deleted!", mimetype="text/html", status=201)
            else:
                return Response("Something went wrong!", mimetype="text/html", status=500)
    
        

