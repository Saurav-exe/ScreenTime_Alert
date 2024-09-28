import tkinter as tk
from tkinter import Toplevel

def show_custom_alert():
    alert_window = Toplevel()
    alert_window.title("Take a Break!")
    alert_window.geometry("400x200+500+300")
    alert_window.configure(bg="lightblue")
    alert_window.resizable(False, False)
    alert_window.attributes("-topmost", True)
    
    # label
    label = tk.Label(
        alert_window, 
        text="It's time to take a break!\n Have a Kit-Kat¯\_(ツ)_/¯ \nLook outside for a while to keep your eyes healthy.",
        font=("Helvetica", 16, "bold"),
        bg="lightblue",
        fg="darkblue",
        pady=20
    )
    label.pack()

    # Close Button
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
    
    alert_window.overrideredirect(True)
    alert_window.eval('tk::PlaceWindow . center')
    alert_window.grab_set()

root = tk.Tk()
root.withdraw()  # Hide the root window

show_custom_alert()

root.mainloop()
