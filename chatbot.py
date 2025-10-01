
import re
import requests

# SUA chave da API (já fornecida)
API_KEY = "c0de08e1810298854bfe5411e09e6b45"

def obter_clima(cidade):
    
    """Consulta o clima de uma cidade na API do OpenWeatherMap"""
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?q={cidade}"
        f"&appid={API_KEY}&units=metric&lang=pt_br"
    )
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperatura = data['main']['temp']
        descricao = data['weather'][0]['description']
        return (
            f"O clima em {cidade} é de {temperatura}°C com {descricao}."
        )
    else:
        return (
            "Não consegui encontrar o clima dessa cidade. "
            "Verifique o nome e tente novamente."
        )


def chatbot():
    """Chatbot simples em linha de comando"""
    print(
        "🤖 Olá! Eu sou o ChatBot do Clima. "
        "Pergunte algo como 'Qual o clima em São Paulo?'"
    )
    print("Digite 'sair' para encerrar.\n")

    while True:
        pergunta = input("Você: ")

        if pergunta.lower() == "sair":
            print("🤖 Até logo!")
            break

        # Identifica se o usuário perguntou sobre clima
        if "clima" in pergunta or "tempo" in pergunta:
            # Tenta extrair a cidade usando regex para frases como 'Qual o clima em São Paulo?'
            match = re.search(r"em ([\w\sãáâéêíóôõúçÃÁÂÉÊÍÓÔÕÚÇ-]+)", pergunta, re.IGNORECASE)
            if match:
                cidade = match.group(1).strip(" ?!.,")
            else:
                # fallback: pega a última palavra
                palavras = pergunta.split()
                cidade = palavras[-1]
            try:
                resposta = obter_clima(cidade)
            except Exception as e:
                resposta = f"Erro ao buscar clima: {e}"
            print("🤖", resposta)
        else:
            print("🤖 Desculpe, só consigo responder perguntas sobre o clima.")


if __name__ == "__main__":
    try:
        chatbot()
    except Exception as e:
        print(f"Erro ao iniciar o chatbot: {e}")
