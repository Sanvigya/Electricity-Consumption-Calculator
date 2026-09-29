from appliances import add_appliance, edit_appliance, list_appliances, remove_appliance
from consumption import show_consumption
from report import energy_saving_report
from settings import set_rate
from storage import load_data
from top_consumer import show_top_consumer

MENU = """
===== Hostel Electricity & Appliance Tracker =====
1. Add appliance
2. View appliances
3. Edit appliance
4. Remove appliance
5. Daily & monthly consumption / bill
6. Highest-consuming appliance
7. Set electricity rate
8. Energy-saving report
0. Exit
"""

ACTIONS = {
    "1": add_appliance,
    "2": list_appliances,
    "3": edit_appliance,
    "4": remove_appliance,
    "5": show_consumption,
    "6": show_top_consumer,
    "7": set_rate,
    "8": energy_saving_report,
}


def main():
    data = load_data()
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        action = ACTIONS.get(choice)
        if action:
            action(data)
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
