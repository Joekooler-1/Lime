# app.py

import tkinter as tk
from processor import Processor
from ui import MainUI

if __name__ == "__main__":
    root = tk.Tk()

    # Initialize processor with None; references will be updated after UI initialization
    processor = Processor(main_data=None, date_picker=None)

    # Create the main UI which loads main_data and sets up everything
    app = MainUI(root, processor)

    # After UI is created, UI now has main_data and a date_picker, so we update processor
    processor.main_data = app.main_data
    processor.date_picker = app.date_picker

    root.mainloop()
