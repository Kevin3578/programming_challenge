import csv

class schoolDataParser:
    def __init__(self, schoolDataFile):
        self.schoolData = schoolDataFile
        self.cities = {}
        self.states = {}
        self.metrolocales = {}
        with open(self.schoolData, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['LCITY05'] not in self.cities:
                    self.cities[row['LCITY05']] = 1
                else:
                    self.cities[row['LCITY05']] += 1
                if row['LSTATE05'] not in self.states:
                    self.states[row['LSTATE05']] = 1
                else:
                    self.states[row['LSTATE05']] += 1
                if row['MLOCALE'] not in self.metrolocales:
                    self.metrolocales[row['MLOCALE']] = 1
                else:
                    self.metrolocales[row['MLOCALE']] += 1

    def print_counts(self):
        print("Total Schools: " + str(sum(self.cities.values())))

        print('Schools by State')
        for key, value in self.states.items():
            print(key + ': ' + str(value))

        print('Schools by Metro-centric locale')
        for key, value in self.metrolocales.items():
            print(key + ': ' + str(value))
        
        most_schools = max(self.cities, key=self.cities.get)
        print("City with most schools: " + most_schools + ' (' + str(self.cities[most_schools]) + ' schools)')
        print("Unique cities with at least one school: " + str(len(self.cities)))

if __name__ == '__main__':
    schoolData = schoolDataParser('school_data.csv')
    schoolData.print_counts()