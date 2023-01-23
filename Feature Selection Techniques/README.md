
# Feature Selection Techniques

Feature Selection playes an important role in data science work flow. Where we pick the appropriate and important feature/column for a machine learning project.
Here, I described some techniques ...

## 1. Dropping Constant Features : [Open Code](https://github.com/Saksham093/Data-Science/blob/main/Feature%20Selection%20Techniques/Dropping%20Constant%20Features.ipynb)
Drop the `column/feature`, not applied for Target column. Constant features are of two types :
* Constand Features : Same value in all the records
* Quasi Constand Feature : One of the value is dominant 99.9% in column.

## Using

```python
# Install sklearn
sklearn.feature_selection.VarianceThreshold(threshold = 0.0)
```
```python
# Install fast_ml
fast_ml.feature_selection.get_constant_features()
```

---

## 🚀 About Me
Developer : [**`M.SAKSHAM`**](https://twitter.com/M_Saksham093)
