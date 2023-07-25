import os
import pickle
import pyttsx3
from colorama import Fore, Style


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  #
engine.setProperty('rate', 173)  
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Define functions
def add_task(task):
    tasks.append({'name': task, 'done': False})
    print(Fore.GREEN + "Task successfully added to the list.")
    speak("Task successfully added to the list.")


def remove_task(task):
    for t in tasks:
        if t['name'] == task:
            tasks.remove(t)
            print(Fore.GREEN + "Task successfully removed from the list.")
            speak("Task successfully removed from the list.")
            return

    print(Fore.RED + "No task with this name is in the list.")
    speak("No task with this name is in the list.")


def show_tasks():
    if len(tasks) == 0:
        print(Fore.YELLOW + "There are no tasks in the list.")
        speak("There are no tasks in the list.")
    else:
        print(Fore.GREEN + "List of tasks:")
        speak("List of tasks:")
        for task in tasks:
            status = Fore.GREEN + "Done" if task['done'] else Fore.RED + "Not done"
            print(Fore.BLUE + f"- {task['name']} ({status})")
            speak(f"{task['name']} ({status})")
        if all(task['done'] for task in tasks):
            tasks.clear()
            print(Fore.YELLOW + "All tasks are done and have been removed from the list.")
            speak("All tasks are done and have been removed from the list.")
            


def save_tasks():
    with open('tasks.pkl', 'wb') as f:
        pickle.dump(tasks, f)

    with open('task.txt', 'w') as f:
        for task in tasks:
            f.write(task['name'] + '\n')


def load_tasks():
    if os.path.exists('tasks.pkl'):
        with open('tasks.pkl', 'rb') as f:
            tasks = pickle.load(f)
    else:
        tasks = []

    if os.path.exists('task.txt'):
        with open('task.txt', 'r') as f:
            for line in f:
                task_name = line.strip()
                task_exist = False
                for task in tasks:
                    if task['name'] == task_name:
                        task_exist = True
                        break
                if not task_exist:
                    tasks.append({'name': task_name, 'done': False})

    return tasks


# Load task list from file
tasks = load_tasks()

# Start main loop of the program
while True:
    print("Please choose an option:")
    speak("Please choose an option:")
    print("1. Add a task")
    speak("1. Add a task")
    print("2. Show tasks")
    speak("2. Show tasks")
    print("3. Remove a task")
    speak("3. Remove a task")
    print("4. Mark a task as done")
    speak("4. Mark a task as done")
    print("5. Exit")
    speak("5. Exit")
    choice = input("Enter your choice: ")
    

    if choice == '1':
        speak("Enter task name ")
        task_name = input("Enter task name: ")
        add_task(task_name)
        save_tasks()

    elif choice == '2':
        show_tasks()
        speak("Here are the list of tasks:")
        for task in tasks:
            if task['done']:
                print(Fore.BLUE + f"- {task['name']} (Done)")
                speak(f"{task['name']} Done")
            else:
                print(Fore.BLUE + f"- {task['name']}")
                speak(f"{task['name']}")
                

    elif choice == '3':
        speak("Enter task name ")
        task_name = input("Enter task name: ")
        remove_task(task_name)
        save_tasks()

    elif choice == '4':
        speak("Enter task name ")
        task_name = input("Enter task name: ")
        task_exist = False
        for task in tasks:
            if task['name'] == task_name:
                task['done'] = True
                task_exist = True
                print(Fore.GREEN + "Task marked as done.")
                speak("Task marked as done.")
                break
        if not task_exist:
            print(Fore.RED + "No task with this name is in the list.")
            speak("No task with this name is in the list.")
        save_tasks()
    elif choice == "5":
        
        print(Fore.GREEN + "Goodbye!")
        speak("Goodbye!")
        break
    else:
        print(Fore.RED + "Invalid choice. Please try again.")
        speak("Invalid choice. Please try again.")
    