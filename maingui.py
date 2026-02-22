#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

class TrackerMain(tk.Frame):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent=None, **kwargs)

        btn = ttk.Button(self, text="Log a study session", command=self.log_session)
        btn.pack()

        btn = ttk.Button(self, text="View study history", command=self.view_history)
        btn.pack()

        btn = ttk.Button(self, text="Set study goals", command=self.set_goals)
        btn.pack()

        btn = ttk.Button(self, text="View progress report", command=self.veiw_report)
        btn.pack()

        btn = ttk.Button(self, text="Subject distribution chart", command=self.dist_chart)
        btn.pack()

        btn = ttk.Button(self, text="Weekly study trend", command=self.show_trend)
        btn.pack()


    def log_session(self):
        print("code to Log a study session goes here")

    def view_history(self):
        print("View study history")

    def set_goals(self):
        print("Set study goals")

    def veiw_report(self):
        print("View progress report")

    def dist_chart(self):
        print("Subject distribution chart")

    def show_trend(self):
        print("Weekly study trend")

def main():
    root = tk.Tk()
    frm = TrackerMain(root)
    frm.pack(expand=True, fill=tk.BOTH)
    root.mainloop()

if __name__ == "__main__":
    main()
