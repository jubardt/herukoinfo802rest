from flask import Flask
from flask_restful import reqparse, Api, Resource
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
api = Api(app)

class calculator(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('autonomie', type=int), #location='headers') #Valeur en km
        parser.add_argument('chargement', type=int),#location='headers') #Valeur en min
        parser.add_argument('distance', type=int),#location='headers' ) #Valeur en km
        parser.add_argument('vitesse', type=int),#location='headers') #Valeur en km/h
        param = parser.parse_args()
        autonomie = param.get('autonomie')*1000 #valeur en m
        chargement = param.get('chargement') #valeur en min
        distance = param.get('distance')*1000 #valeur en m
        vitesse = param.get('vitesse')/3.6 #valeur en m/s
        if(autonomie>=distance):
            nbCharge = 0
        elif(((distance/autonomie) % 1) == 0):
            nbCharge = int(distance/autonomie)
        else:
            nbCharge = int(distance/autonomie)+1
        tempsCharge = (nbCharge)*chargement
        tempsParcours = int(((distance/vitesse)/60)+(distance/vitesse)%60)
        tempsTotal = tempsCharge +tempsParcours
        print("Requete OK")
        return {"nombreDeCharge":nbCharge,"tempsDeCharge":tempsCharge,"DureeParcours":tempsParcours,"DureeTotal":tempsTotal}




api.add_resource(calculator,'/tempsTrajet',endpoint="tempsTrajet")

if __name__ == '__main__':
    app.run(debug=True)