# show menu
# list all
# search
# add/remove/edit entries
# record:
# - firstname, lastname
# - location
# - email
# - mobilephone
# https://www.shellscript.sh/exercises.html
#!/bin/bash

key_code=0

function show_menu()
{
  echo -e "\n"
  echo "*** Contact Management CLI ***"
  echo "1. Add a new contact (a)"
  echo "2. Search a contact (s)"
  echo "3. List all contacts (l)"
  echo "4. Delete a contact (d)"
  echo "5. Edit a contact (e)"
  read -n1 -p "Enter a shortcut key (a/s/l/d/e) " key_code
  echo -e "\n"
}

function list()
{
  echo "list function"
  total=`wc -l db.csv | awk '{print $1}'`
  echo "Total record = $total"
  i=0
  while IFS=":" read -r fname lname email location phone
  do
    (( i=i+1 ))
    echo "******* $i"
    echo "Firsname: $fname"
    echo "Lastname: $lname"
    echo "Email: $email"
    echo "Location: $location"
    echo "Mobile Phone: $phone"
  done < db.csv
}

function analyze_record()
{
  IFS=":" read -r fname lname email location phone <<< "$1"
  echo "Analyzing..."
  echo "Firsname: $fname"
  echo "Lastname: $lname"
  echo "Email: $email"
  echo "Location: $location"
  echo "Mobile Phone: $phone"
}

function search_by_field()
{
  keyword=$1
  case $2 in
    fname) field=1
    ;;
    lname) field=2
    ;;
    email) field=3
    ;;
    location) field=4
    ;;
    phone) field=5
    ;;
    *) field=0
    ;;
  esac
  if [ ! $field -eq 0 ]; then
    grep -F "$keyword" db.csv | while read -r line; do
        echo $line
        if [ "$(echo $line | cut -d ":" -f$field)" = $keyword ]; then
          echo "analyze_record: $line"
          analyze_record "$line"
        fi
    done
  else
    grep -F "$keyword" db.csv | while read -r line; do
          echo "analyze_record: $line"
          analyze_record "$line"
    done
  fi
}

function search()
{
  echo "search function"
  read -p "Enter search keyword " keyword
  read -p "Search by field: (fname|lname|email|location|phone|all) " field
  search_by_field "$keyword" "$field"
  read -p  "Do you want search more (y/n) " more
  case $more in
    [yY]) search
    ;;
    [nN]) main
    ;;
    *) search
  esac
}

function add()
{
  echo "add function"
  read -p "Enter first name: " firstname
  read -p "Enter last name: " lastname
  read -p "Enter email: " email
  read -p "Enter location: " location
  read -p "Enter mobilephone " mobilephone
  echo "$lastname:$firstname:$email:$location:$mobilephone" >> db.csv
  read -p  "Do you want add more (y/n) " more
  case $more in
    [yY]) add
    ;;
    [nN]) main
    ;;
    *) add
  esac
}

function delete()
{
  echo "delete function"
}

function edit()
{
  echo "edit function"
}

function main()
{
  while :
  do
    show_menu
    echo "key_code = $key_code"
    [ "$key_code" = "a" ] && add
    [ "$key_code" = "s" ] && search
    [ "$key_code" = "l" ] && list
    [ "$key_code" = "d" ] && delete
    [ "$key_code" = "e" ] && edit
  done
}

main
