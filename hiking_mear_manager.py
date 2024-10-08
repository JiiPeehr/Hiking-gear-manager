import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hiking Gear Manager")
        self.geometry("1100x800")

        # Main header
        self.label = tk.Label(self, text="Enter the gear info:")
        self.label.grid(row=0, column=0, columnspan=2)

        # Item name entry header and entry
        self.item_name_label = tk.Label(self, text="Item name:")
        self.item_name_label.grid(row=1, column=0, columnspan=2)

        self.item_name_entry = tk.Entry(self)
        self.item_name_entry.grid(row=1, column=2, columnspan=2)

        # Item category entry header and entry
        self.item_category_label = tk.Label(self, text="Item category:")
        self.item_category_label.grid(row=1, column=4, columnspan=2)

        self.item_category_entry = tk.Entry(self)
        self.item_category_entry.grid(row=1, column=6, columnspan=2)

        # Item weight entry header and entry
        self.item_weight_label = tk.Label(self, text="Item weight in grams:")
        self.item_weight_label.grid(row=1, column=8, columnspan=2)

        self.item_weight_entry = tk.Entry(self)
        self.item_weight_entry.grid(row=1, column=10, columnspan=2)

        # Add item button
        self.add_item_button = tk.Button(self, text="Add item", command=self.add_item)
        self.add_item_button.grid(row=1, column=12, columnspan=2)

         # function to add item
    def add_item(self):
        item_name = self.item_name_entry.get()
        item_category = self.item_category_entry.get()
        item_weight = self.item_weight_entry.get()

        print(f"Item name: {item_name}")
        print(f"Item weight: {item_weight}")

        self.item_name_entry.delete(0, tk.END)
        self.item_weight_entry.delete(0, tk.END)

    def remove_item(self):
        pass

        

       






if __name__ == "__main__":
    app = App()
    app.mainloop()