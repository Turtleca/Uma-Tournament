# Designing an Uma Json.

# Veteran Uma JSON

Veteran data is imported from the `veterans.json` array written by
[horseACT](https://github.com/ayaliz/horseACT).

```python
from uma_tournament import UmaCollection

collection = UmaCollection("veterans.json")
```

The loader uses horseACT field names directly and supports its camelCase,
snake_case, and normalized race-cache aliases. Do not add manually designed
example entries to this directory.
