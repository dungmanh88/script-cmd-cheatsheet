https://shapeshed.com/jq-json/
https://medium.com/cameron-nokes/working-with-json-in-bash-using-jq-13d76d307c4
https://stackoverflow.com/questions/44656515/how-to-remove-double-quotes-in-jq-output-for-parsing-json-files-in-bash

http://api.icndb.com/jokes/random

# remove quote
jq -r

# Get each object in list
echo '[ {"id": 1}, {"id": 2} ]' | jq '.[]'
{
  "id": 1
}
{
  "id": 2
}

# Get each value (same key)
echo '[ {"id": 1}, {"id": 2} ]' | jq '.[].id'
1
2

# Working with object
only get keys
echo '{ "a": 1, "b": 2 }' | jq 'keys | .[]'
"a"
"b"
only get values
echo '{ "a": 1, "b": 2 }' | jq 'values | .[]'
1
2

# get length of list
echo '[1,2,3]' | jq 'length'
3

# Get values of each property, apply [] to an object
echo '{ "a": 1, "b": 2 }' | jq '.[]'
1
2

# Get an item in list
echo '["foo", "bar"]' | jq '.[1]'
"bar"

# Get a property
echo '{ "foo": 123, "bar": 456 }' | jq '.foo'
123

# Get all values in list
echo '[1,2,3]' | jq '.[]'
1
2
3
