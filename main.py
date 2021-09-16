import requests
from mimesis import Person
from datetime import datetime

website_pet = 'https://petstore.swagger.io/v2/pet'
website_pet_fps = 'https://petstore.swagger.io/v2/pet/findByStatus'
website_pet_store= 'https://petstore.swagger.io/v2/store/'
website_pet_user= 'https://petstore.swagger.io/v2/user/'

def add_new_pet(idp, namep):
    new_pet = {
        "id": idp,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": namep,
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

    added_pet = requests.post(website_pet, json=new_pet)
    stat_code = added_pet.status_code
    if added_pet.status_code < 400:
        print(f'Pet № {idp} added. Status code is {stat_code}')
    else:
        print(f'Pet № {idp} is NOT added. Status code is {stat_code}')
        print(added_pet.headers)
        print(added_pet.text)


def find_pet_by_id(idp):
    rsp = requests.get(website_pet + "/" + idp)
    stat_code = rsp.status_code
    if stat_code < 400:
        print(f'Pet № {idp} found. Status code is {stat_code}')
    else:
        print(f'Pet № {idp} is NOT found. Status code is {stat_code}')
        print(rsp.headers)
        print(rsp.text)


def update_an_existing_pet(idp, namep):
    upd_pet = {
        "id": idp,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": namep,
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

    added_pet = requests.put(website_pet, json=upd_pet)
    stat_code = added_pet.status_code
    if added_pet.status_code < 400:
        print(f'Pet № {idp} updated. Status code is {stat_code}')
    else:
        print(f'Pet № {idp} is NOT updated. Status code is {stat_code}')
        print(added_pet.headers)
        print(added_pet.text)


def find_pet_by_status(status):
    rsp = requests.get(website_pet_fps, params=status)
    stat_code = rsp.status_code
    if stat_code < 400:
        print(f'Pet with status {status} found. Status code is {stat_code}')
    else:
        print(f'Pet with status {status} is NOT found. Status code is {stat_code}')
        print(rsp.headers)
        print(rsp.text)


def update_pet_with_data(idp, namep, status):
    upd_pet = {
        "id": idp,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": namep,
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

    added_pet = requests.post(website_pet, json=upd_pet)
    stat_code = added_pet.status_code
    if added_pet.status_code < 400:
        print(f'Pet № {idp} updated. Status code is {stat_code}')
    else:
        print(f'Pet № {idp} is NOT updated. Status code is {stat_code}')
        print(added_pet.headers)
        print(added_pet.text)


def ReturnPetInventoriesByStatus():
    rsp = requests.get(website_pet_store + 'inventory')
    stat_code = rsp.status_code
    if stat_code < 400:
        print(f'Inventory is success. Status code is {stat_code}')
        print(rsp.text)
    else:
        print(f'Inventory is NOT success. Status code is {stat_code}')
        print(rsp.headers)
        print(rsp.text)


def OrderPet(dataN):
    new_order = {
        "id": 0,
        "petId": 0,
        "quantity": 0,
        "shipDate": dataN,
        "status": "placed",
        "complete": True
    }
    added_ord = requests.post(website_pet_store +'order', json=new_order)
    stat_code = added_ord.status_code
    if added_ord.status_code < 400:
        print(f'Order added. Status code is {stat_code}')
    else:
        print(f'Order is NOT added. Status code is {stat_code}')
        print(added_ord.headers)
        print(added_ord.text)


def FindPurchaseOrderByID(idp):
    rsp = requests.get(website_pet_store+'order/' + idp)
    stat_code = rsp.status_code
    if stat_code < 400:
        print(f'Purchase order № {idp} found. Status code is {stat_code}')
        print(rsp.text)
    else:
        print(f'Purchase order № {idp} is NOT found. Status code is {stat_code}')
        print(rsp.headers)
        print(rsp.text)


def DeletePurchaseOrderByID(idp):
    rsp = requests.delete(website_pet_store + 'order/' + idp)
    print(website_pet_store + 'order/' + idp)
    stat_code = rsp.status_code
    if stat_code < 400:
        print(f'Purchase order № {idp} deleted. Status code is {stat_code}')
        print(rsp.text)
    else:
        print(f'Purchase order № {idp} is NOT deleted. Status code is {stat_code}')
        print(rsp.headers)
        print(rsp.text)


def CreateListOfUsers():
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

    added_user = requests.post(website_pet_user+'createWithList', json=new_user)
    stat_code = added_user.status_code
    if added_user.status_code < 400:
        print(f'User added. Status code is {stat_code}')
        print(added_user.text)
    else:
        print(f'User is NOT added. Status code is {stat_code}')
        print(added_user.headers)
        print(added_user.text)


def GetUserByUserName(User_name):
    rsp = requests.get(website_pet_user+'createWithList' + "/" + User_name)
    stat_code = rsp.status_code
    if stat_code < 400:
        print(f'User № {User_name} found. Status code is {stat_code}')
    else:
        print(f'User № {User_name} is NOT found. Status code is {stat_code}')
        print(rsp.headers)
        print(rsp.text)


if __name__ == '__main__':
    # for i in range(2,10):
    #     add_new_pet(i, Person('en').name())

    # find_pet_by_id('3')
    # update_an_existing_pet('2', 'shushu')
    # stat = ['pending', 'available', 'sold']
    # for i in stat:
    #     find_pet_by_status(i)
    # update_pet_with_data('2', 'ricki', 'sold')

    # ReturnPetInventoriesByStatus()
    # OrderPet(f'{datetime.now().date()}T{str(datetime.now().time())[0:-3]}Z')
    # FindPurchaseOrderByID('1') # 1<=ID<=10
    # DeletePurchaseOrderByID('3')
    CreateListOfUsers()
    GetUserByUserName('user1')