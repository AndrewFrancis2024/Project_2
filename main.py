"""

"""

from itertools import permutations, combinations_with_replacement

city_temps = {
    "Casa_Grande": [76, 69, 60, 64, 69],
    "Chandler": [77, 68, 61, 65, 67],
    "Flagstaff": [46, 35, 33, 40, 44],
    "Lake Havasu City": [71, 65, 63, 66, 68],
    "Sedona": [62, 47, 45, 51, 56]
}

hotel_rates = {
    "Motel 6": 89,
    "Best Western": 109,
    "Holiday Inn Express": 115,
    "Courtyard by Marriott": 229,
    "Residence Inn": 199,
    "Hampton Inn": 209
}


HOTEL_BUDGET = 850

# finding the route


def find_route():
    """ This will take the highest average of all the permutations of the cities'
    temperatures to find a route"""
    # test_perm = []
    # cities, temps = zip(*city_temps)
    # for i in temps:
    #     for t in i:
    #         test_perms.append(permutations())


# finding the hotel
days = len(city_temps)


def find_max():
    """ This will give us the best combination for which hotels
    to stay to use as much of our budget as possible."""
    test_hotels = list(filter(lambda x: sum(x) <= HOTEL_BUDGET,
                              (combinations_with_replacement(hotel_rates.values(), days))))
    return max(test_hotels)


def list_hotel(lst):
    """This returns the names of the hotels for the best fitting our budget"""
    hotels = []
    for i in lst:
        for key, value in hotel_rates.items():
            if i == value:
                hotels.append(key)
    return hotels


if __name__ == "__main__":
    cities = list(city_temps.keys())
    # ..
    print(f'Here is your best route: {None} the average of the daily max temp. is {None}F')

    print(f'To max out your hotel budget, stay at these hotels:'
          f' {", ".join((list_hotel(find_max())))},\ntotaling ${sum(find_max())}')
