import uuid

from flask import Flask, request
from db import lant_de_magazine, produse
from flask_smorest import abort
app = Flask(__name__)

@app.get("/lant_de_magazine") #afiseaza toate datele din lantul de magazine
def toate_datele_din_lantul_de_magazine():
    return {"Lant_de_magazine": list(lant_de_magazine.values())}


@app.post("/lant_de_magazine")
def creare_magazin_nou(): #creeaza un magazin nou in lantul de magazine
    magazin_data = request.get_json()
    magazin_id = uuid.uuid4().hex
    magazin_nou = {**magazin_data, "id": magazin_id}
    lant_de_magazine[magazin_id] = magazin_nou
    return magazin_nou, 201


@app.post("/produs")
def creare_produs(): #creeaza un produs nou intr-un magazin
    produs_data = request.get_json()
    if("pret" not in produs_data or
    "magazin_id" not in produs_data or
    "nume" not in produs_data):
        abort(400, message = "Asigura-te ca 'pret', 'magazin id' si 'nume' sunt incluse in requestul JSON" )
    if produs_data["magazin_id"] not in lant_de_magazine:
        abort(404, message = "Magazinul nu a fost gasit")

    produs_id = uuid.uuid4().hex
    produs_nou = {**produs_data, "id": produs_id}
    produse[produs_id] = produs_nou

    return produs_nou, 201

@app.get("/produs") #afiseaza toate produsele din lanturile de magazine
def toate_produsele_din_lanturile_de_magazine():
    return {"produse": list(produse.values())}

@app.get("/lant_de_magazine/<string:store_id>") #afiseaza toate datele din magazin
def afiseaza_nume_magazin(store_id):
    try:
        return lant_de_magazine[store_id]
    except KeyError:
        abort(404, message = "Magazinul nu a fost gasit")


@app.get("/produse/<string:produs_id>")
def afiseaza_produsele_din_magazin(produs_id):
    try:
        return produse[produs_id]
    except KeyError:
        abort(404, message = "Produsul nu a fost gasit")
