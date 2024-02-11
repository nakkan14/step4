from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    number: int

def is_aho(number: int) -> bool:
    if number % 3 == 0 or '3' in str(number):
        return True
    return False

@app.post("/aho")
def aho_number(item: Item):
    if is_aho(item.number):
        return {"message": f"{item.number}(○дο)"}
    else:
        return {"number": item.number}