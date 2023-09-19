import json
from django.shortcuts import render
from django.http import HttpResponse
from New_work.form import OurForm, PetForm, ThirdForm


def index(req):
    data = {'title': 'Главная'}
    return render(req, 'index.html', context=data)


def form_1(req):
    title = 'Авторизация'
    if req.method == 'POST':
        if req.is_valid():
            name = req.POST.get('name')
            num = req.POST.get('num')
            output = f'<h1>Спасибо!</h1>' \
                     f'<h2>Ваше имя -- {name}</h2>' \
                     f'<h2>Ваше число -- {num}</h2>'
            return HttpResponse(output)
    form1 = OurForm()
    data = {'form': form1, 'title': title}
    return render(req, 'form.html', context=data)


def form_2(req):
    title: str = 'Зверюха'
    if req.method == 'POST':
        name = req.POST.get('name')
        breed = req.POST.get('breed')
        age = req.POST.get('age')
        color = req.POST.get('color')
        food = req.POST.get('food')
        img_obj = req.FILES.get('image')

        data: dict[str, str] = {
            'name': name,
            'breed': breed,
            'age': age,
            'color': color,
            'food': food,
            'img_path': f'media/{img_obj.name}' if img_obj is not None else 'media/no_img.jpg'
        }

        for key in data.keys():
            data[key] = data[key] if data[key] != '' else 'N/D'

        if data['img_path'] != 'media/no_img.jpg':
            with open(f'New_work/static/media/{img_obj.name}', 'wb+') as file:
                file.write(img_obj.read())

        data_json: dict[str, dict[str, str]] = {f'{data["name"]}': data}

        with open(f'New_work/json_files/pets.json', 'r') as file:
            temp: dict = json.loads(file.read())
            temp.update(data_json)

        with open(f'New_work/json_files/pets.json', 'w') as file:
            json.dump(
                temp,
                file,
                indent=2
            )
        data.update({'title': title})
        return render(req, 'final.html', context=data)

    else:
        form_pet = PetForm(req.POST, req.FILES)
        data = {'form': form_pet, 'title': title}
        return render(req, 'form.html', context=data)


def see_pets(req):
    with open(f'New_work/json_files/pets.json', 'r') as file:
        temp: dict = json.loads(file.read())

    pets: list[dict] = [temp[key] for key in temp.keys() if key != 'No_name']
    data: dict[str, list[dict[str, str]] | str] = {'pets': pets, 'title': 'Зверюхи'}

    return render(req, 'all_pets.html', context=data)


def third(req):
    if req.method == 'POST':
        k1 = req.POST['field_1']
        k2 = req.POST['field_2']
        k3 = req.POST['field_3']
        k4 = req.POST['field_4']
        print(f'{k1 = }, {k2 = }, {k3 = }, {k4 = }')
        output = f'<h1>Спасибо!</h1>' \
                 f'<h2>{k1}</h2>' \
                 f'<h2>{k2}</h2>' \
                 f'<h2>{k3}</h2>' \
                 f'<h2>{k4}</h2>'
        return HttpResponse(output)
    anketa = ThirdForm()
    data = {'form': anketa}
    return render(req, 'form.html', context=data)
