# PetLovin Chatbot

Este projeto é um chatbot desenvolvido como parte do desafio técnico para a Petlove. O objetivo é criar um assistente virtual capaz de ajudar clientes de pet shop a encontrar produtos, tirar dúvidas e fornecer informações sobre cuidados com pets.

## Tópicos

:small_blue_diamond: [Tecnologias Utilizadas](#tecnologias-utilizadas)

:small_blue_diamond: [Como rodar o projeto](#como-rodar-o-projeto)

:small_blue_diamond: [Endpoints](#endpoints)

:small_blue_diamond: [Observações](#observações)

## Tecnologias Utilizadas
- **Python 3.12+**
- **FastAPI**
- **LangChain**
- **OpenAI API**

## Como rodar o projeto
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure as variáveis de ambiente em um arquivo `.env`:
   ```env
   OPENAI_API_KEY=seu_token_openai
   OPENAI_MODEL=gpt-3.5-turbo
   ```
3. Execute o servidor:
   ```bash
   uvicorn core.app:app --reload 
    # ou, caso queira rodar em uma porta específica:
   uvicorn core.app:app --reload --port 3000
   ```
4. Acesse a documentação interativa em [http://localhost:8000/docs](http://localhost:8000/docs)

## Endpoints

### POST `/api/question-and-answer`
Recebe uma pergunta sobre pets ou produtos para pets e retorna uma resposta gerada pelo chatbot.

- **Request Body:**
  ```json
  {
    "question": "Qual a melhor ração para cachorro?"
  }
  ```
- **Response:**
  ```json
  {
    "response": "A melhor ração depende do porte, idade e necessidades do seu cachorro..."
  }
  ```
- **Erros:**
  - 400: Pergunta não enviada
  - 500: Erro interno ao processar a resposta


## Observações
- O chatbot responde apenas perguntas relacionadas ao universo pet. Perguntas fora do contexto recebem uma resposta padrão informando que não pode ajudar.
- O projeto foi criado da maneira mais simples possível, atendendo os requisistos do desafio e também mantendo boas práticas.
- Mesmo que feito de forma simples, o projeto ainda sim está bem modularizado e pronto para receber modificações para escalar.

---
