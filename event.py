from skyfield.api import load, Topos
from datetime import datetime, timedelta

# Load ephemeris data
planets = load('de421.bsp')
earth = planets['earth']
ts = load.timescale()

# Observer location (example: New Delhi)
observer = earth + Topos('28.6139 N', '77.2090 E')
from skyfield import almanac

def get_moon_phases(start_date, end_date):
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = load('de421.bsp')
    f = almanac.moon_phases(eph)
    times, phases = almanac.find_discrete(t0, t1, f)

    phase_names = ['New Moon', 'First Quarter', 'Full Moon', 'Last Quarter']
    for t, p in zip(times, phases):
        print(f"{t.utc_strftime('%Y-%m-%d %H:%M')} UTC - {phase_names[p]}")

# Example: Next 30 days
today = datetime.utcnow()
get_moon_phases(today, today + timedelta(days=30))
import requests

def get_meteor_showers():
    url = "https://ssd-api.jpl.nasa.gov/fireball.api"
    params = {"date-min": "2024-01-01", "req-loc": "false"}
    response = requests.get(url, params=params)
    data = response.json()

    print("Recent Fireball Events (NASA):")
    for event in data.get("data", [])[:5]:
        print(f"Date: {event[0]}, Energy: {event[1]} kt")

get_meteor_showers()
def track_planets(date):
    t = ts.utc(date.year, date.month, date.day)
    for name in ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn']:
        planet = planets[name]
        astrometric = observer.at(t).observe(planet)
        alt, az, distance = astrometric.apparent().altaz()
        print(f"{name}: Altitude {alt.degrees:.2f}°, Azimuth {az.degrees:.2f}°")

track_planets(datetime.utcnow())

