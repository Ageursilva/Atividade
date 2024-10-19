import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do arquivo Excel
file_path = 'cidades.xlsx'  # Altere para o caminho real do seu arquivo
df = pd.read_excel(file_path)

# Agrupar os dados pela 'regiao' e calcular a média de 'idhm'
idhm_por_regiao = df.groupby('regiao')['idhm'].mean()

# Exibir as médias por região
print(idhm_por_regiao)

# Função para formatar o rótulo com porcentagem e média
def funcao_rotulo(pct, valores):
    indice = int(pct / 100. * len(valores))
    media_idhm = list(valores)[indice]
    return f'{pct:.1f}%\n(IDHM: {media_idhm:.3f})'

# Criar o gráfico de pizza com as médias de IDHM por região
plt.figure(figsize=(8, 8))
plt.pie(idhm_por_regiao, labels=idhm_por_regiao.index, autopct=lambda pct: f'{pct:.1f}%\n(IDHM: {list(idhm_por_regiao)[int(pct/100*len(idhm_por_regiao))]:.3f})',
        startangle=90)
plt.title('Média de IDHM por Região')
plt.show()
