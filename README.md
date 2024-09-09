**KeystrokeML-Snippet** is a web snippet example that collects data from a user attempting to log in. The data is processed using machine learning, which allows distinguishing the user based on how they type their password, differentiating them from other users.

### Project Overview
- **Web Snippet**: A small JavaScript snippet with login form, sends the typing data in real time.
- **Flask Backend**: A Python-based Flask server handles the incoming data from the web snippet and processes it through the machine learning model to determine the user's identity.
- **Machine Learning Model**: Using `scikit-learn`, we trained a model to analyze keystroke patterns and classify them as authentic or not.
----
![Selection_604](https://github.com/user-attachments/assets/4ce8bf7a-7f94-4d40-8dfb-f5c44d6b1ee3)

----

### Getting Started
1. **Clone the repository**:
    ```bash
    git clone https://gitlab.com/tier61wro/KeystrokeML_WebSnippet.git 
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
