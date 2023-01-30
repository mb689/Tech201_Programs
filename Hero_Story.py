story1 = {
    "Start": "Clark Kent was a normal young man, until he discovered he had incredible powers including super strength, flight and heat vision.",
    "Middle": "Clark struggled with the weight of his powers and the responsibility that came with them, but after saving a group of people from a burning building, he knew he had to use his abilities for good. He created a secret identity as Superman and used his powers to fight against evil and protect the world.",
    "End": "Superman becomes a beacon of hope and a symbol of truth, justice, and the American way. Despite the challenges he faces, he remains dedicated to his mission, always putting others before himself and working to make the world a better place. He continues to fly high, protecting the innocent and fighting for what is right."
}

print(story1.items())
print(type(story1))
print(story1.keys())
print(story1.values())
print(story1["Start"])
print(story1["Middle"])
print(story1["End"])
story1["Heros"] = "SuperHero"
print(story1)