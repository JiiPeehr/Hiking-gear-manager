import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hiking Gear Manager")
        self.geometry("1200x600")

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

        # Add to inventory button
        self.add_item_button = tk.Button(self, text="Add to inventory", command=self.add_item)
        self.add_item_button.grid(row=1, column=12, columnspan=2)
        
        # Remove from inventory button
        self.remove_item_button = tk.Button(self, text="Remove from inventory", command=self.remove_from_inventory)
        self.remove_item_button.grid(row=4, column=0, columnspan=2, padx=(20, 20))

        # Pack item button
        self.pack_item_button = tk.Button(self, text="Pack item \u2192", command=self.pack_item)
        self.pack_item_button.grid(row=4, column=3, columnspan=2)

        # Unpack item button
        self.unpack_item_button = tk.Button(self, text="Unpack item \u00D7", command=self.unpack_item)
        self.unpack_item_button.grid(row=4, column=7, columnspan=2)

        # Listbox to display all items
        self.items_listbox = tk.Listbox(self, height=20, width=50, yscrollcommand=True)
        self.items_listbox.grid(row=3, column=0, columnspan=7, sticky="w",pady=(20, 0), padx=(20, 20))

        # Listbox to display added items. Tarvitaan myös nappi tuotteen siirtämiseen toiseen listboxiin
        self.added_items_listbox = tk.Listbox(self, height=20, width=50, yscrollcommand=True)
        self.added_items_listbox.grid(row=3, column=7, columnspan=7, sticky="w", pady=(20, 0))

        # Placeholder for total amount and weight display
        self.total_display_label = tk.Label(self, text="Total items: 0, Total weight: 0g")
        self.total_display_label.grid(row=4, column=9, columnspan=14, pady=(10, 0))        

    # function to add item
    def add_item(self):
        item_name = self.item_name_entry.get()
        item_category = self.item_category_entry.get()
        item_weight = self.item_weight_entry.get()

        print(f"Item name: {item_name}")
        print(f"Item weight: {item_weight}")

        self.item_name_entry.delete(0, tk.END)
        self.item_weight_entry.delete(0, tk.END)


    # function to remove item
    def remove_from_inventory(self):
        pass

    # function to pack item
    def pack_item(self):
        pass

    # function to unpack item
    def unpack_item(self):
        pass

        

       






if __name__ == "__main__":
    app = App()
    app.mainloop()