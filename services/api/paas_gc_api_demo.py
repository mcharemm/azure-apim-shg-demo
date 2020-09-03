import os
from flask import Flask, jsonify, request
from flask_swagger import swagger

app = Flask(__name__)

apiId = os.getenv('API_ID')
apiCloud = os.getenv('API_CLOUD')
apiTitle = os.getenv('API_TITLE')
basePath = "/"+apiId+"/"+apiCloud+"/"
apihelloPath = basePath+"hello"
apispecPath = basePath+"spec"

@app.route(apispecPath)
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = apiTitle
    return jsonify(swag)

@app.route(apihelloPath)
def dummy_api():
    """
        GC PaaS Demo
        ---
        tags:
          - api
        summary: "demo"
        operationId: "demo"
        responses:
            200:
                description: ""
    """
    apiHeaders = request.headers.get("Demo")
    cloudCapital = apiCloud.capitalize()
    apiMessage = "Hola! Soy el API #"+apiId+" y estoy desplegado en "+cloudCapital+" Cloud"
    result = {
        "header": apiHeaders,
        "text": apiMessage
    }

    return result

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')