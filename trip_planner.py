def main():
    print("=== Welcome to the Road Trip Budget Planner ===\n")

    # --- User Inputs ---
    destination = input("Enter your destination: ")
    distance = float(input("Enter total distance in miles: "))
    mpg = float(input("Enter your car's fuel efficiency (MPG): "))
    gas_price = float(input("Enter current gas price per gallon ($): "))
    nights = int(input("Enter number of nights you'll stay: "))
    hotel_cost = float(input("Enter average hotel cost per night ($): "))
    food_budget = float(input("Enter daily food budget ($): "))

    # --- Calculations ---
    # Calculate gas requirements and costs
    gallons_needed = distance / mpg
    total_gas_cost = gallons_needed * gas_price
    
    # Calculate lodging and food costs
    total_hotel_cost = nights * hotel_cost
    # Food is calculated for (nights + 1) because a trip has one more day than nights spent
    total_food_cost = (nights + 1) * food_budget
    
    # Calculate overall grand total
    grand_total = total_gas_cost + total_hotel_cost + total_food_cost

    # --- Trip Summary Output ---
    print("\n" + "="*40)
    print(f" TRIP SUMMARY TO {destination.upper()} ")
    print("="*40)
    print(f"Total Distance: {distance:.1f} miles")
    print(f"Estimated Gas Needed: {gallons_needed:.2f} gallons")
    print("-"*40)
    print(f"Gas Cost: ${total_gas_cost:.2f}")
    print(f"Hotel Cost ({nights} nights): ${total_hotel_cost:.2f}")
    print(f"Food Cost ({nights + 1} days): ${total_food_cost:.2f}")
    print("-"*40)
    print(f"GRAND TOTAL BUDGET: ${grand_total:.2f}")
    print("="*40)

if __name__ == "__main__":
    main()
