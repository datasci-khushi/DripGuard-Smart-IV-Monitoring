# DripGuard: Smart IV Infusion Monitoring and Prediction System

## Software Repository

DripGuard is a software project designed to monitor IV infusion readings, display infusion status, maintain historical records, and present alerts through a web-based dashboard. The software is developed as an academic prototype.

## Project Overview

The software uses a Flask backend, a Streamlit dashboard, and an SQLite database to manage and display infusion-related data.

The dashboard provides a central interface for viewing current readings, reviewing historical data, checking alerts, and accessing configuration settings.

## Key Features

- **Dashboard:** Provides an overview of recorded infusion readings and system status.
- **Live Monitoring:** Displays available infusion readings, such as drip rate, flow rate, bag volume, remaining time, and status.
- **History:** Allows users to review previously recorded readings.
- **Alerts:** Provides an interface for viewing recorded alerts.
- **Database:** Uses SQLite to store infusion readings and timestamps.
- **Settings:** Provides an interface for configuring infusion-related parameters through backend API requests.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Flask | Backend server and REST API |
| Streamlit | Dashboard interface |
| SQLite | Database storage |
| Pandas | Data handling and tabular display |
| Requests | HTTP communication between software components |
| DB Browser for SQLite | Desktop application used to view, browse, and inspect SQLite database tables and records |

## Repository Structure

```text
.
├── backend/
│   └── app.py
├── dashboard/
│   └── app.py
├── requirements.txt
├── dashboard_code.pdf
├── source_codes.pdf
├── DripGuard_Presentation.pptx
├── current_readings.jpg
├── historical_readings.jpg
└── README.md
```

## Software Components

### 1. Flask Backend

The backend is responsible for receiving requests, processing infusion-reading data, interacting with the SQLite database, and returning information through API endpoints.

### 2. Streamlit Dashboard

The dashboard provides the user interface for monitoring readings, viewing history and alerts, accessing database information, and managing available settings.

### 3. SQLite Database

The database stores infusion readings and associated information, including bed identification, drip rate, flow rate, bag volume, remaining time, status, and timestamp.

### 4. Database Inspection Using DB Browser for SQLite

DB Browser for SQLite is used to open and inspect the SQLite database file. It provides a visual interface for viewing database tables and records, reviewing current readings, and checking historical data during development and testing.

## Setup and Execution

### Prerequisites

- Python 3.10 or a compatible version
- pip (Python package installer)

### 1. Download the Repository

Clone the repository or download it from GitHub.

### 2. Install Dependencies

Open a terminal in the project directory and run:

```bash
pip install -r requirements.txt
```

### 3. Start the Backend

From the project directory, run:

```bash
python backend/app.py
```

The backend code is configured to use port `5000`.

### 4. Start the Dashboard

Open a second terminal in the project directory and run:

```bash
streamlit run dashboard/app.py
```

The dashboard and backend must be configured to communicate with each other. If running on another computer or deployment environment, update the API address in the dashboard as needed.

## Project Documentation

- **Dashboard Code:** `dashboard_code.pdf`
- **Source Code Collection:** `source_codes.pdf`
- **Project Presentation:** `DripGuard_Presentation.pptx`
- **Current Database Readings:** `current_readings.jpg`
- **Historical Database Readings:** `historical_readings.jpg`

## Project Scope and Safety

DripGuard is an academic software prototype intended for project demonstration and development. Its monitoring, prediction, and alerting capabilities require appropriate testing and validation. It is not a certified medical device and must not be used to make clinical decisions or replace professional medical monitoring.

## Future Improvements

- Improve consistency between the backend API and dashboard.
- Enhance real-time updates and data validation.
- Improve alert handling and reporting.
- Develop and validate prediction functionality using suitable historical data.
- Add testing, error handling, and deployment configuration.

## Conclusion

DripGuard brings together a Python backend, a web-based monitoring dashboard, and database storage to organize and display IV infusion-related information. The project provides a foundation for further software development, integration, and testing.
