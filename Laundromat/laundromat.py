import datetime as dt

# main menu layout
def menu():
    print()
    print("========== FreshFold Laundromat ==========")
    print(" W - Wash Only\n D - Dry Only\n B - Both (wash, then dry) - 5% discount \n Q - Close shop")
    print(" ==========================================")
    print()

def optional_extras():
    """Asks user for optional detergent and softener preferences."""
    while True:
        detergent = input("Do you want Detergent ? (Y/N): ").strip().upper()
        if detergent == "Y":
            supply_of_detergent = input("Will you use your own detergent ? (Y/N): ").strip().upper()
            break  
        elif detergent == "N":
            print("No detergent selected.")
            supply_of_detergent = None
            break 
        else:
            print("Enter a valid option (Y/N)") 

    while True:
        softner = input("Do you want softner ? (Y/N): ").strip().upper()
        if softner == "Y":
            supply_of_softner = input("Will you use your own softner ? (Y/N): ").strip().upper()
            break  
        elif softner == "N":
            print("No softner selected.")
            supply_of_softner = None
            break  
        else:
            print("Enter a valid option (Y/N)")    
            
    return detergent, supply_of_detergent, softner, supply_of_softner  

def washing():          #determining the washing machine
    washing_machine_load1 = 0
    washing_machine_load2 = 0
    washing_machine_load3 = 0
     
    if customer_wash_load <= 5:
        print("Assigned : washing machine 1")
        print("--- Washing machine 1 started ---\nWasher 1: Washing   40 min remaining\nWasher 1: Washing   30 min remaining\nWasher 1: Rinsing   20 min remaining\nWasher 1: Spinning   10 min remaining\nWasher 1: Done!\n")
        washing_machine_load1 += 1
        #return washing_machine_load1

    elif customer_wash_load > 5 and customer_wash_load <= 8:
        print("Assigned : washing machine 2")
        print("--- Washing machine 2 started ---\nWasher 2: Washing   40 min remaining\nWasher 2: Washing   30 min remaining\nWasher 2: Rinsing   20 min remaining\nWasher 2: Spinning   10 min remaining\nWasher 2: Done!\n")
        washing_machine_load2 += 1
        #return washing_machine_load2
        
    elif customer_wash_load > 8 and customer_wash_load <= 12:
        print("Assigned : washing machine 3")
        print("--- Washing machine 3 started ---\nWasher 3: Washing   40 min remaining\nWasher 3: Washing   30 min remaining\nWasher 3: Rinsing   20 min remaining\nWasher 3: Spinning   10 min remaining\nWasher 3: Done!\n")
        washing_machine_load3 += 1
        #return washing_machine_load3
    
    else:
        print("washing load not catered for !!!")

    return washing_machine_load1, washing_machine_load2, washing_machine_load3

def drying():     # determining the drying machine
    dryer_load1 = 0
    dryer_load2 = 0
    dryer_load3 = 0
     
    if customer_dry_load <= 6:
        print("Assigned : Dryer 1")
        print("--- Dryer 1 started ---\nDryer 1: Drying 30 min remaining\nDryer 1: Drying 20 min remaining\nDryer 1: Drying 10 min remaining\nDryer 1: Done!\n")
        dryer_load1 += 1
        #return dryer_load1

    elif customer_dry_load > 6 and customer_dry_load <= 10:
        print("Assigned : Dryer 2")
        print("--- Dryer 2 started ---\nDryer 2: Drying 30 min remaining\nDryer 2: Drying 20 min remaining\nDryer 2: Drying 10 min remaining\nDryer 2: Done!\n")
        dryer_load2 += 1
        #return dryer_load2

    elif customer_dry_load > 10 and customer_dry_load <= 14:
        print("Assigned : Dryer 3")
        print("--- Dryer 3 started ---\nDryer 3: Drying 30 min remaining\nDryer 3: Drying 20 min remaining\nDryer 3: Drying 10 min remaining\nDryer 3: Done!\n")
        dryer_load3 += 1
        #return dryer_load3

    else:
        print("drying load not catered for !!!")

    return dryer_load1, dryer_load2, dryer_load3       

