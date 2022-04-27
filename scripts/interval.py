import random

def intervalRandOrNot(interval=-1,approx=-1):
    
    spaceTime = 0

    if interval == -1: # Evite répétition demande de saisie

      literralInterval = "NaN"

      while True:

        try:

            literralInterval = int(input("Veuillez saisir l\'intervalle de temps entre chaque envoi en minutes (minimum 1) : \n"))
            break

        except ValueError:
            print("Valeur invalide, veuillez réessayer.")

      interval = int(literralInterval) # en minutes

    if approx == -1: # Evite répétition demande de saisie
      
      while True:

        try:

            approx = int(input("Si vous souhaitez que cette intervalle soit approximative (pour plus de crédibilité),\nveuillez renseigner un pourcentage d\'approximation (sinon, saisir 0) : \n"))
            break

        except ValueError:
            print("Valeur invalide, veuillez réessayer.")

    if interval == 0:
      
      print ("Intervalle de temps en minute trop petite ("+str(interval)+"), redéfinie automatiquement à 1 minute." )
      interval = 1
      
    if approx == 0:

      randomInterval = 0
      spaceTime = (interval * 60)

    else :

      approxed = int(approx)/100
      randomInterval = random.uniform(-(interval*60*approxed),interval*60*approxed)
      spaceTime = (interval * 60) + randomInterval

    return {"spaceTime":spaceTime,"randomInterval":randomInterval, "interval":interval, "approx":approx}