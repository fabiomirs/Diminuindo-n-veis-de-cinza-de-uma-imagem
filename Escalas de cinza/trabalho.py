from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

# Carrega a imagem 
imagem = Image.open("Escalas de cinza/5.1.11.tiff").convert("L") 
imagem_array = np.array(imagem)

# Lista de níveis de cinza
niveis_cinza = [256, 128, 64, 32, 16, 8, 4, 2]

# Função para reduzir a intensidade dos níveis de cinza
def reduzir_niveis_cinza(imagem_array, niveis):
    fator = 255 / (niveis - 1)
    imagem_reduzida = np.round(imagem_array / 255 * (niveis - 1)) * fator
    return imagem_reduzida.astype(np.uint8)

# Criar diretório para armazenar as matrizes
output_dir = "matrizes"
os.makedirs(output_dir, exist_ok=True)

# Plotar as imagens
fig, axes = plt.subplots(1, len(niveis_cinza), figsize=(15, 5))

for i, niveis in enumerate(niveis_cinza):
    # Reduzir níveis de cinza
    imagem_reduzida = reduzir_niveis_cinza(imagem_array, niveis)

    # Salvar a matriz como arquivo de texto
    matriz_file = os.path.join(output_dir, f"matriz_{niveis}_niveis.txt")
    np.savetxt(matriz_file, imagem_reduzida, fmt='%3d')

    # Exibir a imagem reduzida
    axes[i].imshow(imagem_reduzida, cmap="gray", vmin=0, vmax=255)
    axes[i].set_title(f"Níveis de Cinza: {niveis}")
    axes[i].axis("off")

plt.tight_layout()
plt.show()
