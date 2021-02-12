from datetime import datetime
import io

import matplotlib.pyplot as plt
import math

from obspy.geodetics.base import gps2dist_azimuth
from obspy.imaging.beachball import beachball
from obspy.imaging.beachball import beach
from libcomcat.dataframes import get_detail_data_frame
from libcomcat.search import search, get_event_by_id

# Paths to save data

outfilename = 'C:\\Users\\bmelosh\\Projects\\Geologic_mapping\\Coast_ranges\\Cow_mountain\\Code\\Earthquakes\\mt_symbols'
 

 # Search and download earthquake data from libcomcat

# Download in a cricle,
#summary_events = search(starttime=datetime(1994, 1, 17, 12, 30), endtime=datetime(1997, 1, 18, 12, 35),
#                  maxradiuskm=3, minmagnitude=3, maxmagnitude=8, latitude=38.806467, longitude=-122.449948)

# Download in a box,
box_events = search(starttime=datetime(1984, 1, 1, 12, 30), endtime=datetime(2020, 12, 31, 12, 0), minmagnitude=3,
                   minlatitude=38.884431, maxlatitude=39.370466, minlongitude=-123.296648, maxlongitude=-122.861249)

detail_df = get_detail_data_frame(box_events)

#Print and save focal mechanism

mt = []
name = []
for i in range(0,len(detail_df)):
    if math.isnan(detail_df.nc_np1_strike[i]):
        pass
    else:
        mt_step = [detail_df.nc_np1_strike[i], detail_df.nc_np1_dip[i], detail_df.nc_np1_rake[i]]
        mt.append(mt_step)
        name_step = detail_df.id[i]
        name.append(name_step)

for i in range(0,len(mt)):
    f = beachball(mt[i], outfile = outfilename + '\\%s.svg' % name[i])


# Remove data rows with NaN values in focal mechanisms for data export

df = detail_df.dropna(subset=['nc_np1_strike'])

# Save data as csv for plotting in GIS

df.to_csv('1984-2020.csv')