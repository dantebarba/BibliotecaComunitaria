import requests

class BibliotecaComunitaria:

    def isbn(self, isbn=""):
        return requests.get("http://localhost:8080/api/"+isbn).content
