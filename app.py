from flask import Flask, request

app = Flask(__name__)

lant_de_magazine = [
    {
        "nume": "Magazinul meu",
        "stoc": [
            {
                "nume": "Scaun",
                "pret": 18

            }
        ]
    }
]


@app.get("/lant_de_magazine")
def toate_datele_din_lantul_de_magazine():
    return {"Lant_de_magazine": lant_de_magazine}


@app.post("/lant_de_magazine")
def creare_magazin_nou():
    request_data = request.get_json()
    magazin_nou = {"nume": request_data["nume"], "stoc": []}
    lant_de_magazine.append(magazin_nou)
    return magazin_nou, 201


@app.post("/lant_de_magazine/<string:nume>/produs")
def creare_produs(nume):
    request_data = request.get_json()
    for mag in lant_de_magazine:
        if mag["nume"] == nume:
            produs_nou = {"nume": request_data["nume"], "pret": request_data["pret"]}
            mag["stoc"].append(produs_nou)
            return produs_nou, 201
    return {"mesaj": "categorie inexistenta"}, 404


@app.get("/lant_de_magazine/<string:nume>")
def afiseaza_nume_magazin(nume):
    for mag in lant_de_magazine:
        if mag["nume"] == nume:
            return mag
    return {"mesaj": "categorie inexistenta"}, 404


@app.get("/lant_de_magazine/<string:nume>/produs")
def afiseaza_produse_magazin(nume):
    for mag in lant_de_magazine:
        if mag["nume"] == nume:
            return {"produse": mag["stoc"]}
    return {"mesaj": "categorie inexistenta"}, 404
