import matplotlib.pyplot as plt
import numpy as np
import os

# Definindo o intervalo de amostras (eixo X) de 0 a 2000
amostras = np.arange(0, 2001, 1)

# Método 1: Sobe linearmente 1:1
simulacoes_m1 = amostras

# Método 2: Constante inicial de 1500 + 1 simulação a cada 10 amostras (10%)
# Usamos a divisão inteira (//) para que o degrau mude estritamente a cada 10 unidades
simulacoes_m2 = 1500 + (amostras // 10)

# Criando a figura
plt.figure(figsize=(10, 6))

# Plotando os gráficos em formato de degrau
# O parâmetro where='post' garante que o degrau suba logo após atingir o valor
plt.step(amostras, simulacoes_m1, where='post', label='Método 1 (1:1)', color='blue', linewidth=2)
plt.step(amostras, simulacoes_m2, where='post', label='Método 2 (1500 + 10%)', color='orange', linewidth=2)

# Configurações dos eixos e títulos
plt.title('Comparação de Desempenho: Método 1 vs Método 2', fontsize=14, fontweight='bold')
plt.xlabel('Número de Amostras (X)', fontsize=12)
plt.ylabel('Número de Simulações (Y)', fontsize=12)

# Adicionando uma grade para facilitar a visualização dos degraus
plt.grid(True, linestyle='--', alpha=0.6)

# Posicionando a legenda
plt.legend(fontsize=11)

# Exibindo o gráfico
plt.tight_layout()
output_path = os.path.join(os.path.dirname(__file__), "genetic_ga_result.png")
plt.savefig(output_path, dpi=150)
plt.close()
print(f"Gráfico salvo em: {output_path}")