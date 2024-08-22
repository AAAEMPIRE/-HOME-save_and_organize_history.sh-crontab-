{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNqGdDIeLQStN/2zZKELLMP",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AAAEMPIRE/-HOME-save_and_organize_history.sh-crontab-/blob/main/tasks_automation_.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "G3mdDMH37G60"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Necessary Imports\n",
        "import requests  # For making API requests\n",
        "from datetime import datetime  # For handling dates and times\n",
        "from googleapiclient.discovery import build  # For interacting with Google APIs\n",
        "from google.oauth2 import service_account  # For authentication\n",
        "\n",
        "# Google Calendar API Setup\n",
        "SCOPES = ['https://www.googleapis.com/auth/calendar']\n",
        "SERVICE_ACCOUNT_FILE = 'your_service_account_credentials.json' # Replace with your actual file\n",
        "\n",
        "credentials = service_account.Credentials.from_service_account_file(\n",
        "        SERVICE_ACCOUNT_FILE, scopes=SCOPES)\n",
        "\n",
        "service = build('calendar', 'v3', credentials=credentials)\n",
        "\n",
        "# Task Retrieval (Example using a hypothetical Task API)\n",
        "def get_tasks():\n",
        "    # Replace with the actual API endpoint and parameters for your task management system\n",
        "    response = requests.get('https://api.yourtaskmanager.com/tasks',\n",
        "                            params={'status': 'incomplete'})\n",
        "    response.raise_for_status()  # Raise an exception for bad responses\n",
        "    return response.json()['tasks']\n",
        "\n",
        "# Calendar Event Creation\n",
        "def create_calendar_event(task):\n",
        "    event = {\n",
        "        'summary': task['title'],\n",
        "        'description': task['description'],\n",
        "        'start': {\n",
        "            'dateTime': task['due_date'],  # Assuming your task API provides due dates in ISO format\n",
        "            'timeZone': 'America/Los_Angeles',  # Adjust to your timezone\n",
        "        },\n",
        "        'end': {\n",
        "            'dateTime': task['due_date'],  # You might want to add some buffer time here\n",
        "            'timeZone': 'America/Los_Angeles',\n",
        "        },\n",
        "        'reminders': {\n",
        "            'useDefault': False,\n",
        "            'overrides': [\n",
        "                {'method': 'email', 'minutes': 24 * 60},  # 1 day before\n",
        "                {'method': 'popup', 'minutes': 60},  # 1 hour before\n",
        "            ],\n",
        "        },\n",
        "    }\n",
        "\n",
        "    event = service.events().insert(calendarId='primary', body=event).execute()\n",
        "    print(f'Event created: {event.get(\"htmlLink\")}')\n",
        "\n",
        "# Main Execution\n",
        "if __name__ == '__main__':\n",
        "    tasks = get_tasks()\n",
        "    for task in tasks:\n",
        "        create_calendar_event(task)"
      ],
      "metadata": {
        "id": "AmsVBOb47gXo"
      }
    }
  ]
}