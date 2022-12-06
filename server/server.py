from flask import Flask,jsonify,render_template,request
import util
app=Flask(__name__)

@app.route("/get_locations_name")
def get_locations_name():
    response=jsonify(
        
        locations=util.get_locations_name()
    )
    response.header.add("'Access-Control-Allow-Origin', '*'")

if __name__=="__main__":
    app.run(debug=True)