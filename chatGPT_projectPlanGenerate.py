import csv
import random
import datetime
import string
import os

# Set the number of tasks to generate
num_tasks = 10

# Set the range for created dates
start_date = datetime.date(2022, 11, 1)
end_date = datetime.date.today()
date_range = (end_date - start_date).days

# Generate a list of random words
words = ["SpinVR", "FidgetSpin", "VirtualReality", "VR", "TechStartup", "Innovate", "R&D", "BetaTest", "Launch", "Gamify"]
action_words = ["User", "Abstract", "Reporting", "Audit", "Approval"]
task_words = ["Feature", "Defect", "Task", "Requirements", "Decision", "Risk", "Meeting", "Deployment"]
status = ["To Do", "In Progress", "Done"]

# Read the list of assignees from a CSV file, if it exists
assignees = []
assignee_file = 'assignees.csv'
if os.path.exists(assignee_file):
    with open(assignee_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            assignees.append(row[0])
else:
    print("Warning: Assignee file not found, assignee column will be blank.")

# Generate a list of tasks
tasks = []
for i in range(num_tasks):
    first_word = random.choice(words)
    second_word = random.choice(action_words)
    third_word = random.choice(task_words)
    title = f"{first_word} {second_word} {third_word}"
    summary = " ".join(random.choices(words, k=random.randint(5, 10)))
    created_date = start_date + datetime.timedelta(days=random.randint(0, date_range))
    task_status = random.choice(status)
    if assignees:
        assignee = random.choice(assignees)
    else:
        assignee = ""
    if task_status == "Done":
        completed_date = created_date + datetime.timedelta(days=random.randint(1, 30))
        resolution = "Done"
    else:
        completed_date = ""
        resolution = ""
    tasks.append([title, summary, created_date, completed_date, assignee, task_status, resolution])

# Write the list of tasks to a CSV file
with open('project_plan.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Summary", "Created Date", "Completed Date", "Assignee", "Status", "Resolution"])
    writer.writerows(tasks)
