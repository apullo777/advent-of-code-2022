from time import time_ns
import sys
import re

def read_input_lines() -> list:
    lines = [re.split('[\\s=;,]+', x) for x in open("input.txt").read().splitlines()]
    return lines

def get_valves_data(lines: list) -> dict:
    # dict values are sets containing the valves that can be reached directly from the key valve.
    valves = {x[1]: set(x[10:]) for x in lines}
    sorted_candidates_rates = {x[1]: int(x[5]) for x in lines if int(x[5]) != 0}

    # using bit masks to represent the state of which valves have been opened.
    states = {x: 1 << i for i, x in enumerate(sorted_candidates_rates)} 

    # This represents the minimum cost of traveling between each pair of nodes.
    distances_to_valves = {x: {y: 1 if y in valves[x] else float('+inf') for y in valves} for x in valves}

    # using distances_to_valves to calculate the minimum cost of traveling 
    # between each pair of nodes using the Floyd-Warshall algorithm.
    for k in distances_to_valves:
        for i in distances_to_valves:
            for j in distances_to_valves:
                distances_to_valves[i][j] = min(distances_to_valves[i][j], 
                                                distances_to_valves[i][k] + distances_to_valves[k][j])
    return {
        'valves': valves,
        'sorted_candidates_rates': sorted_candidates_rates,
        'states': states,
        'distances_to_valves': distances_to_valves
    }

def visit(valve: str, time: int, state: int, value: int, res: dict, valves_data: dict) -> dict:
    # Update the result dictionary with the maximum value seen so far for the given state
    res[state] = max(res.get(state, 0), value)

    for next_valve in valves_data['sorted_candidates_rates']:
        new_time = time - valves_data['distances_to_valves'][valve][next_valve] - 1
        # If a candidate valve has been opened or running out of time, skip this iteration
        if valves_data['states'][next_valve] & state or new_time < 0:
            continue
        # bfs: recursively visit the next candidate
        visit(next_valve, new_time, state | valves_data['states'][next_valve], value + new_time * valves_data['sorted_candidates_rates'][next_valve], res, valves_data)
    return res

def part1(valves_data):
    return max(visit('AA', 30, 0, 0, {}, valves_data).values())

def part2(valves_data):
    visited_2 = visit('AA', 26, 0, 0, {}, valves_data)
    return max(v1+v2 for k1, v1 in visited_2.items() 
                     for k2, v2 in visited_2.items() if not k1 & k2)

def main():
    lines = read_input_lines()
    valves_data = get_valves_data(lines)

    visited_2 = visit('AA', 26, 0, 0, {}, valves_data)

    start = time_ns()
    print(f"Part 1: {part1(valves_data)} in {(time_ns()-start)/1e6}ms")
    start = time_ns()
    print(f"Part 2: {part2(valves_data)} in {(time_ns()-start)/1e6}ms")

if __name__ == '__main__':
    main()