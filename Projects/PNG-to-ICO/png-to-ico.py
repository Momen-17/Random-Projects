import os
import sys
from PIL import Image
import customtkinter as ctk
from tkinter import filedialog


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set the title of the application window
        self.title("PNG-to-ICO")

        # Set the application icon
        self.iconbitmap(self.get_resource_path("Images/repost.ico"))

        # Set the initial window size
        self.geometry("400x400")

        # Initialize variables to store the file path and the uploaded image
        self.file_path = None
        self.uploaded_image = None

        # Load the main frame with the image display
        self.load_frame()

        # Create a frame for the buttons (Convert and Clear)
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10)

        # Create the Convert button
        convert = ctk.CTkButton(
            button_frame,
            text="Convert",
            width=100,
            fg_color="#3EB489",
            text_color="#E0FFFF",
            border_color="#E0FFFF",
            border_width=1,
            command=self.convert,  # Call the convert function when clicked
        )
        convert.pack(side="left", padx=5)

        # Create the Clear button
        clear = ctk.CTkButton(
            button_frame,
            text="Clear",
            width=100,
            fg_color="#FB607F",
            text_color="#E0FFFF",
            border_color="#E0FFFF",
            border_width=1,
            command=self.clear,  # Call the clear function when clicked
        )
        clear.pack(side="left", padx=5)

    def get_resource_path(self, relative_path):
        """Get the absolute path to a resource."""
        # If the app is bundled by PyInstaller, use the temporary _MEIPASS directory
        if hasattr(sys, "_MEIPASS"):
            return os.path.join(sys._MEIPASS, relative_path)
        # Otherwise, use the script's directory
        return os.path.join(os.path.dirname(__file__), relative_path)

    def load_frame(self):
        """Load the main frame that displays the image."""
        # Create a frame to display the image
        self.frame = ctk.CTkFrame(
            self, width=300, height=300, border_color="#E0FFFF", border_width=2
        )
        self.frame.pack_propagate(False)
        self.frame.pack(pady=(20, 0))

        # Load the placeholder "add" image
        self.add_image = Image.open(self.get_resource_path("Images/add.png"))
        self.add_image_ctk = ctk.CTkImage(self.add_image, size=(150, 150))

        # Display the "add" image in the label
        self.add_image_label = ctk.CTkLabel(
            self.frame, image=self.add_image_ctk, text=""
        )
        self.add_image_label.pack(anchor="center", expand=True)

        # Bind the frame and label to trigger image upload on click
        self.frame.bind("<Button-1>", self.upload_image)
        self.add_image_label.bind("<Button-1>", self.upload_image)

    def upload_image(self, event):
        """Handle the image upload process."""
        # Open a file dialog to select an image file
        self.file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")]
        )
        if self.file_path:
            # Load the selected image
            self.uploaded_image = Image.open(self.get_resource_path(self.file_path))
            self.uploaded_image_ctk = ctk.CTkImage(self.uploaded_image, size=(290, 290))

            # Update the label to display the uploaded image
            self.add_image_label.configure(image=self.uploaded_image_ctk)

    def convert(self):
        """Convert the uploaded image to ICO format."""
        if self.file_path:
            # Get the directory and base name of the uploaded file
            dir_name = os.path.dirname(self.file_path)
            base_name = os.path.splitext(os.path.basename(self.file_path))[0]

            # 1. Save the .ico file in the same directory as the uploaded image
            ico_path_same_dir = os.path.join(dir_name, f"{base_name}.ico")
            self.uploaded_image.save(ico_path_same_dir, format="ICO")

            # 2. Save the .ico file in the "Converted" directory (in the same directory as this script)
            converted_dir = self.get_resource_path("Converted")
            if not os.path.exists(converted_dir):
                os.makedirs(converted_dir)

            ico_path_converted_dir = os.path.join(converted_dir, f"{base_name}.ico")
            self.uploaded_image.save(ico_path_converted_dir, format="ICO")

    def clear(self):
        """Clear the uploaded image and reset the label."""
        # Reset the file path and uploaded image variables
        self.file_path = None
        self.uploaded_image = None

        # Reload the placeholder "add" image
        self.add_image = Image.open(self.get_resource_path("Images/add.png"))
        self.add_image_ctk = ctk.CTkImage(self.add_image, size=(150, 150))

        # Update the label to display the placeholder image again
        self.add_image_label.configure(image=self.add_image_ctk)


if __name__ == "__main__":
    # Create and run the application
    app = App()
    app.mainloop()
