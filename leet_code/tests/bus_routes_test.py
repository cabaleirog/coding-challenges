from leet_code.bus_routes import buses_to_destination


def test_website_example():
    assert buses_to_destination([[1, 2, 7], [3, 6, 7]], 1, 6) == 2


def test_same_bus_route_to_destination():
    routes = [[1, 2], [2, 3], [3, 4], [4, 5]]
    assert buses_to_destination(routes, 1, 2) == 1
    assert buses_to_destination(routes, 2, 3) == 1
    assert buses_to_destination(routes, 3, 4) == 1
    assert buses_to_destination(routes, 4, 5) == 1


def test_two_buses_required_to_destination():
    routes = [[1, 2], [2, 3], [3, 4], [4, 5]]
    assert buses_to_destination(routes, 1, 3) == 2
    assert buses_to_destination(routes, 2, 4) == 2
    assert buses_to_destination(routes, 3, 5) == 2


def test_no_route_to_destination():
    routes = [[1, 2], [2, 3], [4, 5]]
    assert buses_to_destination(routes, 1, 4) == -1
    assert buses_to_destination(routes, 2, 4) == -1
    assert buses_to_destination(routes, 3, 4) == -1


def test_only_one_bus_route_available():
    routes = [[1, 2, 3, 4]]
    assert buses_to_destination(routes, 1, 2) == 1
    assert buses_to_destination(routes, 2, 3) == 1
    assert buses_to_destination(routes, 3, 4) == 1


def test_starting_stop_equals_destination_stop():
    # No need to take a bus if start and destination are the same.
    routes = [[1, 2, 3, 4], [3, 4]]
    assert buses_to_destination(routes, 1, 1) == 0
    assert buses_to_destination(routes, 2, 2) == 0
    assert buses_to_destination(routes, 3, 3) == 0
    assert buses_to_destination(routes, 4, 4) == 0
