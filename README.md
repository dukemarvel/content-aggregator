# Content Aggregator

A simple RSS aggregator built with Python.

## Installation

This project requires Python 3.8 or higher and Pipenv. To set up your development environment:

1. Clone the repository: `git clone https://github.com/dukemarvel/content-aggregator`
2. Navigate to the project directory: `cd content-aggregator`
3. Install the required packages and create the virtual environment: `pipenv install`

## Usage

To run the aggregator, first activate the virtual environment with `pipenv shell`. Then, to limit to 5 entries per feed, use the following command:

python cli.py --limit 5
