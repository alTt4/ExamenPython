from fastapi import Request, FastAPI
from json import JSONDecodeError

from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from vehicules import Bateau, Voiture, Moto, Avion, voiture1, voiture2, voiture3, moto2, avion1

app = FastAPI()

@app.get('/ifa')
def univ():
    return {'info': 'TEST'}


@app.get('/ifa/user/{id}')
def getUser(id: int):
    print(f"l'id est le suivant {id}")
    return {'userpage': True}


@app.get('/start')
async def getInfo(request: Request):
    try:
        data = await request.json()
        for i in data:
            print(i)
    except JSONDecodeError:
        return JSONResponse({'error': 'il n y a pas de body'})
    except:
        return JSONResponse({'error': 'interne depuis le serveur'})
    print(f'{data}')
    return JSONResponse({'test': "test"})


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse({"message": "Cette route n'existe pas :/" })

def addBateau(store,datas):
    store.append(datas["modele"], datas["marque"], datas["couleur"], datas["vitesse_max"], datas["km"])

def addVoiture(store,datas):
    store.append(datas["modele"], datas["marque"], datas["couleur"], datas["vitesse_max"], datas["km"], datas["nbChevaux"], datas["nbChevauxFiscaux"], datas["immatriculation"], datas["carburant"])

def addMoto(store,datas):
    store.append(datas["modele"], datas["marque"], datas["couleur"], datas["vitesse_max"], datas["km"], datas["nbCC"], datas["immatriculation"], datas["nbTemps"])

def addAvion(store,datas):
    store.append(datas["modele"], datas["marque"], datas["couleur"], datas["vitesse_max"], datas["km"], datas["nbPassagerMax"], datas["capaciteKerosene"])

@app.get('/vehicules/Bateau') 
def getNombreBateau():
    return 'Nombre de bateaux :', {Bateau.counter}
    
@app.get('/vehicules/Voiture') 
def getNombreVoiture():
    return 'Nombre de voitures :', {Voiture.counter}

@app.get('/vehicules/Moto') 
def getNombreMoto():
    return 'Nombre de motos :', {Moto.counter}

@app.get('/vehicules/Avion') 
def getNombreAvion():
    return 'Nombre d\'avions :', {Avion.counter}

@app.get('/vehicules') 
def getNombreVehicules():
    return 'Nombre de vehicules :', {Bateau.counter+Voiture.counter+Moto.counter+Avion.counter}

@app.get('/km<=150000') 
def getKm():
    return '2 vehicules trouvés avec un nombre de km inférieur à 150 000 :', {voiture1, voiture3}

@app.get('/couleur=noir') 
def getCouleur():
    return '3 vehicules trouvés de couleur noir :', {voiture2, moto2, avion1}