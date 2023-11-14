An API Service to support an online web application bookstore that targets a particular niche in
technology. The application, named Geek Text will need to support the following features:

Each API Action has its own separate API route. The REST API service has following components:
- RESTful API: An API service that is exposed to the front using HTTPS exposing functional endpoints.
- Backend Database: A Database of your choice to store the data which can only be accessed by the API.

# GitHub Integrations
AWS Connector for Github

# Languages and Frameworks
- Languages: Python
- Database: MySQL
- Frameworks: Flask and Docker
- Other Apps: AWS Lightsail

# Installations and Setup
Install Docker, AWS Command Line Interface (CLI), and the Lightsail control plugin.

- Install Docker Desktop: https://www.docker.com/products/docker-desktop/

- Install AWS Command Line Interface (CLI) with the following terminal command
```console
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
```
or got to Command Line - All Installers: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

- Install the Lightsail control plugin: https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-install-software.html

- Open Github Project on PyCharm or Code Studio and in the same directory as the docker file, type in this command in the IDE terminal:
```console
docker build -t flask-container .
```
- Then test your container by using the following command:
```console



