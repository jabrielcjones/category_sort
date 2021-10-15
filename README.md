# Category Sort

We're going to insert categories from a source database to a destination database.

There are parent categories and child categories.

The destination database has a rule that the source database does not have:

* a child category cannot be inserted before its parent category has been inserted

We need to sort the source categories before we insert them to avoid an error.


Category Lists

* Source: product database (flat database)
* Destination: storefront database (hierarchy-constrained flat database)

Each category has:

* category name
* one parent category
* zero or more children categories

Category Info in Database

* category ID
* parent category ID
* category name

Write a function that can:

* take a JSON string of categories from product DB
* sort the categories in the "optimal insertion" order for the storefront DB so no category is inserted before its parent
* return a JSON string of ordered categories for the storefront DB

Sample Input

```json
[
  {
    "name": "Accessories",
    "id": 1,
    "parent_id": 20,
  },
  {
    "name": "Watches",
    "id": 57,
    "parent_id": 1
  },
  {
    "name": "Men",
    "id": 20,
    "parent_id": null
  }
]
```

Sample Output

```json
[
  {
    "name": "Men",
    "id": 20,
    "parent_id": null
  },
  {
    "name": "Accessories",
    "id": 1,
    "parent_id": 20
  },
  {
    "name": "Watches",
    "id": 57,
    "parent_id": 1
  }
]
```
