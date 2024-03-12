from pathlib import Path
from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name="st_ydata_profiling",
    version="0.1.0",
    description="YData Profiling component for Streamlit.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arpy8/st-ydata-profiling",
    author="arpy8",
    license="MIT",
    license_file="LICENSE",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=[
        "ydata-profiling>=4.0.0",
        "streamlit >= 0.63",
    ],
    extras_require={
        "devel": [
            "wheel",
            "pytest==7.4.0",
            "playwright==1.39.0",
            "requests==2.31.0",
            "pytest-playwright-snapshot==1.0",
            "pytest-rerunfailures==12.0",
        ]
    }
)