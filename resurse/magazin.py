import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import lant_de_magazine

blp = Blueprint("lant_de_magazine", __name__, description="Operatiuni lant de magazin")

@blp.route("/lant_de_magazine/<magazin_id>")
class Magazin(MethodView):
    def get(self, magazin_id):
        try:
            return lant_de_magazine[magazin_id]
        except KeyError:
            abort(404, message="Magazinul nu a fost gasit")

    def delete(self, magazin_id):
        try:
            del lant_de_magazine[magazin_id]
            return {"mesaj":"Magazinul a fost sters"}
        except KeyError:
            abort(404, message="Magazinul nu a fost gasit")

@blp.route("/lant_de_magazine")
class LantDeMagazine(MethodView):
    def get(self):
        return {"Lant_de_magazine": list(lant_de_magazine.values())}

    def post(self):
        magazin_data = request.get_json()
        magazin_id = uuid.uuid4().hex
        magazin_nou = {**magazin_data, "id": magazin_id}
        lant_de_magazine[magazin_id] = magazin_nou
        return magazin_nou, 201