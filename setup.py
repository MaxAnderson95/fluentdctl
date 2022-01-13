from importlib.metadata import entry_points
from setuptools import setup, find_packages

VERSION = '0.0.4'
DESCRIPTION = 'A CLI for Fluentd API'


def long_description():
    with open('README.md', encoding='utf-8') as f:
        return f.read()


# Setting up
setup(
    name="fluentdctl",
    version=VERSION,
    author="Max Anderson",
    author_email="<cctpmax@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description(),
    packages=find_packages(),
    install_requires=['fire', 'requests'],
    keywords=['fluentd', 'cli'],
    entry_points={
        'console_scripts': [
            'fluentdctl = fluentdctl.fluentdctl:main'
        ]
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    project_urls={
        'GitHub': 'https://github.com/MaxAnderson95/fluentdctl'
    }
)
