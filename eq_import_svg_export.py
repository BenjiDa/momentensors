# stdlib imports
from datetime import datetime
import io

# Third party imports
from IPython.display import display, HTML
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from obspy.geodetics.base import gps2dist_azimuth
from obspy.imaging.beachball import beachball
from obspy.imaging.beachball import beach

# Local imports
from libcomcat.dataframes import (get_detail_data_frame, get_dyfi_data_frame,
                                  get_history_data_frame, get_magnitude_data_frame,
                                  get_pager_data_frame, get_phase_dataframe,
                                  get_summary_data_frame)
from libcomcat.search import search, get_event_by_id


# Search and download earthquake data from libcomcat

summary_events = search(starttime=datetime(1985, 1, 17, 12, 30), endtime=datetime(1995, 1, 18, 12, 35),
                   maxradiuskm=3, minmagnitude=3, maxmagnitude=8, latitude=38.806467, longitude=-122.449948)

detail_df = get_detail_data_frame(summary_events)


#Write dataframe to csv in file
detail_df.to_csv('/your/path/data/EQ_search.csv')

# This plots beachballs and exports them as svg files
for i in range(0,len(detail_df)):
    mt = [detail_df.nc_np1_strike[i], detail_df.nc_np1_dip[i], detail_df.nc_np1_rake[i]]
    f = beachball(mt, outfile='/your/path/data/bbs/svg/%s.svg' % detail_df.id[i])



