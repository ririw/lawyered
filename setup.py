from setuptools import setup

setup(
    name="lawyered",
    version="1.0",
    description="An experiment in textual lie detection",
    packages=['lawyered'],
    install_requires=[
        "numpy",
        "scipy",
        "nltk",
        "pyprind==2.9.2",
        "sklearn"
    ],
    build_requires = ['numpy'],
    include_package_data=True,
)
