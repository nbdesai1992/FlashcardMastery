# FlashcardMastery

FlashcardMastery is a comprehensive educational tool leveraging OpenAI to enable dynamic flashcard creation, spaced repetition learning, and simulated exam question generation, built on Django.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Flashcard Creation and Management:** Easily create, manage, and categorize flashcards.
- **Spaced Repetition Learning:** Learn efficiently using the same spaced repetition algorithm as Anki.
- **Simulated Exam Question Generation:** Utilize OpenAI to simulate exam questions based on flashcards.
- **User Accounts:** Manage your progress with user accounts, with support for password resets.



To provide instructions for users to start and use the app, we need to cover the basic setup, initial configuration, and running the app itself. Here's what you might include in the `Getting Started` and `Usage` sections of your `README.md`:

### Getting Started

**Prerequisites:**

1. Ensure you have Python (version X.X or newer) installed.
   - You can verify your Python version with `python --version` or `python3 --version`.

2. It's recommended to have `virtualenv` installed to manage project dependencies separately.
   - Install it with: `pip install virtualenv` or `pip3 install virtualenv`.

**Installation and Setup:**

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/FlashcardMastery.git
   ```

2. Navigate to the project directory:
   ```bash
   cd FlashcardMastery
   ```

3. Set up a virtual environment (optional but recommended):
   ```bash
   make venv
   ```

4. Activate the virtual environment:
   ```bash
   source FlashcardMastery_venv/bin/activate  # On Windows, use: .\FlashcardMastery_venv\Scripts\activate
   ```

5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Apply migrations to set up the database:
   ```bash
   make migrate
   ```

2. Run the Django development server:
   ```bash
   make run
   ```

3. Open a web browser and navigate to `http://127.0.0.1:8000/` to start using the `FlashcardMastery` app.

4. (Optional) To access the admin dashboard, create a superuser:
   ```bash
   make createsuperuser
   ```
   Then navigate to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials.

5. When finished, deactivate the virtual environment:
   ```bash
   deactivate
   ```

## Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Can adapt the URLs, user names, and other specific details as needed. I will create additional markdown files such as `CONTRIBUTING.md` and `LICENSE` as they are referenced in the `README.md`.