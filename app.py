from flask import json
from flask import Flask
import logging

app = Flask(__name__)



@app.route('/status')
def healthcheck():
    response = app.response_class(
        response=json.dumps({"result":"OK-healthy"}),
        status=200,
        mimetype='application/json'
    )

    app.logger.info('Status request Successfull')
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
        response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Metrics Request Succesfull')
    return response

@app.route("/")
def hello():
    app.logger.info('Main request Succesfull')
    return "Hello World! First jenkins Pipeline !!!! hurrayyy"

if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')