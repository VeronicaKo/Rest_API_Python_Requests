import requests

website_pet = 'https://petstore.swagger.io/v2/pet'
website_pet_fps = 'https://petstore.swagger.io/v2/pet/findByStatus'
website_pet_store = 'https://petstore.swagger.io/v2/store/'
website_pet_user = 'https://petstore.swagger.io/v2/user/'


def upload_image(id_pet: str, img_pet) -> int:
    add_img = requests.post(f'{website_pet}/{id_pet}/uploadImage', files=img_pet)
    return add_img.status_code


def add_new_pet(id_pet: str, name_pet: str) -> int:
    new_pet = {
        "id": id_pet,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": name_pet,
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    add_pet = requests.post(website_pet, json=new_pet)
    return add_pet.status_code


def find_pet_by_id(id_pet: str) -> int:
    rsp = requests.get(f'{website_pet}/{id_pet}')
    return rsp.status_code


def update_an_existing_pet(id_pet: str, name_pet: str) -> int:
    upd_pet = {
        "id": id_pet,
        "category": {
            "id": 0,
        },
        "name": name_pet,
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    add_pet = requests.put(website_pet, json=upd_pet)
    return add_pet.status_code


def find_pet_by_status(status: str) -> int:
    rsp = requests.get(website_pet_fps, params=status)
    return rsp.status_code


def update_pet_with_data(id_pet: str, name_pet: str, status: str) -> int:
    upd_pet = {
        "id": id_pet,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": name_pet,
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": status
    }

    add_pet = requests.post(website_pet, json=upd_pet)
    return add_pet.status_code


def deletes_pet(id_pet: str) -> int:
    del_pet = requests.delete(f'{website_pet}/{id_pet}')
    return del_pet.status_code


def return_pet_inventories_by_status() -> int:
    rsp = requests.get(f'{website_pet_store}inventory')
    return rsp.status_code


def order_pet(data_order) -> int:
    new_order = {
        "id": 0,
        "petId": 0,
        "quantity": 0,
        "shipDate": data_order,
        "status": "placed",
        "complete": True
    }
    add_order = requests.post(f'{website_pet_store}order', json=new_order)
    return add_order.status_code


def find_purchase_order_by_id(id_pet: str) -> int:
    rsp = requests.get(f'{website_pet_store}order/{id_pet}')
    return rsp.status_code


def delete_purchase_order_by_id(id_pet: str) -> int:
    rsp = requests.delete(f'{website_pet_store}order/{id_pet}')
    print(website_pet_store + 'order/' + id_pet)
    return rsp.status_code


def create_list_of_users_with_given_input_array(user_name: str) -> int:
    new_user = [{
        "id": 0,
        "username": user_name,
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }]

    added_user = requests.post(f'{website_pet_user}createWithList', json=new_user)
    return added_user.status_code


def get_user_by_user_name(user_name: str) -> int:
    rsp = requests.get(f'{website_pet_user}{user_name}')
    return rsp.status_code


def updated_user(user_name: str) -> int:
    upd_user = {
        "id": 0,
        "username": user_name,
        "firstName": user_name,
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }

    rsp = requests.put(f'{website_pet_user}{user_name}', json=upd_user)
    return rsp.status_code


def delete_user(user_name: str) -> int:
    rsp = requests.delete(f'{website_pet_user}{user_name}')
    return rsp.status_code


def logs_user_into_the_system(user_name: str, user_password: str) -> int:
    rsp = requests.get(f'{website_pet_user}login?username={user_name}&password={user_password}')
    return rsp.status_code


def logs_out_current_logged_in_user_session() -> int:
    rsp = requests.get(f'{website_pet_user}logout')
    return rsp.status_code


def create_user(user_name: str) -> int:
    new_user = {
        "id": 0,
        "username": user_name,
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }

    rsp = requests.post(f'{website_pet_user}', json=new_user)
    return rsp.status_code
