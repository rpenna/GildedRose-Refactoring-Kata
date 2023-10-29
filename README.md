# Gilded Rose Refactoring Kata Fork

Python code refactoring challenge for learning purpose. As every refactoring, the code behavior should NOT change after the improvements. The goal is to make it easier to add a new category of item. 

You can read the [original Gilded Rose Refactoring Kata README here](./original_README.md).

## Prerequisites

* Python 3.10+
* Pip 32.2.1

## Installation

1. Create Python virtual environment:
    ```
    python -m venv .
    ```

2. Install Python dependencies:
    ```
    pip install -r python/requirements.txt
    ```

## Testing
Just run the following pytest command:
    ```
    pytest
    ```

## Running the code
Since it's a refactoring challeng code, there is no software to run. The purpose was to not change the code behavior, but make it more readable and easy to maintain.

With the improvements made, it's now easier to add a new item with specific behavior by using the following steps:

1. (Optional) Create tests.
2. Add item name to settings.ini file.
3. Create Updater class using UpdaterDefaultItem as parent class.
4. Add new Updater declaration to __items_updaters dict, the attribute from GildedRose class.