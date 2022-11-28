import setuptools

# Get all modules.
PACKAGES = setuptools.find_packages()

# Include configuration files.
PACKAGE_DATA = {"markov_decision_processes.config": ["*.yaml"]}

# Parse requirements.
with open("requirements.txt") as f:
    INSTALL_REQUIRES = [line.strip() for line in f.readlines()]

setuptools.setup(
    name="markov_decision_processes",
    version="2022.11.27",
    author="Jack Bruck",
    packages=PACKAGES,
    package_data=PACKAGE_DATA,
    install_requires=INSTALL_REQUIRES,
)