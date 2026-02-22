#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

class BaseFrame(tk.Frame):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent
        , **kwargs)
        self.parent = parent

        btn = ttk.Button(self, text="Back", command=self.go_back)
        btn.pack()

    def go_back(self):
        self.parent.change_frame(MainMenu)

class LogSession(BaseFrame):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent

        # put code for the log session here.

class ViewHistory(BaseFrame):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)

class SetGoals(BaseFrame):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)

class ProgressReport(BaseFrame):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)

class DistChart(BaseFrame):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)

class StudyTrend(BaseFrame):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)

class MainMenu(tk.Frame):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent

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
        self.parent.change_frame(LogSession)

    def view_history(self):
        print("View study history")
        self.parent.change_frame(ViewHistory)

    def set_goals(self):
        print("Set study goals")
        self.parent.change_frame(SetGoals)

    def veiw_report(self):
        print("View progress report")
        self.parent.change_frame(ProgressReport)

    def dist_chart(self):
        print("Subject distribution chart")
        self.parent.change_frame(DistChart)

    def show_trend(self):
        print("Weekly study trend")
        self.parent.change_frame(StudyTrend)

class TrackerMain(tk.Frame):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)

        frames = LogSession, ViewHistory, SetGoals, ProgressReport, DistChart, StudyTrend, MainMenu
        self.frm_ref = {}
        for frmcls in frames:
            frm = frmcls(self)
            frm.grid(row=0, column=0, sticky="nsew")
            self.frm_ref[frmcls] = frm

    def change_frame(self, frmcls):
        self.frm_ref[frmcls].tkraise()

def main():
    root = tk.Tk()
    frm = TrackerMain(root)
    frm.pack(expand=True, fill=tk.BOTH)
    root.mainloop()

if __name__ == "__main__":
    main()
