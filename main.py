import webview
import os

def load_html_in_window():
    # Path to the index.html file (update this to the correct path if needed)
    html_file_path = os.path.abspath('index.html')
    
    # Create a webview window
    window = webview.create_window(
        "Project Bolt | Item Shop",  # Window title
        html_file_path,  # HTML file to load
        width=800,  # Window width
        height=600  # Window height
    )
    
    # Start the webview
    webview.start()

if __name__ == '__main__':
    load_html_in_window()
