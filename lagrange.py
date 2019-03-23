#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def print_poly(li):
    st = "P = "
    if len(li) is 0:
        st = st + "0"
    else:
        st_monomes = []
        for i in range(len(li)):
                s = str(li[i])
                ma = len(li) - 1
                if i != ma:
                    s = s + " * X"
                    if i < ma - 1:
                        s = s + "^" + str(ma - i)
                st_monomes.append(s)
        st = st + " + ".join(st_monomes)
    print(st)

def build_lagrange_poly(li_x, li_y):
    res = []

    if len(li_x) != len(li_y):
        return None

    for i in range(len(li_x)):
        base = [1]
        for j in range(len(li_x)):

            if i == j:
                continue
            p = [1, -li_x[j]]
            denum = li_x[i] - li_x[j]
            p = np.polymul(p, [1. / denum])
            base = np.polymul(base, p)

        base = np.polymul(base, [li_y[i]])
        res = np.polyadd(res, base)
    return (res)

def draw_poly(li_x, li_y):
    if len(li_x) != len(li_y):
        return
    x = li_x.copy()
    y = li_y.copy()
    if (len(x) == 0):
        x.append(0)
        y.append(0)
    p = build_lagrange_poly(x, y)
    print_poly(p)
    for i in range(len(x)):
        val = np.polyval(p, x[i])
        print(y[i], "= P(", x[i], ") => ", val)
    
    mi = min(x)
    ma = max(x)
    ecart = ma - mi
    xvals = np.linspace(mi - 0.5, ma + 0.5, 100)
    yvals = []
    for val in xvals:
        yvals.append(np.polyval(p, val))

    plt.clf()
    plt.title("Lagrange plot")
    plt.xlabel("Input")
    plt.ylabel("Eval values")

    plt.plot(xvals, yvals, "b", x, y, "ro")
    plt.draw()

    plt.pause(0.1)

def main():
    x = []
    y = []
    running = True

    while running:
        draw_poly(x, y)
        print("Quit / X Y ?")
        st = input()
        if st == "Quit":
            running = False
        else:
            try:
                x0, y0 = list(map(int, st.split(" ")))
                if x0 in x:
                    print(x0, "already in x list")
                else:
                    x.append(x0)
                    y.append(y0)
            except:
                print("Fail to parse...")

if __name__ == "__main__":
    main()
