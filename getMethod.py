import requests


haed={
    "Accept" : "text/plain"
}
response=requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities",headers=haed)

print(response.status_code)
print(response.json())
assert response.status_code==200