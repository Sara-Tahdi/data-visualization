# Performance Dashboard

## Overview

This project provides a **user-friendly GUI** built with **Streamlit** to display and analyze car performance metrics. It enhances data accessibility and usability, making it easier for team members to visualize key car performance indicators and make data-driven decisions.

---

## Features

- **Car Data Upload**: Users can upload Excel files containing car performance data.
- **Interactive Data Visualization**: Automatically generates interactive graphs to help visualize performance trends.
- **Customizable Data Filtering**: Users can filter and select variables from the data to focus on specific metrics.
- **Default Data**: If no data is uploaded, the app will load a default dataset for analysis.
- **Car Performance Metrics**: Displays important performance indicators like speed, time, fuel efficiency, etc.
- **Racing Dashboard**: The app includes a racing theme with car-related graphics and a race car emoji to enhance the user experience.

---

## Usage

### 1. **Upload Data**:
   - Click on the sidebar's **"Upload your data file"** button to upload your Excel file containing car performance data.
   - If no file is uploaded, the app will automatically load a **default file** from the `data` folder (e.g., `data/mfe_log.xlsx`).

### 2. **Filter Data**:
   - Use the **"Filter"** dropdown in the dataset viewer to select which columns of the data you want to display. This will allow you to focus on specific metrics such as speed, time, fuel efficiency, etc.

### 3. **Interactive Graphs**:
   - Once the data is loaded, the app will automatically display **line graphs** to visualize the performance metrics over time.
   - These graphs are interactive, allowing you to hover over data points and zoom into specific ranges to gain deeper insights.

### 4. **Customization**:
   - Customize the data display by selecting different columns through the **"Filter"** dropdown.
   - The graphs will automatically update to reflect the selected data, allowing you to focus on specific performance metrics.
   - Modify the **default file** or upload a different dataset to tailor the analysis to your specific needs.

## Contribution

If you'd like to contribute to this project, feel free to fork the repository and submit pull requests. Please ensure to update the README if you add any significant features.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Notes:

- **Data Format**: The app expects the uploaded Excel file to contain car performance metrics with a header starting from row 14 (as specified in the app). If you are using a different format, you may need to adjust the code to accommodate it.

- **Customization**: The app uses a custom theme (through `style.css`) and a car-related logo (through `assets/logo.png`). You can modify these files to fit your own branding.

