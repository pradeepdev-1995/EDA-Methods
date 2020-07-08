# Pandas profiling

Pandas profiling is an open source Python module with which we can quickly do an exploratory data analysis with just a few lines of code. It generates profile reports from a pandas DataFrame. The pandas df.describe() function is great but a little basic for serious exploratory data analysis. pandas_profiling extends the pandas DataFrame with df.profile_report() for quick data analysis.

## Dependancies

pip install -r requirements.txt

## Run
python3 eda_pandas_profiling.py

## Output

Some of the generated outputs are shown below

### Overview
![Alt text](output/overview.png?raw=true "Overview")
### Variables
![Alt text](output/variables.png?raw=true "Variables")
### Interactions
![Alt text](output/interactions.png?raw=true "Interactions")
