# PTV Visum related scripts

The set of the scripts used for automating tasks in PTV Visum software.

Scripts are using Visum COM interface to interfere with software's objects and methods.

#### Edit Count location

Script assign proper count location number to the set of detectors inside .net file (a file containing all elements of Visum's network model).
Assigining of count location is crucial for the model update process - only detectors with a count location number are taken into PTV Optima (Real-time Traffic Management system) database.

#### New set of paths

The script was used to find the shortest path (using travel time criterium) between zones of the transport model (Stuttgart city model - City Center area).
1.  The script takes the set of active zones as the area where the search should be conducted
2.  Then for each pair origin zone - destination zone a search is conducted using Visum's object for Shortest Path searching: `RS = Visum.Analysis.RouteSearchPrT`
3.  The result for each path is then stored in Paths Set.

Based on the paths the fare for Mobility as a Service ride was calculated (a ride cost dependent on the number of zones crossed during trip)

#### Matrix Creation

The script was used for calculation the demand matrix (matrix containg the number of trips from an origin zone to a destination zone) for a date picked by the user based on the trial phase data.

Data about trip requests were gathered during a trial run of the service (trip request for a ride using the mobile app). Each request was described using the origin coordinates, destination coordinates, user id, number of passengers and timestamps.

1. Raw data was imported and converted to the shapefile (using QGIS software) as a point objects.
2. The file was later on imported into Visum as a POI.
3. Each point was assign with the proper id of the zone in which it was located.

Using the script directly in Visum:
1. A user prompts a date for which the matrix should be created.
2. Only valid POI are filterd out
3. The origin and destination zoneis checked for each trip request, including number of passengers.
4. The final matrix is created and stored in Visum.


