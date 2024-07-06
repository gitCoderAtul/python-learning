import requests
api_url = "https://fakestoreapi.com/products/1"
response = requests.get(api_url)
ans = response.json()
print(ans)
print(type(ans))

for values in ans:
    print(values)
    print(end="\n")
