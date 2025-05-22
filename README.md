# ⌚️ Work Break Timer (Pomodoro Style)

A simple desktop application that helps you stay productive and healthy by applying the **Pomodoro Technique** – alternating between focused work sessions and short breaks, with sound alerts and an easy-to-use GUI.

## 📟 Features

- 25-minute work session timer 
- 5-minute break session timer 
- Simple graphical interface using `tkinter`
- Start, Pause, and Reset buttons
- Bell sound when each session ends and session begin (`self.root.bell()`)

## 🖼️ GUI Preview

When you run the app, a window will appear showing:

- A message indicating the current session (Work time / Break time)
- A countdown timer
- Buttons: **Start**, **Pause**, and **Reset**

## 📖 How to Use

1. Click **Start** to begin a 25-minute work session.
2. When the work session ends:
   - A 2 short **bell sound** will play.
   - A 5-minute break session begins automatically.
3. After the break ends:
   - Another bell sound will play.
   - A new work session begins (session count increases).
4. Use **Pause** to temporarily stop the timer.
5. Use **Reset** to restart everything to the initial state.

## 🛠️ Installation & Run

I use Linux Ubuntu 22.04.5 and Python3 3.10.12

### 1. Clone the repository
```bash
git clone https://github.com/ArmPhongsakorn/Pomodoro_Timer.git
cd Pomodoro_Project
```

### 2. Install the module tkinter
```bash
sudo apt update
sudo apt install python3-tk 
```

### 3. Run the app
```bash
python3 pomodoro_timer.py 
```

# 🍅 What is the Pomodoro Technique?

The Pomodoro Technique is a time management method that breaks work into intervals:

- 25 minutes of focused work

- Followed by a 5-minute break

- After 4 sessions, take a longer break (15–30 minutes)

- This technique improves focus, reduces fatigue, and boosts productivity.

# 📁 Project Files
- pomodoro_timer.py – The main application script

- README.md – Project description

# 📄 License
- This project is licensed under the GPL 3.0 License. 

# 👨‍💻 Author
- ArmPhongsakorn
