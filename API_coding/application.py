from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)

            
    def to_dict(self):
        return{'id':self.id,
            'name':self.name,
            'email':self.email,
            'country':self.country 
            }
    
    
# get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return [user.to_dict() for user in users]


# get user by id
@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = User.query.get_or_404(id) 
    return jsonify(user.to_dict())


# add user 
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'], country=data['country'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201


# update user by id
@app.route('/users/<int:id>', methods=["PUT"])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.name = data.get('name', user.name)
    user.email  = data.get('email', user.email)
    user.country = data.get('country', user.country)
    db.session.commit()
    return jsonify(user.to_dict())

# delete user by id
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'messager':'User deleted successfully'})


if __name__=='__main__':
    app.run(debug=True)
       