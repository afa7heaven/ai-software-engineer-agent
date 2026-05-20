import json

def save_memory(data):
    try:
        with open("memory.json", "r") as f:
            memory = json.load(f)
    except:
        memory = []

    memory.append(data)

    with open("memory.json", "w") as f:
        json.dump(memory, f)

def get_memory():
    try:
        with open("memory.json", "r") as f:
            memory = json.load(f)
        return "\n".join(memory[-10:])
    except:
        return ""
