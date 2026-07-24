# AI Support Ticket Triage Agent

## About the Project

This project is a Support Ticket Triage Agent developed in Python. It reads customer support tickets from a CSV file and automatically classifies each ticket into a category, assigns a priority, provides a confidence score, and routes it to the appropriate support team.

The main goal of this project is to reduce manual effort in handling customer support tickets and make the ticket management process faster and more organized.

## Features

- Reads support tickets from a CSV file
- Classifies tickets into different categories
- Assigns High, Medium, or Low priority
- Generates a confidence score
- Routes tickets to the correct support team
- Saves the results to an output CSV file

## Technologies Used

- Python
- Pandas
- CSV

## Project Files

- `ticket_classifier.py` – Main program
- `test_ticket_classifier.py` – Test cases
- `sample_tickets.csv` – Sample input data
- `output.csv` – Generated output
- `requirements.txt` – Required Python libraries

## How to Run

Clone the repository:

```bash
git clone https://github.com/Anitapoojari/AI-Support-Ticket-Triage-Agent.git
```

Move into the project folder:

```bash
cd AI-Support-Ticket-Triage-Agent
```

Install the required library:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python ticket_classifier.py
```

Run the tests:

```bash
python test_ticket_classifier.py
```

## Sample Input

The input file contains support tickets with the following columns:

- Subject
- Description

## Sample Output

The generated output contains:

- Category
- Priority
- Confidence Score
- Routing Team

## Challenges Faced

While developing this project, I focused on creating a simple and understandable rule-based classification system. Choosing suitable keywords for each ticket category and assigning appropriate priorities required careful testing and refinement.

## Future Improvements

- Add AI/LLM-based ticket classification
- Build a simple web interface
- Store ticket data in a database
- Improve the confidence scoring system

 ##Author

**Anita Poojari**

GitHub: https://github.com/Anitapoojari/AI-Support-Ticket-Triage-Agent
