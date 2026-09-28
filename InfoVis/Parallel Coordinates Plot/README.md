# Twitch Data Visualization with Plotly.js

This project visualizes Twitch user data from CSV files using Plotly.js, with an interactive parallel coordinates plot that allows you to explore various attributes, including language, partner status, mature content, and number of views.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)

## Features

- **Parallel Coordinates Plot**: Visualize multiple attributes of Twitch user data in an interactive plot.
- **Interactive Filtering**: Select specific dimensions, such as days, views, partner status, and language, and adjust ranges directly on the plot.
- **Customizable Axes**: Dynamically set ranges and constraints for each axis to focus on data subsets.

## Setup

### Requirements

- [Node.js](https://nodejs.org/) (with `http-server` for serving files locally)
- A modern web browser with WebGL support (e.g., Chrome, Firefox)

### Installation

1. **Start a Local Server**: User `http-server` to serve files locally. Install it if you haven't yet:
```bash
npm install -g http-server
```

2. **Run the server**: In the 'Parallel Coordinates Plot' directory, start the server:
```bash
npx http-server
```

3. **Access the Application**: Open your browser and navigate to `http://localhost:8080` (or the port `http-server` specifies).

### CSV Data Structure
Each CSV file should contain the following columns:
- days: Number of days since account creation.
- views: Total view count.
- partner: Partner status (True or False).
- mature: Mature content flag (True or False).
- language: Language of the user (appended programmatically).

## Usage
1. **Select Dimensions**: Use the checkboxes to choose which dimensions to display (e.g., days, views, partner, language).

2. **View Ranges**: The plot shows view counts divided into two ranges for views for better clarity:
- Flexible (set initially as [min, max])
- [50000, 1000000]
- [0, 50000]

3. **Interactive Plot**:
- Brushing and Axes reordering is implemented.