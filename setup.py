from setuptools import setup, find_packages
setup(
    name="OSMTranslationScrapper",
    version="0.1",
    packages=find_packages(),
    install_requires=['beautifulsoup4', 'requests']
)
