import requests


def test_get_all_authors(url: str):
    res = requests.get(url).json()
    assert(res == [{'id': 1, 'name': 'Alice', 'nationality': 'A'}, {'id': 2, 'name': 'Bob', 'nationality': 'B'}, {'id': 3, 'name': 'Eva', 'nationality': 'C'}])


def test_get_author_by_id(url: str):
    res = requests.get(url).json()
    assert(res == {'id': 1, 'name': 'Alice', 'nationality': 'A'})

if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/'
    test_get_author_by_id(URL + '1')
    test_get_all_authors(URL)
