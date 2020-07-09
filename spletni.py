''' Spletni vmesnik bo narejen s pomočjo knjižnice bottle '''

import bottle

from model import Vektor, Permutacija, Matrika 


# Izriše začetno stran

@bottle.get("/")
def main_page():
    return bottle.template("main_page.html")

bottle.run(reloader=True, debug=True)
