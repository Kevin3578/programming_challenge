**Part 1**

To run `count_schools.py`, you can either run the script directly or import `schoolDataParser` from `count_schools.py`

Creating an instance of `schoolDataParser` requires one argument, the location of the `school_data.csv` you want to parse.

For example, `parser = schoolDataParser('school_data.csv')`

All the metrics are printed by one method that takes no arguments, `print_counts()`

For example, `parser.print_counts()`


**Part 2**

To run `school_search.py`, you can either run the script directly or import `schoolDataParser` from `school_search.py`

You can also edit the script under the line `if __name__ == "__main__":` to change the search queries.

Creating an instance of `schoolDataParser` requires one argument, the location of the `school_data.csv` you want to parse.

For example, `parser = schoolDataParser('school_data.csv')`

To run a search query, use the method `search_schools()` and pass in your query.

For example, `parser.search_schools("elementary school highland park")`

Part 2 searching uses set intersections to determine the best match. The school name, city, and state are placed into 1 set after being split on spaces. 
Likewise, the search query is placed into another set after being split on spaces. The schools that have the highest number of common elements are likely to be a correct match.
The string "school" is also removed from the user query if it's included for better matching.