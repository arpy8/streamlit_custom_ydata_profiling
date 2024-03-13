from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="streamlit-custom-ydata-profiling",
    version="0.1.1",
    author="Arpit Sengar (arpy8)",
    author_email="arpitsengar99@gmail.com",
    description="Custom YData Profiling component for Streamlit.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arpy8/streamlit_custom_ydata_profiling",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
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
