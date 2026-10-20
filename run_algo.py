"""
Run one FD discovery algorithm from Desbordante on one CSV file and print
the result as JSON: {"fds": <number of minimal FDs>, "seconds": <runtime>}.

It runs in its own process, so the notebook can stop it when it goes over
the time limit (the paper used a 4-hour limit, "TL" in Table 1).

Usage: python run_algo.py <algorithm> <csv_path> <threads>
"""
import json
import sys
import time

import desbordante
import pandas as pd

ALGORITHMS = {
    "Tane": desbordante.afd.algorithms.Tane,   # exact FDs when error = 0
    "Fun": desbordante.fd.algorithms.FUN,
    "FdMine": desbordante.fd.algorithms.FdMine,
    "Dfd": desbordante.fd.algorithms.DFD,
    "DepMiner": desbordante.fd.algorithms.Depminer,
    "FastFDs": desbordante.fd.algorithms.FastFDs,
    "Fdep": desbordante.fd.algorithms.FDep,
    "HyFD": desbordante.fd.algorithms.HyFD,
}
MULTI_THREADED = {"Dfd", "FastFDs", "HyFD"}


def main():
    name, path, threads = sys.argv[1], sys.argv[2], int(sys.argv[3])
    # every value is read as text; empty cells and "?" stay ordinary values
    df = pd.read_csv(path, header=None, dtype=str, keep_default_na=False)
    algo = ALGORITHMS[name]()
    algo.load_data(table=df)

    start = time.perf_counter()          # time only the discovery itself
    if name == "Tane":
        algo.execute(error=0.0)
    elif name in MULTI_THREADED:
        algo.execute(threads=threads)
    else:
        algo.execute()
    seconds = time.perf_counter() - start

    print(json.dumps({"fds": len(algo.get_fds()), "seconds": seconds}))


if __name__ == "__main__":
    main()
