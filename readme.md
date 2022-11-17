# eHaltth Corp 

## Description

## Authors

- Vicente Barros (NMec: 97787)
- Daniel Ferreira (NMec: 102442)
- Guilherme Antunes (NMec:103600)
- Mariana Andrade (NMec: 103823)

## Vulnerability 
 
 - **Sql Injection**
 - 


## Execute
To execute locally you need to have Docker Compose installed and updated.

After making sure of it, follow the steps below:
1. In the root folder of the app or app_sec, run the following command:
```
    $ docker-compose up
```

2. Open your browser and go to the following address:
```
    http://localhost:5000
```

3. In browser, you nead to generate a database with the following command:
```
    http://localhost:5000/generate/admin
    http://localhost:5000/generate/users
    http://localhost:5000/generate/appointments
    http://localhost:5000/generate/reports
```