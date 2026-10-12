# CodeOrbit Rule-Based Chatbot

## Project Overview
CodeBot is a simple rule-based chatbot developed as part of the CodeOrbit Tech Artificial Intelligence Internship. It interacts with users by identifying keywords and responding according to predefined rules.

## Features
- Responds to common greetings.
- Answers basic questions about itself.
- Provides internship-related information.
- Responds to help requests.
- Displays a fallback response for unknown inputs.
- Exits when the user types "bye" or "goodbye".

## Technologies Used
- Python 3
- Conditional statements (`if`, `elif`, `else`)
- String handling
- User input and output

## How to Run
1. Install Python 3.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

   `python chatbot.py`

## Sample Interaction

**User:** hello  
**CodeBot:** Hello! How can I help you?

**User:** what is your name  
**CodeBot:** My name is CodeBot. I'm a simple rule-based chatbot.

**User:** bye  
**CodeBot:** Goodbye! Have a great day!

## How It Works
The chatbot converts user input to lowercase and checks for predefined keywords using conditional statements. It returns a matching response or a fallback message when no rule matches.

## Learning Outcomes
- Understanding basic chatbot logic.
- Using conditional statements in Python.
- Processing user input.
- Implementing keyword-based response handling.
