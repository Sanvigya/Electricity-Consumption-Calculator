from inputs import ask_float
from storage import save_data


def set_rate(data):
    print(f"\nCurrent rate: {data['rate_per_unit']:g} per unit (kWh)")
    data["rate_per_unit"] = ask_float("New rate per unit: ")
    save_data(data)
    print("Rate updated.")
