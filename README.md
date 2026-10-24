# DripGuard: Smart IV Infusion Monitoring and Prediction System

## Software Repository

This repository contains the software components of DripGuard, a smart IV infusion monitoring and prediction system developed as an academic team project.

## Project Overview

DripGuard is designed to monitor IV infusion readings, display current and historical data, and present alerts through a software dashboard. The system uses a Flask backend, a Streamlit dashboard, and an SQLite database.

## Key Features

- Live IV infusion monitoring dashboard
- Display of current infusion readings
- Historical readings and data visualization
- Alert display for infusion monitoring
- SQLite database for storing and inspecting readings
- Dashboard settings interface

## Technologies Used

- Python
- Flask
- Streamlit
- SQLite
- Pandas
- Requests
- DB Browser for SQLite — desktop application used to inspect database tables and records

## Repository Structure

```text
DripGuard-Smart-IV-Monitoring/
│
├── backend/
│   └── app.py
│
├── dashboard/
│   └── app.py
│
├── dashboard_code.pdf
├── source_codes.pdf
├── dashboard_visualization.pdf
├── DripGuard_Presentation.pptx
├── current_readings.jpg
├── historical_readings.jpg
├── requirements.txt
└── README.md
```

## Software Components

### 1. Flask Backend

The backend handles API requests and works with the SQLite database to provide infusion readings and related information.

### 2. Streamlit Dashboard

The dashboard provides an interface for viewing monitoring information, historical readings, alerts, and database-related information.

### 3. SQLite Database

SQLite stores infusion reading records, including drip rate, flow rate, bag volume, remaining time, status, and timestamp.

### 4. Database Inspection

DB Browser for SQLite is used as a desktop application to view and inspect the SQLite database and its records.

## Setup and Execution

### Prerequisites

- Python installed on your computer
- Required Python packages installed
- Project files downloaded from this repository

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Backend

```bash
python backend/app.py
```

### Run the Dashboard

Open a separate terminal and run:

```bash
streamlit run dashboard/app.py
```

**Note:** The backend and dashboard may require configuration or API adjustments to work together correctly.

## Project Documentation

- [Dashboard source code PDF](dashboard_code.pdf)
- [Source code documentation PDF](source_codes.pdf)
- [Dashboard visualizations PDF](dashboard_visualization.pdf)
- [Project presentation](DripGuard_Presentation.pptx)
- [Current database readings](current_readings.jpg)
- [Historical database readings](historical_readings.jpg)

## Project Scope and Safety

DripGuard is an academic prototype developed for educational and demonstration purposes. It is not a certified medical device and must not be used to make clinical decisions or replace professional medical supervision.

## Future Improvements

- Integration with physical infusion monitoring hardware
- Improved prediction and alert mechanisms
- Enhanced data visualization
- Further testing and validation of the complete system

## Project Team

This project was developed collaboratively as part of an academic project.

- **Khushi Patil**
- **Swati Mahto**
- **Mrunali Kamble**

## Conclusion

DripGuard demonstrates a software-based approach to IV infusion monitoring using a Flask backend, a Streamlit dashboard, and an SQLite database. The project provides a foundation for future development and integration with hardware components.
