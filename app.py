from flask import Flask, request, Response
import mariadb
import json
import random
import functions

app = Flask(__name__)

@app.route("/animals", methods=["GET", "POST", "PATCH", "DELETE"])
def animalpage():
    if request.method == 'GET':
        animals = functions.get_animal()
        animal_number = random.randrange(len(animals))
        return Response(json.dumps(animals[animal_number][0], default=str), mimetype="application/json", status=200)
    elif request.method == 'POST':
        animalAdd = request.json.get('name')
        if functions.add_animal(animalAdd):
            return Response(animalAdd + " has been successfully added to the list!", mimetype="text/html", status=201)
        else: 
            return Response("Sorry, add animal failed!", mimetype="text/html", status=201)
    elif request.method == 'PATCH':
        oldAnimal = request.json.get('change')
        newAnimal = request.json.get('name')
        if functions.edit_animal(oldAnimal, newAnimal):
            return Response(oldAnimal + " has been changed to " + newAnimal + "!", mimetype="text/html", status=201)
        else:
            return Response("Sorry, change animal failed!", mimetype="text/html", status=201)
    elif request.method == 'DELETE':
        animalDelete = request.json.get('name')
        if functions.delete_animal(animalDelete):
            return Response(animalDelete + " has been deleted!", mimetype="text/html", status=201)
        else:
            return Response("Sorry, delete animal failed!", mimetype="text/html", status=201)
        

