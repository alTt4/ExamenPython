
class Bateau:
	counter = 0
	def __init__(self, modele, marque, couleur, vitesse_max, km):
		self.modele = modele
		self.marque = marque
		self.couleur = couleur
		self.vitesse_max = vitesse_max
		self.km = km
		Bateau.counter += 1

bateau1 = Bateau('pneumatique', 'Zodiac', 'rouge', '300','560')


class Voiture:
	counter = 0
	def __init__(self, modele, marque, couleur, vitesse_max, km, nbChevaux, nbChevauxFiscaux, immatriculation, carburant):
		self.modele = modele
		self.marque = marque
		self.couleur = couleur
		self.vitesse_max = vitesse_max
		self.km = km
		self.nbChevaux = nbChevaux
		self.nbChevauxFiscaux = nbChevauxFiscaux
		self.immatriculation = immatriculation
		self.carburant = carburant
		Voiture.counter += 1

voiture1 = Voiture('Ibiza', 'Seat', 'rouge', '190', '147 574', '95', '5', 'CD-277-ML', 'Ethanol')
voiture2 = Voiture('147', 'Alfa Roméo', 'noir', '210', '168 500', '105', '7', 'FK-575-KF', 'Essence')
voiture3 = Voiture('Série 1', 'BMW', 'blanc', '240', '114 650', '116', '6', 'WW-065-AP', 'Diesel')


class Moto:
	counter = 0
	def __init__(self, modele, marque, couleur, vitesse_max, km, nbCC, immatriculation, nbTemps):
		self.modele = modele
		self.marque = marque
		self.couleur = couleur
		self.vitesse_max = vitesse_max
		self.km = km
		self.nbCC = nbCC
		self.immatriculation = immatriculation
		self.nbTemps = nbTemps
		Moto.counter += 1
		
moto1 = Moto('SuperMot', 'Derby', 'vert', '110', '437', '50', 'AA-123-BB', '2')
moto2 = Moto('Urban', 'Z', 'noir', '250', '200', '950', 'PD-606-KO', '4')


class Avion:
	counter = 0
	def __init__(self, modele, marque, couleur, vitesse_max, km, nbPassagerMax, capaciteKerosene):
		self.modele = modele
		self.marque = marque
		self.couleur = couleur
		self.vitesse_max = vitesse_max
		self.km = km
		self.nbPassagerMax = nbPassagerMax
		self.capaciteKerosene = capaciteKerosene
		Avion.counter += 1

avion1 = Avion('Boeing', '737', 'noir', '900', '12 000', '168', '26 000')