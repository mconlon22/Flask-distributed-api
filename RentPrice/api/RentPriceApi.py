from sqlalchemy import and_
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify,  request
import flask
from geopy.geocoders import Nominatim


app = flask.Flask("HousePriceAPI")
app.config["DEBUG"] = True
app = flask.Flask("HousePriceAPI")
ma = Marshmallow(app)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:password@database1:5432/postgres'
db = SQLAlchemy(app)

class rent_row(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Float)
    bedrooms = db.Column(db.String(50), nullable=False)
    property_type = db.Column(db.String(50))
    suburb = db.Column(db.String(50))
    county = db.Column(db.String(50))
    value = db.Column(db.Float)
    foundcounty = db.Column(db.String(50))

def find_county(address):
    print(address)
    counties={' antrim',' armagh',' carlow',' cavan',' clare',' cork',' derry',' donegal',' dublin',' fermanagh', ' galway',' kerry',' kildare',' kilkenny',' laois',' leitrim',' limerick',' longford',' louth',' mayo',' meath',' monaghan',' offaly',' roscommon',' sligo',' tipperary',' tyrone',' waterford',' westmeath',' wexford',' wicklow',' down'}
    for county in counties:
            if county in address.lower():
                return county.strip()

class RentSchema(ma.Schema):
    class Meta:
        model = rent_row
        fields = ("year", "bedrooms", "type", "suburb",
                  "county", "value", "foundcounty")


@app.route('/getRentPrices', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lat = request.form.get('lat')
        lon = request.form.get('lon')
        numBeds = request.form.get('numBeds')
        propertyType = request.form.get('propertyType')

        rent_schema=RentSchema(many=True)
        print(lat, lon, numBeds, propertyType)

        geolocator = Nominatim(user_agent="martin")
        location = geolocator.reverse(lat+","+lon)

        nums = ("", 'One bed', 'Two bed', 'Three bed', 'Four plus bed')
        searchingFor = ('town', 'suburb', 'municipality', 'county')
        print(str(location))
        county = find_county(str(location))
        for type in searchingFor:
            print('type')
            print(type)
            try:
                search = location.raw['address'][type]
                print('search')

                print(search,nums[int(numBeds)],propertyType,county)

                searchResult = rent_row.query.filter(and_(rent_row.suburb.ilike("%"+search+"%"), rent_row.bedrooms == 'One bed', rent_row.property_type == propertyType,rent_row.foundcounty==(county) )).all()
                print('searchResult')
                output=rent_schema.dump(searchResult)

                print(output)
                return jsonify(output)
            except Exception as e:
                print(e )
                continue
            print(searchResult)
            if searchResult.empty != True:
                break
        return {}



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)


