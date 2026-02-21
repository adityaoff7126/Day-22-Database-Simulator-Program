
# Mini Database Simulator (Python)

## Overview
A simple command-line database simulator using a 2D list (list of lists).  
Each row represents a record, and each column represents a field.

---

## Features
- Create table (rows × columns)
- Insert value into a cell
- Edit existing value
- View full table
- Delete a row
- Search value by index
- Menu-driven interface

---

## Data Structure
```python
database = [
    [None, None, None],
    [None, None, None]
]
````

---

## Functions

### table()

Creates a new table with given rows and columns.

### insert_value()

Inserts value into a cell if empty.

### edit()

Updates a cell value.

### view()

Prints the database.

### remove()

Deletes a row by index.

### search()

Returns value from a specific cell.

### menu()

Controls the program using user input.

---

## How to Run

1. Run the script
2. Choose options from menu:

   * 1: Create Table
   * 2: Insert Value
   * 3: Edit Value
   * 4: View Table
   * 5: Delete Row
   * 6: Search Value
   * 7: Exit

---

## Limitations

* No data persistence (resets on exit)
* No column names
* No advanced search or filtering

---

## Future Improvements

* Add JSON/CSV storage
* Add column headers
* Add sorting and filtering
* Build SQL-like commands

```
```
