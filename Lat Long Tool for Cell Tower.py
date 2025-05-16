import tkinter as tk
from tkinter import messagebox
import folium
from geopy.distance import geodesic
import webbrowser
import os

class CellTowerLocationTool:
    def __init__(self, master):
        self.master = master
        master.title("Cell Tower Location Tool")

        self.map_frame = tk.Frame(master)
        self.map_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.control_frame = tk.Frame(master)
        self.control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=20, pady=20)

        self.operator_label = tk.Label(self.control_frame, text="Select Operator:")
        self.operator_label.pack()

        self.operator_var = tk.StringVar(value="airtel")
        self.operator_menu = tk.OptionMenu(self.control_frame, self.operator_var,
                                           "airtel", "reliance", "bsnl", "tata",
                                           "idea", "uninor", "jio", "videocon",
                                           "mtnl", "vodafone", "mts")
        self.operator_menu.pack()

        self.lat_label = tk.Label(self.control_frame, text="Latitude:")
        self.lat_label.pack()
        self.lat_entry = tk.Entry(self.control_frame)
        self.lat_entry.pack()

        self.lng_label = tk.Label(self.control_frame, text="Longitude:")
        self.lng_label.pack()
        self.lng_entry = tk.Entry(self.control_frame)
        self.lng_entry.pack()

        self.add_marker_button = tk.Button(self.control_frame, text="Add Marker", command=self.add_marker)
        self.add_marker_button.pack(pady=5)

        self.calculate_distance_button = tk.Button(self.control_frame, text="Calculate Distance", command=self.calculate_distance)
        self.calculate_distance_button.pack(pady=5)

        self.zoom_level_button = tk.Button(self.control_frame, text="Find Nearest Zoom Level", command=self.find_nearest_zoom_level)
        self.zoom_level_button.pack(pady=5)

        self.output_label = tk.Label(self.control_frame, text="Output:")
        self.output_label.pack()
        self.output_text = tk.Text(self.control_frame, height=8, width=40)
        self.output_text.pack()

        self.markers = []
        self.map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
        self.map_path = "map.html"

    def add_marker(self):
        try:
            lat = float(self.lat_entry.get())
            lng = float(self.lng_entry.get())
            operator = self.operator_var.get()

            position = (lat, lng)
            folium.Marker(location=position, popup=operator).add_to(self.map)
            self.markers.append(position)

            self.map.save(self.map_path)
            self.update_map_view()

            self.output_text.insert(tk.END, f"Added marker for {operator} at ({lat}, {lng})\n")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values for latitude and longitude.")

    def calculate_distance(self):
        if len(self.markers) < 2:
            messagebox.showerror("Error", "Add at least two markers to calculate the distance.")
            return

        try:
            dist = geodesic(self.markers[0], self.markers[1]).kilometers
            self.output_text.insert(tk.END, f"Distance between markers: {dist:.2f} km\n")
        except Exception as e:
            messagebox.showerror("Calculation Error", f"An error occurred while calculating the distance: {e}")

    def find_nearest_zoom_level(self):
        if not self.markers:
            messagebox.showerror("Error", "Add at least one marker to find the nearest zoom level.")
            return

        try:
            bounds = [[lat, lng] for lat, lng in self.markers]
            self.map.fit_bounds(bounds)
            self.map.save(self.map_path)
            self.update_map_view()
            self.output_text.insert(tk.END, "Updated map to nearest zoom level.\n")
        except Exception as e:
            messagebox.showerror("Zoom Error", f"An error occurred while adjusting the zoom level: {e}")

    def update_map_view(self):
        path = os.path.abspath(self.map_path)
        webbrowser.open(f"file://{path}", new=0)  # Opens or refreshes in the same tab

def main():
    root = tk.Tk()
    app = CellTowerLocationTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()
