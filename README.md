# National Identity Card (NIC) Checker

This repository contains Python scripts (`MainProgram.py` and `NIC.py`) to validate and extract details from Sri Lankan National Identity Card (NIC) numbers.

## Overview

The National Identity Card (NIC) in Sri Lanka has evolved over the years, and this project provides functionality to determine whether a given NIC number is old or new and extract relevant details such as birth year, gender, and voter status.

## Files

### MainProgram.py

This script interacts with the user to input an NIC number and utilizes functions defined in `NIC.py` to validate the NIC type (old or new) and extract details accordingly.

#### Usage

1. Run the script `MainProgram.py`:

   ```
   python MainProgram.py
   ```

2. Enter a valid NIC number when prompted.

### NIC.py

This module defines two functions:
- `new_NIC(nic_num)`: Extracts details from a new format NIC number.
- `old_NIC(nic_num)`: Extracts details from an old format NIC number.

These functions are called by `MainProgram.py` based on the NIC number format detected.

## NIC Details Extracted

- **Birth Year**: Extracts the birth year from the NIC number.
- **Gender**: Determines gender based on specific digits in the NIC number.
- **Voter Status**: Identifies whether the person is registered as a voter based on the last character of the NIC number.

## Example

If the NIC number `200132450123` is entered:
- It will recognize it as a new NIC format.
- Output:
  ```
  NIC type: new
  You were born on  2001
  You are a male/female (based on specific digits)
  You are a voter/none voter (based on last character)
  ```

## Requirements

- Python 3.x

## Contributions

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
