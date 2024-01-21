<h1 align='center'>NY Times Scraping - Challenge</h1>

<p align="center">
<img src='https://img.shields.io/badge/Python-v3.11.7-yellow'>
<img src='https://img.shields.io/badge/rpaframework-v28.0.0-green'>
<img src='https://img.shields.io/badge/openpyxl-v3.1.2-red'>
</p>

<p align='center'>
<img width=150 src='/public/robot.png'>
</p>

## Summary

- [Summary](#summary)
- [Overview](#overview)
- [Notes](#notes)
- [Requirements](#requirements)
- [Configuration](#configuration)
- [File Descriptions](#file-descriptions)
- [Dependencies](#dependencies)

## Overview

This repository contains a Python script designed to perform a web scraping challenge. The script utilizes Selenium for browser automation and interacts with the New York Times website to retrieve and process news information based on specified criteria. Additionally, there are supporting functions in `functions.py` that handle various tasks such as date manipulation, file operations, and text analysis.

## Notes

During the code development, I noticed that the "Date Range" function on the New York Times website is not working correctly. Therefore, I had to manually develop the logic for date filtering. This adds a bit of extra code to the automation, but it functions as expected.

## Requirements

Before running the script, ensure you have the necessary dependencies installed. You can install them using the following command:

```pip install -r requirements.txt```

## Configuration

Adjust the configuration in `config.py` to customize the script's behavior. Modify variables such as `SEARCH_PHRASE`, `SECTIONS`, and `MONTHS` to tailor the script to your specific needs.

## File Descriptions

- `challenge.py`: Script for the web scraping challenge.
- `functions.py`: Collection of utility functions used by the script.
- `config.py`: Configuration file containing script parameters.
- `xpaths.py`: Configuration file containing xpaths used by the automation.
- `tasks.py`: Task file for Robocorp.

## Dependencies

- `Selenium` (with `rpaframework`): Used for browser automation.
- `openpyxl`: Handles Excel file creation.