import setuptools

setuptools.setup(
    name="streamlit-custom-ydata-profiling",
    version="0.1.0",
    author="arpy8",
    packages=setuptools.find_packages(),
    include_package_data=True,
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