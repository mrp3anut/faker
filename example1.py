import faker_boun as fk 
import matplotlib.pyplot as plt

c = fk.generate_noise_and_eq(100, scale = 100, noise_type='perlin')


#plt.figure(figsize=(40,20))
plt.plot(c)
plt.show()