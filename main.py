import random
import pickle

def vote(tasks):
    task1, task2 = random.sample(sorted(tasks), 2)

    answer = input(f"Choose from 1 - {task1}, 2 - {task2}, 3 - tie: ")
    if answer == "1":
        result = 1
    elif answer == "2":
        result = 0
    elif answer == "3":
        result = 0.5
    else:
        return

    k = 16
    task1_rating = tasks[task1]
    task2_rating = tasks[task2]
    expected = 1 / (1 + (10 ** ((tasks[task2] - tasks[task1]) / 400.)))
    tasks[task1] += k * (result - expected)
    tasks[task2] -= k * (result - expected)
        

def main():
    tasks = {}

    try:
        with open('tasks.pkl', 'rb') as f:
            tasks = pickle.load(f)
    except:
        pass

    while True:
        try:
            command = input("Enter command: ").strip()
            if command == "exit":
                print("Exiting the program.")
                break

            command_parts = command.split()
            action = command_parts[0]

            if action == "add":
                task_name = " ".join(command_parts[1:])
                tasks[task_name] = 1200
            elif action == "list" and len(tasks) > 0:
                print(f"{'Task':<20}{'Score':<20}")
                for key, value in reversed(sorted(tasks.items(), key=lambda item: item[1])):
                    print(f"{key:<20}{int(value):<20}")
            elif action == "vote" and len(tasks) >= 2:
                for i in range(10):
                    vote(tasks)
                with open('tasks.pkl', 'wb') as f:
                    pickle.dump(tasks, f)
            else:
                print("Invalid command.")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting the program.")
            break

if __name__ == "__main__":
    main()
