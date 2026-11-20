import tkinter as tk

class GymTrackerGUI:
    """Main window for the repair tracker."""

    def __init__(self, root):
        self.root = root
        self.root.title("Gym Equipment Repair Tracker")
        self.root.geometry("600x650")

        title_label = tk.Label(
            self.root,
            text="Gym Equipment Repair Tracker",
            font=("Arial", 18)
        )
        title_label.pack(pady=20)
        self.create_equipment_form()
        self.create_lookup_form()
        self.create_repair_form()
        

    def create_equipment_form(self):
        """Creates fields for entering gym equipment."""
        equipment_frame = tk.LabelFrame(
            self.root,
            text="Add Equipment",
            padx=10,
            pady=10
        )
        equipment_frame.pack(padx=20, pady=10, fill="x")

        tk.Label(equipment_frame, text="Equipment ID:").grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.equipment_id_entry = tk.Entry(equipment_frame)
        self.equipment_id_entry.grid(row=0, column=1, pady=5)

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

    def create_lookup_form(self):
        """Equipment look up fields and result."""
        lookup_frame = tk.LabelFrame(
            self.root,
            text="Find Equipment",
            padx=10,
            pady=10
        )
        lookup_frame.pack(padx=20, pady=10, fill="x")

        tk.Label(lookup_frame, text="Equipment ID:").grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.lookup_id_entry = tk.Entry(lookup_frame)
        self.lookup_id_entry.grid(row=0, column=1, pady=5)

        self.lookup_result_label = tk.Label(
            lookup_frame,
            text="Place holder text for now."
        )
        self.lookup_result_label.grid(
            row=1, column=0, columnspan=2, sticky="w", pady=5
        )

    def create_repair_form(self):
        """Creates fields for entering a repair request."""
        repair_frame = tk.LabelFrame(
            self.root,
            text="Request Repair",
            padx=10,
            pady=10
        )
        repair_frame.pack(padx=20, pady=10, fill="x")

        tk.Label(repair_frame, text="Equipment ID:").grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.repair_id_entry = tk.Entry(repair_frame)
        self.repair_id_entry.grid(row=0, column=1, pady=5)

        tk.Label(repair_frame, text="Problem:").grid(
            row=1, column=0, sticky="nw", pady=5
        )

        # A Text widget allows a description with multiple lines.
        self.repair_description_text = tk.Text(
            repair_frame,
            width=35,
            height=4
        )
        self.repair_description_text.grid(
            row=1, column=1, pady=5
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = GymTrackerGUI(root)
    root.mainloop()