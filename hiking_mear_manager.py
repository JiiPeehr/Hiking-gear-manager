import tkinter as tk
import classes as cl

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hiking Gear Manager")
        self.geometry("1400x550")
        self.base_inventory = cl.BaseInventory()
        self.packed_inventory = cl.PackedInventory()
        self.total_weight = 0
        self.total_items = 0
        self.messagebox = None
        

        # Main header
        self.label = tk.Label(self, text="Enter the gear info:")
        self.label.grid(row=0, column=0, columnspan=2)

        # Item name entry header and entry
        self.item_name_label = tk.Label(self, text="Item name:")
        self.item_name_label.grid(row=1, column=0)

        self.item_name_entry = tk.Entry(self)
        self.item_name_entry.grid(row=1, column=1)

        # Item category entry header and entry
        self.item_category_label = tk.Label(self, text="Item category:")
        self.item_category_label.grid(row=1, column=2)

        self.item_category_entry = tk.Entry(self)
        self.item_category_entry.grid(row=1, column=3)

        # Item weight entry header and entry
        self.item_weight_label = tk.Label(self, text="Item weight in grams:")
        self.item_weight_label.grid(row=1, column=4)

        self.item_weight_entry = tk.Entry(self)
        self.item_weight_entry.grid(row=1, column=5)

        # Add to base inventory button
        self.add_item_button = tk.Button(self, text="Add to base inventory", command=self.add_and_save)
        self.add_item_button.grid(row=1, column=6, columnspan=2)

        # Headers for listboxes
        self.base_items_listbox_header = tk.Label(self, text="All Items")
        self.base_items_listbox_header.grid(row=5, column=0, columnspan=7, sticky="w", pady=(10, 0), padx=(20, 20))

        self.packed_items_listbox_header = tk.Label(self, text="Packed Items")
        self.packed_items_listbox_header.grid(row=5, column=7, columnspan=7, sticky="w", pady=(10, 0))

        # Listbox to display base inventory items
        self.base_inventory_listbox = tk.Listbox(self, height=20, width=50, yscrollcommand=True)
        self.base_inventory_listbox.grid(row=6, column=0, columnspan=7, sticky="w", pady=(10, 0), padx=(20, 20))

        # Listbox to display packed items 
        self.packed_items_listbox = tk.Listbox(self, height=20, width=50, yscrollcommand=True)
        self.packed_items_listbox.grid(row=6, column=7, columnspan=7, sticky="w", pady=(10, 0))

        # Remove from inventory button
        self.remove_item_button = tk.Button(self, text="Remove from inventory", command=self.remove_and_save)
        self.remove_item_button.grid(row=7, column=0, columnspan=2, padx=(20, 20))

        # Pack item button
        self.pack_item_button = tk.Button(self, text="Pack item \u2192", command=self.press_pack_button)
        self.pack_item_button.grid(row=7, column=3, columnspan=2)

        # Unpack item button
        self.unpack_item_button = tk.Button(self, text="Unpack item \u00D7", command=self.press_unpack_button)
        self.unpack_item_button.grid(row=7, column=7, columnspan=2)

        # Total amount and weight display
        self.total_display_label = tk.Label(self, text=f"Total items: {self.total_items}, Total weight: {self.total_weight}g")
        self.total_display_label.grid(row=8, column=8, columnspan=14, pady=(10, 0))

        # Save base inventory button
        #self.save_base_inventory_button = tk.Button(self, text="Save base inventory", command=self.save_base_inventory)
        #self.save_base_inventory_button.grid(row=9, column=0, columnspan=2, pady=(10, 0), padx=(20, 20))

        # Messagebox placeholder
        self.messagebox = tk.Label(self, text=self.messagebox)
        self.messagebox.grid(row=9, column=0, columnspan=2, pady=(10, 0), padx=(20, 20))

        # Save packed items button
        self.save_packed_items_button = tk.Button(self, text="Save packed items", command=self.save_packed_items_inventory)
        self.save_packed_items_button.grid(row=9, column=7, columnspan=2, pady=(10, 0))

        self.start()


    """Widget functions"""

    # function to add item to base inventory
    def add_item(self):
        item_name = self.item_name_entry.get()
        item_category = self.item_category_entry.get()
        item_weight = self.item_weight_entry.get()

        if not item_name or not item_category or not item_weight:
            self.messagebox.config(text="Please fill all fields")
        elif not item_weight.isdigit():
            self.messagebox.config(text="Weight must be a number")
        else:
            item = cl.Item(item_name, item_category, item_weight)
            self.base_inventory_listbox.insert(tk.END, item)

            self.item_name_entry.delete(0, tk.END)
            self.item_category_entry.delete(0, tk.END)
            self.item_weight_entry.delete(0, tk.END)
            self.messagebox.config(text="Item added successfully")

    # function to remove selected item from base inventory
    def remove_from_base_inventory(self):
        selected_indices = self.base_inventory_listbox.curselection()
        if selected_indices:
            selected_index = selected_indices[0]
            self.base_inventory_listbox.delete(selected_index)
            
    # function to pack item
    def pack_item(self):
        selected_indices = self.base_inventory_listbox.curselection()
        if selected_indices:
            selected_index = selected_indices[0]
            self.packed_items_listbox.insert(tk.END, self.base_inventory_listbox.get(selected_index))

    # function to unpack item
    def unpack_item(self):
        selected_indices = self.packed_items_listbox.curselection()
        if selected_indices:
            selected_index = selected_indices[0]
            self.packed_items_listbox.delete(selected_index)
        
    # function to update total weight
    def update_total_weight(self):
        self.total_weight = 0
        for i in range(self.packed_items_listbox.size()):
            item_str: str = self.packed_items_listbox.get(i)
            name, category, weight = item_str.split(",")
            self.total_weight += int(weight[:-1])
        
        

    # function to update total amount of items
    def update_total_items(self):
        self.total_items = self.packed_items_listbox.size()
        
    
    def press_pack_button(self):
        self.pack_item()
        self.update_total_weight()
        self.update_total_items()
        self.total_display_label.config(text=f"Total items: {self.total_items}, Total weight: {self.total_weight}g")

    def press_unpack_button(self):
        self.unpack_item()
        self.update_total_weight()
        self.update_total_items()
        self.total_display_label.config(text=f"Total items: {self.total_items}, Total weight: {self.total_weight}g")


    """functions to run at the start of the app"""

    # function to load items to base inventory display
    def load_base_inventory_display(self):
        for item in self.base_inventory.get_items():
            self.base_inventory_listbox.insert(tk.END, item)
        self.base_inventory.remove_all_items()


    # funktion to load items to packed items display
    def load_packed_items_inventory_display(self):
        for item in self.packed_inventory.get_items():
            self.packed_items_listbox.insert(tk.END, item)
        self.packed_inventory.remove_all_items()
        self.update_total_weight()
        self.update_total_items()
        self.total_display_label.config(text=f"Total items: {self.total_items}, Total weight: {self.total_weight}g")
        

    def start(self):
        self.load_base_inventory_display()
        self.load_packed_items_inventory_display()
        

    # function to save base inventory items to list -> save to file
    def save_base_inventory(self):
        for i in range(self.base_inventory_listbox.size()):
            item_str: str = self.base_inventory_listbox.get(i)
            name, category, weight = item_str.split(",")
            item = cl.Item(name, category, weight[:-1])
            self.base_inventory.add_item(item)
        self.base_inventory.save_file(self.base_inventory.get_items()) # voiko tänne lisätä saman itemin?
        self.base_inventory.remove_all_items()
        

    # function to save packed items to list -> save to file
    def save_packed_items_inventory(self):
        for i in range(self.packed_items_listbox.size()):
            item_str: str = self.packed_items_listbox.get(i)
            name, category, weight = item_str.split(",")
            item = cl.Item(name, category, weight[:-1])
            self.packed_inventory.add_item(item)
        self.packed_inventory.save_file(self.packed_inventory.get_items())
        self.packed_inventory.remove_all_items()

    
    def add_and_save(self):
        self.add_item()
        self.save_base_inventory()

    def remove_and_save(self):
        self.remove_from_base_inventory()
        self.save_base_inventory()



if __name__ == "__main__":
    app = App()
    app.mainloop()