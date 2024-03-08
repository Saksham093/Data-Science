# P02 Data Science Cheatsheet : 08-03-2024

> Page - 2/2

## Table of Contents

- [P02 Data Science Cheatsheet : 08-03-2024](#p02-data-science-cheatsheet--08-03-2024)
  - [Table of Contents](#table-of-contents)
  - [Data Cleaning](#data-cleaning)
    - [Errors vs. Artifacts](#errors-vs-artifacts)
    - [Data Compatibility](#data-compatibility)
    - [Data Imputation](#data-imputation)
    - [Outlier Detection](#outlier-detection)
    - [Miscellaneous](#miscellaneous)

## Data Cleaning

Data Cleaning is the process of turning raw data into a clean and analyzable data set. `"Garbage in, garbage out."` Make sure garbage doesn’t get put in.

### Errors vs. Artifacts

1. **Errors**: information that is lost during acquisition and can never be recovered e.g. power outage, crashed servers
2. **Artifacts**: systematic problems that arise from the data cleaning process. these problems can be corrected but we must first discover them

### Data Compatibility

Data compatibility problems arise when merging datasets. Make sure you are comparing `"apples to apples"` and not `"apples to oranges"`. Main types of conversions/unifications:

- **units** (metric vs. imperial)
- **numbers** (decimals vs. integers)
- **names** (John Smith vs. Smith, John)
- **time/dates** (UNIX vs. UTC vs. GMT)
- **currency** (currency type, inflation-adjusted, dividends)

### Data Imputation

Process of dealing with missing values. The proper methods depend on the type of data we are working with. General methods include:

- Drop all records containing missing data
- Heuristic-Based: make a reasonable guess based on knowledge of the underlying domain
- Mean Value: fill in missing data with the mean
- Random Value
- Nearest Neighbor: fill in missing data using similar data points
- Interpolation: use a method like linear regression to predict the value of the missing data

### Outlier Detection

Outliers can interfere with analysis and often arise from mistakes during data collection. It makes sense to run a ”sanity check”.

### Miscellaneous

Lowercasing, removing non-alphanumeric, repairing, unidecode, removing unknown characters

*Note*: When cleaning data, always maintain both the raw data and the cleaned version(s). The raw data should be kept intact and preserved for future use. Any type of data cleaning/analysis should be done on a copy of the raw data.

<div align="left"><a href="./P_01_DSC.md">Previous Page</a></div>

<div align="right"><a href="./P_03_DSC.md">Next Page</a></div>
