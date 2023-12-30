import openai

# Substitua 'colocar chave api' pela sua chave de API da OpenAI
openai.api_key = "colocar sua chave privada"

def obter_resposta(prompt):
    try:
        # Faz a chamada para a API do GPT-3.5
        response = openai.Completion.create(
            engine="text-davinci-002",  # Endpoint correto para a GPT-3.5
            prompt=prompt,
            max_tokens=150,  # Limite de tokens para a resposta
            n=1,  # Número de respostas desejadas
            stop=None  # Não interromper automaticamente
        )

        # Obtém a resposta gerada
        resposta = response['choices'][0]['text'].strip()
        return resposta

    except Exception as e:
        print(f"Erro ao chamar a API do GPT-3.5: {e}")
        return None

# Exemplo de uso
if __name__ == "__main__":
    # Pergunta ao modelo
    pergunta = "O que é inteligência artificial?"

    # Obtém a resposta
    resposta = obter_resposta(pergunta)

    # Exibe a pergunta e a resposta
    print(f"Pergunta: {pergunta}")
    print(f"Resposta: {resposta}")