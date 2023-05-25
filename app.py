import threading
from flask import Flask
import schedule
import time
import requests
import json

app = Flask(__name__)

# Load the questions from the JSON files
with open('dsa_basic.json') as f:
    strings_data = json.load(f)

questions = strings_data['questions']

# Function to select three random questions
selected_questions = questions
question_count = 0

# Function to send questions to Discord webhook
def send_questions():
    payload = {
        'embeds': [
            {
                'title':f'\n\nQuestion 1 :\n\n',
                'description':f'**{selected_questions[question_count]["question"]}**\n**Explanation**\n{selected_questions[question_count]["explanation"]}\n**Input**\n```{selected_questions[question_count]["input"]}```\n**Output**\n```{selected_questions[question_count]["output"]}```',
                'color':'16776960',
            },
            {
                'title':f'\n\nQuestion 2 :\n\n',
                'description': f'**{selected_questions[question_count+1]["question"]}**\n**Explanation**\n{selected_questions[question_count+1]["explanation"]}\n**Input**\n```{selected_questions[question_count+1]["input"]}```\n**Output**\n```{selected_questions[1]["output"]}```',
                'color':'204'
            },
            {
                'title':f'\n\nQuestion 3 :\n\n',
                'description': f'**{selected_questions[question_count+2]["question"]}**\n**Explanation**\n{selected_questions[question_count+2]["explanation"]}\n**Input**\n```{selected_questions[question_count+2]["input"]}```\n**Output**\n```{selected_questions[question_count+2]["output"]}```',
                'color':'32768',
            }
        ]

    }
    # Send the payload to the Discord webhook
    webhook_url = 'https://discord.com/api/webhooks/1110440444724256779/7aT9Eiv7zYC0tWPDFiTJHBcjYMewUUil0WBOlP6OoTj9RSTdeaNc8DQn4LCV01dBj-EJ'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(webhook_url, headers=headers, json=payload)
    if response.status_code == 204:
        print('Questions sent successfully.')
    else:
        print(f'Failed to send questions. Status code: {response.status_code}')

# Function to send answers to Discord webhook
def send_answers():
    payload = {
        'embeds': [
            {
                'title': 'Today\'s Answers 1',
                'description': f'Explanation:\n**Code Explanation**\n{selected_questions[question_count]["explanation_code"]}\n\n**Python Code:**\n{selected_questions[question_count]["python"]}\n\n**Cpp Code:**\n{selected_questions[question_count]["cpp"]}\n\n**Java Code:**\n{selected_questions[question_count]["java"]}',
                'color':'16776960'
            }
        ]
    }
    # Send the payload to the Discord webhook
    webhook_url = 'https://discord.com/api/webhooks/1110440444724256779/7aT9Eiv7zYC0tWPDFiTJHBcjYMewUUil0WBOlP6OoTj9RSTdeaNc8DQn4LCV01dBj-EJ'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(webhook_url, headers=headers, json=payload)
    if response.status_code == 204:
        print('Answers sent successfully.')
    else:
        print(f'Failed to send answers. Status code: {response.status_code}')


def send_answers121():
    payload = {
        'embeds': [
            {
                'title': 'Today\'s Answers 2',
                'description': f'Explanation:\n**Code Explanation**\n{selected_questions[question_count+1]["explanation_code"]}\n\n**Python Code:**\n{selected_questions[question_count+1]["python"]}\n\n**Cpp Code:**\n{selected_questions[question_count+1]["cpp"]}\n\n**Java Code:**\n{selected_questions[question_count+1]["java"]}',
                'color':'204'
            }
        ]
    }
    # Send the payload to the Discord webhook
    webhook_url = 'https://discord.com/api/webhooks/1110440444724256779/7aT9Eiv7zYC0tWPDFiTJHBcjYMewUUil0WBOlP6OoTj9RSTdeaNc8DQn4LCV01dBj-EJ'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(webhook_url, headers=headers, json=payload)
    if response.status_code == 204:
        print('Answers sent successfully.')
    else:
        print(f'Failed to send answers. Status code: {response.status_code}')


def send_answers221():
    payload = {
        'embeds': [
            {
                'title': 'Today\'s Answers 3',
                'description': f'Explanation:\n**Code Explanation**\n{selected_questions[question_count+2]["explanation_code"]}\n\n**Python Code:**\n{selected_questions[question_count+2]["python"]}\n\n**Cpp Code:**\n{selected_questions[question_count+2]["cpp"]}\n\n**Java Code:**\n{selected_questions[question_count+2]["java"]}',
                'color':'32768'
            }
        ]
    }
    # Send the payload to the Discord webhook
    webhook_url = 'https://discord.com/api/webhooks/1110440444724256779/7aT9Eiv7zYC0tWPDFiTJHBcjYMewUUil0WBOlP6OoTj9RSTdeaNc8DQn4LCV01dBj-EJ'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(webhook_url, headers=headers, json=payload)
    if response.status_code == 204:
        print('Answers sent successfully.')
    else:
        print(f'Failed to send answers. Status code: {response.status_code}')

def increseCount():
    global question_count
    question_count += 4
    print(question_count)

schedule.every().day.at('09:00').do(send_questions)
schedule.every().day.at('16:00').do(send_answers)
schedule.every().day.at('16:00').do(send_answers121)
schedule.every().day.at('16:00').do(send_answers221)
schedule.every().day.at('16:05').do(increseCount)



# Run the scheduled tasks
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)


# Run the Flask application
if __name__ == '__main__':
    schedule_thread = threading.Thread(target=run_schedule)
    schedule_thread.start()
    app.run()
