__author__ = 'amuneer'
import math
from datetime import datetime

from ..models import (
    DBSession,
    Base,
    Station, Phase, Route
    )




class Ticketer():
    def __init__(self, request):
        self.request = request

    def calculate_fare(self,start_station=None, end_station=None):

        start_station_id = DBSession.query(Station).filter(Station.name==start_station).one().id
        end_station_id = DBSession.query(Station).filter(Station.name==end_station).one().id
        total_stations = int(DBSession.query(Route).filter(Route.phase_id==1).count())
        start_station_order = int(DBSession.query(Route).filter(Route.station_id==start_station_id).one().order)
        end_station_order = int(DBSession.query(Route).filter(Route.station_id==end_station_id).one().order)

        number_of_stops = abs(start_station_order - end_station_order) + 1  # we count start and end stations

        '''
        Minimum number of stations for pricing: 5 stations
        For every 5 stations, the price of ticket  is 5 rupees.
        '''
        considered_fare = math.ceil(number_of_stops/5.0)*5

        '''
        if journey is from beginning of the central line to end,
        then traveller  should get a 20% discount on the ticket
        '''

        #in case of even number of stations, there can be two center station.
        center_stations = [total_stations/2 + 1] if total_stations%2 else [total_stations/2, total_stations/2 + 1]
        if total_stations%2:
            eligible_for_discounts = [(1, total_stations/2 + 1), (total_stations/2 + 1, total_stations)]
        else:
            eligible_for_discounts = [(1, total_stations/2), (total_stations/2 + 1, total_stations)]

        if tuple(sorted((start_station_order, end_station_order))) in eligible_for_discounts:
            considered_fare = considered_fare*80/100

        message = '<br />'.join(('===== CENTRAL RAILWAY======',
                             'Ticket Date/Time: {}'
                             '', 'Journey Begin: {}',
                             'Journey End: {}',
                             'Ticket Cost: {} rupees',
                             '============================ '
                             )).format(str(datetime.now()),
                                       start_station, end_station, str(considered_fare))

        if self.validate_stations(start_station, end_station):
            result = {'amount': str(abs(start_station_order-end_station_order)+1)+' '+str(eligible_for_discounts) +
                                str([start_station_order, end_station_order]),
                      'message': message,
                      'status' : 'success'
                      }
        else:
            result = {'amount': -1,
                      'message': 'Invalid station',
                      'status' : 'failure'
                      }
        return result

    def validate_stations(self, start_station, end_station):
        #TODO: implement validation
        #return all((start_station, end_station))
        return True

#total stations
#middle station
