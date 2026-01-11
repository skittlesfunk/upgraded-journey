# upgraded-journey
"Python data cleaning engine using human-in-the-loop validation to sort and audit raw text data into structured CSV outputs."

# Interactive Math Data Cleaner

### 📌 Project Overview
This is a Python-based utility designed to merge, clean, and validate data from two different sources: a raw `.txt` file and a Python list. It uses a "Human-in-the-Loop" verification system (a math game) to ensure data accuracy before saving it to a final record.

The project demonstrates core data engineering concepts like **data transformation**, **real-time file flushing**, and **audit logging**.

### 🚀 Features
* **Dual-Source Integration:** Seamlessly combines data from a text file and a static list using `zip`.
* **Safety First:** Includes a `try/except` safety net to handle non-numeric user input without crashing.
* **Real-Time Updates:** Uses the `flush()` method so you can watch the CSV files update in your spreadsheet viewer line-by-line.
* **Audit Trail:** Every record is stamped with a high-resolution timestamp to track exactly when the data was processed.
* **Automatic Sorting:** Correct entries are saved to `data1.csv`, while mistakes are sent to `data2.csv` for later review.

### 🛠️ How to Use
1.  **Setup:** Ensure you have a `data.txt` file in the same directory as the script.
2.  **Run:** Execute the script in your terminal: `python script.py`.
3.  **Validate:** The program will prompt you with math problems based on the merged data.
4.  **Results:** Check your folder for two generated CSV files containing your cleaned and sorted data.

### 📂 File Structure
* `data.txt` — Raw input data (one value per line)
* `script.py` — Main cleaning & validation logic
* `README.md` — Project documentation

### 🛣️ Roadmap (Next Steps)
I am currently transitioning this project from a procedural script to a more scalable architecture.
* **Phase 3: OOP Refactoring** – Moving the logic into a `GameSession` class to handle state and file writers more efficiently.
* **Dynamic Rule Engine** – Implementing "FizzBuzz" style logic where operators change dynamically.
* **Performance Metrics** – Adding a summary report showing accuracy percentage at the end of each session.

### 👋 Contributions & Feedback
I am a self-taught developer focused on building scalable data tools. I am open to **recommendations** or **code reviews**, specifically regarding:
* Transitioning from scripts to **Object-Oriented Programming (OOP)**.
* Optimizing file I/O operations.
