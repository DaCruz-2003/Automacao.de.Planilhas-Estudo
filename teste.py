import pandas as pd
import matplotlib.pyplot as plt

arquivos = "dados.xlsx"
dados = pd.read_excel(arquivos)

print(dados)

plt.figure(figsize=(10, 5))
plt.plot(dados["Login"], dados["Quinzena"], marker="o")
plt.title("Chamados Por Analista")
plt.xlabel("Login")
plt.ylabel("Chamados")
plt.grid(True)

plt.savefig("grafico_chamados.png")

