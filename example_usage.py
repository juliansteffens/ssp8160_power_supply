# Example usage:
import time
import ssp8160_power_supply as ps

if __name__ == "__main__":
    port = "COM5"  # Replace with the actual COM port of your SSP-8160 (get from Windows Device Manager)

    try:
        # Step 1: Initialize the connection
        psu = ps.initialize_power_supply(port)

        # Step 2: Set voltage and current
        print("Setting voltage to 12.0V...")
        ps.set_voltage(psu, 12.0)

        print("Setting current to 2.0A...")
        ps.set_current(psu, 2.0)

        # Step 3: Turn output on
        print("Turning output on...")
        ps.turn_output_on(psu)

        # Step 4: Query status, voltage, and current
        print("Querying status...")
        print(ps.query_status(psu))

        print("Querying output voltage and current...")
        voltage, current = ps.query_voltage_current(psu)
        print(f"Voltage: {voltage}V, Current: {current}A")

        time.sleep(5)

        # Step 5: Turn output off
        print("Turning output off...")
        ps.turn_output_off(psu)

    except Exception as e:
        print("Error:", e)

    finally:
        # Step 6: Close the connection
        ps.close_connection(psu)
