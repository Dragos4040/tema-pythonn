import pandas as pd
import matplotlib.pyplot as plt

file_path = 'data.csv'   
data = pd.read_csv(file_path)

durata = data['Durata']
puls = data['Puls']
maxpuls = data['MaxPuls']
calorii = data['Calorii']

X = len("Savin")
Y = len("DragosMarian")  

plt.figure()
plt.plot(durata, label='Durata',color="blue")
plt.plot(puls, label='Puls',color="red")
plt.plot(maxpuls, label='Max Puls',color="yellow")
plt.plot(calorii, label="Calorii",color="red")
plt.title("Toate valorile")
plt.show()

plt.figure()
plt.plot(durata[:X], label='Durata (primele X valori)',color="blue")
plt.plot(puls[:X], label='Puls (primele X valori)',color="red")
plt.plot(maxpuls[:X], label='Max Puls',color="green")
plt.plot(calorii[:X], label="Calorii",color="black")
plt.title(f"Primele {X} valori")
plt.show()

plt.figure()
plt.plot(durata[-Y:], label='Durata (ultimele Y valori)',color="blue")
plt.plot(puls[-Y:], label='Puls (ultimele Y valori)',color="orange")
plt.title(f"Ultimele {Y} valori")
plt.show()


#cd "C:\Users\_\Desktop\Savin Dragos Marian\ex2"
#python ex2.py
