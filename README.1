# Hostel Electricity & Appliance Tracker

## Overview
A menu-driven Python command-line application that helps hostel residents record the electrical appliances in their room, estimate daily and monthly energy consumption (kWh), calculate the expected electricity bill, find the highest-consuming appliance, and receive personalised energy-saving tips. All data is stored locally in a JSON file, so no database or internet connection is needed.

## Features
- **Appliance management (CRUD)** – add, view, edit and remove appliances (name, wattage, daily usage hours, quantity).
- **Consumption and bill estimation** – per-appliance and total daily/monthly kWh and cost, based on a 30-day month and a configurable rate per unit.
- **Highest-consuming appliance** – identifies the biggest energy user with its share of the total bill.
- **Configurable tariff** – change the rate per unit at any time (default 7.0 per kWh).
- **Energy-saving report** – top three consumers, appliance-specific tips (fan, tv, heater, ac, etc.) and a "quick win" showing the saving from using the top appliance one hour less per day.
- **Validated input** – non-numeric, zero, negative and out-of-range values (e.g. more than 24 hours/day) are rejected and re-prompted.
- **Persistent storage** – changes are saved instantly to `data.json`; a missing or corrupt file falls back to safe defaults.

## Technologies / Tools Used
- Python 3.8+ (standard library only: `json`, `os`)
- JSON for data storage
- `unittest` for validation tests
- Git / GitHub for version control

## Project Structure
```
.
├── main.py           # Entry point and menu loop
├── appliances.py     # Add / list / edit / remove appliances
├── calculations.py   # kWh and bill calculations
├── consumption.py    # Consumption and bill display
├── top_consumer.py   # Highest-consuming appliance
├── report.py         # Energy-saving report and tips
├── settings.py       # Set electricity rate
├── inputs.py         # Validated numeric input helpers
├── storage.py        # Load / save JSON data
├── config.py         # Constants (data file path, days in month, default rate)
├── data.json         # Persistent data store
├── tests/
│   └── test_calculations.py
├── README.md
└── statement.md
```

## Installation and Running
1. Install Python 3.8 or newer (`python --version` to check).
2. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd <repository-folder>
   ```
3. No third-party packages are needed.
4. Run the application:
   ```bash
   python main.py
   ```
5. Choose an option (0–8) from the menu.

## Usage
| Option | Action |
|--------|--------|
| 1 | Add appliance |
| 2 | View appliances |
| 3 | Edit appliance |
| 4 | Remove appliance |
| 5 | Daily & monthly consumption / bill |
| 6 | Highest-consuming appliance |
| 7 | Set electricity rate |
| 8 | Energy-saving report |
| 0 | Exit |

**Formula:** `daily kWh = wattage × hours per day × quantity ÷ 1000`; `monthly kWh = daily kWh × 30`; `bill = monthly kWh × rate`.

## Testing
Run the automated validation tests from the project root:
```bash
python -m unittest discover -s tests -v
```
The tests cover the kWh/bill calculations, input validation (`ask_float`, `ask_int`) and storage (missing file, round-trip save/load, corrupt file recovery).

Suggested manual checks:
1. Add a 100 W fan used 24 h/day → option 5 should show 2.40 kWh/day and 72.00 kWh/month.
2. Enter `abc`, `0` or `30` for hours → the app should reject each and re-prompt.
3. Delete or corrupt `data.json` and restart → the app starts with an empty list and the default rate.
4. Set the rate to 8 (option 7) → the bill in option 5 updates accordingly.

## Sample Output
```
--- Consumption (30-day month, rate 7/unit) ---
Appliance           Daily kWh  Monthly kWh       Cost
Fan                      2.40        72.00     504.00
fan x2                  24.43       732.96    5130.72
fan x3                   3.60       108.00     756.00
tv                       0.40        12.00      84.00
-----------------------------------------------------
TOTAL                   30.83       924.96    6474.72
```
(Add your own terminal screenshots in a `screenshots/` folder and link them here.)

## Author
Your Name – Reg. No. – VITyarthi Build Your Own Project
