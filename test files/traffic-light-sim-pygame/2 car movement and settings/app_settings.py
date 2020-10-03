




shift=50

directions=["south","east","north","west"]

locations={
    "north":(shift+250,shift+0),
    "west":(shift+0,shift+250),
    "south":(shift+250,shift+500),
    "east":(shift+500,shift+250)
    }




# settings used in app.py
carmovepersecond=1

mincargen=0

maxcargen=25



# settings used in Car.py

carsize = 40


setcaracc=False
caracc=1

setcarvel=True
carvel=2


# settings used in Light.py

defaultyellowlighttime=2

defaultgreenlighttime=10


useautocar=True

carcountsettings= [

    {
        "mincars":20,
        "yellow":5,
        "green":10
    },

    {
        "mincars":10,
        "yellow":2,
        "green":5
    },

    {
        "mincars":5,
        "yellow":2,
        "green":5
    },

    {
        "mincars":0,
        "yellow":2,
        "green":5
    }

    ]




