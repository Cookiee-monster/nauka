#! Python 3

# adding new pathset
path_set_no = 43
Visum.Net.AddPathSet(path_set_no)

# get the list of active zones
active_zone_tuples = Visum.Net.Zones.GetMultiAttValues("NO", OnlyActive=True)
active_zones = []
for zone_tuple in active_zone_tuples:
    active_zones.append(zone_tuple[1])

i = 1 # iterator of paths
for start_zone in active_zones:
    for end_zone in active_zones:
        if start_zone != end_zone:

            # Shortest route search
            RS = Visum.Analysis.RouteSearchPrT

            # Pick the zones
            N1 = Visum.Net.Zones.ItemByKey(start_zone)
            N2 = Visum.Net.Zones.ItemByKey(end_zone)

            # Create a new network element - pair of zones
            NElem = Visum.CreateNetElements()
            NElem.Add(N1)
            NElem.Add(N2)

            # To search the shortest path for desired zones pair
            RS.Execute(NElem, "P", 0, IndexAttribute=u'')

            # To extract nodeschain
            node_chain = RS.NodeChainPrT

            # To add a path to the set
            Visum.Net.AddPath(i, path_set_no, start_zone, end_zone, node_chain)

            # Clearing last result
            RS.Clear()
            RS = None
            i += 1
