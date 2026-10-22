# DripGuard — Smart IV Infusion Monitoring and Prediction System

## 1. Project Overview

DripGuard is a smart IV infusion monitoring prototype designed to monitor IV drip activity, display readings on a web dashboard, and provide visual and audio alerts based on the drip status.

The system combines hardware components, a Python backend, a web dashboard, and an SQLite database to monitor and store IV readings.

## 2. Project Components

### Hardware

* **NodeMCU ESP8266:** Microcontroller with 2.4 GHz Wi-Fi connectivity.
* **LM393 IR Sensor Module:** Detects drops passing through the IV drip chamber.
* **LED Indicators:** Green for normal, yellow for attention, and red for critical status.
* **Active Buzzer:** Provides an audible alert.
* **220Ω Resistors:** Used with the LED indicators.
* **Breadboard and Jumper Wires:** Used for circuit connections.
* **IV Administration Set:** Includes the drip chamber, tubing, roller clamp, and spike.
* **USB Data Cable:** Used to upload code and power the NodeMCU.

### Software

* Python backend for communication and processing.
* Web dashboard for real-time monitoring and configuration.
* SQLite database for storing monitoring readings.
* DB Browser for SQLite for viewing and managing database records.

## 3. Hardware Connections

| Component                | NodeMCU Pin |
| ------------------------ | ----------- |
| IR sensor digital output | D5          |
| Green LED                | D1          |
| Yellow LED               | D2          |
| Red LED                  | D3          |
| Active buzzer signal     | D6          |

The LEDs are connected through 220Ω resistors. The sensor and other components must be powered according to their specifications, with compatible logic levels and a common ground.

## 4. System Architecture

1. The IR sensor detects drops in the IV drip chamber.
2. The NodeMCU ESP8266 counts detected drops and calculates monitoring values.
3. The NodeMCU communicates with the Python backend over Wi-Fi.
4. The Python dashboard sends configurable settings, including bag volume, drip factor, and target drip rate, to the NodeMCU.
5. The NodeMCU sends monitoring readings back to the backend.
6. The dashboard displays the readings and status indicators.
7. The backend stores monitoring readings in the SQLite database, which can be inspected using DB Browser for SQLite.

## 5. Dashboard

The DripGuard dashboard displays:

* Total IV beds and their monitoring status.
* Drip rate in drops per minute.
* Flow rate in mL per minute.
* Estimated remaining time.
* Configured IV bag volume.
* Normal, attention, and critical alerts.
* Historical readings and database-related information.
* Settings for bag volume, drip factor, and target drip rate.

### Bed Monitoring

| Bed ID | Monitoring Type                            |
| ------ | ------------------------------------------ |
| B01    | Connected to the physical NodeMCU hardware |
| B02    | Simulated monitoring data                  |
| B03    | Simulated monitoring data                  |
| B04    | Simulated monitoring data                  |

**Note:** B01 is the physical hardware-connected bed. B02, B03, and B04 display simulated readings and are not connected to separate physical monitoring units.

## 6. SQLite Database

DripGuard uses SQLite to store monitoring readings. DB Browser for SQLite is used as a graphical tool to inspect the database and its tables.

The stored records can be reviewed to examine readings over time. Dashboard readings and database records depend on the backend's data-storage implementation.

## 7. Alert Logic

The current hardware code uses the configured target drip rate to determine status:

* **Normal:** Drip rate is at least 80% of the configured target rate.
* **Attention:** Drip rate is above zero but below 80% of the target.
* **Critical:** No drops are detected during the measurement interval.

The NodeMCU uses LEDs and the buzzer to indicate status according to the implemented code.

## 8. Configuration

The dashboard allows settings to be configured for a bed, including:

* Bed ID
* IV bag volume (mL)
* Drip factor (drops/mL)
* Target drip rate (drops/min)

The NodeMCU periodically requests settings from the Python backend and uses them in its calculations.

## 9. Repository Structure

A suggested repository structure is:

```text
DripGuard/
├── README.md
├── hardware/
│   └── nodemcu_firmware.ino
├── backend/
│   └── Python backend files
├── dashboard/
│   └── Dashboard files
├── database/
│   └── SQLite database file
└── docs/
    └── Project documentation
```

Adjust the folders and filenames to match the files actually present in your repository.

## 10. Limitations

* Only B01 is connected to physical monitoring hardware.
* B02, B03, and B04 use simulated data.
* Wi-Fi connectivity depends on the network and hotspot configuration.
* Drop detection and calculated values require further testing and validation.
* This is an academic prototype and is not clinically validated for patient care.

## 11. Future Improvements

* Improve automatic Wi-Fi reconnection.
* Improve sensor reliability and drop detection.
* Connect additional physical monitoring units.
* Enhance database history and reporting.
* Perform extensive testing and validation before considering any clinical application.

## 12. Disclaimer

DripGuard is developed for academic demonstration and prototyping. It must not be used as a substitute for approved medical equipment or clinical monitoring.
