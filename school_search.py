import csv
import time

class schoolDataParser:
    def __init__(self, schoolDataFile):
        state_abbreviations = {
            "AL": "Alabama",
            "AK": "Alaska",
            "AZ": "Arizona",
            "AR": "Arkansas",
            "CA": "California",
            "CO": "Colorado",
            "CT": "Connecticut",
            "DC": "District of Columbia",
            "DE": "Delaware",
            "FL": "Florida",
            "GA": "Georgia",
            "HI": "Hawaii",
            "ID": "Idaho",
            "IL": "Illinois",
            "IN": "Indiana",
            "IA": "Iowa",
            "KS": "Kansas",
            "KY": "Kentucky",
            "LA": "Louisiana",
            "ME": "Maine",
            "MD": "Maryland",
            "MA": "Massachusetts",
            "MI": "Michigan",
            "MN": "Minnesota",
            "MS": "Mississippi",
            "MO": "Missouri",
            "MT": "Montana",
            "NE": "Nebraska",
            "NV": "Nevada",
            "NH": "New Hampshire",
            "NJ": "New Jersey",
            "NM": "New Mexico",
            "NY": "New York",
            "NC": "North Carolina",
            "ND": "North Dakota",
            "OH": "Ohio",
            "OK": "Oklahoma",
            "OR": "Oregon",
            "PA": "Pennsylvania",
            "RI": "Rhode Island",
            "SC": "South Carolina",
            "SD": "South Dakota",
            "TN": "Tennessee",
            "TX": "Texas",
            "UT": "Utah",
            "VT": "Vermont",
            "VA": "Virginia",
            "WA": "Washington",
            "WV": "West Virginia",
            "WI": "Wisconsin",
            "WY": "Wyoming",
        }

        self.schoolData = schoolDataFile
        self.mapping = {}

        with open(self.schoolData, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                myset = {word.lower() for word in row["SCHNAM05"].split()}
                myset.update(row["LCITY05"].lower().split())
                myset.update(state_abbreviations.get(row["LSTATE05"], "").lower().split())
                fset = frozenset(myset)
                self.mapping[fset] = row["SCHNAM05"] + '\n' + row['LCITY05'] + ',' + row['LSTATE05']                

    def search_schools(self, search_string):
        start = time.time()
        results = {}
        original_search_string = search_string
        search_string_list = search_string.lower().split()
        if "school" in search_string_list:
            search_string_list.remove("school")
        search_set = frozenset(search_string_list)

        for d in self.mapping:
            intersection_size = len(d & search_set)
            if intersection_size > 0:
                results[d] = intersection_size
        results = dict(sorted(results.items(), key=lambda x: x[1], reverse=True))
        end = time.time()

        print("Results for " + original_search_string + " (Search took " + str(round(end-start,4)) + " seconds)")
        counter = 1
        for result in results:
            print(str(counter)+'. '+self.mapping[result])
            counter += 1
            if counter == 4:
                break

if __name__ == "__main__":
    schoolData = schoolDataParser("school_data.csv")
    schoolData.search_schools("elementary school highland park")
    schoolData.search_schools("jefferson belleville")
    schoolData.search_schools("riverside school 44")
    schoolData.search_schools("granada charter school")
    schoolData.search_schools("foley high alabama")
    schoolData.search_schools("KUSKOKWIM")