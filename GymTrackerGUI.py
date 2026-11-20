import tkinter as tk

class GymTrackerGUI:
    """Main window for the repair tracker."""

    def __init__(self, root):
        self.root = root
        self.root.title("Gym Equipment Repair Tracker")
        self.root.geometry("600x400")

        title_label = tk.Label(
            self.root,
            text="Gym Equipment Repair Tracker",
            font=("Arial", 18)
        )
        title_label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = GymTrackerGUI(root)
    root.mainloop()