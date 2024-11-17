import random

# Define creative bio components
categories = {
    "Career": [
        "Adventurous Foodie", "Creative Bookworm", "Sporty Entrepreneur", 
        "Compassionate Musician", "Tech-Savvy Gamer", "Travel Enthusiast", 
        "Dreamy Artist", "Curious Scientist", "Culinary Explorer", 
        "Fitness Enthusiast", "Movie Buff", "Passionate Teacher"
    ],
    "Lines": [
        "Globe-trotting architect with a passion for spicy food and sustainable design.",
        "Introverted writer with a love for classic literature and indie coffee shops.",
        "Energetic entrepreneur with a passion for fitness and outdoor adventures.",
        "Soulful musician with a heart for social justice and a love for live music.",
        "Software engineer by day, gamer by night.",
        "Part-time chef, full-time foodie on a mission to find the perfect croissant.",
        "Explorer of ideas, books, and places, with a knack for solving riddles.",
        "Dreamer by the ocean, innovator by the desk, and a dancer when no one's watching.",
        "Coffee addict with a penchant for technology and a love for deep conversations.",
        "Hiker with a camera and a playlist for every mood.",
        "Movie enthusiast with a knack for quoting obscure lines.",
        "Teacher who loves sharing knowledge and making people smile."
    ],
    "Interests": [
        "Cooking and traveling", "Fitness and yoga", "Music and literature", 
        "Gaming and technology", "Hiking and photography", "Dancing and baking",
        "Reading and solving puzzles", "Painting and exploring new cuisines", 
        "Writing and stargazing", "Surfing and playing the ukulele"
    ],
    "Relationship Goals": [
        "Finding a partner-in-crime", "Building a lifelong connection", 
        "Exploring life's adventures together", "Creating unforgettable memories", 
        "Chasing dreams hand-in-hand", "Laughing until we cry", 
        "Building something meaningful", "Sharing deep conversations and sunsets"
    ]
}

# Generate creative bios
def generate_creative_bios(num_bios=5000):
    bios = []
    for _ in range(num_bios):
        career = random.choice(categories["Career"])
        line = random.choice(categories["Lines"])
        interests = random.choice(categories["Interests"])
        goal = random.choice(categories["Relationship Goals"])

        bio = (
            f"- **{career}**\n\n"
            f"    \"{line} I'm passionate about {interests}. "
            f"Seeking someone who shares my enthusiasm for {goal}.\"\n"
        )
        bios.append(bio)
    return bios

# Save bios to a file
def save_creative_bios_to_file(filename, bios):
    with open(filename, "w", encoding="utf-8") as file:
        for bio in bios:
            file.write(bio + "\n")

# Generate and save bios
print("Generating creative Tinder-friendly bios... (this may take a moment)")
creative_bios = generate_creative_bios(10000)  # Adjust number for a larger/smaller dataset
save_creative_bios_to_file("bios.txt", creative_bios)
print("Creative bios have been successfully saved to 'bios.txt'.")
