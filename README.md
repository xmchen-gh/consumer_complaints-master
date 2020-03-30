##  Approach

* The code is in a single file "consumer_complaints.py"
* "consumer_complaints.py" includes two functions: **`structCSV`** and **`sortCSV`**
* **`structCSV`** takes oniginal CSV input file and build a structure using dictionary in the format <font color="green"> {product:{year:{company:occurrence}}} </font>. It returns this structure.
* **`sortCSV`** calculates total number of complaints <font color="green"> *TotNumCpt* </font>, total number of companies <font color="green"> *TotNumCpn* </font>, highest percentage <font color="green"> *MaxPercnt* </font> as it sorts dictionary for product name and year. At the same time, in the most inner loop, it writes output line by line to the output file.


* When unexpected data written in CSV file, **`structCSV`** prints in command line, the row number of the CSV file as well as the error

## Misc

* The code was written in Python 3.6 enviornment. It runs with Python3. 