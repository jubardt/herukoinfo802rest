from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)





class calculator(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('autonomie', type=int)
        parser.add_argument('chargement', type=int)
        parser.add_argument('distance', type=int)
        parser.add_argument('vitesse', type=int)
        param = parser.parse_args()
        autonomie = param.get('autonomie')
        chargement = param.get('chargement')
        distance = param.get('distance')
        vitesse = param.get('vitesse')
        nbCharge = int(distance/autonomie)
        tempsCharge = (nbCharge+1)*chargement
        tempsParcours = distance/vitesse
        tempsTotal = tempsCharge +tempsParcours
        return "autonomie: "+str(autonomie)+" km, temps d'une charge: "+ str(chargement)+" heures, distance a parcourir: "+str(distance)+" km, vitesse: "+str(vitesse)+" km/h, nombre de charge: "+str(nbCharge)+", temps de charge: "+str(tempsCharge)+" heures, temps parcours: "+str(tempsParcours)+" heures, temps total: "+str(tempsTotal)



api.add_resource(calculator,'/tempsTrajet',endpoint="tempsTrajet")

if __name__ == '__main__':
    app.run(debug=True)