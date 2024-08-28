# Autofilling PDF files for visa application (v1)

## Description
Form Progress Saver is a simple Flask application that allows users to save and load their form progress without the need for a database. This is useful for applications where users may need to return later to complete a form.

## Features
- Save form progress using sessions
- Load form progress from sessions
- Simple and easy to integrate

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/form-progress-saver.git
    ```
2. Navigate to the project directory:
    ```sh
    cd form-progress-saver
    ```
3. Create a virtual environment:
    ```sh
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    ```sh
    source venv/bin/activate
    ```
5. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Run the Flask application:
    ```sh
    python app.py
    ```
2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Endpoints
- `GET /`: Renders the form page.
- `POST /save_progress`: Saves the form progress to the session.
- `GET /load_progress`: Loads the form progress from the session.

## Technologies
- Python
- Flask
- Flask-Session

## Contributing
1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```sh
    git commit -m "Description of changes"
    ```
4. Push to the branch:
    ```sh
    git push origin feature-branch
    ```
5. Create a pull request.

## License
This project is licensed under the MIT License.
