# st_ydata_profiling
This is a slightly tweaked version of the `streamlit-pandas-profiling` component but with the latest dependencies. I've created this for my another ongoing project whose dependencies kept on clashing with the `streamlit-pandas-profiling` by okld.


[![GitHub][github_badge]][github_link] [![PyPI][pypi_badge]][pypi_link] 

## Installation

```sh
pip install st_ydata_profiling
```

## Getting started

```python
import pandas as pd
from st_ydata_profiling import display_profile_report
import streamlit as st

from streamlit_pandas_profiling import st_profile_report

df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
display_profile_report(df)
```

[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
[github_link]: https://github.com/arpy8/st_ydata_profiling

[pypi_badge]: https://badgen.net/pypi/v/st_ydata_profiling?icon=pypi&color=black&label
[pypi_link]: https://pypi.org/project/st_ydata_profiling