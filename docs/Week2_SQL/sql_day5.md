## Week 2.5 Formatting Date and Time, Subqueries

### Section 1 Formatting Date and Time 

**Using `FORMAT` function**

```sql
SELECT 
FORMAT(o.ShippedDate, 'MMM-yy') AS "Shipping Month"
FROM Orders;
```

Query returns Shipped Date in String Format i.e 06-20 -> JUN-20

Common date and time formatting: 

- `dd` - this is day of month from 01-31
- `dddd` - this is the day spelled out
- `MM` - this is the month number from 01-12
- `MMM` - month name abbreviated
- `MMMM` - this is the month spelled out
- `yy` - this is the year with two digits
- `yyyy` - this is the year with four digits
- `hh` - this is the hour from 01-12
- `HH` - this is the hour from 00-23
- `mm` - this is the minute from 00-59
- `ss` - this is the second from 00-59
- `tt` - this shows either AM or PM
- `d` - this is day of month from 1-31 (if this is used on its own it will display the entire date)
- `us` - this shows the date using the US culture which is MM/DD/YYYY

### Section 2 Subqueries

The following subquery would be more efficient if it was changed to a `JOIN` as there are **no aggregate** functions in the queries

Compare this query:

```sql
SELECT payment FROM salary WHERE rank =
 (SELECT rank FROM ranks WHERE title =
 (SELECT title FROM jobs 
   WHERE employee = 'Andrew Cumming'))
```

With this query:

```sql
SELECT p.payment 
  FROM salary s JOIN ranks r
    ON (s.rank = r.rank)
  JOIN jobs j ON (r.title = j.title)
  WHERE j.employee = 'Andrew Cumming'
```


> Week 2 Day 5 (26-06-2020) SQL exercise: *Subqueries, Formatting Date and Time* [HERE](day5_exercise.sql)
