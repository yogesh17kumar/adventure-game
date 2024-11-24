import streamlit as st

# Title of the game
st.title("The Mystical Forest Adventure")

# Define the extended story structure
story = {
    "start": {
        "text": (
            "You wake up in a dark forest with no memory of how you got there. "
            "You see two paths ahead:\n\n"
            "1. A well-trodden path leading towards faint lights.\n"
            "2. A narrow trail that disappears into the dense forest."
        ),
        "choices": {
            "1": "village",
            "2": "forest",
        },
    },
    "village": {
        "text": (
            "You follow the well-trodden path and arrive at a small village. "
            "The villagers seem wary of strangers but an old man offers to help. He gives you two options:\n\n"
            "1. Rest at his house.\n"
            "2. Visit the village elder for advice on your journey."
        ),
        "choices": {
            "1": "rest",
            "2": "elder",
        },
    },
    "forest": {
        "text": (
            "You venture into the dense forest. It's eerily quiet. Suddenly, you hear a growl behind you. "
            "Do you:\n\n"
            "1. Run as fast as you can.\n"
            "2. Turn around and face the source of the growl.\n"
            "3. Climb a nearby tree to hide."
        ),
        "choices": {
            "1": "run",
            "2": "face_beast",
            "3": "hide_tree",
        },
    },
    "rest": {
        "text": (
            "You rest at the old man's house and wake up feeling refreshed. "
            "He gives you a map to the treasure and warns of dangerous creatures ahead. "
            "Do you:\n\n"
            "1. Follow the map through the mountain pass.\n"
            "2. Take the longer but safer route along the river."
        ),
        "choices": {
            "1": "mountain_pass",
            "2": "river_route",
        },
    },
    "elder": {
        "text": (
            "The village elder tells you of a hidden cave that holds a powerful artifact. "
            "He warns that the cave is guarded by puzzles and traps. "
            "Do you:\n\n"
            "1. Head to the cave and try your luck.\n"
            "2. Ignore the elder's advice and explore the forest instead."
        ),
        "choices": {
            "1": "cave",
            "2": "forest",
        },
    },
    "run": {
        "text": "You stumble and fall. The growling creature catches up to you. Game over!",
        "choices": {},
    },
    "face_beast": {
        "text": (
            "You stand your ground and the beast retreats, revealing a hidden cave. "
            "Do you:\n\n"
            "1. Enter the cave to search for treasure.\n"
            "2. Continue deeper into the forest."
        ),
        "choices": {
            "1": "cave",
            "2": "deeper_forest",
        },
    },
    "hide_tree": {
        "text": (
            "You climb a tree and watch as the beast prowls below. After some time, it leaves. "
            "You notice a distant mountain glowing in the moonlight. "
            "Do you:\n\n"
            "1. Head towards the glowing mountain.\n"
            "2. Wait until morning to safely climb down and return to the path."
        ),
        "choices": {
            "1": "mountain_pass",
            "2": "forest_path",
        },
    },
    "mountain_pass": {
        "text": (
            "You brave the treacherous mountain pass. Along the way, you find an abandoned hut. "
            "Inside, there is a chest and a strange map. "
            "Do you:\n\n"
            "1. Open the chest.\n"
            "2. Examine the map carefully."
        ),
        "choices": {
            "1": "trap_chest",
            "2": "treasure_map",
        },
    },
    "river_route": {
        "text": (
            "You follow the river and find a boat. However, it looks unstable. "
            "Do you:\n\n"
            "1. Use the boat to cross the river.\n"
            "2. Build a raft using nearby materials."
        ),
        "choices": {
            "1": "unstable_boat",
            "2": "raft_crossing",
        },
    },
    "cave": {
        "text": (
            "You enter the cave and face a series of puzzles. You solve them and find a golden chest. "
            "Do you:\n\n"
            "1. Open the chest.\n"
            "2. Leave the cave and continue exploring."
        ),
        "choices": {
            "1": "golden_chest",
            "2": "forest_path",
        },
    },
    "deeper_forest": {
        "text": "You lose your way in the forest and are never seen again. Game over!",
        "choices": {},
    },
    "trap_chest": {
        "text": "The chest was booby-trapped! Poisonous gas fills the hut. Game over!",
        "choices": {},
    },
    "treasure_map": {
        "text": "The map leads you to a hidden valley filled with gold. You win!",
        "choices": {},
    },
    "unstable_boat": {
        "text": "The boat capsizes halfway. You couldn't survive. Game over!",
        "choices": {},
    },
    "raft_crossing": {
        "text": "You successfully cross the river and find a treasure chest hidden under a tree. You win!",
        "choices": {},
    },
    "golden_chest": {
        "text": "The chest contains the artifact of legends. You are hailed as a hero. You win!",
        "choices": {},
    },
    "forest_path": {
        "text": "You safely return to the forest path but find no treasure. The adventure ends. Game over!",
        "choices": {},
    },
}

# Initialize game state
if "current_node" not in st.session_state:
    st.session_state.current_node = "start"

# Display the current part of the story
current_node = st.session_state.current_node
st.markdown(f"### {story[current_node]['text']}")

# Display choices if available
if story[current_node]["choices"]:
    for choice, next_node in story[current_node]["choices"].items():
        # Use unique keys for each button
        if st.button(f"Choice {choice}", key=f"{current_node}_{choice}"):
            st.session_state.current_node = next_node
            st.rerun()
else:
    # Game over or win
    if st.button("Restart Game"):
        st.session_state.current_node = "start"
        st.rerun()
