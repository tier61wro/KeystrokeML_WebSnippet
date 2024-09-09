**KeystrokeML-Snippet** is a project that uses machine learning to identify users based on their typing patterns, also known as keystroke dynamics. 
By tracking the way a user interacts with the keyboard, we can build a unique profile to verify their identity.

### Project Overview
- **Web Snippet**: A small JavaScript snippet is embedded into any webpage to collect the typing data in real time.
- **Keystroke Dynamics**: This project collects data on how long keys are pressed and the timing between key presses. These subtle patterns differ from person to person, which allows us to use them for identification.
- **Flask Backend**: A Python-based Flask server handles the incoming data from the web snippet and processes it through the machine learning model to determine the user's identity.
- **Machine Learning Model**: Using `scikit-learn`, we trained a model to analyze keystroke patterns and classify them as authentic or not.


### Getting Started
1. **Clone the repository**:
    ```bash
    git clone https://gitlab.com/username/keystrokeml-snippet.git
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask server**:
    ```bash
    python3 app.py
    ```

4. **Open the web snippet page** just open main_site_page.html from folder in your browser, and type some pass to form samples.txt file

### Technology Stack
- **JavaScript**: Used for the web snippet that collects keystroke timing data in the browser.
- **Python & Flask**: The backend server processes keystroke data and interacts with the machine learning model.
- **Pandas & Numpy**: For data manipulation and feature extraction from the keystroke data.
- **Scikit-learn**: The machine learning library used to train and evaluate the keystroke dynamics model.
