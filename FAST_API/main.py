from typing import Optional, Any
from fastapi import FastAPI, HTTPException, status , Response, Depends
from models import Pato

app = FastAPI(title="Api de patos dads14", version="0.0.1", description="Api de patos por que a ds 14 escolheu")

def fake_db():
    try:
        print("conectando no banco de dados")
    finally:
        print("fechando a conexão com o bancos de dados")

patos = {
    1: {
        "nome": "Lucca",
        "especie": "Pato Grande",
        "idade": "25",
        "cor": "amarelo",
        "foto": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fnoareeiroeporai.blogs.sapo.pt%2Fo-pato-de-toronto-e-o-meu-253198&psig=AOvVaw1SYqwdpE_4xcKEAUND3GT2&ust=1743248106563000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMiE_7LXrIwDFQAAAAAdAAAAABAc"
    },
    
    2: {
        "nome": "Perry",
        "especie": "Ornintorrinco",
        "idade": "5",
        "cor": "verde",
        "fotos": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fdynami-battles.fandom.com%2Fpt-br%2Fwiki%2FPerry_o_Ornitorrinco&psig=AOvVaw1SV06WQAGkJ8Fxugqq7yyA&ust=1743248768238000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCPD9ou_ZrIwDFQAAAAAdAAAAABAE"
    }
}

@app.get("/")
async def raiz():
    return {"AVISO": "OK!!"}

@app.get("/patos", description="Retorna todos os patos do banco de dados", summary="Retorna todos os patos")
async def get_patos(db: any = Depends(fake_db)):
    return patos

@app.get("/patos/{pato_id}")
async def get_patos(pato_id: int):
    try:
        pato = patos[pato_id]
        return pato
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"não existe pato com ID {pato_id}")
        

@app.post("/patos", status_code=status.HTTP_201_CREATED)
async def post_pato(pato: Optional[Pato] = None):
    next_id = len(patos) + 1
    patos[next_id] = pato
    del pato.id
    return pato

@app.put("/patos/{pato_id}", status_code=status.HTTP_202_ACCEPTED)
async def put_pato(pato_id: int, pato: Pato):
    if pato_id in patos:
        patos[pato_id] = pato
        pato_id = pato_id
        del pato_id
        return pato
    else: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"não existe pato com o ID : {pato_id}")
    
@app.delete("/patos/{pato_id}")
async def delete_pato(pato_id: int):
    if pato_id in patos:
        del patos[pato_id]
        return Response(status_code=status. HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"não existe pato com o ID : {pato_id}")

        


@app.get("/calculadora")
async def calcular(num1: int, num2: int):
    soma = num1 + num2
    return soma


if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run("main:app", host="127.0.0.1", port=8001, log_level="info", reload=True)


