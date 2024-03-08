# P01 Data Science Cheatsheet : 08-03-2024

> Page - 1/2

## Table of Contents

- [P01 Data Science Cheatsheet : 08-03-2024](#p01-data-science-cheatsheet--08-03-2024)
  - [Table of Contents](#table-of-contents)
  - [What is Data Science?](#what-is-data-science)
  - [Types of Data](#types-of-data)
    - [Data Sources/Fomats](#data-sourcesfomats)
  - [Main Types of Problems](#main-types-of-problems)
  - [Probability Overview](#probability-overview)
    - [Terminology](#terminology)
    - [Independence, Conditional, Compound](#independence-conditional-compound)
    - [Probability Distributions](#probability-distributions)
  - [Descriptive Statistics](#descriptive-statistics)
    - [Centrality](#centrality)
    - [Variability](#variability)
    - [Interpreting Variance](#interpreting-variance)
    - [Correlation Analysis](#correlation-analysis)

## What is Data Science?

Multi-disciplinary field that brings together concepts from computer science, statistics/machine learning, and data analysis to understand and extract insights from the ever-increasing amounts of data.

Two paradigms of data research.

1. **Hypothesis-Driven**: Given a problem, what kind of data do we need to help solve it?
2. **Data-Driven**: Given some data, what interesting problems can be solved with it?

The heart of data science is to always ask questions. Always be curious about the world.

1. What can we learn from this data?
2. What actions can we take once we find whatever it is we are looking for?

## Types of Data

**Structured**: Data that has predefined structures. e.g. tables, spreadsheets, or relational databases.

**Unstructured Data**: Data with no predefined structure, comes in any size or form, cannot be easily stored in tables. e.g. blobs of text, images, audio

**Quantitative Data**: Numerical. e.g. height, weight

**Categorical Data**: Data that can be labeled or divided into groups. e.g. race, sex, hair color.

**Big Data**: *Massive datasets*, or data that contains *greater variety* arriving in increasing *volumes* and with ever-higher *velocity* $(3 Vs)$. Cannot fit in the memory of a single machine.

### Data Sources/Fomats

**Most Common Data Formats** CSV, XML, SQL, JSON, Protocol Buffers **Data Sources** Companies/Proprietary Data, APIs, Government, Academic, Web Scraping/Crawling

## Main Types of Problems

Two problems arise repeatedly in data science.

**Classification**: Assigning something to a discrete set of possibilities. e.g. spam or non-spam, Democrat or Republican, blood type $(A, B, AB, O)$

**Regression**: Predicting a numerical value. e.g. someone’s income, next year GDP, stock price

## Probability Overview

Probability theory provides a framework for reasoning about likelihood of events.

### Terminology

**Experiment**: procedure that yields one of a possible set of outcomes e.g. repeatedly tossing a die or coin

**Sample Space S**: set of possible outcomes of an experiment e.g. if tossing a die, $S = (1,2,3,4,5,6)$

**Event E**: set of outcomes of an experiment e.g. event that a roll is 5, or the event that sum of $2$ rolls is $7$

**Probability of an Outcome s or P(s)**: number that satisfies 2 properties

1. for each outcome $s, 0 ≤ P(s) ≤ 1$
2. $\sum_ {} p(s) = 1$

**Probability of Event E**: sum of the probabilities of the outcomes of the experiment: $p(E) = \sum_{s⊂E} p(s)$

**Random Variable V**: numerical function on the outcomes of a probability space

**Expected Value of Random Variable V**: $E(V) = p(E) = \sum_{s⊂E} p(s) \ast V(s)$

### Independence, Conditional, Compound

**Independent Events**: A and B are independent iff:

$P(A ∩ B) = P(A)P(B)$

$P(A|B) = P(A)$

$P(B|A) = P(B)$

**Conditional Probability**:

$P(A|B) = P(A,B)/P(B)$

**Bayes Theorem**:

$P(A|B) = P(B|A)P(A)/P(B)$

**Joint Probability**:

$P(A,B) = P(B|A)P(A)$

**Marginal Probability**:

$P(A)$

### Probability Distributions

**Probability Density Function (PDF)** Gives the probability that a rv takes on the value

$x: px(x) = P(X = x)$

**Cumulative Density Function (CDF)** Gives the probability that a random variable is less than or equal to

$x: Fx(x) = P(X ≤ x)$

*Note*: The PDF and the CDF of a given random variable contain exactly the same information.

## Descriptive Statistics

Provides a way of capturing a given data set or sample. There are two main types: **centrality** and **variability** measures.

### Centrality

**Arithmetic Mean** Useful to characterize symmetric distributions without outliers 

$µX = \frac{1}{n}\sum_{}x$

**Geometric Mean** Useful for averaging ratios. Always less than arithmetic

$mean = \sqrt[n]{a_1a_2...a_3}$

**Median** Exact middle value among a dataset. Useful for skewed distribution or data with outliers. 

**Mode** Most frequent element in a dataset.

### Variability

**Standard Deviation** Measures the squares differences between the individual elements and the mean

$σ = \sqrt{\frac{\sum_{i=1}^N (x_i - \bar x)^2}{N-1}}$

**Variance** $V = σ^2$

### Interpreting Variance

Variance is an inherent part of the universe. It is impossible to obtain the same results after repeated observations of the same event due to random noise/error. Variance can be explained away by attributing to sampling or measurement errors. Other times, the variance is due to the random fluctuations of the universe.

### Correlation Analysis

Correlation coefficients r(X,Y) is a statistic that measures the degree that Y is a function of X and vice versa. Correlation values range from -1 to 1, where 1 means fully correlated, -1 means negatively-correlated, and 0 means no correlation.

**Pearson Coefficient** Measures the degree of the relationship between linearly related variables 

$r = \frac{Cov(X,Y)}{σ(X)σ(Y)}$

**Spearman Rank Coefficient** Computed on ranks and depicts monotonic relationships

*Note*: Correlation does not imply causation!

<div align="right"><a href="./P_02_DSC.md">Next Page</a></div>
