import pandas as pd
import sqlite3 as sql
import matplotlib.pyplot as plt


#passed/failed analytics
def grade():
    conn = sql.connect('database.db')
    passed = 0
    failed = 0
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * FROM studentInfo")

    for record in cursor:
        if record[8] >= 75:
            passed += 1
        else:
            failed +=1

    data = [passed,failed]
    pieLabels = ["Passed","Failed"]
    gradeColors = ["#34A1C7","#34C7A3"]

    plt.title("Grade Analytics")
    plt.pie(data,labels=pieLabels,colors=gradeColors,startangle=90,autopct='%1.2f%%')
    plt.show()


#year analytics
def year():
    conn = sql.connect('database.db')
    yr1=0
    yr2=0
    yr3=0
    yr4=0
    yr5=0
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * FROM studentInfo")

    for record in cursor:
        if record[4] == 1:
            yr1 += 1
        elif record[4] == 2:
            yr2 +=1
        elif record[4] == 3:
            yr3 +=1
        elif record[4] == 4:
            yr4 +=1
        elif record[4] == 5:
            yr5 +=1

    x = ["First Year", "Second Year", "Third Year", "Fourth Year", "Fifth Year"]
    y = [yr1,yr2,yr3,yr4,yr5]
    
    plt.title("Year Analytics")
    plt.xlabel("Year Level")
    plt.ylabel("Number of Students")
    plt.bar(x,y)
    plt.show()

#age analytics
def age():
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * FROM studentInfo")

    age19=0
    age20=0
    age21=0
    age22=0
    age23=0
    age24=0
    age25=0

    for record in cursor:
        if record[3] == 19:
            age19 += 1
        elif record[3] == 20:
            age20 +=1
        elif record[3] == 21:
            age21 +=1
        elif record[3] == 22:
            age22 +=1
        elif record[3] == 23:
            age23 +=1
        elif record[3] == 24:
            age24 +=1
        elif record[3] == 25:
            age25 +=1
        

    ageLabels = ["19", "20", "21", "22", "23","24","25"]
    data = [age19,age20,age21,age22,age23,age24,age25]
    ageColors = ["#FADCC8","#F6BB93","#FBA490","#FB8985","#FC666F","#B83253","#651B40"]

    plt.title("Age Analytics")
    plt.pie(data,labels=ageLabels,colors=ageColors,startangle=90,autopct='%1.2f%%')
    plt.show()
