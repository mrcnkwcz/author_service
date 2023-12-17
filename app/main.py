from fastapi import FastAPI

app = FastAPI()

authors = [
    {'id': 1, 'name':'Alice', 'nationality': 'A'},
    {'id': 2, 'name':'Bob', 'nationality': 'B'},
    {'id': 3, 'name':'Eva', 'nationality': 'C'},
]

@app.get("/")
def all_authors():
    return authors


@app.get("/{author_id}")
def read_item(author_id: int):
    try:
        return authors[author_id]
    except IndexError:
        return "Author not found"