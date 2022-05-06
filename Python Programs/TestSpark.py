
a= [1,2,3,[4,5],6,7]
b=sc.parallelize(a)
c=b.flatmap(lambda x=>x)
c.collect

customer id , transaction date,
1,2/04/2022
2,3/04/2022
4,4/04/2022
5,5/04/2022
1,3/04/2022
2,4/04/2022
4,5/04/2022
5,6/04/2022

customer,How many days before he has done trasanction

df =spark.read.csv("test.csv").option()
df1=df.groupby($"customerId").max($"date")dateformat("ddMMyyyy")).as(MaxDate)
todaysDate=Date()


df1.withColumn("Last Transaction",date_diff($"todaysDate",$"MaxDate"))