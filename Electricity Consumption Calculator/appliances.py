from inputs import ask_float, ask_int
from storage import save_data


def add_appliance(data):
    print("\n--- Add Appliance ---")
    name = input("Appliance name (e.g. Fan): ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    wattage = ask_float("Wattage (W): ")
    hours = ask_float("Daily usage (hours, max 24): ", max_val=24)
    qty = 1
    if input("More than one of these? (y/N): ").strip().lower() == "y":
        qty = ask_int("Quantity: ")
    data["appliances"].append(
        {"name": name, "wattage": wattage, "hours_per_day": hours, "quantity": qty}
    )
    save_data(data)
    print(f"Added {name}.")


def list_appliances(data):
    if not data["appliances"]:
        print("\nNo appliances added yet.")
        return False
    print("\n--- Appliances ---")
    print(f"{'#':<3} {'Name':<18} {'Watts':>7} {'Hrs/day':>8} {'Qty':>4}")
    for i, a in enumerate(data["appliances"], 1):
        print(f"{i:<3} {a['name']:<18} {a['wattage']:>7g} "
              f"{a['hours_per_day']:>8g} {a.get('quantity', 1):>4}")
    return True


def edit_appliance(data):
    if not list_appliances(data):
        return
    idx = ask_int("Number to edit (0 to cancel): ", min_val=0,
                  max_val=len(data["appliances"]))
    if idx == 0:
        return
    a = data["appliances"][idx - 1]
    print("Press Enter to keep the current value.")

    name = input(f"Name [{a['name']}]: ").strip()
    if name:
        a["name"] = name

    w = input(f"Wattage [{a['wattage']:g}]: ").strip()
    if w:
        try:
            if float(w) > 0:
                a["wattage"] = float(w)
            else:
                print("  Wattage must be positive, kept old value.")
        except ValueError:
            print("  Invalid wattage, kept old value.")

    h = input(f"Hours/day [{a['hours_per_day']:g}]: ").strip()
    if h:
        try:
            if 0 < float(h) <= 24:
                a["hours_per_day"] = float(h)
            else:
                print("  Hours must be between 0 and 24, kept old value.")
        except ValueError:
            print("  Invalid hours, kept old value.")

    save_data(data)
    print("Updated.")


def remove_appliance(data):
    if not list_appliances(data):
        return
    idx = ask_int("Number to remove (0 to cancel): ", min_val=0,
                  max_val=len(data["appliances"]))
    if idx == 0:
        return
    removed = data["appliances"].pop(idx - 1)
    save_data(data)
    print(f"Removed {removed['name']}.")
