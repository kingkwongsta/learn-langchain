# pip install python-dotenv langchain "fastapi[all]" octoai-sdk 
# .venv\Scripts\Activate.ps1
# uvicorn main:app --reload

from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

from cocktail import generate_cocktail_recipe
user_liquor = "Whiskey"
user_flavor = "Spicy"
user_mood = "Relaxed"

@app.get("/cocktail")
async def test():
    return generate_cocktail_recipe(user_liquor, user_flavor, user_mood)
