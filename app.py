from flask import Flask, request

from components.CentralUnit import CentralUnit

app = Flask(__name__)
foo = CentralUnit


@app.route("/")
def health_check():
    return app.response_class(status=200)


@app.route("/signal", methods=["Post"])
def receive_signal():
    data = request.json

    # TODO Receiver
    response = app.response_class(
        data,
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/sensor", methods=["Post"])
def send_sensor_status():
    data = request.json
    # Todo sensor magic
    response = app.response_class(
        status=200,
        mimetype='application/json'
    )


if __name__ == '__main__':
    app.run()
