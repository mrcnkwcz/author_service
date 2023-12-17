from fastapi import FastAPI


app = FastAPI()

authors = [
    {'id': 1, 'name':'Alice', 'nationality': 'A'},
    {'id': 2, 'name':'Bob', 'nationality': 'B'},
    {'id': 3, 'name':'Eva', 'nationality': 'C'},
]

@app.get("/")
def get_all_authors():
    return authors


@app.get("/{author_id}")
def get_author_by_id(author_id: int):
    try:
        return authors[author_id-1]
    except IndexError:
        return "Author not found"

if __name__ == '__main__':
    import uvicorn
    import os
    try:
        PORT = int(os.environ['PORT'])
    except KeyError as keyerr:
        PORT = 80
    uvicorn.run(app, host='0.0.0.0', port=PORT)