class Logement:
def __init__(self, code, surface, prixInitial, reserve, hauteSaison):
self.code = code
self.surface = surface
self.prixInitial = prixInitial
self.reserve = reserve
self.hauteSaison = hauteSaison
def getReserve (self):
return self.reserve
def reserver(self):
if self.reserve == False:
self.reserve = True
return self.reserve
class ChambreHotel(Logement):
def __init__(self, code, surface, prixInitial, reserve, hauteSaison):
Logement.__init__(self,code, surface, prixInitial, reserve, hauteSaison)
def PrixTotal(self):
if self.hauteSaison:
return (self.prixInitial * 2.5 + (0.1 * self.surface) )
else:
return self.prixInitial + (0.1 * self.surface)
