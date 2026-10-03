# Quick Python tutorial

This guide gets Quick Python running and walks you through your first programs.

- [1. Check you have Python and tkinter](#1-check-you-have-python-and-tkinter)
- [2. Download Quick Python](#2-download-quick-python)
- [3. Start the app](#3-start-the-app)
- [4. Tour of the window](#4-tour-of-the-window)
- [5. Your first programs](#5-your-first-programs)
- [6. Saving and opening files](#6-saving-and-opening-files)
- [Troubleshooting](#troubleshooting)

---

## 1. Check you have Python and tkinter

Open a terminal (Windows: *Command Prompt* or *PowerShell*; macOS: *Terminal*) and run:

```bash
python --version
python -m tkinter
```

- The first line should print `Python 3.8` or newer. If `python` isn't found, try `python3` (macOS/Linux) or `py` (Windows) and use that word from now on.
- The second line should open a tiny test window. Close it. If you get an error instead, install tkinter:
  - **Windows / macOS:** reinstall Python from <https://www.python.org/downloads/> (it includes tkinter).
  - **Debian / Ubuntu:** `sudo apt install python3-tk`
  - **Fedora:** `sudo dnf install python3-tkinter`
  - **macOS with Homebrew Python:** `brew install python-tk`

## 2. Download Quick Python

**With git:**

```bash
git clone https://github.com/npcrit5-AI-pro/Quick-Python.git
cd Quick-Python
```

**Without git:** on GitHub click **Code → Download ZIP**, unzip it, and open a terminal in that folder.

There is nothing to `pip install`.

## 3. Start the app

```bash
python main.py
```

A window called **Python Runner** opens with some sample code already in the editor.

## 4. Tour of the window

- **Top buttons:** `▶ Run (Ctrl+Enter)`, `Clear Output`, `Clear Editor`, `💾 Save`, `📂 Open`
- **Left pane, 📝 Code Editor:** type your Python here. Tab inserts 4 spaces. Ctrl+Z undoes.
- **Right pane, 📤 Output:** each run prints a `▶ Executing...` banner, then your program's output and any error messages.
- **Middle divider:** drag it to make either side bigger.
- **Bottom status bar:** says `Running...` while your code runs and `Ready` when it's done.

## 5. Your first programs

Click in the editor, delete the sample code, type a program, and press **Ctrl+Enter**.

### Hello world

```python
print("Hello, World!")
```

### Asking for input

```python
name = input("What's your name? ")
print(f"Nice to meet you, {name}!")
```

A small **Input Required** window pops up. Type your name and click **OK**. (Don't click Cancel. See [Troubleshooting](#troubleshooting).)

### Loops and math

`math`, `random`, and `time` are already loaded for you:

```python
for i in range(1, 6):
    print(f"{i} squared is {i**2}, square root is {math.sqrt(i):.2f}")

print("Dice roll:", random.randint(1, 6))
```

### Errors

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught error: {e}")

print(undefined_name)  # this one is not caught
```

The first error is handled by your code. The second shows a full traceback in the Output pane, so you can see the line that failed.

### Turtle drawing

```python
t = turtle.Turtle()
t.speed(0)
for i in range(36):
    t.forward(100)
    t.left(170)
turtle.done()
```

A separate turtle window opens and draws a star. Close it when you're finished.

## 6. Saving and opening files

- **💾 Save** (Ctrl+S) asks where to save the code as a `.py` file. The window title changes to show the file name.
- **📂 Open** (Ctrl+O) loads a `.py` file into the editor (it replaces what's there).
- **Clear Editor** empties the editor and forgets the file name, so the next save asks for a new name.

Files saved here are normal Python files. You can also run them outside the app with `python yourfile.py`.

---

## Troubleshooting

**The app froze after an input pop-up**
If you click **Cancel** (or close the pop-up), the app keeps waiting for an answer and stops responding. Close the app window (or press Ctrl+C in the terminal) and start it again. Always answer input pop-ups with **OK**.

**My program printed nothing**
Output only appears when the program finishes. If it is still running (a big loop, `time.sleep`, or an infinite loop), wait or close the app to stop it. There is no Stop button yet.

**"No module named tkinter"**
See [step 1](#1-check-you-have-python-and-tkinter) for how to install tkinter on your system.

**Ctrl+S / Ctrl+O / Ctrl+Enter don't work**
The shortcuts only work while the code editor has focus. Click inside the editor first, or use the buttons.

**My code works in normal Python but not here**
Your code runs inside the app's own Python process, so a few things behave differently:
- Calling `sys.exit()` or `exit()` ends your program early, its output is not shown, and the status bar stays on `Running...`.
- Code that creates its own `tkinter` windows can clash with the app's window.
- Output only appears at the end (see above).

For those programs, save the file and run it from a terminal with `python yourfile.py`.
