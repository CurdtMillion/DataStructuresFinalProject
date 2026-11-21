import tkinter as tk
from tkinter import messagebox

class GymTrackerGUI:
    """Main window for the repair tracker."""

    def __init__(self, root):
        self.root = root
        self.root.title("Gym Equipment Repair Tracker")
        self.root.geometry("650x800")
        self.root.configure(
            bg="#20242b",
            padx=15,
            pady=15
        )
        self.root.option_add("*Font", ("Arial", 10))

        self.root.option_add("*LabelFrame.Background", "#f3f1ed")
        self.root.option_add("*LabelFrame.Foreground", "#252a32")
        self.root.option_add("*LabelFrame.Font", ("Arial", 11, "bold"))
        self.root.option_add("*LabelFrame.Relief", "flat")

        self.root.option_add("*Label.Background", "#f3f1ed")
        self.root.option_add("*Label.Foreground", "#252a32")

        self.root.option_add("*Entry.Background", "#e2dfd9")
        self.root.option_add("*Entry.Foreground", "#252a32")
        self.root.option_add("*Entry.Relief", "flat")
        self.root.option_add("*Entry.Width", 30)

        self.root.option_add("*Text.Background", "#e2dfd9")
        self.root.option_add("*Text.Foreground", "#252a32")
        self.root.option_add("*Text.Relief", "flat")

        self.root.option_add("*Button.Background", "#a94312")
        self.root.option_add("*Button.Foreground", "#f3f1ed")
        self.root.option_add("*Button.ActiveBackground", "#87330c")
        self.root.option_add("*Button.ActiveForeground", "#f3f1ed")
        self.root.option_add("*Button.Font", ("Arial", 10, "bold"))
        self.root.option_add("*Button.Relief", "flat")
        self.root.option_add("*Button.BorderWidth", 0)
        self.root.option_add("*Button.Cursor", "hand2")
        self.root.option_add("*Button.Pady", 7)

        title_label = tk.Label(
            self.root,
            text="GYM EQUIPMENT\nREPAIR TRACKER",
            font=("Arial", 20, "bold"),
            bg="#20242b",
            fg="#f3f1ed"
        )
        title_label.pack(pady=(5, 5))

        subtitle_label = tk.Label(
            self.root,
            text="Equipment management • Maintenance requests",
            font=("Arial", 10),
            bg="#20242b",
            fg="#b9bec7"
        )
        subtitle_label.pack(pady=(0, 15))
        self.create_equipment_form()
        self.create_lookup_form()
        self.create_repair_form()
        

    def create_equipment_form(self):
        """Creates fields for entering gym equipment."""
        equipment_frame = tk.LabelFrame(
            self.root,
            text="Add Equipment",
            padx=20,
            pady=12,
            bg="#f3f1ed",
            fg="#252a32",
            font=("Arial", 11, "bold"),
            relief="flat",
            borderwidth=0
        )
        equipment_frame.pack(padx=20, pady=10, fill="x")
        equipment_frame.columnconfigure(1, weight=1)

        tk.Label(equipment_frame, text="Equipment ID:").grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.equipment_id_entry = tk.Entry(equipment_frame)
        self.equipment_id_entry.grid(
            row=0, column=1, sticky="ew", padx=(15, 0), pady=6,
            ipady=5
        )

        tk.Label(equipment_frame, text="Name:").grid(
            row=1, column=0, sticky="w", pady=5
        )
        self.equipment_name_entry = tk.Entry(equipment_frame)
        self.equipment_name_entry.grid(row=1, column=1, pady=5)

        tk.Label(equipment_frame, text="Location:").grid(
            row=2, column=0, sticky="w", pady=5
        )
        self.equipment_location_entry = tk.Entry(equipment_frame)
        self.equipment_location_entry.grid(row=2, column=1, pady=5)

        add_button = tk.Button(
            equipment_frame,
            text="Add Equipment",
            width=18,
            command=self.preview_action
        )
        add_button.grid(
            row=3, column=0, columnspan=2, pady=(10, 5)
        )

    def create_lookup_form(self):
        """Equipment look up fields and result."""
        lookup_frame = tk.LabelFrame(
            self.root,
            text="Find Equipment",
            padx=20,
            pady=12,
            bg="#f3f1ed",
            fg="#252a32",
            font=("Arial", 11, "bold"),
            relief="flat",
            borderwidth=0
        )
        lookup_frame.pack(padx=20, pady=10, fill="x")
        lookup_frame.columnconfigure(1, weight=1)

        tk.Label(lookup_frame, text="Equipment ID:").grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.lookup_id_entry = tk.Entry(lookup_frame)
        self.lookup_id_entry.grid(
            row=0, column=1, sticky="ew", padx=(15, 0), pady=6,
            ipady=5
        )

        self.lookup_result_label = tk.Label(
            lookup_frame,
            text="Place holder text for now."
        )
        self.lookup_result_label.grid(
            row=1, column=0, columnspan=2, sticky="w", pady=5
        )
        lookup_button = tk.Button(
            lookup_frame,
            text="Find Equipment",
            width=18,
            command=self.preview_action
        )
        lookup_button.grid(
            row=2, column=0, columnspan=2, pady=(10, 5)
        )

    def create_repair_form(self):
        """Creates fields for entering a repair request."""
        repair_frame = tk.LabelFrame(
            self.root,
            text="Request Repair",
            padx=20,
            pady=12,
            bg="#f3f1ed",
            fg="#252a32",
            font=("Arial", 11, "bold"),
            relief="flat",
            borderwidth=0
        )
        repair_frame.pack(padx=20, pady=10, fill="x")
        repair_frame.columnconfigure(1, weight=1)

        tk.Label(repair_frame, text="Equipment ID:").grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.repair_id_entry = tk.Entry(repair_frame)
        self.repair_id_entry.grid(
            row=0, column=1, sticky="ew", padx=(15, 0), pady=6,
            ipady=5
        )

        tk.Label(repair_frame, text="Problem:").grid(
            row=1, column=0, sticky="nw", pady=5
        )

        self.repair_description_text = tk.Text(
            repair_frame,
            width=35,
            height=4,
            wrap="word"
        )
        self.repair_description_text.grid(
            row=1, column=1, sticky="ew", padx=(15, 0), pady=6
        )
        repair_button = tk.Button(
            repair_frame,
            text="Request Repair",
            width=18,
            command=self.preview_action
        )
        repair_button.grid(
            row=2, column=0, columnspan=2, pady=(10, 5)
        )

    def preview_action(self):
        """Make sure button works."""
        messagebox.showinfo(
            "Button has been clicked, bro!"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = GymTrackerGUI(root)
    root.mainloop()