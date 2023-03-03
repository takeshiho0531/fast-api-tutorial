# 最もシンプルなFastAPIファイル
from fastapi import FastAPI

app = FastAPI() # uvicorn main:app --reload の"app"はインスタンス名


@app.get("/")  # POST: データの作成, # GET: データの読み取り, # PUT: データの更新, # DELETE: データの削除
async def root():
    return {"message": "Hello World"}

# 複数種類のUIがある
