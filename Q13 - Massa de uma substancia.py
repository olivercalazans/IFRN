massa_ini = (float(input("determine o peso inicial em gramas: ")))
massa_fin = massa_ini
aux = 0
tmph = 0
tmpm = 0
tmps = 0

while massa_fin >= 0.5:
    massa_fin /=2
    aux += 1

tmph = (aux * 50) // 3600
resth = (aux * 50) % 3600
tmpm = resth // 60
restm = resth % 60

print(f"Massa inicial: {massa_ini} Massa final: {massa_fin:.2f}. O tempo total é de {tmph:.1f} hora(s), {tmpm:.1f} minuto(s) e {restm:.1f} segundos.")