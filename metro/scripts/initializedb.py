import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models import (
    DBSession,
    Station,
    Phase,
    Route,
    Base,
    )

original_stations = ["CST",
"Masjid",
"Sandhurst Road",
"Byculla",
"Chinchpokli",
"Currey Road",
"Parel",
"Dadar",
"Matunga",
"Sion",
"Kurla",
"Vidyavihar",
"Ghatkopar",
"Vikhroli",
"Kanjurmarg",
"Bhandup",
"Nahur",
"Mulund",
"Thane",
"Kalyan"]

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    add_phase(settings)
    add_station_routes(settings)

def add_phase(settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        phase = Phase(id=1, name='phase1')
        DBSession.add(phase)


def add_station_routes(settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)

    with transaction.manager:
        stations = [Station(id=station_order, name= station_name)
                    for (station_order, station_name) in enumerate(original_stations,1)]
        route = [Route(phase_id=1, station_id=station.id, order=station_order)
                 for (station_order, station) in enumerate(stations,1)]
        [DBSession.add(station) for station in stations]
        [DBSession.add(stop) for stop in route]
