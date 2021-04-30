```
sports - directory
    games - directory
        __init__.py
        game.py - Python class Game
            attribute 1 - name 
            attribute 2 - date (datetime.datetime)
            def __init__(.... name, date)
            def __str__
    players - directory
        __init__.py
        player.py - Python class Player
            attribute 1 - name 
            attribute 2 - age
            def __str__
    play.py 
        import Game class  [from games/__init__.py and also games/game.py]
        import Player  class [from players/__init__.py and also players/player.py]

        new Game
        new Player

        print game object 
        print player object 
```
