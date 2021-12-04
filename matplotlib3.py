# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 15:42:04 2021

@author: German
"""

import matplotlib.pyplot as plt

import numpy as np

a= np.linspace(0,5,10)
b=a**3

#print(a)
#print(b)


#print(plt.plot(a,b))
#print(plt.xlabel('a array'))
#print(plt.ylabel('b array'))
#print(plt.title('Plot for a and b arrays'))


#print(plt.subplot(1,2,1))
#print(plt.plot(a,b,'r'))
#print(plt.subplot(1,2,2))
#print(plt.plot(b,a,'b'))


#figure=plt.figure()
#axes=figure.add_axes([0.1,0.1,0.8,0.8])
#axes.plot(a,b)
#axes.set_xlabel('a array value')
#axes.set_ylabel('b array value')
#axes.set_title('Some title')




#figure1=plt.figure()
#axes1=figure1.add_axes([0.1,0.1,0.8,0.8])
#axes2=figure1.add_axes([0.3,0.6,0.5,0.4])





#figure2=plt.figure()
#axes3=figure2.add_axes([0.0,0.0,1,1])
#axes4=figure2.add_axes([0.3,0.6,0.5,0.4])




#figure3=plt.figure()
#axes5=figure3.add_axes([0.0,0.0,1,1])
#axes6=figure3.add_axes([0.5,0.0,0.5,0.4])



#figure4=plt.figure()
#axes7=figure4.add_axes([0.0,0.0,1,1])
#axes8=figure4.add_axes([0.2,0.3,0.5,0.4])
#axes7.plot(a,b)
#axes8.plot(b,a)



#figure6=plt.figure()
#axes10=figure6.add_axes([0.0,0.0,1,1])
#axes11=figure6.add_axes([0.1,0.4,0.5,0.4])

#axes10.plot(a,b)
#axes11.plot(b,a)
#axes10.set_xlabel('a array value')
#axes10.set_ylabel('b array value')
#axes10.set_title('Axes10 title')

#axes11.set_xlabel('b array value')
#axes11.set_ylabel('a array value')
#axes11.set_title('Axes11 title')





#figure7=plt.figure()
#axes12=figure7.add_axes([0.0,0.0,1,1])
#axes12.plot(a,b)



#figure, axes = plt.subplots()
#axes.plot(a,b)




#figure, axes = plt.subplots(1,2)





#figure, axes = plt.subplots(nrows=1,ncols=2)














#figure, axes = plt.subplots(nrows=2,ncols=4)







#figure, axes = plt.subplots(nrows=2,ncols=4)
#plt.tight_layout()






#figure, axes1 = plt.subplots(nrows=1,ncols=2)
#for current_ax in axes1:
    #current_ax.plot(a,b)
#print(axes1)






#figure, axes1 = plt.subplots(nrows=1,ncols=2)
#print(axes1[0].plot(a,b))




#figure, axes1 = plt.subplots(nrows=1,ncols=2)
#print(axes1[0].plot(a,b))
#print(axes1[1].plot(a,b))



#figure, axes1 = plt.subplots(nrows=1,ncols=2)
#print(axes1[0].plot(a,b))
#print(axes1[1].plot(b,a))





#figure, axes1 = plt.subplots(nrows=1,ncols=2)
#print(axes1[0].plot(a,b))
#axes1[0].set_xlabel('a arrays value')
#axes1[0].set_ylabel('b arrays value')
#axes1[0].set_title('Axes[0] title')


#print(axes1[1].plot(b,a))
#axes1[1].set_xlabel('b arrays value')
#axes1[1].set_ylabel('a arrays value')
#axes1[1].set_title('Axes[1] title')




#figure=plt.figure(figsize=(4,3))
#axes=figure.add_axes([0,0,1,1])
#print(axes.plot(a,b))



#figure=plt.figure(figsize=(7,2))
#axes=figure.add_axes([0,0,1,1])
#print(axes.plot(a,b))




#figure,axes=plt.subplots(figsize=(7,2))
#print(axes.plot(a,b))





#figure,axes=plt.subplots(nrows=2, ncols=1,figsize=(7,2))
#print(axes[0].plot(a,b))






#figure,axes=plt.subplots(nrows=2, ncols=1,figsize=(7,2))
#print(axes[0].plot(a,b))
#print(axes[1].plot(b,a))





#figure,axes=plt.subplots(nrows=2, ncols=1,figsize=(7,2))
#print(axes[0].plot(a,b))
#print(axes[1].plot(b,a))
#plt.tight_layout()
#print(figure)
#figure.savefig('myplot.png')
#figure.savefig('myplot1.png',dpi=300)




#figure=plt.figure()
#axes=figure.add_axes([0,0,1,1])
#axes.plot(a,b)
#axes.plot(b,a)




#figure=plt.figure()
#axes=figure.add_axes([0,0,1,1])
#axes.plot(a,b,label='a,b plot')
#axes.plot(b,a, label='b,a plot')
#axes.legend()





#figure=plt.figure()
#axes=figure.add_axes([0,0,1,1])
#axes.plot(a,b,label='a,b plot')
#axes.plot(b,a, label='b,a plot')
#axes.legend(loc=9)




#figure=plt.figure()
#axes=figure.add_axes([0,0,1,1])
#axes.plot(a,b, color='#CD5C5C', linewidth=2, alpha=1, linestyle='-.',
          #marker='o', markersize='20', markerfacecolor='blue',
          #markeredgewidth=3, markeredgecolor='purple')
#alpha-прозрачность
#linewidth или lw
#linestyle или ls
#markerfacecolor граница маркера





#figure=plt.figure()
#axes=figure.add_axes([0,0,1,1])
#axes.plot(a,b, color='#CD5C5C', linewidth=2, alpha=1, linestyle='-.',
          #marker='o', markersize='20', markerfacecolor='blue',
          #markeredgewidth=3, markeredgecolor='purple')
#axes.set_xlim([0,1])




#figure=plt.figure()
#axes=figure.add_axes([0,0,1,1])
#axes.plot(a,b, color='#CD5C5C', linewidth=2, alpha=1, linestyle='-.',
          #marker='o', markersize='20', markerfacecolor='blue',
          #markeredgewidth=3, markeredgecolor='purple')
#axes.set_ylim([0,3])





figure=plt.figure()
axes=figure.add_axes([0,0,1,1])
axes.plot(a,b, color='#CD5C5C', linewidth=2, alpha=1, linestyle='-.',
          marker='o', markersize='20', markerfacecolor='blue',
          markeredgewidth=3, markeredgecolor='purple')
axes.set_xlim([0,1])
axes.set_ylim([0,3])






