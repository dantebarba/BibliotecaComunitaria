import requests

class Book:
    def __init__(self, isbn, editorial, autor):
        self.autor = autor
        self.editorial = editorial
        self.isbn = isbn

    def stringify(self):
        return '''
ISBN: %s
Autor: %s
Editorial: %s''' % (self.isbn, self.autor, self.editorial)

class BibliotecaComunitaria:

    def isbn(self, isbn=""):
        response = requests.get("http://docker.for.mac.localhost:8080/api/"+isbn)
        if (response.status_code == 404):
            return "El ISBN ingresado no fue encontrado"
        return self.prettyPrint(response.json())

    def books(self):
        response = requests.get("http://docker.for.mac.localhost:8080/api/books)
        if (response.status_code == 404):
            return "El ISBN ingresado no fue encontrado"
        return self.prettyPrint(response.json())

    def prettyPrint(self, response=[]):
        result = ''
        for book in response:
            result += Book(book['isbn'], book['editorial'], book['autor']).stringify()

        return result