# calculates prive for receipt
def price_generator():
    washing_rate = 12.00
    drying_rate = 8.00
    detergent_supplied = 2.50
    softner_supplied = 3.00

    subtotal = 0
    total_revenue = 0.0

    # --- Choice W: Wash Only ---
    if choice == "W":
        wash_total = customer_wash_load * washing_rate
        print(f"Washing         R {wash_total:7.2f}")
        subtotal += wash_total

        if detergent == "Y":
            if supply_of_detergent == "N":  # 'N' means using shop detergent
                det_total = customer_wash_load * detergent_supplied
                print(f"Detergent       R {det_total:7.2f}")
                subtotal += det_total

        if softner == "Y":
            if supply_of_softner == "N":    # 'N' means using shop softener
                soft_total = customer_wash_load * softner_supplied
                print(f"Softener        R {soft_total:7.2f}")
                subtotal += soft_total
                
        print("-" * 31)
        print(f"TOTAL           R {subtotal:7.2f}")

    # --- Choice D: Dry Only ---
    if choice == "D":
        dry_total = customer_dry_load * drying_rate
        print(f"Drying          R {dry_total:7.2f}")
        subtotal += dry_total
        print("-" * 31)
        print(f"TOTAL           R {subtotal:7.2f}")

    # --- Choice B: Both (Wash and Dry) with 5% Discount ---
    if choice == "B":
        wash_total = customer_wash_load * washing_rate
        dry_total = customer_dry_load * drying_rate
        print(f"Washing         R {wash_total:7.2f}")
        print(f"Drying          R {dry_total:7.2f}")
        subtotal += (wash_total + dry_total)

        if detergent == "Y":
            if supply_of_detergent == "N":
                det_total = customer_wash_load * detergent_supplied
                print(f"Detergent       R {det_total:7.2f}")
                subtotal += det_total

        if softner == "Y":
            if supply_of_softner == "N":
                soft_total = customer_wash_load * softner_supplied
                print(f"Softener        R {soft_total:7.2f}")
                subtotal += soft_total

    if choice == "W" or choice == "D":
        total_revenue = subtotal


        # Calculate 5% discount for choosing both
        discount = subtotal * 0.05
        final_total = subtotal - discount
        

        
        print(f"Discount (5%)  -R {discount:7.2f}")
        print("-" * 31)
        print(f"TOTAL           R {final_total:7.2f}")

        return total_revenue

        

def receipt():
    customers_served = 0
    total_Kg = 0.0
    total_revenue = 0.0

    current_date = dt.date.today().strftime("%d %B %Y")
    print("========== RECEIPT ==========")
    print(f"FreshFold Laundromat    {current_date}")
    
    if choice == "W":
        print(f"Service: Wash only    Load: {customer_wash_load} kg")
    elif choice == "D":
        print(f"Service: Dry only     Load: {customer_dry_load} kg")
    elif choice == "B":
        print(f"Service: Wash and Dry Load: {customer_wash_load} kg")
        
    print("-" * 31)
    total_revenue = price_generator()

    print("=============================")
    print("Thank you for using FreshFold!\n")

    """Added"""
    customers_served += 1
    

    if choice == "W":
        total_Kg += customer_wash_load
    elif choice == "D":
        total_Kg += customer_dry_load
    elif choice == "B":
        total_Kg += (customer_wash_load + customer_dry_load)

    return customers_served, total_Kg, total_revenue

    """Added"""
def report():
    print("\n========== Daily Report ==========")
    print()
    print(f"Customers served: {customers_served}")
    print(f"Total kg processed: {total_Kg:.2f} kg")
    print(f"Total revenue: R{total_revenue:.2f}")

    print("\n------ Washing Machine Loads -------")
    print(f"Washing Machine 1: {washing_machine_load1}")
    print(f"Washing Machine 2: {washing_machine_load2}")
    print(f"Washing Machine 3: {washing_machine_load3}")

    print("\n---------- Dryer Loads ------------")
    print(f"Dryer 1: {dryer_load1}")
    print(f"Dryer 2: {dryer_load2}")
    print(f"Dryer 3: {dryer_load3}")
    print("\n===================================")
    print("FreshFold Closed!")

# --- Main Loop ---
while True:
    menu()
    choice = input("Choose a service [W, D, B, or Q]: ").upper().strip()
    try:
        if choice == "W":
            while True:
                customer_wash_load = float(input("Enter load for washing in Kg (max 12 Kg): "))
                if customer_wash_load <= 12:
                    break
                else:
                    print("Enter a load appropriate to the maximum capacity")
            
            # calls variables inside defined function into main environment
            detergent, supply_of_detergent, softner, supply_of_softner = optional_extras()
            washing_machine_load1, washing_machine_load2, washing_machine_load3 = washing()
            customers_served, total_Kg, total_revenue = receipt()
            report()

        elif choice == "D":
            while True:
                customer_dry_load = float(input("Enter load for drying in Kg (max 14 Kg): "))
                if customer_dry_load <= 14:
                    break
                else:
                    print("Enter a load appropriate to the maximum capacity")
            dryer_load1, dryer_load2, dryer_load3 = drying()
            customers_served, total_Kg, total_revenue = receipt()
            report()

        elif choice == "B":
            while True:
                customer_wash_load = float(input("Enter load for washing in Kg (max 12 Kg): "))
                if customer_wash_load <= 12:
                    break
                else:
                    print("Enter a load appropriate to the maximum capacity")            
            while True:
                customer_dry_load = float(input("Enter load for drying in Kg (max 14 Kg): "))
                if customer_dry_load <= 14:
                    break
                else:
                    print("Enter a load appropriate to the maximum capacity")
                    
            detergent, supply_of_detergent, softner, supply_of_softner = optional_extras()
            washing_machine_load1, washing_machine_load2, washing_machine_load3 = washing()
            dryer_load1, dryer_load2, dryer_load3 = drying()
            customers_served, total_Kg, total_revenue = receipt()
            report()

        elif choice == "Q":
            print("Shop closed. Goodbye!")
            break
        else:
            print("Invalid choice. Please select W, D, B, or Q.")
    except ValueError:
        print("Invalid choice or load. Please enter a valid number.")