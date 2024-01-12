<h1 align='center'>NY Times Scraping - Challenge</h1>

<p align="center">
<img src='https://img.shields.io/badge/Python-v3.11.7-yellow'>
<img src='https://img.shields.io/badge/rpaframework-v28.0.0-green'>
<img src='https://img.shields.io/badge/openpyxl-v3.1.2-red'>
</p>

<p align='center'>
<img width=150 src='https://raw.githubusercontent.com/pzzzl/nytimes_challenge/main/public/robot.png?token=GHSAT0AAAAAACMMR3BB776KMMZ4P6UDK4S4ZNAYMOA'>
</p>

## Summary

- [Summary](#summary)
- [Overview](#overview)
- [Notes](#notes)
- [Requirements](#requirements)
- [Usage](#usage)
- [Configuration](#configuration)
- [File Descriptions](#file-descriptions)
- [Dependencies](#dependencies)
- [Important Note](#important-note)

## Overview

This repository contains a Python script designed to perform a web scraping challenge. The script utilizes Selenium for browser automation and interacts with the New York Times website to retrieve and process news information based on specified criteria. Additionally, there are supporting functions in `functions.py` that handle various tasks such as date manipulation, file operations, and text analysis.

## Notes

During the code development, I noticed that the "Date Range" function on the New York Times website is not working correctly. Therefore, I had to manually develop the logic for date filtering. This adds a bit of extra code to the automation, but it functions as expected.

Additionally, the code creates an `img` folder to store images and an output spreadsheet, currently named `result.xlsx`, but this is customizable.

## Requirements

Before running the script, ensure you have the necessary dependencies installed. You can install them using the following command:

```pip install -r requirements.txt```

## Usage

To execute the challenge script, follow these steps:

- Open a terminal or command prompt.
- Navigate to the project directory.
- Run the following command:

```python main.py```

## Configuration

Adjust the configuration in `imports.py` to customize the script's behavior. Modify variables such as `URL`, `SEARCH_PHRASE`, `SECTIONS`, and `MONTHS` to tailor the script to your specific needs.

## File Descriptions

- `main.py`: Challenge entry point.
- `challenge.py`: Script for the web scraping challenge.
- `functions.py`: Collection of utility functions used by the script.
- `config.py`: Configuration file containing script parameters.
- `xpaths.py`: Configuration file containing xpaths used by the automation.
- `imports.py`: Most of the imports used by the script.

## Dependencies

- `Selenium` (with `rpaframework`): Used for browser automation.
- `openpyxl`: Handles Excel file creation.

## Important Note

- The script forcefully closes all open Google Chrome instances during execution.
