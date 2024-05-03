import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from ui_mainwindow import Ui_MainWindow

def parse_plugin_info(plugin_info):
    # Split the plugin_info string at the period
    parts = plugin_info.split(".")
    
    # Extract the plugin name and plugin ID
    plugin_name = parts[0]
    plugin_id = int(parts[1])  # Convert the ID to an integer
  
    return plugin_name, plugin_id

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect button click signals to functions
        self.ui.Add_Plugin.clicked.connect(self.add_plugin)
        self.ui.Remove_Sel_Plugin.clicked.connect(self.remove_selected_plugin)

    def add_plugin(self):
        plugin_info = self.ui.Plugin_URL_Field.text()
        print("Add button clicked with plugin name:", plugin_info)
        plugin_name, plugin_id = parse_plugin_info(plugin_info)
        # Set User-Agent header
        headers = {"User-Agent": "MyUserAgent"}

        # Construct the request URL with the plugin ID
        request_url = f"https://api.spiget.org/v2/resources/{plugin_id}"

        try:
            # Send GET request
            response = requests.get(request_url, headers=headers)

            # Check if request was successful
            if response.status_code == 200:
                # Parse response as JSON
                data = response.json()

                # Check if the response is a JSON object
                if isinstance(data, dict):
                    # Get plugin name from data
                    #plugin_name = data.get('name', '')
                    print(data.get('name', ''))
                    # Add plugin name to the table
                    row_count = self.ui.Plugin_List.rowCount()
                    self.ui.Plugin_List.insertRow(row_count)
                    self.ui.Plugin_List.setItem(row_count, 0, QTableWidgetItem(plugin_name))
                else:
                    print("Unexpected response format:", data)
            else:
                # Handle unsuccessful request
                print("Failed to fetch data from Spiget API. Status code:", response.status_code)

        except Exception as e:
            # Handle exceptions
            print("An error occurred:", e)

    def remove_selected_plugin(self):
        print("Remove button clicked")
        # Add your code to handle removing a selected plugin here

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
