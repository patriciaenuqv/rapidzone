import subprocess
import os

class RapidZone:
    def __init__(self):
        self.current_plan_guid = self.get_current_power_plan()

    def get_current_power_plan(self):
        """Get the GUID of the current power plan."""
        try:
            output = subprocess.check_output(["powercfg", "/getactivescheme"], shell=True)
            guid = output.decode().split(' ')[3].strip()
            return guid
        except Exception as e:
            print(f"Error retrieving current power plan: {e}")
            return None

    def list_power_plans(self):
        """List all available power plans."""
        try:
            output = subprocess.check_output(["powercfg", "/list"], shell=True)
            print(output.decode())
        except Exception as e:
            print(f"Error listing power plans: {e}")

    def create_custom_power_plan(self, plan_name, plan_description):
        """Create a custom power plan."""
        try:
            output = subprocess.check_output(
                ["powercfg", "/create", plan_name, "/d", plan_description], shell=True)
            new_plan_guid = output.decode().split(' ')[-1].strip()
            print(f"Created power plan: {plan_name} with GUID: {new_plan_guid}")
            return new_plan_guid
        except Exception as e:
            print(f"Error creating custom power plan: {e}")
            return None

    def set_power_plan(self, plan_guid):
        """Set the specified power plan as active."""
        try:
            subprocess.check_call(["powercfg", "/setactive", plan_guid], shell=True)
            print(f"Switched to power plan with GUID: {plan_guid}")
        except Exception as e:
            print(f"Error setting power plan: {e}")

    def delete_power_plan(self, plan_guid):
        """Delete the specified power plan."""
        try:
            subprocess.check_call(["powercfg", "/delete", plan_guid], shell=True)
            print(f"Deleted power plan with GUID: {plan_guid}")
        except Exception as e:
            print(f"Error deleting power plan: {e}")

if __name__ == "__main__":
    rz = RapidZone()
    print("Current Power Plan GUID:", rz.current_plan_guid)
    rz.list_power_plans()

    # Example usage:
    # new_guid = rz.create_custom_power_plan("GamingMode", "High performance for gaming")
    # rz.set_power_plan(new_guid)
    # rz.delete_power_plan(new_guid)