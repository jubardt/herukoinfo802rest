from flask import Flask
from flask_restful import reqparse, Api, Resource

app = Flask(__name__)
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
        if(autonomie>distance):
            nbCharge = 0
        elif(((distance/autonomie) % 1) == 0):
            nbCharge = int(distance/autonomie)
        else:
            nbCharge = int(distance/autonomie)+1
        tempsCharge = (nbCharge)*chargement
        tempsParcours = int(((distance/vitesse)/60)+(distance/vitesse)%60)
        tempsTotal = tempsCharge +tempsParcours
        return {"nombreDeCharge":nbCharge,"tempsDeCharge":tempsCharge,"DureeParcours":tempsParcours,"DureeTotal":tempsTotal}
        #return "autonomie: "+str(autonomie)+" km, temps d'une charge: "+ str(chargement)+" heures, distance a parcourir: "+str(distance)+" km, vitesse: "+str(vitesse)+" km/h, nombre de charge: "+str(nbCharge)+", temps de charge: "+str(tempsCharge)+" heures, temps parcours: "+str(tempsParcours)+" heures, temps total: "+str(tempsTotal)



api.add_resource(calculator,'/tempsTrajet',endpoint="tempsTrajet")

if __name__ == '__main__':
    app.run(debug=True)