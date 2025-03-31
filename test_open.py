import pytesseract
from PIL import Image
import json
import os

# Caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Carregar imagem
imagem = Image.open("teste_imagem_oct.png")

# Extrair dados da imagem
dados = pytesseract.image_to_data(imagem, lang="eng", output_type=pytesseract.Output.DICT)

file_path = "data.json"

# Se o arquivo já existe, carregar os dados antigos
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []
else:
    data = []

# Processar palavras e armazenar no JSON
for i in range(len(dados["text"])):
    palavra = dados["text"][i].strip()
    if palavra:  # Ignorar palavras vazias
        x, y, largura, altura = dados["left"][i], dados["top"][i], dados["width"][i], dados["height"][i]

        # Criar dicionário com as informações
        palavra_info = {
            "palavra": palavra,
            "coordenadas": {"x": x, "y": y, "largura": largura, "altura": altura}
        }

        # Adicionar ao JSON
        data.append(palavra_info)

# Salvar todas as palavras extraídas no arquivo JSON
with open(file_path, "w") as file:
    json.dump(data, file, indent=4)

    print("Dados salvos em 'data.json' com sucesso!")

print(data)

objeto_qa = next((item for item in data  if item["palavra"] == "Q&A"), None)

# Exibir o resultado
if objeto_qa:
    print(f"a palavra e: {objeto_qa["palavra"]}")
else:
    print("Palavra 'Q&A' não encontrada.")