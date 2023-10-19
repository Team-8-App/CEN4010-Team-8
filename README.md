An API Service to support an online web application bookstore that targets a particular niche in
technology. The application, named Geek Text will need to support the following features:

Each API Action has its own separate API route. The REST API service has following components:
- RESTful API: An API service that is exposed to the front using HTTPS exposing functional endpoints.
- Backend Database: A Database of your choice to store the data which can only be accessed by the API.

# GitHub Integrations
AWS Connector for Github and AWS Amplify

# Languages and Frameworks
- Languages: Python, Javascript
- Database: MySQL
- Frameworks: Flask and Django 
- Other Apps: AWS Amplify, AWS Cognito, AWS Lambda, and Amazon API Gateway

# Installations and Setup
Open terminal and type in the command:
```console
pip3 install aws-shell
```
```console
aws configure
```
It will then ask for the AWS Access Key, and the AWS Secret Access Key.

Then connected the AWSConnector to the Github Repository.

The following information is found in Amplify Studio under REST API:
- Install Amplify CLI with terminal command: 
```console
curl -sL https://aws-amplify.github.io/amplify-cli/install | bash && $SHELL
```
- Pulled Amplify project with terminal command: 
```console
amplify pull --appId <app id> --envName staging
```
- Added rest capabilities and can create backend api with terminal command: 
```console
amplify add api
```
After this command, it will give you some of the following options while setting up your backend environment:
- Chose REST and labeled the category "api".
- Provide a path: /items
- Provide an AWS Lambda function name: apilambda
- Choose the runtime: Python

Name and create environment with awscloudformation using the following terminal command:
```console
amplify init
```

BELOW ARE OTHER IMPORTANT COMMANDS:
- Shows what you've already added and deployed:
```console
amplify status
```
- Allows you to add features like user login and backend API:
```console
amplify add <category>
```
- Builds all local backend resources and provisions it in the cloud:
```console
amplify push
```
```console
amplify publish
```
- Open Amplify Console and view project status:
```console
amplify console
```




