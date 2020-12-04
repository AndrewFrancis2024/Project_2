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
def temp_route(route):  # a permutation
    """This will find the average temp for a certain route"""
    for i in range(len(route)):
        city = route[i]
        temp_list = [city_temps[city][i] for i in range(len(route))]
    return sum(temp_list)/len(route)  # average temp of route


def best_route(all_routes):
    """This will provide the route with the highest average temperature"""
    max_temp = 0
    best = None
    for r in all_routes:
        if max_temp < temp_route(r):
            max_temp = temp_route(r)
            best = r
    return best, max_temp


our_route, best_avg_temp = best_route((permutations(city_temps.keys())))


# finding the hotel
def find_max():
    """ This will give us the best combination for which hotels
    to stay to use as much of our budget as possible."""
    test_hotels = list(filter(lambda x: sum(x) <= HOTEL_BUDGET,
                              (combinations_with_replacement(hotel_rates.values(), len(city_temps)))))
    return max(test_hotels)


def list_hotel(lst):
    """This returns the names of the hotels for the best fitting our budget"""
    hotels = [key for i in lst for key, value in hotel_rates.items() if i == value]
    return hotels


if __name__ == "__main__":
    cities = list(city_temps.keys())
    # ..
    print(f'Here is your best route: {str(our_route)[1:-1]} the average of the daily max temp. is {best_avg_temp}F')
    print(f'To max out your hotel budget, stay at these hotels:'
          f' {", ".join((list_hotel(find_max())))},\ntotaling ${sum(find_max())}')
