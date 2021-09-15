import requests

website_pet = 'https://petstore.swagger.io/v2/pet'
website_pet_fps = 'https://petstore.swagger.io/v2/pet/findByStatus'


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


def upload_image_for_pets(idp, file_img):
    upd_pet = {"id": idp,
               "photoUrls": [
                   file_img
               ],
               }
    upda_pet = requests.post(
        website_pet + '/' + idp + 'uploadImage',
        files={'image': ('@dog.jpg', file_img.content, 'image/jpg')})

    # upda_pet = requests.post(website_pet+'/'+idp+'uploadImage', json=upd_pet)
    stat_code = upda_pet.status_code
    if upda_pet.status_code < 400:
        print(f'Pet № {idp} updated. Status code is {stat_code}')
    else:
        print(f'Pet № {idp} is NOT updated. Status code is {stat_code}')
        print(upda_pet.headers)
        print(upda_pet.text)


if __name__ == '__main__':
    add_new_pet('2', 'sharik')
    find_pet_by_id('2')
    update_an_existing_pet('2', 'shushu')
    stat = ['pending', 'available', 'sold']
    for i in stat:
        find_pet_by_status(i)

    # file_img = open("C:/Users/Admin/Downloads/dog.jpg", "r")
    # upload_image_for_pets('2', file_img)
    # file_img.close()