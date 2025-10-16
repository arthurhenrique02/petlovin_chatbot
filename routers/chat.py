import os

from dotenv import load_dotenv
from fastapi import APIRouter
from fastapi.responses import JSONResponse, Response

from core.services.bot import OpenAIChatBot
from models.chat import ChatRequest

load_dotenv()

blueprint_name = "chat"

router = APIRouter(
    prefix="/api",
    tags=[blueprint_name],
    responses={404: {"description": "Not found"}},
)

bot = OpenAIChatBot(
    name="PetLovin",
    system_prompt=(
        "Você é um ótimo assistente de vendas de pet shop e responsável por ajudar os clientes a "
        "encontrar os produtos ideais para seus pets, responder à dúvidas e outros"
        "questionamentos sobre pets em geral. Sempre mantendo a ética e o respeito,"
        "sem ultrapassar os limites do bom senso e da moralidade, tal qual um humano faria e"
        "respeitando as leis vigentes. Responda de forma clara, objetiva, amigável"
        "e apenas em texto, sem formatações ou listas."
        "Em caso de perguntas não relacionadas ao tema (pets, produtos para pets, cuidados com pets, etc)"
        "apenas responda que não pode ajudar com isso."
    ),
    model=os.getenv("OPENAI_MODEL"),
)


@router.post("/question-and-answer")
async def question_and_answer(request: ChatRequest):
    fmtd_question = request.question.strip().capitalize()

    if not fmtd_question:
        return Response(content="Deve-se enviar ao menos uma pergunta", status_code=400)

    try:
        response = bot.task(request.question)
    except Exception as e:
        return Response(content=str(e), status_code=500)

    return JSONResponse(content={"response": response}, status_code=200)
