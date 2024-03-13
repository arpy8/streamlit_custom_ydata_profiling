from pathlib import Path
from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="streamlit-custom-ydata-profiling",
    version="0.1.0",
    author="arpy8",
    description="Custom YData Profiling component for Streamlit.",
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    url="https://github.com/arpy8/streamlit_custom_ydata_profilingg",
    classifiers=[],
    license="MIT",
    license_file="LICENSE",
    python_requires=">=3.6",
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