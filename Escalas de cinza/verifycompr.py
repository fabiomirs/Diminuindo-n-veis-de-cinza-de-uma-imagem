from PIL import Image

# Abrir a imagem TIFF
imagem = Image.open("5.1.11.tiff")

# Exibir informações da imagem
print(f"Formato: {imagem.format}")
print(f"Modo: {imagem.mode}")
print(f"Info: {imagem.info}")

# Verificar compressão
if "compression" in imagem.info:
    print(f"Compressão usada: {imagem.info['compression']}")
else:
    print("A imagem não está comprimida.")
