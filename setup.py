from setuptools import setup, find_packages

setup(
    name="weathercli",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests",
        "python-dotenv"
    ],
    entry_points={
        'console_scripts': [
            'weathercli = src.cli:main',
        ],
    },
    include_package_data=True,
    author="",
    description="WeatherCLI is a futuristic command-line tool to check real-time weather information stylishly.",
    license="MIT",
)
