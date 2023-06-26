import matplotlib.pyplot as plt
import numpy as np


class Runner:
    def run():
        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")

        # Setup 2x2 subplots with specific dimensions and edge styles
        fig,axes = plt.subplots(2,2,
                        facecolor='0.75',
                        linewidth=10,
                        edgecolor='Green')
        
        # Unpack the 2D array into separate var iables for easier access
        t = np.arange(-3.0, 3.0, 0.05)
        ax0,ax1,ax2,ax3 = axes.flatten() 

        ax0.spines['left'].set_position('center')
        ax0.spines['right'].set_color('none')
        ax0.spines['bottom'].set_position('center')
        ax0.spines['top'].set_color('none')
        ax0.set_xticks(np.arange(-2,3,2))
        ax0.text(-3,0.5,'$Sine$')
        ax0.plot(t,np.sin(1*np.pi*t))

        # 2 * Cos plot
        ax1.spines['left'].set_position('center')
        ax1.spines['right'].set_color('none')
        ax1.spines['bottom'].set_position('center')
        ax1.spines['top'].set_color('none')
        ax1.set_xticks(np.arange(-2,3,2))
        ax1.text(-3,1,'$2*Cosine$')  # Change 'sine' to '2cosine'
        ax1.plot(t, 2*np.cos(0.5*np.pi*t))  # Change np.sin to 2*np.cos


        # -t^3 plot
        ax2.plot(t, -t**3, label='')
        ax2.spines['left'].set_position('center')
        ax2.spines['bottom'].set_position('center')
        ax2.spines['right'].set_color('none')
        ax2.spines['top'].set_color('none')
        ax2.xaxis.set_ticks_position('bottom')
        ax2.yaxis.set_ticks_position('left')
        ax2.text(1, 8, '$y=-x^3$')
        ax2.legend()

        # 0.5 * t^2 plot
        ax3.plot(t, 0.5 * t**2)
        ax3.spines['left'].set_position('center')
        ax3.spines['bottom'].set_position('center')
        ax3.spines['right'].set_color('none')
        ax3.spines['top'].set_color('none')
        ax3.xaxis.set_ticks_position('bottom')
        ax3.yaxis.set_ticks_position('left')
        ax3.text(0.25, 3.5, '$y=0.5*x^2$')
        ax3.set_ylim(-4.5,4.5)
        ax3.legend()

        # Improve the layout
        plt.figtext(0.1,0.02,'Sam Beers Haskins')
        plt.show()
