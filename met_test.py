import json

from time import sleep
from datetime import datetime, timezone
from metno_locationforecast import Place, Forecast

USER_AGENT = "axeltb@stud.ntnu.no"
MOHOLT = Place("Moholt", 63.4113, 10.4339, 116)

moholt_forecast = Forecast(MOHOLT, USER_AGENT, forecast_type="compact")

while True:
    try:
        print(moholt_forecast.update(), datetime.now(timezone.utc).isoformat())
        # with open("data/data.json", "w") as forecast_json:
        #     json.dump(moholt_forecast.data.intervals[0].variables, forecast_json)
        sleep(30)
    except Exception as e:
        print(e)
        break