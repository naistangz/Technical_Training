# What is CRUD?

Create, Read, Update and Delete
- Four basic functions that models should be able to do. 

Example of `JSON` object:

```json
"book": {
    "id":<Integer>
    "title":<String>
    "author":<String>,
    "isbn":<Integer
}
```

To make this library system usable, we want to make sure there are **clear** mechanisms for completing CRUD operations:

**`CREATE`** - Consists of a function we call when a new library book is added to the catalog. The program calling the function would supply the values for `"title"`, `"author"`, and `"isbn"`.
After this function is called, a new entry in the `books` corresponds to the new book. The new entry is also assigned a unique `id`, which can be used to access this resource later.

**`READ`** - Consists of a function we call to see all of the books currently in the catalog. The function does not alter the books in the catalog, it retrieves the resource and displays the results. The object is not be modified, only retrieved.

**`UPDATE`** - 