from flask import Flask
from flask_smorest import Api
from resurse.produse import blp as BlueprintProdus
from resurse.magazin import blp as BlueprintMagazin
app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stocheaza REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/"

api = Api(app)
api.register_blueprint(BlueprintProdus)
api.register_blueprint(BlueprintMagazin)

