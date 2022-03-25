import csv
segments = {}

class Route:
    def __init__(self, origin, dest, airline, pax, seats):
        self.origin = origin
        self.dest = dest
        self.airline = airline
        self.pax = pax
        self.seats = seats
    def __repr__(self):
        return self.airline if not(self.airline == None) else self.origin + '-' + self.dest
    def __eq__(self, other):
        return (self.origin == other.origin) and (self.dest == other.dest) and (self.airline == other.airline) and (self.pax == other.pax) and (self.seats == other.seats)
    def __add__(self,other):
        newOrigin = self.origin if self.origin == other.origin else None
        newDest = self.dest if self.dest == other.dest else None
        newAirline = self.airline if self.airline == other.airline else None
        newPax = (self.pax) + (other.pax)
        newSeats = (self.seats) + (other.seats)
        return Route(newOrigin, newDest, newAirline, newPax, newSeats)
    def stats(self):
        return self.airline, self.seats, self.pax

airport = input('From which airport? ')

def set_up(year):
    year = str(year)
    with open(year + 'pax.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        global segments
        for i in range(1,13):
            segments[i] = {}
        for row in reader:
            global airport
            match = 0
            if row['CLASS'] == 'F' and row['ORIGIN'] == airport:
                if segments[int(row['MONTH'])].get(row['DEST']) == None:
                    segments[int(row['MONTH'])][row['DEST']] = []
                for j in range(len(segments[int(row['MONTH'])][row['DEST']])):
                    if segments[int(row['MONTH'])][row['DEST']][j].airline == row['UNIQUE_CARRIER']:
                        segments[int(row['MONTH'])][row['DEST']][j] += Route(row['ORIGIN'],row['DEST'],row['UNIQUE_CARRIER'],float(row['PASSENGERS']),float(row['SEATS']))
                        match = 1
                if match == 0:
                    segments[int(row['MONTH'])][row['DEST']].append(Route(row['ORIGIN'],row['DEST'],row['UNIQUE_CARRIER'],float(row['PASSENGERS']),float(row['SEATS'])))
        print('finished')

def collate():
    for i in range(1,13):
        for j in segments[i]:
            segments[i][j] = total_int(i,j)
    print('collated')

def total(month,dest):
    global airport
    answer = Route(airport,dest,None,0,0)
    for i in segments[month][dest]: answer += i
    print(answer.dest + "\t" + str(answer.seats) + "\t" + str(answer.pax))

def total_int(month,dest):
    global airport
    answer = Route(airport,dest,None,0,0)
    for i in segments[month][dest]: answer += i
    return answer

def mon_total(month):
    for i in segments[month]:
        total(month,i)

def coll_mon(month):
    for i in segments[month]:
        print(segments[month][i],segments[month][i].seats,segments[month][i].pax)

def coll_yr():
    answer = {}
    for i in range(1,13):
        for j in segments[i]:
            if not(j in answer):
                global airport
                answer[j] = Route(airport,j,None,0,0)
            answer[j] += segments[i][j]
    for i in answer:
        print(i,answer[i].seats,answer[i].pax)
