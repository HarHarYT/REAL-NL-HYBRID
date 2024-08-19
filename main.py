import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import webbrowser  # For opening URLs
import logging

# Configure the logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class NLHybridLauncher(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("NL Hybrid Launcher")
        self.geometry("900x500")
        self.configure(bg="#1e1e1e")

        self.sidebar_frame = tk.Frame(self, bg="#2d2d2d", width=200)
        self.sidebar_frame.pack(side="left", fill="y")

        self.main_frame = tk.Frame(self, bg="#1e1e1e")
        self.main_frame.pack(side="right", expand=True, fill="both")

        logger.info("Application started")
        self.create_sidebar()
        self.create_main_content()  # Create the initial content

    def create_sidebar(self):
        title_label = tk.Label(self.sidebar_frame, text="NL Hybrid", font=("Arial", 18), bg="#2d2d2d", fg="white")
        title_label.pack(pady=20)

        self.nav_buttons = {
            "NL Hybrid": self.create_main_content,
            "NL Hybrid Premium": self.create_premium_content,
            "Stat Changer": self.create_stat_changer,
            "Custom Locker": self.create_custom_locker,
        }

        for button_text in self.nav_buttons:
            self.create_nav_button(button_text)

        settings_button = tk.Button(self.sidebar_frame, text="Settings", bg="#2d2d2d", fg="white", bd=0, anchor="w", padx=10, font=("Arial", 12))
        settings_button.pack(side="bottom", pady=10, fill="x")

    def create_nav_button(self, text):
        button = tk.Button(self.sidebar_frame, text=text, bg="#2d2d2d", fg="white", bd=0, anchor="w", padx=10, font=("Arial", 12),
                           command=lambda: self.switch_frame(text))
        button.pack(pady=5, fill="x")
        logger.debug(f"Navigation button created: {text}")

    def switch_frame(self, text):
        logger.debug(f"Switching frame to: {text}")
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        if text in self.nav_buttons:
            self.nav_buttons[text]()

    def create_main_content(self):
        try:
            img = Image.open("D:\\tiktok method\\tiktok method\\fn.png")
            img = img.resize((200, 300), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            img_label = tk.Label(self.main_frame, image=img, bg="#1e1e1e")
            img_label.image = img  # Keep a reference
            img_label.pack(pady=20)
            
            # Bind the click event to the image
            img_label.bind("<Button-1>", self.open_fortnite)
            logger.info("Main content created successfully")
            
        except Exception as e:
            logger.error(f"Error loading image: {e}")

        title_label = tk.Label(self.main_frame, text="Fortnite [NL Hybrid]", font=("Arial", 16), bg="#1e1e1e", fg="white")
        title_label.pack(pady=10)

        self.key_entry = tk.Entry(self.main_frame, width=30, font=("Arial", 14))
        self.key_entry.pack(pady=10)

        get_key_button = tk.Button(self.main_frame, text="Get A Key", bg="#3d3d3d", fg="white", bd=0, padx=10, pady=5, font=("Arial", 12), command=self.check_key)
        get_key_button.pack(pady=10)

        discord_button = tk.Button(self.main_frame, text="Fix Issues", bg="#3d3d3d", fg="white", bd=0, padx=10, pady=5, font=("Arial", 12))
        discord_button.pack(pady=10)

    def open_fortnite(self, event):
        url = "com.epicgames.launcher://apps/fn%3A4fe75bbc5a674f4f9b356b5c90567da5%3AFortnite?action=launch&silent=true"
        try:
            webbrowser.open(url)
            logger.info("Attempted to open Fortnite")
        except Exception as e:
            logger.error(f"Error opening Fortnite: {e}")

    def check_key(self):
        key = self.key_entry.get()
        logger.debug(f"Key entered: {key}")
        if key == "1":
            self.open_fortnite(None)  # Pass None as event is not used
        else:
            logger.warning("Invalid key entered")

    def create_premium_content(self):
        title_label = tk.Label(self.main_frame, text="NL Hybrid Premium", font=("Arial", 24), bg="#1e1e1e", fg="white")
        title_label.pack(pady=20)

        purchase_label = tk.Label(self.main_frame, text="Purchase Available in The Discord Server", font=("Arial", 18), bg="#1e1e1e", fg="white")
        purchase_label.pack(pady=20)

        username_label = tk.Label(self.main_frame, text="Username:", font=("Arial", 14), bg="#1e1e1e", fg="white")
        username_label.pack(pady=5)
        username_entry = tk.Entry(self.main_frame, width=30, font=("Arial", 14))
        username_entry.pack(pady=5)

        password_label = tk.Label(self.main_frame, text="Password:", font=("Arial", 14), bg="#1e1e1e", fg="white")
        password_label.pack(pady=5)
        password_entry = tk.Entry(self.main_frame, show="*", width=30, font=("Arial", 14))
        password_entry.pack(pady=5)

        sign_in_button = tk.Button(self.main_frame, text="Sign In", bg="#3d3d3d", fg="white", bd=0, padx=10, pady=5, font=("Arial", 12))
        sign_in_button.pack(pady=20)
        logger.info("Premium content created")

    def create_stat_changer(self):
        title_label = tk.Label(self.main_frame, text="Stat Changer", font=("Arial", 24), bg="#1e1e1e", fg="white")
        title_label.pack(pady=20)

        account_label = tk.Label(self.main_frame, text="Your Account", font=("Arial", 14), bg="#1e1e1e", fg="white")
        account_label.pack(pady=5)
        account_entry = tk.Entry(self.main_frame, width=30, font=("Arial", 14))
        account_entry.pack(pady=5)

        login_button = tk.Button(self.main_frame, text="Login With Epic", bg="#3d3d3d", fg="white", bd=0, padx=10, pady=5, font=("Arial", 12))
        login_button.pack(pady=5)

        stat_fields = ["Level", "Vbucks", "Crowns", "Stars"]
        for stat in stat_fields:
            stat_label = tk.Label(self.main_frame, text=stat, font=("Arial", 14), bg="#1e1e1e", fg="white")
            stat_label.pack(pady=5)
            stat_entry = tk.Entry(self.main_frame, width=30, font=("Arial", 14))
            stat_entry.pack(pady=5)
            submit_button = tk.Button(self.main_frame, text=f"Submit {stat}", bg="#3d3d3d", fg="white", bd=0, padx=10, pady=5, font=("Arial", 12))
            submit_button.pack(pady=5)
        logger.info("Stat Changer content created")

    def create_custom_locker(self):
        # Clear the main_frame before adding new content
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Title for Custom Locker
        title_label = tk.Label(self.main_frame, text="Custom Locker", font=("Arial", 24), bg="#1e1e1e", fg="white")
        title_label.pack(pady=20)

        # Instructions Label
        instructions_label = tk.Label(self.main_frame, text="Customize your locker items below:", font=("Arial", 16), bg="#1e1e1e", fg="white")
        instructions_label.pack(pady=10)

        # Example fields for customization
        fields = ["Select Item", "Color", "Size", "Quantity"]
        
        self.entries = {}
        for field in fields:
            field_label = tk.Label(self.main_frame, text=field, font=("Arial", 14), bg="#1e1e1e", fg="white")
            field_label.pack(pady=5)
            entry = tk.Entry(self.main_frame, width=30, font=("Arial", 14))
            entry.pack(pady=5)
            self.entries[field] = entry  # Store reference to the entry widget
        
        # Submit button
        submit_button = tk.Button(self.main_frame, text="Submit Customizations", bg="#3d3d3d", fg="white", bd=0, padx=10, pady=5, font=("Arial", 12), command=self.submit_custom_locker)
        submit_button.pack(pady=20)
        logger.info("Custom Locker content created")

    def submit_custom_locker(self):
        # Collect data from entries
        data = {field: entry.get() for field, entry in self.entries.items()}
        
        # Print data to console (or handle it as needed)
        logger.info("Custom Locker Data Submitted:")
        for field, value in data.items():
            logger.info(f"{field}: {value}")
        
        # Here you can add additional logic to handle the submitted data

if __name__ == "__main__":
    app = NLHybridLauncher()
    app.mainloop()
