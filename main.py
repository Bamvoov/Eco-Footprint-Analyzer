import customtkinter as ctk
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


DATA_DB = {
    "Beef (Meat)": {"carbon": 99.48, "water": 15415, "unit": "kg"},
    "Chicken (Meat)": {"carbon": 9.87, "water": 4325, "unit": "kg"},
    "Rice (Grain)": {"carbon": 4.45, "water": 2497, "unit": "kg"},
    "Milk (Dairy)": {"carbon": 3.0, "water": 1020, "unit": "Liter"},
    "Cheese (Dairy)": {"carbon": 23.88, "water": 5605, "unit": "kg"},
    "Vegetables": {"carbon": 0.4, "water": 322, "unit": "kg"},
    "Coffee": {"carbon": 28.5, "water": 18900, "unit": "kg"},
    "Chocolate": {"carbon": 46.6, "water": 17196, "unit": "kg"},
}
    
class EcoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        
        self.title("Eco-Footprint Analyzer (EVS Project)")
        self.geometry("900x600")
        ctk.set_appearance_mode("Dark")  # Dark Mode
        ctk.set_default_color_theme("green")

     
        self.cart = []
        self.total_carbon = 0.0
        self.total_water = 0.0

        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        
        self.sidebar = ctk.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        self.logo_label = ctk.CTkLabel(self.sidebar, text="🌱 Eco-Calc", font=ctk.CTkFont(size=24, weight="bold"))
        self.logo_label.pack(pady=20)

      
        self.label_item = ctk.CTkLabel(self.sidebar, text="Select Item:")
        self.label_item.pack(pady=(10, 0))
        self.option_menu = ctk.CTkOptionMenu(self.sidebar, values=list(DATA_DB.keys()))
        self.option_menu.pack(pady=5)

       
        self.label_qty = ctk.CTkLabel(self.sidebar, text="Quantity (kg/L):")
        self.label_qty.pack(pady=(10, 0))
        self.entry_qty = ctk.CTkEntry(self.sidebar, placeholder_text="1.0")
        self.entry_qty.pack(pady=5)

        
        self.add_btn = ctk.CTkButton(self.sidebar, text="+ Add to List", command=self.add_item)
        self.add_btn.pack(pady=20)

        
        self.reset_btn = ctk.CTkButton(self.sidebar, text="Reset All", fg_color="transparent", border_width=2, command=self.reset_app)
        self.reset_btn.pack(pady=10)
        
        
        self.info_box = ctk.CTkTextbox(self.sidebar, height=150)
        self.info_box.pack(pady=20, padx=10)
        self.info_box.insert("0.0", "DID YOU KNOW?\n\nVirtual Water is the hidden water used to produce goods.\n\nE.g., 1kg of Chocolate takes ~17,000 Liters of water!")
        self.info_box.configure(state="disabled")

        
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        
        self.metric_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.metric_frame.pack(fill="x", pady=10)

       
        self.card_c = ctk.CTkFrame(self.metric_frame)
        self.card_c.pack(side="left", fill="x", expand=True, padx=5)
        self.lbl_c_title = ctk.CTkLabel(self.card_c, text="Total Carbon (CO2)", font=("Arial", 14))
        self.lbl_c_title.pack(pady=5)
        self.lbl_c_val = ctk.CTkLabel(self.card_c, text="0.0 kg", font=("Arial", 24, "bold"), text_color="#FF6B6B")
        self.lbl_c_val.pack(pady=10)

     
        self.card_w = ctk.CTkFrame(self.metric_frame)
        self.card_w.pack(side="left", fill="x", expand=True, padx=5)
        self.lbl_w_title = ctk.CTkLabel(self.card_w, text="Total Virtual Water", font=("Arial", 14))
        self.lbl_w_title.pack(pady=5)
        self.lbl_w_val = ctk.CTkLabel(self.card_w, text="0 L", font=("Arial", 24, "bold"), text_color="#4ECDC4")
        self.lbl_w_val.pack(pady=10)

       
        self.list_label = ctk.CTkLabel(self.main_frame, text="Your Shopping List:", anchor="w")
        self.list_label.pack(fill="x", pady=(10, 0))
        
        self.list_box = ctk.CTkTextbox(self.main_frame, height=150)
        self.list_box.pack(fill="x", pady=5)
        self.list_box.configure(state="disabled")

    
        self.chart_frame = ctk.CTkFrame(self.main_frame)
        self.chart_frame.pack(fill="both", expand=True, pady=10)
        
      
        self.init_chart()

    def init_chart(self):
       
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.fig.patch.set_facecolor('#2b2b2b') 
        self.ax.set_facecolor('#2b2b2b')
        
        self.ax.bar(["Carbon", "Water (x100)"], [0, 0], color=['#FF6B6B', '#4ECDC4'])
        self.ax.tick_params(colors='white')
        self.ax.spines['bottom'].set_color('white')
        self.ax.spines['left'].set_color('white') 
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.chart_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def add_item(self):
        item = self.option_menu.get()
        try:
            qty = float(self.entry_qty.get())
        except ValueError:
            return

        if qty <= 0: return

        # Calculation
        data = DATA_DB[item]
        c_footprint = data["carbon"] * qty
        w_footprint = data["water"] * qty

        self.cart.append(f"{qty} {data['unit']} {item}")
        self.total_carbon += c_footprint
        self.total_water += w_footprint

       
        self.update_display()
    
    def update_display(self):
        
        self.list_box.configure(state="normal")
        self.list_box.delete("0.0", "end")
        for i in self.cart:
            self.list_box.insert("end", f"• {i}\n")
        self.list_box.configure(state="disabled")

        
        self.lbl_c_val.configure(text=f"{self.total_carbon:.2f} kg")
        self.lbl_w_val.configure(text=f"{self.total_water:,.0f} L")

        # Update Chart
        self.ax.clear()
        
        self.ax.bar(["Carbon (kg)", "Water (100 L)"], [self.total_carbon, self.total_water/100], color=['#FF6B6B', '#4ECDC4'])
        self.ax.tick_params(colors='white')
        self.ax.set_title("Environmental Impact", color='white')
        self.canvas.draw()

    def reset_app(self):
        self.cart = []
        self.total_carbon = 0.0
        self.total_water = 0.0
        self.entry_qty.delete(0, "end")
        self.update_display()

if __name__ == "__main__":
    app = EcoApp()
    app.mainloop()