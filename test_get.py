
import pytest
import requests

class Test:
    def test_get1(self):
        head = {
            "Accept": "text/plain"
           }
        response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities", headers=head)

        print("status code =" ,response.status_code)
        print(response.json())
        assert response.status_code == 200

    def test_post(self):
        head11 = {
            "Accept": "text/plain",
            "Content-Type": "application/*+json"
                 }
        request3 = {
            "id": 204,
            "idBook": "newone",
            "firstName": "Ganesh",
            "lastName": "T A"
              }

        reponse1=requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities",
                           headers=head11,
                           json=request3)
        print("status code =",reponse1.status_code)
        print(reponse1.json())

