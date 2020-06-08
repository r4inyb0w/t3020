
# T3020   Repo for ELEN3020

Name: Samantha Thurgood
Date: 8 June


# Description of code -- for question 1.1 and 1.2

The program `datamunger.py` is used to quality check data files. A
sample data file is given. The first row consists of headings which
the program ignores. The quality checks are

* The column TALL should be the sum of T1 through T8 inclusive
* For each of columns TALL and T1 through T7 inclusive (not T8),  the values increase monotonically. For example if in row 13, column T3 there's a value 49 (for example), then in row 14, column T3 the value should be 49 or greater.

Note, however, there is some missing data in some of the rows. The first few lines only contain values for TALL and only the latter half has values for OTHER.  If there are missing data for any row in columns TALL and T1 through T8 then that row should not be checked. However, we keep track of how many rows there are with missing data


### Errors

There are three deliberate errors, marked E1, E2 and E3. Finding other (non-deliberate and unknown to me)  errors will get a bonus -- clearly add below this line in your copy of the README what the errors are and how you fixed them.

E1: the range was initially 2:9, this left out the T1 column. I changed it to 1:9 to ensure it would calculate the total total correctly.

E2: this condition said <=, however for increasing monotonically the current number can be equal to the previous number, therefore I removed the = so the condition just read: curr[i] <  prev[i]

    Additionally, on line 28, the range was 9, I changed this value to 8 since the T8 column does not need to increase monotonically.

E3: I added [0:9] so that the OTHER column would not be checked if empty since missing data is only checked for columns TALL and T1-T8.