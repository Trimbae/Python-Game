from items import *
from friend import *
room_flat = {

    "required_level": 1,

    "id": "flat",

    "name": "Your flat",

    "lockout_phrase": "",

    "description":
    """Empty bottles litter the kitchen. Plates with half eaten pizzas and kebabs. Tables have empty shot glasses scattered over them as well as half filled pint glasses. Your wallet is next to you, with only some coins left from your depleted funds. In the fridge there is bacon, eggs, milk and chocolate.  """,

    "exits": {"south": "summers", "north": "kebab", "east": "mortys", "west": "taf"},

    "items": [item_bacon, item_kebab_box, item_can_of_coke, item_wallet],

    "friends": [friend_rick],





}

room_mortys = {

    "required_level": 4,

    "id": "mortys",

    "name": "Mortys",

    "lockout_phrase": "I'd better not leave the flat until Rick's awake, I don't have my keys.",

    "description":
    """A clean and tidy flat. In his room is his high end gaming computer hooked up to a large monitor which dominates the room (There's a reason you're friends with him). """,

    "exits":  {"north": "nbuilding", "west":"flat", "south": "starbucks", "east": "walkabout"},

    "items": [],

    "friends": [friend_morty]
}

room_taf = {

    "required_level": 4,

    "id": "taf",

    "name": "The Taf",

    "lockout_phrase": "I'd better not leave the flat until Rick's awake, I don't have my keys.",

    "description": """A relaxed bar atmosphere, a few students (Lizzy and Sarah) are drinking casually as Gunther the bartender wipes the bar. """,

    "exits":  {"east": "flat", "south":"arcade", "north": "talybont"},

    "items": [],

    "friends": [friend_bar_staff, friend_lizzy, friend_sarah]
}

room_pryzm = {

    "required_level": 4,

    "id": "pryzm",

    "name": "PRYZM",

    "description":
    """A totally different setting in the day, but mambo number 5 is playing as the place is being cleaned. A few friends (Bill and Mike) as well as the club rep, Joseph, are here. """,

    "exits": {"south": "mcdonalds", "west": "tutor"},

    "items": [],

    "friends": [friend_bill, friend_club_rep_pryzm, friend_mike]
}

room_kebab = {

    "required_level": 9,

    "id": "kebab",

    "name": "Kebab Shop",

    "lockout_phrase": "It seems the kebab shop is not open yet.",

    "description":
    """A greasy kebab shop, a couple of workers are there (Abdul and Greg) and there are some flyers on the table. """,

    "exits": {"east": "nbuilding", "west": "talybont", "south": "flat"},

    "items": [],

    "friends": [friend_kebab_worker_two, friend_kebab_worker_one]
}

room_summers = {

    "required_level": 10,

    "id": "summers",   

    "name": "Summer's Place",

    "lockout_phrase": "You knock at the door... but no one answers",

    "description":
    """ An arty room (she's an illustration student so..). There are paint brushes dottted about the place and pictures getting in the way. """,

    "exits": {"north": "flat","west":"arcade", "east": "starbucks"},

    "items": [],

    "friends": [friend_summer]
}


room_north_building = {

    "required_level": 4,

    "id": "nbuilding",

    "name": "The North Building",

    "description": "There isn't much of any interest here.",

    "exits": {"north":"tutor", "south": "mortys", "east": "mcdonalds", "west": "kebab"},

    "items": [],

    "friends": []

    

}

room_starbucks = {

    "required_level": 4,

    "id": "starbucks",

    "name": "Starbucks",

    "description": "A busy Starbucks, no one looks like they want to talk, best grab a coffee and get out of the way.",

    "exits": {"north":"mortys", "west": "summers", "east": "wetherspoons"},

    "items": [],

    "friends": [friend_barista]

}

room_arcade = {

    "required_level": 4,

    "id": "arcade",

    "name": "Arcade",

    "description": "There isn't much of any interest here, except a very old and dusty Nokia. Hmmm, I wonder if it still works..",

    "exits": {"north":"taf", "east": "summers"},

    "items": [],

    "friends": [friend_wilko_worker]

}

room_walkabout = {

    "required_level": 4,

    "id": "walkabout",

    "name": "Walkabout",

    "description": "A strange sight in the day, the club rep, James, stands there and greets you on your way in and is stopping you from looking around. ",

    "exits": {"west":"mortys", "north": "mcdonalds", "south": "wetherspoons"},

    "items": [],

    "friends": [friend_club_rep_walkabout]

}

room_personal_tutors_office = {

    "required_level": 4,

    "id": "tutor",

    "name": "Your personal Tutor's office",

    "description": "There isn't much of any interest here.",

    "exits": {"south":"nbuilding", "east": "pryzm"},

    "items": [],

    "friends": []

}

room_wetherspoons = {

    "required_level": 4,

    "id": "wetherspoons",

    "name": "Wetherspoons",

    "description": "Populated by people having lunch, and the occasional alcoholic, nobody you know is here. However there are some very nice looking glasses there that would be great for the flat...",

    "exits": {"north":"walkabout", "west": "starbucks"},

    "items": [],

    "friends": []

}

room_talybont = {

    "required_level": 4,

    "id": "talybont",

    "name": "Talybont",

    "description": "There isn't much of any interest here.",

    "exits": {"south":"taf", "east": "kebab"},

    "items": [],

    "friends": []


}

room_mcdonalds = {

    "required_level": 4,

    "id": "mcdonalds",

    "name": "McDonalds",

    "description": "An extremely busy area, Deborah, the manager, is here and may have been last night. ",

    "exits": {"north":"pryzm", "west": "nbuilding", "south": "walkabout"},

    "items": [],

    "friends": [friend_mcdonalds_worker]
}

room_bedroom = {

    "required_level": 12,

    "id": "bedroom",

    "name": "Bedroom",

    "lockout_phrase": "It's locked, I need my key to get in",


    "description": "A messy but cosy room. ",

    "exits": [],

    "items": [],

    "friends": []
    }

    

rooms = {
    "flat": room_flat,
    "mortys": room_mortys,
    "taf": room_taf,
    "pryzm": room_pryzm,
    "kebab": room_kebab,
    "summers": room_summers,
    "nbuilding": room_north_building,
    "starbucks": room_starbucks,
    "arcade": room_arcade,
    "walkabout": room_walkabout,
    "tutor": room_personal_tutors_office,
    "wetherspoons": room_wetherspoons,
    "talybont": room_talybont,
    "mcdonalds": room_mcdonalds,
    "bedroom": room_bedroom

}
