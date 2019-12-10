from flask import Flask, request

from components.CentralUnit import CentralUnit

app = Flask(__name__)
central_unit = CentralUnit()


@app.route("/")
def health_check():
    return app.response_class(status=200)


@app.route("/signal", methods=["Post"])
def receive_signal():
    data = request.json
    if central_unit.standby:
        central_unit.ligth_up()
    else:
        central_unit.get_direction(data)
        central_unit.standby = True

    response = app.response_class(
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/sensor", methods=["Post"])
def send_sensor_status():
    central_unit.use_signal()

    response = app.response_class(
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run()
