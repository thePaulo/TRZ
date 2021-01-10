# codeminer-test-back-end

# TRZ (The Resident Zombie) - Backend
## Requirements

* Python 3.8.1
* Django
* DjangoRestFramework

## How to run locally

Clone this repo and run:

```shell
pip install -r requirements.txt
```

## Run Django migrations:

```shell
python manage.py makemigrations
```

and then...

```shell
python manage.py migrate
```

## Run tests ( with 2 open terminals ):

```shell
python manage.py runserver
```

along with

```shell
python manage.py test
```

## Run Django server:

```shell
python manage.py runserver
```
# About the project

Assuming that your server should be running on localhost:8000, there are 4 base urls availiable here
* localhost:8000/items
* localhost:8000/survivors
* localhost:8000/reports
* localhost:8000/trading

## On the `survivors` page, there'll be displayed all currently registered survivors .Same way that in items, you can acess it with it's id

survivors creation with `post` ex:
localhost:8000/survivors/

body:
```shell
{
            "name": "viktor",
            "age": 23,
            "gender": 0,
            "latitude": -11,
            "longitude": 23,
            "fiji_water": 1,
            "campbell_soup": 0,
            "first_aid_pouch": 0,
            "ak47": 0
}
```

ps: `fiji_water`,`campbell_soup`,`first_aid_pouch` and `ak47` values indicate how many of these correspondent items will be created.

survivor detail with `get` ex:
```shell
localhost:8000/survivors/1
```

## Then, on the `items` page, there'll  be displayed all currently created items. After the item's creation you can acess each of it with it's id

item details ex:
```shell
localhost:8000/items/1
```

## On the `reports` page, there'll be the requested info about the system

* "infected_percent" tells about the % of suvivors that are infected
* "non_infected_percent" tells about the % of suvivors that aren't infected
* "water_mean" tells about the sum of all fiji waters from non-infected survivors divided by all survivors
* "soup_mean" tells about the sum of all campbell soups from non-infected survivors divided by all survivors
* "aid_pouch_mean" tells about the sum of all first aid pouches from non-infected survivors divided by all survivors
* "ak_mean" tells about the sum of all AK47s from non-infected survivors divided by all survivors
* "lost_points" tells about the sum of all points from all items that were blocked due to infected survivors

## On the `trading` page, there'll be done all the trades from the system, it requires two parameters, `s1` and `s2`

Each of these parameters represent each survivor and it shall be used with its tradable items id's

ex:
```shell
localhost:8000/trading?s1=5+7&s2=8+13
```

After an sucessfull trade, you should be redirected to the item list page to see the changes

# About the tests

There are something around 20 tests but these are the ones that are more relevant to the specifications

* `test_user_creation` creates an user via post request
* `test_user_alter_location` updates an user location via post request
* `test_infection` updates the user's infection
* `test_five_infected_survivors_effect` when there are at least 5 infected survivors, everyone shall become infected.
* `test_trade_successful` trades items with others, according to each accumulated points ( transaction is applied =p )
* `test_trade_on_infected` trading isn't allowed if there are infected survivors
* `test_lost_points` reports current amount of lost points due to infected survivors

Thats about it, HAPPY END OF THE WORLD =/

