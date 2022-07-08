# RESTful API For Automobile Company

## Getting Started

* Instructions to set up the project:

```sh
clone the project
docker-compose up
docker-compose run autocompany python manage.py migrate

```

To migrate database if docker container is already running, execute following command.

```sh
 docker-compose exec autocompany python manage.py migrate
```

* Execute unit testing

SQLite database is used for unit testing and run below command to execute unit cases

```sh
python manage.py makemigrations --settings=autocompany.settings_local
python manage.py migrate --settings=autocompany.settings_local
python manage.py test --settings=autocompany.settings_local
```

## Notes

While doing the development, following assumptions were made

1. Users do not need to register an account to order items. To identify each user session is used based on the device.
2. Shopping cart items for a user is retrieved with cart id which is created when user session is given
