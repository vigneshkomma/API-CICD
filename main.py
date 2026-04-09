import uvicorn
from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/")
async def root():
    return{"message:":"TO DO LIST API:v1.0"}


@app.post("/items/insert")
def insert(item:str):
    items.append(item)
    return item

@app.get("/items/view")     
def view():
    return items

@app.delete("/items/remove")
def remove(id:int) -> str:
    items.remove(items[id])
    return "Task removed" 



if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8000)
