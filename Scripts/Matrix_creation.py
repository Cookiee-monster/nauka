#! Python 3

import numpy
import Tkinter as Tk
from VisumPy import helpers as helpers


# Required date as an input

class window():
    def __init__(self):
        #Start root:
        self.root = Tk.Tk()
        self.root.attributes("-topmost", True)

        #Label:
        Tk.Label(self.root,text="Set the required date You want to use to create the matrix").pack()

        #Define object selector and pack it to the frame:
        self.textctrl=Tk.Entry(self.root)
        self.textctrl.insert(0,"DD.MM.YYYY")
        self.textctrl.pack()

        #Define buttons and pack it to the frame:
        self.button = Tk.Button(self.root, font=("Arial", 10), text="OK", command=self.ok)
        self.cancel_button = Tk.Button(self.root, font=("Arial", 10), text="Cancel", command=self.cancel)
        self.button.pack()
        self.cancel_button.pack()

        #Start window mainloop:
        self.root.mainloop()


    def ok(self):
        self.required_date = str(self.textctrl.get())
        if len(self.required_date) != 10:
            # tkMessageBox.showinfo("Title", "Please enter the date in the DD.MM.YYYY format.")
            self.root.destroy()
            win = window()
        self.cont = True
        self.root.destroy()

    def cancel(self):
        self.cont = False
        self.root.destroy()


#Start GUI:
win = window()
while win.cont == True:

    required_date = win.required_date

    # Filter by the given date

    poi_filter = Visum.Filters.POIFilter(48)
    poi_filter.RemoveConditions()
    poi_filter.AddCondition("OP_NONE", False, "DATE", 9, required_date, Position=-1)
    if poi_filter.UseFilter != True:
        poi_filter.UseFilter = True

    # Creating the clear matrix

    all_matrices = Visum.Net.Matrices.GetMultiAttValues("NO", OnlyActive=False)
    new_matrix_no = all_matrices[-1][1] + 1 # Incrementing the last NO of matrix

    new_matrix = Visum.Net.AddMatrix(new_matrix_no, objectTypeRef=2, MatrixType=3)
    # objectTypeRef=2 - as for a zone-based matrix
    # MatrixType=3 - as for a demand matrix

    new_matrix.SetAttValue("NAME", ("Trip Requests_" + str(required_date)))

    # Getting the matrix as an array

    new_matrix = helpers.GetMatrix(Visum, new_matrix_no)

    # Translation between zones no and array index

    zones = helpers.GetContainer(Visum, "Zones")
    zones_list = helpers.GetMulti(zones, "NO")
    zones_dict = {}
    i = 0
    for zone in zones_list:
        zones_dict[int(zone)] = i
        i += 1

    # Getting the trip requests for the filtered date

    trip_req_poi = helpers.GetContainer(Visum, "POI: Trip Request")
    trip_id = helpers.GetMulti(trip_req_poi, "ID_INTERNA", activeOnly=True)
    trip_type = helpers.GetMulti(trip_req_poi, "O_D", activeOnly=True)
    trip_zone = helpers.GetMulti(trip_req_poi, "ZONE", activeOnly=True)
    trip_passanger = helpers.GetMulti(trip_req_poi, "TOTAL_PAS", activeOnly=True)

    # O-D pair comparing
    for i in range(0, len(trip_id)/2):
        if trip_id[i] == trip_id[i+1]:
            if trip_type[i] == "O":
                origin_zone = trip_zone[i]
                j = i+1
                dest_zone = trip_zone[j]
            else:
                dest_zone = trip_zone[i]
                j = i + 1
                origin_zone = trip_zone[j]
        else:
            if trip_type[i] == "O":
                origin_zone = trip_zone[i]
                id_temp = trip_id[i]
                # First the D type POIs were imported and later the O type
                # due to that they are not pairs
                j = trip_id.index(id_temp, i+1, len(trip_id))
                dest_zone = trip_zone[j]
            else:
                dest_zone = trip_zone[i]
                id_temp = trip_id[i]
                j = trip_id.index(id_temp, i+1, len(trip_id))
                origin_zone = trip_zone[j]

        if origin_zone != 0 and dest_zone != 0:
            origin_row = zones_dict[origin_zone]
            destin_col = zones_dict[dest_zone]
            new_matrix[origin_row, destin_col] += (trip_passanger[i] + trip_passanger[j])

    # Setting the matrix using numpy array

    helpers.SetMatrix(Visum, new_matrix_no, new_matrix)
    win = window()