# pip install python-dotenv langchain "fastapi[all]" octoai-sdk 
# .venv\Scripts\Activate.ps1
# uvicorn main:app --reload

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test")
async def root():
    return {"message": "TESTING TESTING TESTING"}

from cocktail import generate_cocktail_recipe
user_liquor = "Whiskey"
user_flavor = "Spicy"
user_mood = "Relaxed"

@app.get("/cocktail")
async def get_cocktail(liquor: str = Query(default=None), flavor: str = Query(default=None), mood: str = Query(default=None)):
    return generate_cocktail_recipe(liquor, flavor, mood)
