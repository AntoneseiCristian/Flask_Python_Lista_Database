import uuid
from flask.views import MethodView
from flask import request
from flask_smorest import Blueprint, abort
from db import produse

blp = Blueprint("Produse", __name__, description="Operatiuni pe produse")

@blp.route("/produs/<string:produs_id>")
class Produs(MethodView):
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

    def put(self, produs_id):
        produs_data = request.get_json()
        if ("pret" not in produs_data or
                "nume" not in produs_data):
            abort(400, message="Asigura-te ca 'pret' si 'nume' sunt incluse in requestul JSON")
        try:
            produs = produse[produs_id]
            produs |= produs_data

            return produs
        except KeyError:
            abort(404, message="Produsul nu a fost gasit")

@blp.route("/produs")
class ItemList(MethodView):
    def get(self):
        return {"produse": list(produse.values())}

    def post(self):
        produs_data = request.get_json()
        if ("pret" not in produs_data or
                "magazin_id" not in produs_data or
                "nume" not in produs_data):
            abort(400, message="Asigura-te ca 'pret', 'magazin id' si 'nume' sunt incluse in requestul JSON")
        for produs in produse.values():
            if (produs_data["nume"] == produs["nume"]) and (produs_data["magazin_id"] == produs["magazin_id"]):
                abort(400, message=f"Produsl exista deja")

        produs_id = uuid.uuid4().hex
        produs_nou = {**produs_data, "id": produs_id}
        produse[produs_id] = produs_nou

        return produs_nou, 201

