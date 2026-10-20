# HyFD reproduction – INFOMDWR

Reproduction of Table 1 of Papenbrock & Naumann (2016), *A Hybrid Approach to Functional Dependency Discovery* (SIGMOD '16), using the Desbordante library.

## Files
- `Kibanda_2160579_HyFD_reproduction.ipynb` – notebook with all experiments, saved results and the report
- `run_algo.py` – helper script that runs one algorithm on one dataset (used by the notebook)

## How to run
1. Put both files in the same folder (in Google Colab: upload `run_algo.py` via the Files panel).
2. Run the first cell to install `desbordante`, `numpy`, `pandas` and `matplotlib`.
3. Choose **Run all**. The UCI datasets are downloaded automatically.

A full run takes 2–3 hours; all results are already saved in the notebook.
