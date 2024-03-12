# st-ydata-profiling
This is a slightly tweaked version of the `streamlit-pandas-profiling` component but with the latest dependencies. I've created this for my another ongoing project whose dependencies kept on clashing with the `streamlit-pandas-profiling` by okld.


[![GitHub][github_badge]][github_link] [![PyPI][pypi_badge]][pypi_link] 

## Installation

```sh
pip install st-ydata-profiling
```

## Getting started

```python
import pandas as pd
import st_ydata_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report

df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
st_ydata_profiling(df)
```

[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
[github_link]: https://github.com/arpy8/st-ydata-profiling

[pypi_badge]: https://badgen.net/pypi/v/st-ydata-profiling?icon=pypi&color=black&label
[pypi_link]: https://pypi.org/project/st-ydata-profiling