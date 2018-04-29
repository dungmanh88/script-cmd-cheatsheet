#!/bin/bash
project=$1
composer create-project --prefer-dist laravel/laravel ${project}
cd ${project}
php artisan key:generate
