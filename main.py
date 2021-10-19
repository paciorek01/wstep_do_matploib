import numpy as np
import pickle
import matplotlib
import matplotlib.pyplot as plt
import string
import random
def compare_plot(x1:np.ndarray,y1:np.ndarray,x2:np.ndarray,y2:np.ndarray,
                 xlabel: str,ylabel:str,title:str,label1:str,label2:str):
    """Funkcja służąca do porównywania dwóch wykresów typu plot. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    x1(np.ndarray): wektor wartości osi x dla pierwszego wykresu,
    y1(np.ndarray): wektor wartości osi y dla pierwszego wykresu,
    x2(np.ndarray): wektor wartości osi x dla drugiego wykresu,
    y2(np.ndarray): wektor wartości osi x dla drugiego wykresu,
    xlabel(str): opis osi x,
    ylabel(str): opis osi y,
    title(str): tytuł wykresu ,
    label1(str): nazwa serii z pierwszego wykresu,
    label2(str): nazwa serii z drugiego wykresu.
    
    Returns:
    matplotlib.pyplot.figure: wykres zbiorów (x1,y1), (x2,y2) zgody z opisem z zadania 3 
    """
    if x1.shape != y1.shape or x2.shape != y2.shape:
        return None
    fig, ax = plt.subplots()
    ax.plot(x1, y1, "-b", linewidth=4)
    ax.plot(x2, y2, "-k", linewidth=2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(label1, label2)
    return fig

def parallel_plot(x1:np.ndarray,y1:np.ndarray,x2:np.ndarray,y2:np.ndarray,
                  x1label:str,y1label:str,x2label:str,y2label:str,title:str,orientation:str):
    """Funkcja służąca do stworzenia dwóch wykresów typu plot w konwencji subplot wertykalnie lub chorycontalnie. 
    Szczegółowy opis w zadaniu 5.
    
    Parameters:
    x1(np.ndarray): wektor wartości osi x dla pierwszego wykresu,
    y1(np.ndarray): wektor wartości osi y dla pierwszego wykresu,
    x2(np.ndarray): wektor wartości osi x dla drugiego wykresu,
    y2(np.ndarray): wektor wartości osi x dla drugiego wykresu,
    x1label(str): opis osi x dla pierwszego wykresu,
    y1label(str): opis osi y dla pierwszego wykresu,
    x2label(str): opis osi x dla drugiego wykresu,
    y2label(str): opis osi y dla drugiego wykresu,
    title(str): tytuł wykresu,
    orientation(str): parametr przyjmujący wartość '-' jeżeli subplot ma posiadać dwa wiersze albo '|' jeżeli ma posiadać dwie kolumny.

    
    Returns:
    matplotlib.pyplot.figure: wykres zbiorów (x1,y1), (x2,y2) zgody z opisem z zadania 5
    """
    if x1.shape != y1.shape or x2.shape != y2.shape:
        return None
    if orientation == "-":
        fig, (ax1, ax2) = plt.subplots(2, 1)
        ax1.plot(x1, y1)
        ax1.set(xlabel=x1label, ylabel=y1label)
        ax2.plot(x2, y2)
        ax2.set(xlabel=x2label, ylabel=y2label)
        fig.suptitle(title)
        return fig
    elif orientation == "|":
        fig, (ax1, ax2) = plt.subplots(1, 2)
        ax1.plot(x1, y1)
        ax1.set(xlabel=x1label, ylabel=y1label)
        ax2.plot(x2, y2)
        ax2.set(xlabel=x2label, ylabel=y2label)
        fig.suptitle(title)
        return fig
    else:
        return None

def log_plot(x:np.ndarray,y:np.ndarray,xlabel:np.ndarray,ylabel:str,title:str,log_axis:str):
    """Funkcja służąca do tworzenia wykresów ze skalami logarytmicznymi. 
    Szczegółowy opis w zadaniu 7.
    
    Parameters:
    x(np.ndarray): wektor wartości osi x,
    y(np.ndarray): wektor wartości osi y,
    xlabel(str): opis osi x,
    ylabel(str): opis osi y,
    title(str): tytuł wykresu ,
    log_axis(str): wartość oznacza:
        - 'x' oznacza skale logarytmiczną na osi x,
        - 'y' oznacza skale logarytmiczną na osi y,
        - 'xy' oznacza skale logarytmiczną na obu osiach.
    
    Returns:
    matplotlib.pyplot.figure: wykres zbiorów (x,y) zgody z opisem z zadania 7 
    """
    if x.shape != y.shape:
        return None
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    if log_axis == "x":
        ax.set_xscale("log")
    elif log_axis == "y":
        ax.set_yscale("log")
    elif log_axis == "xy":
        ax.set_xscale("log")
        ax.set_yscale("log")
    else:
        return None
def log_spiral(a, b, angle):
    r = a * np.exp(b * angle)
    x = r * np.cos(angle)
    y = r * np.sin(angle)
    return x,y


def fun_f(x):
    return x + 2
def fun_g(x):
    return x**2 - 2*np.sin(x) + 3
x = np.arange(-5,5,1)
compare_plot(x,fun_f(x),x,fun_g(x),"ość x","ość y","f(x) != g(x)","f(x)","g(x)")
plt.show()

ang = np.linspace(0, 4*np.pi, 100)
x, y = log_spiral(0.01, 0.2, ang)
x2, y2 = log_spiral(10, 0.2, ang)

parallel_plot(x, y, x2, y2, "x", "y", "x", "y", "Spirala logarytmiczna", "|")
plt.show()

masa = 3
v_odc = np.arange(0,400,0.5)
c_odc = (masa * v_odc**2)/2
log_plot(v_odc, c_odc, "[m/s]", "[J]", "Q(v)", "x")
plt.show()
log_plot(v_odc, c_odc, "[m/s]", "[J]", "Q(v)", "y")
plt.show()
log_plot(v_odc, c_odc, "[m/s]", "[J]", "Q(v)", "xy")
plt.show()