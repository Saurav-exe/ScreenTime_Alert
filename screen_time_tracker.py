import tkinter as tk
from tkinter import Toplevel
import ctypes 


def hide_console():
    # Only on Windows
    if ctypes.windll.kernel32.GetConsoleWindow():
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


def show_custom_alert():
    alert_window = Toplevel()
    alert_window.title("Take a Break!")
    alert_window.geometry("400x200")
    alert_window.configure(bg="lightblue")
    alert_window.resizable(False, False)
    alert_window.attributes("-topmost", True)

    
    label = tk.Label(
        alert_window, 
        text="It's time to take a break!\n Have a Kit-Kat ¯\\_(ツ)_/¯ \nLook outside for a while.",
        font=("Helvetica", 16, "bold"),
        bg="lightblue",
        fg="darkblue",
        pady=20
    )
    label.pack()

    # button 
    close_button = tk.Button(
        alert_window, 
        text="I'm Gonna Look Outside", 
        command=alert_window.destroy,
        font=("Arial", 12),
        bg="darkblue", 
        fg="white", 
        activebackground="lightblue", 
        relief="raised"
    )
    close_button.pack(pady=10)
    
    # Remove window close buttons
    alert_window.overrideredirect(True)

    # Centering the window on screen
    window_width, window_height = 400, 200
    screen_width = alert_window.winfo_screenwidth()
    screen_height = alert_window.winfo_screenheight()
    
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    
    alert_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    
    alert_window.focus_force()
    alert_window.grab_set()


def track_screen_time():
    reminder_interval = 20 * 60 * 1000  
    root.after(reminder_interval, show_custom_alert)  


hide_console()


root = tk.Tk()
root.withdraw()  
track_screen_time()

root.mainloop()
