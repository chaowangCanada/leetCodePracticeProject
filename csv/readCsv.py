import io
import csv
from datetime import datetime

# Do not edit the StringIO object below
f = io.StringIO(
    """
# FileType: employee-salary
# Columns: employee_id,employee_name,job_title,salary,job_start_date,job_end_date
# Types: int,str,str,int,datetime,datetime
1 ,Alan,Chef,40000,2018-10-29,,
2 ,Brenda,Teacher,30000,,2018-01-13,
3 ,Charlie,CEO,1000000,2015-09-27,,
4 ,Declan,Head of Sales,200000,2018-05-28,,
5 ,Erin, Taxi Driver, 35000,2018-09-21,,
6 ,Frank,Taxi Driver, 35000,016-08-03,,
7 ,Gertrude,Head Chef,45000,2013-12-11,2016-11-29
8 ,Harry,,60000,2012-09-14,2013-09-17
9 ,Isabella,Police Officer,33000,2014-03-21,2014-09-24
10,John,Data Scientist,45000,2015-07-15,2019-04-28
11,Kerry,Shop Keeper, 22000,2017-04-03,,
12,Liam,Chef,40000,2012-06-13,2015-02-18
13,Mandy,Gardener,80000,2018-01-26,,
14,Nigel,Teacher,30000,2015-01-01,,
15,Ophelia,Clergy,55000,2015-04-04,2019-01-24
16,Peter,Chef,40000,2020-01-03,,
17,Quinn,Unemployed,0,2016-02-25,2019-07-04
18,Roger,Martial Arts Teacher,27500,2016-05-03,2018-09-17
19,Samantha,Teacher,,2015-06-29,,
20,Terry,Audio Engineer, 77000,2015-05-01,2015-08-02
21,, Pet Control,42000,2012-09-16,2014-11-06
22,Vanessa,Sous Chef,42000,2018-02-02,,
23,Willhelm,Business Owner,10000,2012-04-12,2014-06-25
24,Xavier,Teacher,30000,2018-02-07,2018-05-26
25,Yolanda,Taxi Driver, 35000,2017-12-17,2018-12-09
26,Zell,Chef,40000,2012-06-29,2013-04-02
14,Nigel,Teacher,30000,2015-01-01,,
15,Ophelia,Clergy,55000,2015-04-04,2019-01-24
16,Peter,Chef,40000,2020-01-03,,
25,Yolanda,Taxi Driver, 35000,2017-12-17,2018-12-09
26,Zell,Chef,40000,2012-06-29,2013-04-02
"""
)


def main():
    reader = csv.reader(f, delimiter=',')
    next(reader, None)
    next(reader, None)
    headers = next(reader, None)
    columns = {}
    for header in headers:
        columns[header] = []
    next(reader, None)
    for row in reader:
        for i in range(0, len(headers)):
            columns[headers[i]].append(row[i])
    count = sum(i != '' and int(i) > 30000 for i in columns['salary'])
    print(f"greater than 30000 count is {count}")
    print(columns['job_start_date'])

    oldest = datetime.now()
    oldest_i = -1
    for i in range(0, len(columns['job_start_date'])):
        try:
            aTime = datetime.strptime(columns['job_start_date'][i], '%Y-%m-%d')
            if (aTime < oldest):
                oldest = aTime
                oldest_i = i
        except Exception:
            pass

    print(columns["employee_name"][oldest_i] + " holds the oldest record")

    salary = [int(i) if i != '' else 0 for i in columns['salary']]
    highest_index = 0 if salary[0] > salary[1] else 1
    second_highest_index = 1 if highest_index == 0 else 0
    for i in range(2, len(salary)):
        if salary[i] > salary[highest_index]:
            second_highest_index = highest_index
            highest_index = i
        elif salary[i] > salary[second_highest_index] and salary[i] != salary[highest_index]:
            second_highest_index = i
    print("second highest salary man is " + columns["employee_name"][second_highest_index])


if __name__ == "__main__":
    main()