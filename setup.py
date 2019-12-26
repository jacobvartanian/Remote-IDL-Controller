from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="IDL_Controller", 
    version="00.00.001",
    author="Jacob Vartanian",
    author_email="jacob.vartanian@uts.edu.au",
    description="Python remote controller for UTS IOT Data Logger (IDL)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={'': 'idl_controller'},
    packages=find_packages(where='idl_controller'),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.5',
    install_requires=[
        'blynkapi'
    ]
)
