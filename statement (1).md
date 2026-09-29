# Problem Statement – Hostel Electricity & Appliance Tracker

## 1. Background
Hostel life depends heavily on electrical appliances. A typical room has one or more fans, a laptop, a phone charger, a table lamp or tube light, and often a kettle, an iron, a small heater, a cooler or a television. Electricity in hostels is usually billed on a monthly basis, either through a shared meter, a room-level meter or a fixed charge that is periodically revised. Residents see the total only after the month ends, and the bill gives no breakdown of *which* appliance caused *how much* of the cost.

Because of this, most students rely on guesswork. A high-wattage appliance that runs for a few hours can quietly use more energy than several small devices combined, yet nothing in the daily routine makes this visible. The result is avoidable wastage, unexpected bills, and disputes between roommates about who is responsible for the cost.

## 2. Problem Statement
Hostel students have no simple way to understand how much electricity each of their appliances consumes, what it costs, and how usage could be reduced. Existing options are unsuitable:

- **Manual calculation** (wattage × hours ÷ 1000 × tariff) is tedious, repetitive and error-prone, especially when several appliances and quantities are involved.
- **Spreadsheets** require setup and formula knowledge, and are not designed to give advice.
- **Smart meters and energy-monitoring plugs** are costly and are not permitted or practical in most hostels.
- **Generic energy-saving advice** ("switch off lights") does not tell a student which of *their own* appliances matters most.

There is therefore a need for a simple, free, offline tool that lets a student record the appliances in a room, instantly calculates daily and monthly consumption and the expected bill, identifies the biggest energy consumer, and gives targeted suggestions with a quantified saving.

## 3. Motivation
- **Awareness:** People cut usage only when they can see the numbers. Turning invisible consumption into a clear table changes behaviour.
- **Cost control:** Students manage tight budgets; even small reductions in fan, heater or iron usage add up over a semester.
- **Fair cost sharing:** A per-appliance breakdown helps roommates split costs on facts rather than assumptions.
- **Sustainability:** Reducing wasted electricity lowers the hostel's overall energy demand and carbon footprint.
- **Academic value:** The problem is small enough to implement completely yet rich enough to demonstrate modular design, validation, persistence, reporting and testing.

## 4. Objectives
1. Provide a menu-driven tool to record appliances with name, wattage, daily usage hours and quantity.
2. Support complete data management: add, view, edit and remove appliances.
3. Calculate daily and monthly energy consumption in kWh and the estimated cost using a configurable rate per unit.
4. Identify the highest-consuming appliance and show its share of total consumption.
5. Generate an energy-saving report with appliance-specific tips and a quantified "quick win".
6. Validate every input so that invalid values never corrupt data or crash the program.
7. Persist data between sessions and recover gracefully from a missing or corrupt data file.
8. Keep the code modular, readable and testable, using only the Python standard library.

## 5. Scope of the Project

### 5.1 In Scope
- **Appliance management (CRUD):** adding appliances with name, wattage (W), usage hours per day (up to 24) and optional quantity; listing them in a formatted table; editing any field while keeping existing values on Enter; removing an appliance by its list number.
- **Consumption calculation:** daily kWh = wattage × hours × quantity ÷ 1000; monthly kWh = daily kWh × 30; cost = monthly kWh × rate per unit.
- **Bill estimation:** per-appliance and total daily/monthly consumption and cost, plus estimated daily cost and monthly bill.
- **Highest-consumer analysis:** the appliance with the largest monthly consumption, its kWh, percentage share and cost.
- **Tariff settings:** a user-configurable rate per unit (default 7.0) that is stored and reused.
- **Energy-saving report:** total consumption summary, top three consumers with percentage shares, keyword-matched tips (e.g. fan, tv, heater, geyser, iron, ac, cooler, light, bulb, tube, charger, laptop, kettle, fridge, monitor) and a "use it one hour less per day" saving estimate.
- **Input validation and error handling:** rejection of text, zero, negative and out-of-range values, with clear messages and re-prompting.
- **Local persistence:** automatic saving to a JSON file after every change.
- **Testing:** unit and validation tests for calculations, input helpers and storage.

### 5.2 Out of Scope
- Real-time metering or integration with smart meters and IoT plugs.
- Slab-based (tiered) tariffs, fixed charges, taxes and surcharges; a single flat rate is assumed.
- User accounts, authentication and multi-user or multi-room management.
- Cloud storage, synchronisation across devices, or a database server.
- A graphical, web or mobile interface (the current version is a command-line application).
- Automatic detection of appliance wattage or usage patterns.

