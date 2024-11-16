from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Carrega a imagem 
imagem = Image.open("5.1.11.tiff").convert("L") 
imagem_array = np.array(imagem)

# Lista de níveis de cinza
niveis_cinza = [256, 128, 64, 32, 16, 8, 4, 2]

# Função para reduzir a intensidade dos níveis de cinza
def reduzir_niveis_cinza(imagem_array, niveis):
    fator = 256 // niveis
    imagem_reduzida = (imagem_array // fator) * fator
    return imagem_reduzida

# Plotar as imagens
fig, axes = plt.subplots(1, len(niveis_cinza), figsize=(15, 5))
for i, niveis in enumerate(niveis_cinza):
    imagem_reduzida = reduzir_niveis_cinza(imagem_array, niveis)
    axes[i].imshow(imagem_reduzida, cmap="gray", vmin=0, vmax=255)
    axes[i].set_title(f"Níveis de Cinza: {niveis}")
    axes[i].axis("off")

plt.tight_layout()
plt.show()
