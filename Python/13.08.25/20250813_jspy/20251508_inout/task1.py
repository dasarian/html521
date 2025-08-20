def calculate_flight_time():
    speed_str = input("Enter plane speed (km/h): ")
    city1 = input("Enter departure city: ")
    city2 = input("Enter arrival city: ")
    distance_str = input(f"Enter distance between {city1} and {city2} (km): ")
    
    speed = float(speed_str)
    distance = float(distance_str)
    
    time_hours = distance / speed
    
    hours = time_hours // 1
    minutes = (time_hours % 1) * 60
    
    print(f"\nFlight time from {city1} to {city2}:")
    print(f"{hours:.0f} hours {minutes:.0f} minutes")

calculate_flight_time()