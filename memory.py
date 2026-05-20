import json
import os

MEMORY_FILE = "memory.json"

def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)

    except:
        return []

def save_memory(data):

    memory = load_memory()

    memory.append(data)

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f)

def get_memory():

    memory = load_memory()

    return "\n".join(memory[-10:])
