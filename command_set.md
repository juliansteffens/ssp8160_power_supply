#command set

initialize_power_supply(port, baudrate=9600, timeout=1):
    """
    Initializes the connection to the SSP-8160 power supply.

    Parameters:
    port (str): The COM port (e.g., 'COM3') to which the power supply is connected.
    baudrate (int): Communication speed (default is 9600).
    timeout (int): Timeout for serial communication in seconds.

    Returns:
    Serial: The initialized serial connection.

    example use:
    port = 'COM3'
    psu = initialize_power_supply()
    """

send_command(ser, command):
    """
    Sends a custom command to the power supply and returns the response.
    For commands see manufacturer data sheet.

    Parameters:
    ser (Serial): The serial connection.
    command (str): The command to send to the power supply.

    Returns:
    str: The response from the power supply.
    """
set_voltage(ser, voltage):
    """
    Sets the output voltage of the power supply.

    Parameters:
    ser (Serial): The serial connection.
    voltage (float): The desired voltage in volts.

    Returns:
    str: The response from the power supply.
    """

set_current(ser, current):
    """
    Sets the output current of the power supply.

    Parameters:
    ser (Serial): The serial connection.
    current (float): The desired current in amperes.

    Returns:
    str: The response from the power supply.
    """

turn_output_on(ser):
    """
    Turns the output of the power supply on.

    Parameters:
    ser (Serial): The serial connection.

    Returns:
    str: The response from the power supply.
    """

turn_output_off(ser):
    """
    Turns the output of the power supply off.

    Parameters:
    ser (Serial): The serial connection.

    Returns:
    str: The response from the power supply.
    """

query_status(ser):
    """
    Queries the current status of the power supply.

    Parameters:
    ser (Serial): The serial connection.

    Returns:
    str: The status information from the power supply.
    """

query_voltage_current(ser):
    """
    Queries the current output voltage and current of the power supply.

    Parameters:
    ser (Serial): The serial connection.

    Returns:
    tuple: The current output voltage and current.
    """

close_connection(ser):
    """
    Closes the connection to the power supply.

    Parameters:
    ser (Serial): The serial connection.
    """
