import flask
import pandas as pd
import sql
from flask import current_app, flash, jsonify, make_response, redirect, request, url_for
from flask import Response

import json

app =flask.Flask("HousePriceAPI")
app.config["DEBUG"] = True

instance=sql
@app.route('/getHousePrices', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        x=request.form.get('x')
        y=request.form.get('y')


        result=instance.find_sold_houses(float(x),float(y)).to_json(orient="split")
        parsed = json.loads(result)
        return Response(json.dumps(parsed, indent=4) ,  mimetype='application/json')
app.run()

        


        
