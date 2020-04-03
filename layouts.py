# # : Walls
# P : Player
# E : Enemy
# I : Item
# S : Stairs
# T : Trap
# O : Oject

LEVEL_SIZE = 10

ROOM_TAGS = {
    "WALL" : "#",
    "PLAYER" : "P",
    "ENEMY": "E",
    "ITEM": "I",
    "STAIRS": "S",
    "TRAP": "T",
    "OBJECT": "O",
    "FLOOR": " "
}

MM_TAGS = {
    "ROOM" : "#",
    "EMPTY" : " "
}

ROOMS = {
    "START":[
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        [" ", " ", " ", " ", "P", " ", " ", " ", " "],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"]
    ],
    "MIDDLE": [
        [
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"],
        ["#", "#", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", "#", " ", " ", " ", "#"],
        ["#", " ", " ", " ", "#", "#", " ", " ", "#"],
        [" ", " ", " ", " ", "#", " ", "#", " ", " "],
        ["#", " ", " ", " ", "#", " ", " ", " ", "#"],
        ["#", " ", " ", " ", "#", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"]
        ],
        [
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"],
        ["#", " ", " ", " ", " ", " ", "O", "O", "#"],
        ["#", " ", " ", "#", " ", " ", "E", "O", "#"],
        ["#", " ", " ", "#", " ", " ", " ", " ", "#"],
        [" ", " ", "I", "#", " ", " ", " ", " ", " "],
        ["#", " ", " ", "#", " ", " ", " ", " ", "#"],
        ["#", " ", " ", "#", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"]
        ],
        [
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"],
        ["#", "E", " ", " ", " ", " ", " ", "E", "#"],
        ["#", " ", " ", " ", "#", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        [" ", " ", " ", "#", "I", "#", " ", " ", " "],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", "#", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"]
        ],
        [
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"],
        ["#", " ", " ", " ", " ", " ", " ", "I", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", " ", "#", "#", "#", " ", " ", "#"],
        [" ", " ", " ", " ", "E", " ", " ", " ", " "],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", "I", " ", " ", " ", " ", " ", " ", "#"],
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"]
        ]
    ],

    "FINAL": [
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", "#", "#", "#", "#", "#", " ", "#"],
        ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
        [" ", " ", "#", " ", "#", " ", "#", " ", " "],
        ["#", " ", "#", " ", "#", "S", "#", " ", "#"],
        ["#", " ", "#", " ", "#", "#", "#", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"]
    ],
    
    "SIZE": 9
}