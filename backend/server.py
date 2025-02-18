from flask import Flask, request, jsonify
from flask_cors import CORS
import services
app=Flask(__name__)

CORS(app)

@app.route('/data')
def get_sensor_data():
    response=jsonify({
        'data':services.get_sensor_data()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/job')
def get_job():
    response=jsonify({
        'data':services.get_job_data()
    })
    response.headers.add('Access-Control-Allow-Origin','*')  
    return response


# @app.route('/cities')
# def get_cities():
#     response=jsonify({
#         'cities':services.get_cities()
#     })
#     response.headers.add('Access-Control-Allow-Origin','*')
#     return response
# @app.route('/predict_home_price',methods=['POST'])
# def predict_home_price():
#     state=request.form['state']
#     city=request.form['city']
#     latitude=float(request.form['latitude'])
#     longitude=float(request.form['longitude'])
#     bedroom=int(request.form['bedroom'])
#     bathroom=int(request.form['bathroom'])
#     area=float(request.form['area'])
#     lotarea=float(request.form['lotarea'])
#     response=jsonify({
#         'estimated_price':services.get_estimated_price(state,city,latitude,longitude,bedroom,bathroom,area,lotarea)
#     })
#     response.headers.add('Access-Control-Allow-Origin','*')
#     return response


if __name__ == '__main__':
    print("Starting Python Flask Server...")
    app.run()
