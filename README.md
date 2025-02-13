# RapidZone

RapidZone is a Python program designed to manage power settings and create custom power plans based on usage on Windows systems. It provides an easy-to-use interface for manipulating power plans directly from the command line.

## Features

- List all available power plans.
- Retrieve the GUID of the current active power plan.
- Create custom power plans with specified names and descriptions.
- Switch between power plans by setting them as active.
- Delete power plans that are no longer needed.

## Requirements

- Windows operating system
- Python 3.x installed
- Administrative privileges to execute power management commands

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/rapidzone.git
   ```

2. Navigate to the project directory:
   ```bash
   cd rapidzone
   ```

3. Run the script:
   ```bash
   python rapidzone.py
   ```

## Usage

The script provides several methods for managing power plans:

- **Get Current Power Plan:**
  Retrieve the GUID of the currently active power plan.
  ```python
  rz = RapidZone()
  print("Current Power Plan GUID:", rz.current_plan_guid)
  ```

- **List All Power Plans:**
  List all available power plans.
  ```python
  rz.list_power_plans()
  ```

- **Create Custom Power Plan:**
  Create a new custom power plan.
  ```python
  new_guid = rz.create_custom_power_plan("GamingMode", "High performance for gaming")
  ```

- **Set Active Power Plan:**
  Change the active power plan.
  ```python
  rz.set_power_plan(new_guid)
  ```

- **Delete Power Plan:**
  Remove an unused power plan.
  ```python
  rz.delete_power_plan(new_guid)
  ```

## Note

- Ensure you have the necessary administrative privileges when running the script.
- Be cautious when creating or deleting power plans, as they can affect system performance and power consumption.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.