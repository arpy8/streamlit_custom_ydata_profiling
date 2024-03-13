# 📈 Streamlit Custom YData-Profiling

[![GitHub][github_badge]][github_link] [![PyPI][pypi_badge]][pypi_link] 

## Installation

```sh
pip install streamlit-custom-ydata-profiling
```

## Getting started

```python
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport

from streamlit_custom_ydata_profiling import st_profile_report

df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = ProfileReport(df)

st_profile_report(pr)
```

[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
[github_link]: https://github.com/arpy8/streamlit_custom_ydata_profiling

[pypi_badge]: https://badgen.net/pypi/v/streamlit_custom_ydata_profiling?icon=pypi&color=black&label
[pypi_link]: https://pypi.org/project/streamlit-custom-ydata-profiling
