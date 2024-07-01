#!/usr/bin/env python3

from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, User, Review, Game

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json_encoder.compact = False  # Corrected the attribute name

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return "Index for Game/Review/User API"

@app.route('/games')
def games():
    games = Game.query.all()
    games_list = [game.to_dict() for game in games]
    return jsonify(games_list), 200

@app.route('/games/<int:id>')
def game_by_id(id):
    game = Game.query.get(id)
    if not game:
        return jsonify({'error': 'Game not found'}), 404
    return jsonify(game.to_dict()), 200

@app.route('/reviews')
def reviews():
    reviews = Review.query.all()
    reviews_list = [review.to_dict() for review in reviews]
    return jsonify(reviews_list), 200

@app.route('/users')
def users():
    users = User.query.all()
    users_list = [user.to_dict() for user in users]
    return jsonify(users_list), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)
