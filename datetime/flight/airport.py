import csv


class Airport:
    """ Airport as represented in airports.dat """
    # CSV columns will become Airport property names in __init__
    prop_names = ('name', 'city', 'country', 'iata', 'lat', 'long',
                  'utc_offset', 'dst_rule', 'tz')

    def __init__(self, csv_entry):
        """ Put values from a CSV reader entry into the internal dictionary """
        assert len(csv_entry) == len(Airport.prop_names)
        self.__dict__.update(dict(zip(Airport.prop_names, csv_entry)))

    def __str__(self):
        return "{0.iata} ({0.name})".format(self)


def load_airports(csv_file_name):
    """Load airports into a dictionary where keys are IATA codes"""
    airports = {}
    with open(csv_file_name, newline='', encoding='utf-8') as data_file:
        for entry in csv.reader(data_file):
            a = Airport(csv_entry=entry)
            airports[a.iata] = a
    return airports


if __name__ == '__main__':
    airports = load_airports('../../data/airports.csv')
    print(len(airports))
    for a in airports.values():
        print(a)
