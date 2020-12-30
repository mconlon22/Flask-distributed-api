import flask
from flask import jsonify,  request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import and_


app = flask.Flask("HousePriceAPI")
ma = Marshmallow(app)

app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://test:password@10.109.208.141:5445/postgres'
db = SQLAlchemy(app)



class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    address = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)


class HouseSchema(ma.Schema):
    class Meta:
        model = House
        fields = ("price", "address", "lat", "lon")


@app.route('/getHousePrices', methods=['POST'])
def index():
    if request.method == 'POST':
        lat = float(request.form.get('lat'))
        lon = float(request.form.get('lon'))
        print(lat, lon)
        house_schema = HouseSchema(many=True)
        housePrices = House.query.filter(and_(House.lat.between(lat-.005, lat+.005), House.lon.between(lon-.005, lon+.005))).limit(200).all()

        output = house_schema.dump(housePrices)
        print(output)
        return jsonify(output)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=82,debug=True)
