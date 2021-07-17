# Hashtables

Hashtables are a data structure that utilize key value pairs. This means every Node or Bucket has both a key, and a value.

The basic idea of a hashtable is the ability to store the key into this data structure, and quickly retrieve the value. This is done through what we call a hash. A hash is the ability to encode the key that will eventually map to a specific location in the data structure that we can look at directly to retrieve the value.

Since we are able to hash our key and determine the exact location where our value is stored, we can do a lookup in an O(1) time complexity. This is ideal when quick lookups are required.

## Challenge

Implement a Hashtable Class with the following methods: add, get, contains and hash

## Approach & Efficiency

the approach taken in this code challenge is simply be creating a Hashtable class, with the init function to take the size parameter, in order to create proper buckets for the keys/values to be stored. then we have the add contains method, that checks if the key is inside the Hashtable, the add method is for adding value to the Hashtable, get method is for retrieving the value for a key when inserted, and returns a None if the key does not exist, and the final method is hash, which simply hashes the key, and return the index of where should this key/value pair should be saved at.

> Big O

Time complexity: O(1), it provides a constant and instantaneous results, because we know exactly the index of where to look

Space complexity: O(n), we are creating an array with a size of n, in order to store the key/value pairs

## API

the methods that are used are listed below:

* add: This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

* get: Returns a value associated with that key in the table if exist

* contains: Returns a boolean, indicating if the key exists in the table already.

* hash: Returns the Index in the collection for that key