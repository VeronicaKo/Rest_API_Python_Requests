import requests

website_pet = 'https://petstore.swagger.io/v2/pet'
website_pet_fps = 'https://petstore.swagger.io/v2/pet/findByStatus'
website_pet_store = 'https://petstore.swagger.io/v2/store/'
website_pet_user = 'https://petstore.swagger.io/v2/user/'


def upload_image():
    pass


def add_new_pet(id_pet: str, name_pet: str):
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
    stat_code = add_pet.status_code
    if add_pet.status_code < 400:
        print(f'Pet № {id_pet} added. Status code is {stat_code}')
    else:
        print(f'Pet № {id_pet} is NOT added. Status code is {stat_code}')
        print(add_pet.headers)
        print(add_pet.text)


def find_pet_by_id(id_pet: str):
    rsp = requests.get(f'{website_pet}"/"{id_pet}')
    stat_code = rsp.status_code
    if stat_code < 400:
        print(f'Pet № {id_pet} found. Status code is {stat_code}')
    else:
        print(f'Pet № {id_pet} is NOT found. Status code is {stat_code}')
        print(rsp.headers)
        print(rsp.text)


def update_an_existing_pet(id_pet: str, name_pet: str):
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
        "status": "available"
    }

    add_pet = requests.put(website_pet, json=upd_pet)
    stat_code = add_pet.status_code
    if add_pet.status_code < 400:
        print(f'Pet № {id_pet} updated. Status code is {stat_code}')
    else:
        print(f'Pet № {id_pet} is NOT updated. Status code is {stat_code}')
        print(add_pet.headers)
        print(add_pet.text)


def find_pet_by_status(status: str):
    rsp = requests.get(website_pet_fps, params=status)
    stat_code = rsp.status_code
    if stat_code < 400:
        print(f'Pet with status {status} found. Status code is {stat_code}')
    else:
        print(f'Pet with status {status} is NOT found. Status code is {stat_code}')
        print(rsp.headers)
        print(rsp.text)


def update_pet_with_data(id_pet: str, name_pet: str, status: str):
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
    stat_code = add_pet.status_code
    if add_pet.status_code < 400:
        print(f'Pet № {id_pet} updated. Status code is {stat_code}')
    else:
        print(f'Pet № {id_pet} is NOT updated. Status code is {stat_code}')
        print(add_pet.headers)
        print(add_pet.text)


def deletes_pet(id_pet: str):
    pass


def return_pet_inventories_by_status():
    rsp = requests.get(f'{website_pet_store}inventory')
    stat_code = rsp.status_code
    if stat_code < 400:
        print(f'Inventory is success. Status code is {stat_code}')
        print(rsp.text)
    else:
        print(f'Inventory is NOT success. Status code is {stat_code}')
        print(rsp.headers)
        print(rsp.text)


def order_pet(dataN):
    new_order = {
        "id": 0,
        "petId": 0,
        "quantity": 0,
        "shipDate": dataN,
        "status": "placed",
        "complete": True
    }
    add_order = requests.post(f'{website_pet_store}order', json=new_order)
    stat_code = add_order.status_code
    if add_order.status_code < 400:
        print(f'Order added. Status code is {stat_code}')
    else:
        print(f'Order is NOT added. Status code is {stat_code}')
        print(add_order.headers)
        print(add_order.text)


def find_purchase_order_by_id(id_pet: str):
    rsp = requests.get(f'{website_pet_store}order/{id_pet}')
    stat_code = rsp.status_code
    if stat_code < 400:
        print(f'Purchase order № {id_pet} found. Status code is {stat_code}')
        print(rsp.text)
    else:
        print(f'Purchase order № {id_pet} is NOT found. Status code is {stat_code}')
        print(rsp.headers)
        print(rsp.text)


def delete_purchase_order_by_id(id_pet: str):
    rsp = requests.delete(f'{website_pet_store}order/{id_pet}')
    print(website_pet_store + 'order/' + id_pet)
    stat_code = rsp.status_code
    if stat_code < 400:
        print(f'Purchase order № {id_pet} deleted. Status code is {stat_code}')
        print(rsp.text)
    else:
        print(f'Purchase order № {id_pet} is NOT deleted. Status code is {stat_code}')
        print(rsp.headers)
        print(rsp.text)


def create_list_of_users():
    new_user = [{
        "id": 0,
        "username": "string",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }]

    added_user = requests.post(f'{website_pet_user}createWithList', json=new_user)
    stat_code = added_user.status_code
    if added_user.status_code < 400:
        print(f'User added. Status code is {stat_code}')
        print(added_user.text)
    else:
        print(f'User is NOT added. Status code is {stat_code}')
        print(added_user.headers)
        print(added_user.text)


def get_user_by_user_name(User_name: str):
    rsp = requests.get(f'{website_pet_user}User_name')
    stat_code = rsp.status_code
    if stat_code < 400:
        print(f'User {User_name} found. Status code is {stat_code}')
    else:
        print(f'User {User_name} is NOT found. Status code is {stat_code}')
        print(rsp.headers)
        print(rsp.text)


def updated_user(param: str):
    pass


def delete_user(param: str):
    pass


def logs_user_into_the_system(param: str, param1: str):
    pass


def logs_out_current_logged_in_user_session():
    pass


def create_user(object):
    pass


