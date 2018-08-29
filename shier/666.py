from tkinter import *
import random
tk =Tk()
canvas = Canvas(tk,width=400,height=400)
canvas.pack()
for m in range(0,3):
    g = ['red', 'pink', 'green','gray']
    h = random.randint(0,3)
    a = 10
    b = 10
    c = 100
    d = 10
    e = 100
    f = 110
    canvas.create_polygon(a,b,c,d,e,f,fill=g[h],outline="black")
    x = ['red', 'pink', 'green', 'gray']
    u = random.randint(0, 3)
    i = a + 90 + 10
    j = b
    k = c * 2 + 10
    l = d
    m = e * 2 + 10
    n = f
    canvas.create_polygon(i,j,k,l,m,n,fill=x[u],outline="black")
    y = ['red', 'pink', 'green', 'gray']
    z = random.randint(0, 3)
    o = i + 90 + 20
    p = j
    q = k + 100 + 20
    r = l
    s = m + 100 + 20
    t = n
    canvas.create_polygon(o,p,q,r,s,t,fill=y[z],outline="black")
    ttt = ['red', 'pink', 'green', 'gray']
    uu = random.randint(0, 3)
    aa = 10
    aaa = 110
    bb = 100
    bbb = 110
    cc = 100
    ccc = 220
    canvas.create_polygon(aa,aaa,bb,bbb,cc,ccc,fill=ttt[uu],outline="black")
    yyy = ['red', 'pink', 'green', 'gray']
    zzz = random.randint(0, 3)
    dd = aa + 90 + 10
    ddd = aaa
    ee = bb * 2 + 10
    eee = bbb
    ff = cc * 2 + 10
    fff = ccc
    canvas.create_polygon(dd,ddd,ee,eee,ff,fff,fill=yyy[zzz],outline="black")
    xxx = ['red', 'pink', 'green', 'gray']
    ooo = random.randint(0, 3)
    gg = dd + 90 + 20
    ggg = ddd
    hh = ee + 100 + 20
    hhh = eee
    ii = ff + 100 + 20
    iii = fff
    canvas.create_polygon(gg,ggg,hh,hhh,ii,iii,fill=xxx[ooo],outline="black")
    uu = ['red', 'pink', 'green', 'gray']
    vv = random.randint(0, 3)
    jj = 10
    jjj = 220
    kk = 100
    kkk = 220
    ll = 100
    lll = 330
    canvas.create_polygon(jj,jjj,kk,kkk,ll,lll,fill=uu[vv],outline="black")
    uuu = ['red', 'pink', 'green', 'gray']
    vvv = random.randint(0, 3)
    mm = jj + 90 + 10
    mmm = jjj
    nn = kk * 2 + 10
    nnn = kkk
    oo = ll * 2 + 10
    oooo = lll
    canvas.create_polygon(mm,mmm,nn,nnn,oo,oooo,fill=uuu[vvv],outline="black")
    ss = ['red', 'pink', 'green', 'gray']
    ww = random.randint(0, 3)
    pp = mm + 90 + 20
    ppp = mmm
    ou = nn + 100 + 20
    ouu = nnn
    rr = oo + 100 + 20
    rrr = oooo
    canvas.create_polygon(pp,ppp,ou,ouu,rr,rrr,fill=ss[ww],outline="black")
tk.mainloop()
