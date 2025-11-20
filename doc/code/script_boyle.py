import matplotlib.pyplot as plt
import math

# --- DATI DI INPUT ---
ms = 0.10  # massa pistone kg
m = 0.05   # massa aggiunta kg
altezze = [0.083, 0.066, 0.060, 0.048, 0.026, 0.021]  
diametro_siringa = 0.030  # m (30 mm)
pressione_atm = 1.020e5  # Pa
g = 9.81  # gravità
masse = [0.10, 1.600, 3.535, 4.335, 5.195, 5.895] # masse in kg

# --- CALCOLI ---
area = math.pi * (diametro_siringa / 2)**2

print(f"{'Massa (kg)':>10} {'Forza peso (N)':>15} {'Altezza (m)':>12} {'Volume (m^3)':>15} {'Pressione (Pa)':>15} {'Pressione totale (Pa)':>22}")

volumes = []
pressioni_totali = []

for massa, altezza in zip(masse, altezze):
    volume = math.pi * (diametro_siringa/2)**2 * altezza  # V = pi*r^2*h
    forza_peso = massa * g  # F = m*g
    pressione = forza_peso / area  # P = F/A
    pressione_totale = pressione + pressione_atm  # P_tot = P + P_atm

    volumes.append(volume)
    pressioni_totali.append(pressione_totale)
    print(f"{massa:10.2f} {forza_peso:15.4f} {altezza:12.4f} {volume:15.6e} {pressione:15.2f} {pressione_totale:22.2f}")

# --- GRAFICO ---
plt.plot(volumes, pressioni_totali, 'o')
for massa, volume, pressione_totale in zip(masse, volumes, pressioni_totali):
    plt.annotate(f'{massa:.2f} kg', (volume, pressione_totale))

plt.xlabel('Volume (m^3)')
plt.ylabel('Pressione totale (Pa)')
plt.title('Pressione totale vs Volume')
plt.grid(True)
plt.show()
