# Study Tracker

A simple Python command-line tool to log your study sessions across different subjects. I built it to log my studies without having to pay any subscription just to get the simple features.

---

## 🧠 What I Learned

Building this helped me move past simple scripts and practice cleaner, more logical coding:

* **Handling Data Structures:** Learned how to use a list of dictionaries to easily append new study sessions to specific subjects.
* **Smart Input Loops:** Figured out how to handle both numbers (selecting an existing subject index) and text (typing a name to find or create a subject) in the same prompt.
* **Modular Code:** Split the main app loop (`main.py`) from the helper functions (`stats.py`) to keep things organized instead of dumping everything into one giant file.

---

## 🕹️ How to Use

1. **Run the script:**
   ```bash
   python main.py


2. **Interact with the menu options:**
* **1. Log study:** If the tracker is empty, type a name to create your first subject. Once you have subjects saved, you can type their number to select them, or type a brand-new name to create a new one on the fly.
   * **2. View report:** See the data collected so far.
   * **3. EXIT:** Close the tracker.

---

## 💻 How It Works

The script runs a continuous loop and processes input based on what you type:

* **First-time Run:** If no subjects exist yet, it automatically prompts you to create one so the script has data to work with.
* **Smart Choices:** When you log time, the app checks if you entered a number or text:
    * **If it's a number:** It checks if the number matches a subject on the list and logs your minutes there.
    * **If it's text:** It searches your existing subjects. If it finds a match, it adds the minutes; if it's a new name, it creates a new subject automatically.

---

## 🛠️ Current Status (Beta)

> ⚠️ **Note:** The core logic for tracking and saving your minutes works great. However, the "View report" option currently just prints out the raw, ugly list/dictionary format. Cleaning this up into a nice summary dashboard is the main focus for the next update.

---

## 🗂️ Files

* `main.py` – Handles the main menu loop and user inputs.
* `stats.py` – Houses the helper functions (`create_sub`, `isNumber`) to keep the main code clean.
* `visual.md` – *(Optional)* Not needed to run the code. Just a personal blueprint I use to reference how I want the final layout to look and behave.

---