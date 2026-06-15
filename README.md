# Study Tracker

A command-line study tracking application written in Python.

This project is an expansion of the original Study Tracker beta version. While the beta focused on recording study sessions, this version introduces report generation, statistical summaries, persistent JSON storage, and a clearer separation between data processing, storage, and presentation.

The goal of the project was to gain more experience designing programs that work with structured data and transforming raw information into meaningful reports.

## Requirements

* Python 3.10+

## Run

```bash
python main.py
```

## Features

* Create study subjects
* Record study sessions
* Add multiple study sessions to existing subjects
* Automatically create new subjects when needed
* Persist study data using JSON storage
* Load previous study records automatically on startup
* View an overall study report
* Calculate total subjects tracked
* Calculate total study sessions
* Calculate total study time
* Generate subject-specific statistics
* Calculate average session duration
* Display formatted study logs
* Separate storage, calculation, and presentation logic into dedicated modules

## Example Output

```text
================ STUDY REPORT ================

Subjects: 2
Total Sessions: 9
Total Study Time: 5h 22m

Math
==================================================
Sessions: 5
Total Time Spent: 2h 30m
Average Session: 30.0

Session 1: 30
Session 2: 60
Session 3: 12

Biology
==================================================
Sessions: 4
Total Time Spent: 2h 52m
Average Session: 43.0
```

## Why Some Functionality Was Implemented Manually

Several parts of this project intentionally avoid Python built-in shortcuts.

Examples include:

* Manual number validation instead of `str.isdigit()`
* Manual time formatting logic instead of relying on more concise alternatives

This was done as a learning exercise. The objective was to understand the underlying logic before using higher-level abstractions. Although Python provides simpler solutions, implementing them manually provided additional practice with loops, conditionals, and data manipulation.

## Project Structure

### main.py

Responsible for:

* User interaction
* Menu navigation
* Subject management
* Recording study sessions

### stats.py

Responsible for:

* Report calculations
* Subject statistics
* Time formatting
* Utility functions

### storage.py

Responsible for:

* Saving study data to JSON
* Loading study data from JSON
* Managing persistent storage between program runs

### report.json

Stores study records between sessions.

## Data Structure

Study data is stored using a list of dictionaries.

```python
[
    {
        "subject": "math",
        "minutes": [30, 60, 12]
    },
    {
        "subject": "biology",
        "minutes": [44, 22, 30]
    }
]
```

## JSON Persistence

Study records are automatically saved to a JSON file (`report.json`) when the program exits and loaded again when the program starts.

This allows study data to persist between program executions instead of being reset each time the application is closed.

Example:

```json
[
    {
        "subject": "math",
        "minutes": [30, 60, 12]
    },
    {
        "subject": "biology",
        "minutes": [44, 22, 30]
    }
]
```

## Improvements Over the Beta Version

### Reporting System

The beta version only stored and displayed raw data.

This version introduces:

* Overall study statistics
* Subject-specific statistics
* Total study time calculations
* Average session calculations
* Formatted reports

### Persistent Storage

The beta version stored data only during program execution.

This version introduces JSON persistence, allowing study records to survive between sessions.

### Better Separation of Responsibilities

The program now distinguishes between:

* Data storage
* Data processing
* Data presentation

This made the code easier to organize and extend.

### Refactoring and Naming

Several parts of the codebase were renamed and reorganized to improve readability and consistency.

Examples include:

* `create_sub()` → `create_subject()`
* `minute` → `minutes`
* More descriptive function names throughout the project

## What I Learned

Through this project, I gained experience with:

* Calculating aggregate statistics from nested data structures
* Transforming raw data into human-readable reports
* Designing functions around specific responsibilities
* Refactoring code as new requirements emerged
* Working with JSON files for persistent storage
* Separating storage, processing, and presentation concerns
* Thinking more carefully about data modeling and program structure
* Identifying and reducing duplication in code
* Debugging programs that operate across multiple modules

One of the most important lessons from this project was realizing that the choice of data structure can significantly affect how easy or difficult the rest of the program becomes to implement.

## Possible Future Improvements

The project is currently functional, but several improvements are planned for future iterations:

* Record dates and timestamps for study sessions
* Validate study duration input and handle invalid values gracefully
* Improve average session formatting and numerical precision
* Prevent invalid subject names (e.g., subjects consisting only of digits)
* Handle empty user input more robustly
* Add the ability to remove subjects
* Improve the command-line interface and overall user experience
* Expand error handling throughout the application
* Add automated tests for core functionality
* Generate more detailed study analytics and reporting features

These improvements would make the application more reliable, easier to use, and better suited for long-term study tracking.

## Purpose

This project was built as a personal learning project before starting college. It represents my progression from creating simple command-line utilities toward designing programs that store, process, and present information in a structured way.

The project focuses on strengthening fundamental programming concepts, data modeling, modular design, and problem-solving skills through practical implementation.
