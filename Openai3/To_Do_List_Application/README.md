---

# To-Do List Application

This To-Do List Application is a simple web-based tool to help you manage your tasks effectively.

## Features

- Add, edit, and delete tasks.
- Mark tasks as completed.
- Filter tasks by status (completed or pending).
- Sort tasks by priority, due date, or creation date.
- Responsive design for seamless usage across devices.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd ToDo-List-Application
    ```

3. Set up a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment (for Windows):

    ```bash
    venv\Scripts\activate
    ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    flask run
    ```

   or

    ```bash
    python -m flask run
    ```

2. Open a web browser and go to `http://127.0.0.1:5000/` to access the To-Do List application.

## Project Structure

- `app.py`: Main Flask application file.
- `templates/`: Directory containing HTML templates for the web application.
- `static/`: Directory containing static files such as CSS, JavaScript, and images.
- `venv/`: Virtual environment directory (ignored by version control).

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/my-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/my-feature`).
6. Create a new Pull Request.
