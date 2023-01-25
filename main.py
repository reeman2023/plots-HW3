import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv("crime_rate_Spain.csv")


# task1

specefic_crime = df1[["Year", "Total cases", "Crime"]].loc[df1["Crime"] == "Kidnapping"]
spe_crime_year = specefic_crime.groupby(["Year"])
y = spe_crime_year["Total cases"].sum()
x = y.index

fig, ax1 = plt.subplots()
ax1.set(xlabel='Years', ylabel='Total cases of Kidnapping ', title='The trend of kidnapping over time')
ax1.set_xticks(x)
ax1.plot(x, y, x, y, "or")


# task2

specefic_city = df1[["Location", "Total cases", "Crime"]].loc[df1["Location"] == "Barcelona"]
spe_city_crime = specefic_city.groupby(["Crime"])
crime_total_cases = spe_city_crime["Total cases"].sum()
label = crime_total_cases.index

fig, ax2 = plt.subplots()


ax2.pie(crime_total_cases, radius=1, rotatelabels= True, startangle=90,
        wedgeprops=dict(width = 1,edgecolor='white'), autopct='%1.0f%%')

plt.legend(label,loc='center left',bbox_to_anchor=(1, 0.5),fontsize=12)
ax2.set_title("Distribution of crimes in Barcelona")

#plt.show()

# task3

crimes_cities = df1[["Location", "Total cases", "Crime"]]
crimes_cities1 = crimes_cities[(crimes_cities["Crime"]=="Kidnapping")&((crimes_cities["Location"]=="Spain")
                        |(crimes_cities["Location"]=="Barcelona")|(crimes_cities["Location"]=="Madrid")
                        |(crimes_cities["Location"]=="Valencia")|(crimes_cities["Location"]=="Murcia"))

                        |(crimes_cities["Crime"]=="Theft")&((crimes_cities["Location"]=="Spain")
                        |(crimes_cities["Location"]=="Barcelona")|(crimes_cities["Location"]=="Madrid")
                        |(crimes_cities["Location"]=="Valencia")|(crimes_cities["Location"]=="Murcia"))

                        | (crimes_cities["Crime"]=="Robberies with force in homes")&
                        ((crimes_cities["Location"]=="Spain")|(crimes_cities["Location"]=="Barcelona")
                         |(crimes_cities["Location"]=="Madrid")|(crimes_cities["Location"]=="Valencia")
                         |(crimes_cities["Location"]=="Murcia"))]

crimes_cities12 = crimes_cities1.groupby(["Crime","Location"])
y3 = crimes_cities12["Total cases"].agg(["sum"]).reset_index()

y3.pivot( index="Crime", columns="Location", values="sum").plot(kind="bar")
plt.title("number of crimes in a few cities")


plt.show()






