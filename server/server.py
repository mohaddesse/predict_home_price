from flask import Flask,jsonify,render_template,request
import util
app=Flask(__name__)

@app.route("/get_locations_name")
def get_locations_name():
    response=jsonify(
        
        locations=util.get_locations_name()
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/predict",methods=["POST","GET"])
def predict_price_home():
    if request.method=="POST":
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        room = int(request.form['room'])
        bath = int(request.form['bath'])

        response = jsonify({
            'estimated_price': util.predict_price(location,total_sqft,bath,room)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        return render_template("index.html")

    

@app.route("/home/")
def home():
    return render_template("index.html")

if __name__=="__main__":
    util.load_saved_artifacts()
    app.run(debug=True)