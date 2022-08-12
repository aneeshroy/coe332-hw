# A Space Turbidity: Martian Water Samples

## Description

This project uses data from a set of samples taken from water on Mars to determine whether the turbidity is low enough to be safe for analysis. It consists of `analyze_water.py`, `test_analyze_water.py`, and `turbidity_data.json`, which should be downloaded before running (intstructions below).

## Downloading the Data Set

Run the following command in your terminal while in the homework directory to get the data file

`wget https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json`

You can also copy and paste the contents of the file into a JSON file named `turbidity_data.json` if you would like.

# analyze_water.py Description

This file calculates the turbidity of the water taken from the 5 most recent samples, determines whether the water is below the threshold for analysis, and if not determines the minimum time required for the turbidity to fall below the threshold.

# test_analyze_water.py Description

This file uses the Pytest library to test different parts of the `analyze_water.py` and assure every function is running as it is supposed to.

# Procedure

1. Download the Dataset (instructions above)
2. Run `analyze_water.py`. The results should look something like this in the terminal:
```
Average turbidity based on most recent five measurements = 1.1621637999999999 NTU
WARNING:root:Turbidity is above threshold for safe use
Minimum time required to return below a safe threshold = 7.4387858017596855 hours
```
3. To see the results of `test_analyze_water.py`, run the program and then use `pytest` command in the terminal to see the results.
