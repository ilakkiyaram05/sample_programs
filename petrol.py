def tour(petrol, distance):
    start = 0
    current_petrol = 0
    total_petrol = 0
    
    for i in range(len(petrol)):
        net_fuel = petrol[i] - distance[i]
        current_petrol += net_fuel
        total_petrol += net_fuel
        
        if current_petrol < 0:
            start = i + 1
            current_petrol = 0
    return start if total_petrol >= 0 else -1
  
def main():
    print("--- Circular Petrol Pump Tour ---")
    try:
        petrol_input = input("Enter petrol at each pump (separated by spaces): ")
        petrol = [int(x) for x in petrol_input.split()]
        distance_input = input("Enter distance to next pump (separated by spaces): ")
        distance = [int(x) for x in distance_input.split()]
        if len(petrol) != len(distance) or len(petrol) == 0:
            print("Error: The number of petrol and distance values must match and cannot be empty.")
            return
        result = tour(petrol, distance)
        if result != -1:
            print(f"\nSuccess! Start at petrol pump index: {result}")
        else:
            print("\nResult: -1 (It is impossible to complete the circle from any pump.)")
    except ValueError:
        print("Error: Please enter only valid integers separated by spaces.")
if __name__ == "__main__":
    main()
