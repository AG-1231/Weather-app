import random
 


LOCATIONS = {
    "1": {
        "label": "Burlington, Canada",
        "temp_range": (-5, 28),       
        "humidity_range": (50, 85),
        "wind_range": (10, 45),
        "conditions": ["clear sky", "partly cloudy", "overcast", "light rain", "snow", "drizzle"]
    },
    "2": {
        "label": "Toronto, Canada",
        "temp_range": (-8, 30),
        "humidity_range": (50, 85),
        "wind_range": (10, 50),
        "conditions": ["clear sky", "partly cloudy", "overcast", "light rain", "snow", "thunderstorm"]
    },
    "3": {
        "label": "India (New Delhi)",
        "temp_range": (10, 45),       
        "humidity_range": (20, 90),
        "wind_range": (5, 35),
        "conditions": ["clear sky", "mainly clear", "partly cloudy", "haze", "heavy rain", "thunderstorm"]
    },
    "4": {
        "label": "USA (New York)",
        "temp_range": (-5, 35),
        "humidity_range": (40, 80),
        "wind_range": (10, 55),
        "conditions": ["clear sky", "partly cloudy", "overcast", "light rain", "heavy rain", "snow"]
    },
    "5": {
        "label": "Antarctica",
        "temp_range": (-70, -10),     
        "humidity_range": (40, 70),
        "wind_range": (30, 150),      
        "conditions": ["clear sky", "blizzard", "heavy snow", "snow", "overcast", "freezing fog"]
    },
}
 
 
def generate_weather(location):
    """make up realistic weather numbers for a location"""
    temp       = round(random.uniform(*location["temp_range"]), 1)
    feels_like = round(temp + random.uniform(-4, 2), 1)   
    humidity   = random.randint(*location["humidity_range"])
    wind       = round(random.uniform(*location["wind_range"]), 1)
    condition  = random.choice(location["conditions"])
 
    return {
        "temp":       temp,
        "feels_like": feels_like,
        "humidity":   humidity,
        "wind":       wind,
        "condition":  condition,
    }
 
 
def print_weather(label, w):
    print("\n  " + "-" * 36)
    print(f"  {label}")
    print("  " + "-" * 36)
    print(f"  condition  :  {w['condition']}")
    print(f"  temp       :  {w['temp']}C")
    print(f"  feels like :  {w['feels_like']}C")
    print(f"  humidity   :  {w['humidity']}%")
    print(f"  wind       :  {w['wind']} km/h")
 
 
def show_all():
    print("\n  generating weather for all locations...\n")
    for loc in LOCATIONS.values():
        weather = generate_weather(loc)
        print_weather(loc["label"], weather)
    print("\n  " + "-" * 36 + "\n")
 
 
def show_one():
    print("\n  pick a location:")
    for key, loc in LOCATIONS.items():
        print(f"  {key}. {loc['label']}")
 
    choice = input("\n  pick: ").strip()
 
    if choice not in LOCATIONS:
        print("  that's not a valid option\n")
        return
 
    loc = LOCATIONS[choice]
    weather = generate_weather(loc)
    print_weather(loc["label"], weather)
    print()
 
 
def main():
    print("\n  weather app")
    print("  realistic random weather, no internet needed\n")
 
    while True:
        print("  what do you want to do?")
        print("  1. show weather for all 5 locations")
        print("  2. pick one location")
        print("  3. quit")
 
        choice = input("\n  pick: ").strip()
 
        if choice == "1":
            show_all()
        elif choice == "2":
            show_one()
        elif choice in ("3", "q", "quit", "exit"):
            print("\n  bye!\n")
            break
        else:
            print("  pick 1, 2, or 3\n")
 
 
if __name__ == "__main__":
    main()
