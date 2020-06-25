f = np.linspace(0,40,2040);
zeta = 0.3;
sigma = 0.9;
fn =5;
T90 = 0.3;
eps = 0.4;
tn = 30;



x,t = some_f(sigma,fn,zeta,f,T90,eps,tn)
print(np.shape(x[0]))
plt.figure(figsize=(40, 20))
plt.plot(t, x[0]+generate_noise(204)/8000)


plt.show()
