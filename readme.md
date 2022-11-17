# eHealth Corp 

## Description

## Authors

- Vicente Barros **97787**
- Daniel Ferreira **102442**
- Guilherme Antunes **103600**
- Mariana Andrade **103823**

## Vulnerability 
 
 - **CWE - 89** - Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
 - **CWE - 79** - Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
 - **CWE - 352** - Cross-Site Request Forgery (CSRF)
 - **CWE - 488** - Exposure of Data Element to Wrong Session
 - **CWE - 798** - Use of Hard-coded Credentials
 - **CWE - 620** - Unverified Password Change
 - **CWE - 521** - Weak Password Requirements
 - **CWE - 522** - Insufficiently Protected Credentials
 - **CWE - 434** - Unrestricted Upload of File with Dangerous Type

## Execute

### Docker

To run in docker you need just have to run the following command inside the version you want to run and execute
```bash
docker-compose up
```
The insecure version will be running on port 8000 and the secure version will be running on port 8080 you may cahnfe the port in the docker-compose.yml file
### Local
To run locally you must use the **run.sh** with the params -a and -p to specify the version and port you want to run the application.

Example:
```bash
./run.sh -a app -p 8080

```
**IMPORTANT**
When you start the application for the first time you must run the following urls to populate the database

    /generate/admin
    /generate/users
    /appointments
    /reports