## 6. Assumptions and Constraints
- Appliances are assumed to draw their rated wattage for the entire time they are on; real consumption may vary with load (for example a fan at low speed or a cooling appliance cycling on and off).
- A month is taken as **30 days** for all calculations.
- The electricity rate is a single flat value per unit (kWh) entered by the user.
- Usage hours per day are averages and must lie between 0 (exclusive) and 24.
- The program is single-user and runs locally on a computer with Python 3.8 or newer.
- The results are **estimates** intended for awareness and planning, not a replacement for the official bill.

## 7. Target Users
| User group | Need | How the tool helps |
|------------|------|--------------------|
| Hostel students | Understand and reduce their own electricity use and bill | Shows the cost of each appliance and gives personalised tips |
| Roommates / shared rooms | Split electricity costs fairly | Provides a transparent per-appliance breakdown with quantities |
| PG and home residents | Quick appliance-level estimate without special equipment | Works offline with no installation beyond Python |
| Hostel wardens / administrators (indirect) | Encourage responsible energy use | Can share the tool as an awareness aid |
| Students and beginners in programming | A clear example of a modular Python project | Small, readable, well-structured codebase |

## 8. High-Level Features
1. **Add Appliance** – guided prompts with validation; quantity asked only when more than one unit exists.
2. **View Appliances** – neatly aligned table showing number, name, watts, hours per day and quantity.
3. **Edit Appliance** – change the name, wattage or hours; press Enter to keep a value; each new value is re-validated.
4. **Remove Appliance** – delete by number, with an option to cancel.
5. **Daily & Monthly Consumption / Bill** – per-appliance kWh and cost, totals, estimated daily cost and monthly bill.
6. **Highest-Consuming Appliance** – identifies the biggest consumer and its percentage of the total.
7. **Set Electricity Rate** – update the tariff, which is immediately used in all calculations.
8. **Energy-Saving Report** – top consumers, targeted tips and a quantified saving suggestion.
9. **Persistent Storage** – automatic JSON saving and safe recovery on start-up.
10. **Robust Input Handling** – reusable helpers that guarantee valid numbers before any calculation.

## 9. User Workflow (Summary)
1. The user starts the program; saved data is loaded (or defaults are created if none exists).
2. A numbered menu (0–8) is displayed and the user chooses an option.
3. The chosen feature prompts for any inputs, which are validated and re-requested until correct.
4. The result (a table, a message or a report) is displayed, and any change is saved immediately.
5. Control returns to the menu until the user selects **0** to exit.

## 10. Inputs and Outputs
| Feature | Inputs | Outputs |
|---------|--------|---------|
| Add appliance | Name, wattage, hours/day, optional quantity | Confirmation; updated stored list |
| Edit appliance | List number, optional new values | "Updated." message; updated record |
| Remove appliance | List number | Confirmation with the removed name |
| Consumption / bill | Stored appliances and rate | Table of daily kWh, monthly kWh and cost with totals |
| Highest consumer | Stored appliances | Name, monthly kWh, percentage share, cost |
| Set rate | New rate per unit | "Rate updated." message |
| Energy-saving report | Stored appliances and rate | Summary, top three consumers, tips and quick-win estimate |

## 11. Expected Outcomes and Benefits
- Users can see, in seconds, how many units and how much money each appliance uses.
- The biggest energy consumers are highlighted so effort goes where it saves most (for example, in the sample data two 509 W fans running all day account for about 79% of the estimated bill).
- Tips are tied to the user's own appliances, making advice practical and actionable.
- Data entered once is remembered, so the tool can be used repeatedly with little effort.
- The project demonstrates good software practice: separation of concerns, validation, error handling, persistence and automated tests.

## 12. Non-Functional Expectations
- **Usability:** simple numbered menu, clear prompts and messages, cancel options.
- **Reliability:** no crash on invalid input or a damaged data file.
- **Maintainability:** small single-purpose modules and centralised constants.
- **Performance and efficiency:** instant results with negligible memory and CPU use.
- **Portability:** runs on Windows, Linux and macOS with no third-party packages.

## 13. Limitations
- Estimates rely on rated wattage and average hours, so they may differ from actual meter readings.
- A flat tariff and 30-day month do not reflect slab rates, taxes or variable month lengths.
- The edit option currently does not change the quantity of an appliance.
- Appliances with the same or similar names (for example "Fan" and "fan") are stored as separate entries.
- The interface is text-based and single-user.

## 14. Future Scope
- Editing of quantity and detection of duplicate appliance names.
- Slab-based tariffs, fixed charges and taxes for closer bill matching.
- Comparison of estimates with actual monthly meter readings.
- Charts and graphs (bar or pie) of consumption, and export to CSV or PDF.
- Cost splitting between roommates for each appliance.
- A graphical or web/mobile interface with SQLite or cloud storage.
- Logging and a larger automated test suite with continuous integration.
