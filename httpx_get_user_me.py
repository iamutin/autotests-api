import httpx

payload = {
    "email": "user@example.com",
    "password": "string"
}

response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload)
access_token = response.json()['token']['accessToken']
headers = {"Authorization": f'Bearer {access_token}'}
response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print(response.json())
print(response.status_code)
