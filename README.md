# Piggsy

Personal Finance Automation and Analysis System

![Status](https://img.shields.io/badge/status-in%20development-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

## Description

**Piggsy** is a system developed in **Python** to automate the registration, storage, and analysis of personal finances.
The project began as the evolution of financial flows managed manually in Excel spreadsheets, transitioning into a programmatic, structured, and reproducible system.

The main objective of Piggsy is to **reduce human errors**, **automate financial calculations**, and **generate clear reports** to support personal finance analysis and decision-making.

## Main Features

- Recording of financial transactions (income, expenses, transfers)
- Hierarchical categorization of financial categories
- Management of multiple accounts (cash, debit, credit)
- Persistence of local financial data
- Analysis of financial summaries and balances
- Automatic generation of reports (CSV, PDF)
- Modular design oriented toward scalability and future improvements

## Quick Start

### Requirements

- Python 3.10 or higher
- Git
- Virtual environment tool (optional but recommended)
- Required Python packages (see `requirements.txt`)

### Installation

Clone the repository:

**SSH**

```bash
git clone git@github.com:armandodev/piggsy.git
```

**HTTPS**

```bash
git clone https://github.com/armandodev/piggsy.git
```

Navigate to the project directory and create a virtual environment (optional but recommended):

```bash
cd piggsy
python -m venv venv
```

Activate the virtual environment:

- **Windows**

```bash
venv\Scripts\activate
```

- **macOS / Linux**

```bash
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### Usage

Run the main script to start using Piggsy:

```bash
python main.py
```

The system will **load sample financial data** and **generate reports** in the `reports/outputs/` directory.
If you want to work with your own data, you should delete the sample data in the main menu and then add your own financial transactions, categories, accounts and financial periods.

## Architecture and Design

The system is based on a domain model with the following entities:

- **Transaction**: Individual financial movement
- **Account**: Payment method or financial account
- **Category**: Hierarchical classification of income and expenses, modifiable by the user
- **Financial Period**: Time frame for financial analysis (monthly, yearly; monthly periods belong to a yearly period)
- **Financial Balance**: Aggregated financial results

### Data Flow

1. Register financial periods
2. Register accounts and categories
3. Register financial transactions linked to accounts, categories and periods
4. Local storage of data using binary storage (pickle)
5. Analysis of financial data
6. Generation of reports in CSV and PDF formats

## Example Reports

The system will generate reports such as:

- Financial summary by category (CSV, PDF)
- Monthly income and expense report (CSV, PDF)
- Monthly comparison of income and expenses (CSV, PDF)

> Example files are located in the `reports/outputs/` directory.

_(Here will be added later screenshots or CSV/PDF snippets)_

# Roadmap

- Migrate to a relational database like PostgreSQL or SQLite for better data management.
- Implement a REST API to allow integration with other applications.
- Advanced data validation and error handling.
- User authentication and multi-user support.
- User interface (web or desktop) for easier interaction.

## Learning Objectives

- Applied programming in Python
- Processing and analysis of financial data
- Automation of manual flows
- Modular software design
- Persistent data management
- Generation of reports in multiple formats

## Contribution

This project is educational in nature.
Suggestions and improvements are welcome via issues or PRs.
Please follow the established code style and include tests for new features.

## License

This project is licensed under the MIT License.

## Author

Developed by Jorge Armando Ceras Cárdenas - [@armandodev](https://github.com/armandodev).
Student of Systems Engineering at the [Instituto Tecnológico de Jiquilpan](https://www.itjiquilpan.edu.mx/).
Python developer focused on automation and data analysis.

## Disclaimer

This project is for educational and experimental purposes.
The financial calculations are illustrative and do not substitute professional accounting systems.
