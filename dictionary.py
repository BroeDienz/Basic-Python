users = {
    "user1": {"name": "bayu", "age": 24, "tag": []},
    "user2": {"name": "erwin", "age": 35, "tag": []},
    "user3": {"name": "joko", "age": 45, "tag": []},
    "user4": {"name": "udin", "age": 45, "tag": []},
    "user5": {"name": "ogi", "age": 10, "tag": []},
    "user6": {"name": "aulia", "age": 10, "tag": []},
    "user7": {"name": "reviano", "age": 7, "tag": []},
    "user8": {"name": "angel", "age": 22, "tag": []},
    "user9": {"name": "april", "age": 60, "tag": []},
    "user10": {"name": "caca", "age": 17, "tag": []},
    "user11": {"name": "drembis", "age": 109, "tag": []},
    "user12": {"name": "dalimo", "age": 66, "tag": []},
}

tag = ["developer", "player", "miner"]

def tambah_tag_ke_user(users, tag):
    for user in users.values():
        user["tag"].extend(tag)
    
print(users)

