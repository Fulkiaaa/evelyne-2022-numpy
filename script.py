import numpy as np
import matplotlib.pyplot as plt

# #  /!\/!\ Le résultat attendu dans le TD est pour l'année 2022... /!\/!\
# # Exercice 1 : Charger les données pour l'année 2016
# tmin_2016 = np.genfromtxt('etudiant/data/2016/tmin.csv', delimiter=',')
# tmax_2016 = np.genfromtxt('etudiant/data/2016/tmax.csv', delimiter=',')
# tmoy_2016 = np.genfromtxt('etudiant/data/2016/tmoy.csv', delimiter=',')

# # Exercice 2 : Créer un tableau 2D avec les températures
# temperatures_2016 = np.column_stack((tmin_2016, tmax_2016, tmoy_2016))

# # Exercice 3 : Calcul des deltas de température et ajout de la colonne
# delta_temps = tmax_2016 - tmin_2016
# temperatures_2016_with_delta = np.column_stack((temperatures_2016, delta_temps))

# # Affichage du tableau final
# print(temperatures_2016_with_delta)

# Exercice 4
all_temperatures = []

# Parcourir les années de 2016 à 2022
for year in range(2016, 2023):
    # Charger les fichiers pour l'année actuelle
    tmin = np.genfromtxt(f'etudiant/data/{year}/tmin.csv', delimiter=',')
    tmax = np.genfromtxt(f'etudiant/data/{year}/tmax.csv', delimiter=',')
    tmoy = np.genfromtxt(f'etudiant/data/{year}/tmoy.csv', delimiter=',')

    temperatures = np.column_stack((tmin, tmax, tmoy))

    delta_temps = temperatures[:, 1] - temperatures[:, 0]
    temperatures = np.column_stack((temperatures, delta_temps))

    all_temperatures.append(temperatures)

# Exercice 5 : Calcul des données pour chaque année
max_temps = []
min_hot_day_temps = []
avg_annual_temps = []
avg_temp_deltas = []

for temperatures in all_temperatures:
    max_temps.append(np.max(temperatures[:, 1]))
    
    # Température minimale du jour le plus chaud de l'année
    hot_day_index = np.argmax(temperatures[:, 1])
    min_hot_day_temps.append(temperatures[hot_day_index, 0])

    # Température moyenne sur l'année
    avg_annual_temps.append(np.mean(temperatures[:, 2]))
    
    # Température moyenne des écarts
    temp_deltas = temperatures[:, 1] - temperatures[:, 0]
    avg_temp_deltas.append(np.mean(temp_deltas))

# Exercice 6 : Création du graphique avec matplotlib
plt.figure(figsize=(10, 6))

# Tracer les courbes
plt.plot(range(2016, 2023), max_temps, label='Température Maximale', color='purple', marker='o')
plt.plot(range(2016, 2023), min_hot_day_temps, label='Température Minimale du jour chaud annuelle', color='pink', marker='o')
plt.plot(range(2016, 2023), avg_annual_temps, label='Température Moyenne Annuelle', color='blue', marker='o')
plt.plot(range(2016, 2023), avg_temp_deltas, label='Température Moyenne des écarts', color='green', marker='o')

# Ajouter un titre et des labels
plt.title("Évolution des températures sur ces 7 dernières années", fontsize=14)
plt.xlabel("Années", fontsize=12)
plt.ylabel("Température (°C)", fontsize=12)

# Ajouter une légende
plt.legend()

# Afficher le graphique
plt.show()

# Exercice 7 : Création du graphique avec matplotlib
# Les températures maximales et minimales augmentent, ce qui pourrait signifier des vagues de chaleur
# plus fréquentes. La température moyenne annuelle monte chaque année, un signe du réchauffement
# climatique. Par contre, l'écart entre les températures maximales et minimales reste assez stable, 
# même si ça fluctue.