# streamlit_custom_ydata_profiling
This is a slightly tweaked version of the `streamlit-pandas-profiling` component but with the latest dependencies. I've created this for my another ongoing project whose dependencies kept on clashing with the [streamlit-pandas-profiling](https://github.com/arpy8/streamlit_custom_ydata_profiling) package by [okld](https://github.com/okld).


[![GitHub][github_badge]][github_link] [![PyPI][pypi_badge]][pypi_link] 

## Installation

```sh
pip install streamlit_custom_ydata_profiling
```

## Getting started

```python
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_custom_ydata_profiling import display_profile_report

df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
report = ProfileReport(df)
display_profile_report(report)
```

[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
[github_link]: https://github.com/arpy8/streamlit_custom_ydata_profiling

[pypi_badge]: https://badgen.net/pypi/v/streamlit_custom_ydata_profiling?icon=pypi&color=black&label
[pypi_link]: https://pypi.org/project/streamlit_custom_ydata_profiling