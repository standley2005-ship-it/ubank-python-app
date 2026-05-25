# UBank Python App

Python Tkinter banking simulation for practicing desktop UI development, basic account logic, validation, and clean project organization.

> Status: Student prototype. This is a local simulation and does not connect to a real bank or payment system.

## Project Overview

UBank is a desktop banking simulation that can be used to demonstrate Python fundamentals, user interface development, object-oriented thinking, and safe handling of simulated account actions.

The project is designed for learning and portfolio presentation. It avoids real financial data and does not process real transactions.

## Features

- Simulated account balance display.
- Deposit and withdrawal workflows.
- Basic validation for invalid amounts.
- In-memory transaction history.
- Organized Python source folder.
- Unit-testable account logic.
- Screenshot placeholder folder for future UI images.

## Tech Stack

- Python 3
- Tkinter
- Object-oriented programming
- Local desktop application structure

## Folder Structure

```text
ubank-python-app/
  README.md
  .gitignore
  requirements.txt
  docs/
    app-flow.md
  src/
    ubank_app/
      __init__.py
      account.py
      main.py
  tests/
    test_account.py
  screenshots/
    .gitkeep
```

## Setup Instructions

1. Install Python 3.
2. Clone the repository.
3. Open a terminal in the project folder.
4. Run the app:

```bash
python src/ubank_app/main.py
```

Tkinter is included with most standard Python installations.

To run the tests:

```bash
python -m unittest discover -s tests
```

## Screenshots

Screenshots will be added after the desktop UI is captured.

## Future Improvements

- Add user login simulation.
- Save transaction history to a local JSON or SQLite database.
- Save transaction history to a local JSON or SQLite database.
- Improve the UI layout and error messages.
- Add screenshots of each workflow.
