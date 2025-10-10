import csv
import os

# 🔹 Fonction pour charger les thetas depuis le fichier CSV
def load_thetas(filename='thetas.csv'):
    if not os.path.exists(filename):
        print("⚠️ Le fichier 'thetas.csv' est introuvable. Avez-vous déjà entraîné le modèle ?")
        return 0.0, 0.0  # valeurs par défaut
    
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            theta0 = float(row['theta0'])
            theta1 = float(row['theta1'])
            return theta0, theta1

# 🔹 Fonction de prédiction
def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage

# 🔹 Programme principal
def main():
    theta0, theta1 = load_thetas()
    print(f"θ0 = {theta0}, θ1 = {theta1}")

    try:
        mileage = float(input("Entrez le kilométrage de la voiture : "))
        price = estimate_price(mileage, theta0, theta1)
        print(f"Prix estimé : {price:.2f}")
    except ValueError:
        print("Veuillez entrer une valeur numérique valide pour le kilométrage.")

if __name__ == "__main__":
    main()
