import os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
os.chdir('/Users/Luis/Desktop')
file=open('region.txt')
data=[]
for line in file:
    data.append(line.rstrip())

locations=[]
for item in data:
    item=item.split('\t')
    locations.append((float(item[1])+float(item[2]))/2)

ccwt=[]
for item in data:
    item=item.split('\t')
    ccwt.append((float(item[-1])))

plt.xlim(max(locations),min(locations))
cc762=[]
for item in data:
    item=item.split('\t')
    cc762.append((float(item[-2])))

chipwt=[]
chip700=[]
for item in data:
    item=item.split('\t')
    chipwt.append((float(item[-3])))

	
for item in data:
    item=item.split('\t')
    chip700.append((float(item[-4])))
plt.figure(figsize=(15,4))
plt.subplots_adjust(bottom=0.12)
plot1=plt.subplot(1,1,1,axisbg='0.92')

ax1=plt.plot(locations,ccwt,linewidth=3,color='orange',alpha=0.65,zorder=4,label='wt')
ax2=plt.plot(locations,cc762,linewidth=3,color='red',alpha=0.65,zorder=4,label='$\Delta$762')
plt.xlim(min(locations),max(locations)-500)
plot1.spines['bottom'].set_linewidth('2')
plot1.spines['top'].set_visible(False)
plot1.spines['right'].set_visible(False)
plot1.spines['left'].set_linewidth('2')
plot1.spines['left'].set_visible(False)
plot1.spines['bottom'].set_color('1')
plot1.spines['bottom'].set_zorder(4)
plot1.grid(axis='y',linestyle="-",color='#D8D8D8',linewidth=2,zorder=0)
plot1.set_title(r"H3K4me$^3$",fontsize=20,fontstyle='italic',fontweight="medium",color='0.35')
plot1.set_ylabel('Fold Enrichment',fontsize=16,fontweight='medium',color='0.35')
plot1.set_xlabel("Chromosome XV",fontsize=16,fontweight="medium",color='0.35')
plt.xlabel('Chromosome XV',fontsize=18, fontweight='bold')
plot1.legend(frameon=False,loc='best',fontsize=14)
plt.show()
