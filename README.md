# tucan-docker

Notifies you via email when there are new grades available in
the campus management system of Technische Universität Darmstadt.

## Installation
```
docker build -t tucan-docker .
```

## Run
```
docker run -e USERNAME="musterman123" -e PASSWORD="secret1337" -e MAIL="mail@example.com" -v /path/to/host_db:/db tucan-docker:latest
```
The mount is used to specify a directory where the database is persistently store. If no volume is mounted the application is not able to restore already retrieved grades