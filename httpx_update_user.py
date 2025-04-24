import httpx

from tools.fakers import fake

create_user_payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post(
    url="http://localhost:8000/api/v1/users",
    json=create_user_payload
)

login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post(
    url="http://localhost:8000/api/v1/authentication/login",
    json=login_payload
)

access_token = login_response.json()['token']['accessToken']
headers = {"Authorization": f'Bearer {access_token}'}
user_id = create_user_response.json()['user']['id']
update_user = {
    "email": fake.email(),
    "lastName": "Иванов",
    "firstName": "Иван",
    "middleName": "Иванович"
}


patch_user_response = httpx.patch(
    url=f"http://localhost:8000/api/v1/users/{user_id}",
    headers=headers,
    json=update_user
)

print(patch_user_response.json())
