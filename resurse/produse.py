import uuid
from flask.views import MethodView
from flask import request
from flask_smorest import Blueprint, abort
from db import produse
from schemas import ProdusSchema, UpdateProdusSchema

blp = Blueprint("Produse", __name__, description="Operatiuni pe produse")

@blp.route("/produs/<string:produs_id>")
class Produs(MethodView):
    @blp.response(200, ProdusSchema)
    def get(self, produs_id):
        try:
            return produse[produs_id]
        except KeyError:
            abort(404, message="Produsul nu a fost gasit")

    def delete(self, produs_id):
            try:
                del produse[produs_id]
                return {"mesaje":"Produsul a fost sters"}
            except KeyError:
                abort(404, message="Produsul nu a fost gasit")

    @blp.arguments(UpdateProdusSchema)
    @blp.response(200, ProdusSchema)
    def put(self, produs_data, produs_id):
        try:
            produs = produse[produs_id]
            produs |= produs_data

            return produs
        except KeyError:
            abort(404, message="Produsul nu a fost gasit")

@blp.route("/produs")
class ItemList(MethodView):
    @blp.response(200, ProdusSchema(many=True))
    def get(self):
        return produse.values()
    @blp.arguments(ProdusSchema)
    @blp.response(201, ProdusSchema)
    def post(self, produs_data):
        for produs in produse.values():
            if (produs_data["nume"] == produs["nume"]) and (produs_data["magazin_id"] == produs["magazin_id"]):
                abort(400, message=f"Produsl exista deja")

        produs_id = uuid.uuid4().hex
        produs_nou = {**produs_data, "id": produs_id}
        produse[produs_id] = produs_nou

        return produs_nou, 201