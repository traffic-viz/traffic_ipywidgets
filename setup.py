from setuptools import find_packages, setup


setup(
    name="traffic_ipywidgets",
    packages=find_packages(),
    entry_points={
        "traffic.plugins": ["TrafficWidget = traffic_ipywidgets.ipywidgets"]
    },
    install_requires=[
        "ipympl",  # interactive matplotlib in notebooks
        "tornado",  # dependency for matplotlib with WebAgg
    ],
)
