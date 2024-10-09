from soap_parser import orb_builder as ob
from soap_parser import os_utils as osu
from soap_parser import soap_utils as su

from tqdm import tqdm
from datetime import date, datetime, timedelta
from itertools import product
from pathlib import Path
from random import sample

base_path = Path(__file__).parent

fmt = "sl_{n}_{duration}_{d:%Y%m%d}.orb"

year_start = 2024
year_end = year_start + 4

years = list(range(year_start, year_end))

for year in years:
    osu.make_folder(base_path / f"data/{year}")

m = 100
n_list = [5, 10, 20, 50, 100]
durations = [5_400, 86_400]
steps = [300, 3_600]

days = {year : sample(list(range(365)), m) for year in years}

indices = list(product(years, zip(durations, steps), n_list, range(m)))
print(f"Generating {len(indices)} simulations...")

filepaths, count = [], 0
for year, (duration, step_size), n, k in tqdm(indices):
    d = datetime.fromisoformat(f"{year}0101") + timedelta(days=days[year][k])
    filename = fmt.format(
        n = n,
        d = d,
        duration = duration,
        step_size = step_size
    )
    filepath = base_path / f"data/{year}" / filename
    ob.save_orb_file(filepath, n, d, duration, step_size = step_size)
    filepaths.append(filepath)
    count += 1

assert count == len(list(set(filepaths)))
print(f"Simulation generation successful")

print(f"Running {len(indices)} simulations...")

su.run_soap(filepaths)

print(f"{count} simulations were generated in total")
