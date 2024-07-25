"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Favorites, People, Planets, Starships, People_Starships_Rel
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

#----- USER ROUTES -----

@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users = [user.serialize() for user in users]

    return jsonify({'msg': 'ok',
                    'users': users}), 200


@api.route('/users/<int:id>', methods=['GET'])
def get_single_user(id):
    user = User.query.get(id)
    user = user.serialize()

    return jsonify({'msg': 'ok',
                    'user': user}), 200


@api.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(
        email = data['email'],
        password = data['password'],
        first_name = data['first_name'],
        last_name = data['last_name']
    )
    user_exist = User.query.filter_by(email = new_user.email).first()
    if user_exist:
        return jsonify({'msg': 'User already exists'})
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'msg': 'ok'}), 200


@api.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'msg': 'User not found'}), 404
    
    db.session.delete(user)
    db.session.commit()

    return jsonify({'msg': 'ok'}), 200


@api.route('/users', methods=['DELETE'])
def delete_all_users():
    users = User.query.all()
    if not users:
        return jsonify({'msg': 'No users found'}), 404
    
    users = list(map(lambda user: db.session.delete(user), users))
    db.session.commit()

    return jsonify({'msg': 'Users deleted'}), 200
    
#----- PEOPLE ROUTES -----------------------------------

@api.route('/people', methods=['GET'])
def get_people():
    people = People.query.all()
    if not people:
        return jsonify({'msg': 'No people found'}), 404
    
    people = [person.serialize() for person in people]
    
    return jsonify({'msg': 'ok',
                    'people': people}), 200


@api.route('/people/<int:id>', methods=['GET'])
def get_single_person(id):
    person = People.query.get(id)
    if not person:
        return jsonify({'msg': 'No person found'}), 404
    
    person = person.serialize()
    
    return jsonify({'msg': 'ok',
                    'people': person}), 200


@api.route('/people', methods=['POST'])
def create_person():
    data = request.json
    new_people = People(
        name = data['name'],
        birth_year = data['birth_year'],
        species	= data['species'],
        height = data['height'],
        mass = data['mass'],
        gender = data.get('gender'),
        hair_color = data.get('hair_color'),
        skin_color = data.get('skin_color'),
        planet_id=data['planet_id']
    )
    people_exist = People.query.filter_by(name = new_people.name).first()
    if people_exist:
        return jsonify({'msg': 'Person already exists'}), 400
    
    db.session.add(new_people)
    db.session.commit()

    return jsonify({'msg': 'ok'}), 200


@api.route('/people/<int:id>', methods=['DELETE'])
def delete_person(id):
    person = People.query.get(id)
    if not person:
        return jsonify({'msg': 'Person not found'}), 404
    
    db.session.delete(person)
    db.session.commit()

    return jsonify({'msg': 'ok'}), 200


@api.route('/people', methods=['DELETE'])
def delete_all_people():
    people = People.query.all()
    if not people:
        return jsonify({'msg': 'No people found'}), 404
    
    people = list(map(lambda person: db.session.delete(person), people))
    db.session.commit()

    return jsonify({'msg': 'ok'}), 200

#----- PLANETS ROUTES -------------------------------------------

@api.route('/planets', methods=['GET'])
def get_planets():
    planets = Planets.query.all()
    if not planets:
        return jsonify({'msg': 'No planets found'}), 404
    
    planets = [planet.serialize() for planet in planets]
    
    return jsonify({'msg': 'ok',
                    'planets': planets}), 200


@api.route('/planets/<int:id>', methods=['GET'])
def get_single_planet(id):
    planet = Planets.query.get(id)
    if not planet:
        return jsonify({'msg': 'Not found'}), 404
    
    planet = planet.serialize()
    
    return jsonify({'msg': 'ok',
                    'planet': planet}), 200


@api.route('/planets', methods=['POST'])
def create_planet():
    data = request.json
    new_planet = Planets(
        name = data['name'],
        diameter = data['diameter'],
        climate	= data['climate'],
        terrain = data['terrain'],
        population = data['population']
    )
    planet_exist = Planets.query.filter_by(name = new_planet.name).first()
    if planet_exist:
        return jsonify({'msg': 'Planet already exists'}), 400
    
    db.session.add(new_planet)
    db.session.commit()

    return jsonify({'msg': 'ok'}), 200


@api.route('/planets/<int:id>', methods=['DELETE'])
def delete_planet(id):
    planet = Planets.query.get(id)
    if not planet:
        return jsonify({'msg': 'Planet not found'}), 404
    
    db.session.delete(planet)
    db.session.commit()

    return jsonify({'msg': 'ok'}), 200


@api.route('/planets', methods=['DELETE'])
def delete_all_planets():
    planets = Planets.query.all()
    if not planets:
        return jsonify({'msg': 'No planets found'}), 404
    
    planets = list(map(lambda planet: db.session.delete(planet), planets))
    db.session.commit()

    return jsonify({'msg': 'ok'}), 200

#----- STARSHIPS ROUTES ----------------------------------------------

@api.route('/starships', methods=['GET'])
def get_starships():
    starships = Starships.query.all()
    if not starships:
        return jsonify({'msg': 'No starships found'}), 404
    
    starships = [starship.serialize() for starship in starships]
    
    return jsonify({'msg': 'ok',
                    'starships': starships}), 200


@api.route('/starships/<int:id>', methods=['GET'])
def get_single_starship(id):
    starship = Starships.query.get(id)
    if not starship:
        return jsonify({'msg': 'Not found'}), 404
    
    starship = starship.serialize()
    
    return jsonify({'msg': 'ok',
                    'starship': starship}), 200


@api.route('/starships', methods=['POST'])
def create_starship():
    data = request.json
    new_starship = Starships(
        name = data['name'],
        model = data['model'],
        manufacturer = data['manufacturer'],
        passengers = data['passengers'],
    )
    starship_exist = Starships.query.filter_by(name = new_starship.name).first()
    if starship_exist:
        return jsonify({'msg': 'Starship already exists'}), 400
    
    db.session.add(new_starship)
    db.session.commit()

    return jsonify({'msg': 'ok'}), 200


@api.route('/starships/<int:id>', methods=['DELETE'])
def delete_starship(id):
    starship = Starships.query.get(id)
    if not starship:
        return jsonify({'msg': 'Starship not found'}), 404
    
    db.session.delete(starship)
    db.session.commit()

    return jsonify({'msg': 'ok'}), 200


@api.route('/starships', methods=['DELETE'])
def delete_all_starships():
    starships = Starships.query.all()
    if not starships:
        return jsonify({'msg': 'No starships found'}), 404
    
    starships = list(map(lambda starship: db.session.delete(starship), starships))
    db.session.commit()

    return jsonify({'msg': 'ok'}), 200

#--------------------------------

@api.route('/people_starships_rel', methods=['POST'])
def people_starships_rel():
    data = request.json
    new_rel = People_Starships_Rel(
        people_id = data['people_id'],
        starship_id = data['starship_id']
        )

    db.session.add(new_rel)
    db.session.commit()

    return jsonify({'msg': 'ok'}), 200

@api.route('/people_starships_rel', methods=['GET'])
def get_people_starships_rel():
    relations = People_Starships_Rel.query.all()
    relations = [rel.serialize() for rel in relations]

    return jsonify({'msg': 'ok',
                    'relations': relations}), 200