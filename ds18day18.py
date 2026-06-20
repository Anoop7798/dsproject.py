#subplots
import matplotlib.pyplot as plt
#first graph
year=[2010,2015,2020,2025]
diary=[100,520,630,400]


#second graph
year=[1990,2000,2005,2010]
farming=[300,200,250,100]


fig , aux =plt.subplots(1,2)
#this is first graph
aux[0].plot(year,diary)#1 col for line chart
aux[0].set_xlabel("year")
aux[0].set_ylabel("diary")
aux[0].set_title("diary production graph")

#this is second graph
aux[1].plot(year,farming)#2 col for line chart
aux[1].set_xlabel("year")
aux[1].set_ylabel("farming")
aux[1].set_title("farming production graph")
plt.show()


#subplots 2d
import matplotlib.pyplot as plt
#first graph
year=[2010,2015,2020,2025]
diary=[100,520,630,400]

#second graph
farming=[300,200,250,100]

#third graph
college=[10,20,25,30]

#fourth graph
transport=[50,75,100,150]

fig , aux =plt.subplots(2,2)
#this is first graph
aux[0,0].plot(year,diary)#1 col of 1 rowfor line chart
aux[0,0].set_xlabel("year")
aux[0,0].set_ylabel("diary")
aux[0,0].set_title("diary production graph")

#this is second graph
aux[0,1].scatter(year,farming)#2 col of 1 row for line chart
aux[0,1].set_xlabel("year")
aux[0,1].set_ylabel("farming")
aux[0,1].set_title("farming production graph")

#this is 3 graph
aux[1,0].bar(year,college)#1 col of 2 rowfor line chart
aux[1,0].set_xlabel("year")
aux[1,0].set_ylabel("college")
aux[1,0].set_title("college production graph")

#this is 4 graph
aux[1,1].pie(year,labels=transport)#2 col of 2 row for line chart
aux[1,1].set_xlabel("year")
aux[1,1].set_ylabel("transport")
aux[1,1].set_title("transport production graph")
plt.tight_layout()
plt.gcf().canvas.get_supported_filetypes()
plt.savefig("subplot.jpeg")
plt.show()