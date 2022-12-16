import re

def parse_valves(data):
    valves = {}  # to store the flow rate and connections of each valve,
    valve_to_num = {}  # a mapping from valve names to numerical values
    for line in data:
        flow_rate = int(re.findall(r"([\d]+)", line)[0])
        valve = re.findall(r"([A-Z]+)", line)[1]
        next_valves = re.findall(r"([A-Z]+)", line)[2:]
        valves[valve] = (flow_rate, next_valves)
        # Add an entry to the valve_to_num dictionary for the current valve, 
        # with a unique numerical value obtained by shifting 1 left by the number of entries in the dictionary
        # to ensure that each valve is assigned a unique numerical value
        # This value can be used to mark whether a valve has been opend.
        valve_to_num[valve] = 1 << len(valve_to_num) 

    # Update the valves dictionary to use the numerical values from the valve_to_num dictionary as keys, 
    # and the names of the connected valves as numerical values
    valves = {
        valve_to_num[valve]: (flow_rate, tuple(map(valve_to_num.get, next_valves)))
        for valve, (flow_rate, next_valves) in valves.items()
    }

    return valves, valve_to_num

def find_max_pressure(s):
    valves, valve_to_num = parse_valves(s)

    TOTAL_TIME = 30
    # Initialize list of states with starting position, opened positions (0: closed, 1: opened), and with pressure set to 0
    states = [(valve_to_num['AA'], 0, 0)] 
    best = {}

    for time in range(1, TOTAL_TIME+1):
        new_states = []
        for loc, opened, pressure in states:
            key = (loc, opened)
            # If this location and opened valves combination has been seen before 
            # and the pressure is lower than the highest pressure achieved, skip this state
            if key in best and pressure <= best[key]:
                continue
            # Update the highest pressure achieved for this location and opened valves combination
            best[key] = pressure
            flow_rate, next_valves = valves[loc]

            # If the valve at the current location is closed and has a positive flow rate, 
            # add a new state with the valve opened and the pressure increased
            if loc & opened == 0 and flow_rate > 0:
                new_states.append((loc, opened | loc, pressure + flow_rate * (TOTAL_TIME - time)))

            # bfs
            for next_valve in next_valves:
                new_states.append((next_valve, opened, pressure))

        states = new_states
        
    answer = max(pressure for _, _, pressure in states)
    return answer

data = open('input.txt').readlines()
print(find_max_pressure(data))