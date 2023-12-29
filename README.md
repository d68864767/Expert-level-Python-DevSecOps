# Expert-level Python DevSecOps

This project is an example of a Python application using Flask and is designed to demonstrate DevSecOps principles. The application is a simple web server that returns a greeting message.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7
- Docker
- Jenkins

### Installing

A step by step series of examples that tell you how to get a development environment running.

1. Clone the repository
```
git clone <repository_url>
```
2. Install the required packages
```
pip install -r requirements.txt
```
3. Run the application
```
python main.py
```
The application will be accessible at `http://localhost:5000`.

## Running the tests

The tests for this project are written in Python's unittest framework. To run the tests, use the following command:
```
python -m unittest test_main.py
```

## Deployment

This application is containerized using Docker. To build and run the Docker container, use the following commands:

1. Build the Docker image
```
docker build -t python-devsecops .
```
2. Run the Docker container
```
docker run -p 5000:5000 python-devsecops
```
The application will be accessible at `http://localhost:5000`.

## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [pytest](https://docs.pytest.org/en/latest/) - The testing framework used

## Authors

* **Your Name** - *Initial work* - [YourGithubUsername](https://github.com/YourGithubUsername)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
