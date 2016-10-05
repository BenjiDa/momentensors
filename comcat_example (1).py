#!/usr/bin/env python

from datetime import datetime
import pprint
from libcomcat import comcat
import numpy as np

if __name__ == '__main__':
    printer = pprint.PrettyPrinter(indent=2)
    ymax,xmin = (37.60954,-122.578583)
    ymin,xmax = (37.116184,-121.919403)
    starttime = datetime(2012,1,1)
    endtime = datetime.utcnow()
    magrange = (2.5,9.9)
    data,maxmags = comcat.getEventData(bounds=(xmin,xmax,ymin,ymax),
                               starttime=starttime,endtime=endtime,
                               magrange=magrange,
                               getComponents=True,
                               getAngles=True)
    for event in data:
        #each value in the event dictionary contains a list the value 
        #and the formatting string used to display that value.
        #for this application, just get the value
        #sometimes these values will be NaN.
        strike1 = event['strike1'][0]
        dip1 = event['dip1'][0]
        rake1 = event['rake1'][0]
        strike2 = event['strike2'][0]
        dip2 = event['dip2'][0]
        rake2 = event['rake2'][0]
        
