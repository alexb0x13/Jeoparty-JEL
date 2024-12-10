# Jeoparty Game

![image](https://github.com/user-attachments/assets/2a1603df-6564-406e-b04e-ed74ceccecf2)

### Bringing the "party" to Jeopardy
A Flask-based Jeopardy-style game application for classroom use. This web application allows teachers to create and manage their own Jeopardy-style quiz games with custom categories and questions.

## Features

- Interactive game board with classic Jeopardy styling
- Admin interface for managing categories and questions
- Custom question values ($200-$1000)
- Simple authentication system
- Easy-to-use interface for adding categories and questions
- Reset functionality to start fresh games

## Prerequisites

- Python 3.7+
- Flask 2.3.3
- Flask-Login
- Werkzeug

## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd myJeopartyGame
```

2. Install the required packages:
```bash
pip install flask==2.3.3 flask-login werkzeug
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5001
```

3. Login with default credentials:
- Username: admin
- Password: admin

## Usage

1. Log in as admin
2. Go to the Admin Panel to:
   - Add categories
   - Add questions to categories
   - Reset the game when needed
3. Return to the main page to play the game
4. Click on dollar values to reveal questions
5. Click "Show Answer" to reveal answers

## Note

This application uses in-memory storage, so all data will be reset when the server restarts. This is designed for local classroom use.

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.
