travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_add, visited_add, places_add):
    add_data = {}
    add_data["country"] = country_add
    add_data["visits"] = visited_add
    add_data["places"] = places_add
    travel_log.append(add_data)
      

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)