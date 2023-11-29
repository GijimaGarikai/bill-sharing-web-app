Flatmates Bill Splitter

This simple Flask application helps you split bills among flatmates based on the number of days each person spent in the house. The application provides a web interface for users to input bill details and calculate how much each flatmate owes.

## Prerequisites

Make sure you have the following dependencies installed:

- Flask
- WTForms

You can install them using the following command:

```bash
pip install Flask WTForms
```

## Usage

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd <project-directory>
```

3. Run the application:

```bash
python <filename>.py
```

Replace `<filename>` with the name of the Python file containing your application code.

4. Open your web browser and go to `http://127.0.0.1:5000/` to access the application.

## Features

### Home Page

- Access the home page at the root URL (`/`).
- Simply serves as an entry point to the application.

### Bill Form Page

- Access the bill form page at `/bill`.
- Input the bill amount, bill period, names of flatmates, and the number of days each flatmate spent in the house.
- Click the "Calculate" button to submit the form.

### Results Page

- Access the results page at `/results`.
- Displays the calculated amounts each flatmate owes based on the provided information.
 representing flatmates and bills.

