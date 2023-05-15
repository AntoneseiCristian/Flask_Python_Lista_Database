import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import lant_de_magazine
from schemas import MagazinSchema

blp = Blueprint("lant_de_magazine", __name__, description="Operatiuni lant de magazin")

@blp.route("/lant_de_magazine/<magazin_id>")
class Magazin(MethodView):
    @blp.response(200, MagazinSchema)
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
    @blp.response(200, MagazinSchema(many=True))
    def get(self):
        return lant_de_magazine.values()

    @blp.arguments(MagazinSchema)
    @blp.response(200, MagazinSchema)
    def post(self, magazin_data):
        for mag in lant_de_magazine.values():
            if magazin_data["nume"] == lant_de_magazine["nume"]:
                abort("400", mesaj = f"Magazinul exista deja")
        magazin_id = uuid.uuid4().hex
        magazin_nou = {**magazin_data, "id": magazin_id}
        lant_de_magazine[magazin_id] = magazin_nou
        return magazin_nou, 201