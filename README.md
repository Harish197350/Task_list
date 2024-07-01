# Task List Application

## Description

This is a simple Task List application built using Python and the Tkinter library. The application allows users to manage their tasks efficiently with features to add, delete, and view tasks. The interface is user-friendly with numbered tasks and alternating row colors for better readability.

## Features

- **Add Task**:
  - Input a new task in the text entry field and add it to the list.
  - Tasks are displayed with a unique number indicating their position in the list.

- **Delete Task**:
  - Select a task from the list and remove it.
  - Task numbering updates accordingly to reflect the current order.

- **Clear All Tasks**:
  - Clear all tasks from the list with a single button press.

## Prerequisites

- Python 3.x
- Tkinter (comes pre-installed with Python)

## Installation

1. Clone the repository or download the `tasklist.py` file.
    ```sh
    git clone https://github.com/yourusername/tasklist-app.git
    cd tasklist-app
    ```

2. Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where the `tasklist.py` file is located.
3. Run the application by executing the following command:
    ```sh
    python tasklist.py
    ```

## Code Overview

The main components of the application include:

- **Task Listbox and Scrollbar**:
  - The Listbox widget is used to display the list of tasks.
  - The Scrollbar widget is linked to the Listbox for scrolling through tasks.

- **Entry Widget**:
  - An Entry widget is provided for users to input tasks.

- **Buttons**:
  - **Add Task** button: Adds the task from the Entry widget to the task list.
  - **Delete Task** button: Deletes the selected task from the task list.
  - **Clear All Tasks** button: Clears all tasks from the task list.

- **Task Management**:
  - `add_task()`: Adds a task to the list if the entry is not empty.
  - `delete_task()`: Deletes the selected task from the list.
  - `clear_tasks()`: Clears all tasks from the list.
  - `update_task_listbox()`: Updates the Listbox with the current tasks, applying alternating colors and numbering.



## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Tkinter documentation: https://docs.python.org/3/library/tkinter.html

