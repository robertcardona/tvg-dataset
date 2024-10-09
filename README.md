# tvg-dataset
TVG Dataset

This dataset is generated as follows.
For each year in `years = [2024, 2025,2026, 2027]`, we generate `m = 100`
simulations, chosen randomly, for each `n` in `[5, 10, 20, 50, 100]`.
`n` represents the number of satellites chosen randomly from satrlink on
that given day. For each `m` we choose a random day of that year and sample
`n` satellites from starlink and run the simulation for `5_400` seconds, 
and then choose another random sample and day of the year and run the 
simulation for `86_400` seconds.

Each simulation also includes moon and mars satellites.
They can be filtered out of the contact plan during the parsing stage.

The starlink satellites orbit Earth every 90 minutes.
In the Distances and Coordinates reports the delta is set to `step_size = 300`
for every 90-minute simulation (`5_400` seconds). 
That is, the distances and coordinates are measured every five minutes.
For the simulations lasting a day (`86_400` seconds), the delta is set to 
`step_size = 3600`, or every hour.

After generating we delete the `.orb` files with `rm -R **/*.orb` in the root
of this repository. We commit by year with `git add ./data/2024/\*` followed
by `git commit -m "Add Starlink simulations : 2024"` and repeat for each year.

Files have the following format : `fmt = "sl_{n}_{duration}_{d:%Y%m%d}.orb"`
where `n` represents the number of satellites chosen from the starlink 
TLE set (obtained from celestrak).

# Usage

Install `soap-parser` and run `generator.py` to generate the dataset.