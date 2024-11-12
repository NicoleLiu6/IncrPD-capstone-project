
# README: IncrePD Dashboard for Incremental Peritoneal Dialysis

## Project Overview

This project is a Streamlit-based dashboard designed to assist healthcare professionals in managing Incremental Peritoneal Dialysis (IncrPD). The dashboard provides tools to calculate patient-specific metrics, assess symptoms, and compare the environmental impact of using IncrPD versus Full PD. The application aims to support clinical decision-making by presenting key health parameters and tracking patient symptoms while highlighting potential resource savings.

## Features

The application consists of three main sections:
1. **IncrPD Health Parameters**: Calculates essential health metrics such as Total Body Water (TBW) and Residual Kidney Function (RKF) to determine the appropriate IncrPD volume.
2. **Symptom Assessment**: Allows clinicians to log and evaluate common symptoms in dialysis patients, generating a symptom score for ongoing monitoring.
3. **Full PD vs IncrPD Comparison**: Compares the volume required for Full PD against IncrPD and provides insights into environmental impact by displaying potential water and plastic savings.

## Installation

### Requirements
- Python 3.7 or higher
- Streamlit library

### Steps to Install and Run
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/IncrePD-Dashboard.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd IncrePD-Dashboard
   ```
3. **Install Dependencies**:
   - Install necessary packages using the requirements file:
     ```bash
     pip install -r requirements.txt
     ```
4. **Run the Application**:
   - Launch the Streamlit app:
     ```bash
     streamlit run capstone.py
     ```
5. **Open in Browser**:
   - Go to `http://localhost:8501` in your browser to access the dashboard.

## Dashboard Functionality

### 1. IncrPD Health Parameters
   - **Purpose**: Calculate key health parameters for patients undergoing IncrPD.
   - **Inputs**:
     - Weight (kg)
     - Gender (Male/Female)
     - 24-hour Urine Volume (L/day)
     - 24-hour Urine Urea (MMOL/L)
     - Serum Urea (MMOL/L)
   - **Outputs**:
     - **Total Body Water (TBW)**: Calculated based on patient weight and gender.
     - **Residual Kidney Function (RKF)**: Urea clearance measurement.
     - **Volume Needed per Day**: Recommended IncrPD volume to meet the patient’s needs.

### 2. Symptom Assessment
   - **Purpose**: Log common symptoms and assess patient well-being.
   - **Inputs**:
     - Nausea, Vomiting, Pruritus (Itching), Appetite, Sleep Quality, Sudden Weight Loss, and Pitting Oedema levels.
   - **Outputs**:
     - **Total Symptom Score**: Calculates a score out of 9 based on the symptoms selected, helping track the patient's overall condition over time.

### 3. Full PD vs IncrPD Comparison
   - **Purpose**: Compare the volume required for Full PD to that of IncrPD, and calculate environmental benefits.
   - **Inputs**:
     - Weight (kg)
     - Gender (Male/Female)
     - Dialysate Urea (MMOL/L)
     - Serum Urea (MMOL/L)
     - IncrPD Dialysate Volume (adjustable)
   - **Outputs**:
     - **Full PD Volume Required**: Displays the recommended volume for Full PD based on a target Kt/V of 1.77.
     - **Volume Saved by IncrPD**: Shows the difference in volume between Full PD and IncrPD.
     - **Environmental Impact**:
       - **Water Saved (L/day)**: Based on the volume saved plus 35L saved in manufacturing per dialysis bag.
       - **Plastic Saved (kg/day)**: Estimated based on bags saved; each 2L saved equates to 1 bag weighing 0.155 kg.

## Notes on Code Structure

The main Python file, `capstone.py`, includes:
- **Function Definitions**: Contains helper functions for TBW calculation, RKF measurement, and environmental impact.
- **Main App Layout**: Organizes the three pages (IncrPD Health Parameters, Symptom Assessment, and Full PD vs IncrPD Comparison) and manages user inputs.
- **Session State**: Stores the IncrPD volume calculated on the Health Parameters page for later use in comparisons.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
