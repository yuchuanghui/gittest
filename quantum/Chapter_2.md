# Chapter 2 Waves and quantum mechanics- Schr&Ouml;dinger's equation

Suppose that electron might be described as waves.

## 2.1 Rationalization of Schr&ouml;dingers' equation

> How can we propose wave behavior for particles such ad electrons?

**Wave-particle duality**: electrons behave both as particles and waves

* Particle: have a specific charge and mass
* Wave: diffraction and interference

**de Broglie's hypothesis**:  
$$
\lambda=\frac{h}{p}
$$
$$
h\cong6.626\times10^{-34}J\cdot s
$$

By de Broglie's hypothesis(p is the momentum of the elect), we propose the electron behave as a plane wave with a "wave function":
$$
\psi \propto \exp (2 \pi i z / \lambda)
$$
 And we also think that the electron wave obeys a scalar equation and choose the simplest one: **Helmholtz wave equation**:

$$
\frac{d \psi}{d z^{2}}=-k^{2} \psi
$$

Solution:

$$
\begin{cases}\sin(kz)\\\sin(-kz)\end{cases} \quad\begin{cases}\cos (k z) \\ \cos (-k z)\end{cases}\quad\begin{cases}\exp(kz) \\ \exp (-k z)\end{cases}
$$
where $k = 2\pi/\lambda=p/\hbar$

The equation above can be expanded into three dimensions($\frac{d}{dz^2}$ becomes Laplacian operator"del squared"$\nabla^2 or \Delta$).

Rewrite this simple wave equation into with k:
$$
-\hbar^2\nabla^2\psi=p^2\psi
$$
Divide both side by 2m~0~ (the rest mass of a free electron):
$$
-\frac{\hbar^2}{2m_0}\nabla^2\psi=\frac{p^2}{2m_0}\psi
$$
Newtonian classical mechanics tell us $\frac{p^2}{2m_0}$ is the kinetic energy of an electron. And if we also involve the potential energy *V*(**r**), then the equation can be rewrite as：
$$
\left(-\frac{\hbar^{2}}{2 m_{o}} \nabla^{2}+V(\mathbf{r})\right) \psi=E \psi
$$

<center>
    <l>Time-independent Schrodinger equation</l>
</center>

**Schr&ouml;dinger's equation** is not derived, is postulated.

## 2.2 Probability densities

$$
P(\mathbf{r})\propto|\psi(\mathbf{r})|^{2}
$$

The probability $P(\mathbf{r})$ of finding the electron neat any specific point **r** in space  is proportional to the modulus squared of the wave amplitude.

## 2.3 Diffraction by two slits

Consider two open slits separated by a distance *s*, in an otherwise opaque screen.

<img src="C:\Users\yisiyuhui\Desktop\gitcontrol\gitbookread\quantum\image-20210113212606149.png" alt="image-20210113212606149" style="zoom:67%;" />

<center>Young's slits</center>

+ A monochromatic electron beam of wavevector *k* shined at the screen

+ The slits is very narrow compared to both the wavelength $\lambda=2\pi/k$ and the separation *s*. 
+ The position of the screen relative to the  slits  $z_0>>s$

Regard the slits as essentially point sources of expanding waves (Huygens' principle). Then we can write these waves in the form $\exp(ikr)$.(why?)

The net wave at the screen is:
$$
\psi(x)\propto\exp\left[ik\sqrt{(x-s/2)^2+z_0^2}\ \right]+\exp\left[ik\sqrt{(x+s/2)^2+z_0^2}\ \right ]
$$
 In the situation of relative small angles, i.e., x<<z~0~:
$$
\sqrt{(x-s/2)^2+z_0^2}\approx z_0\left[1+\frac{(x-s/2)^2}{2z_0^2})\right]\\=z_0+x^2/2z_0+s^2/8z_0-sx/2z_0
$$
Notice that only -sx/2z~0~ has the opposite sign for the two terms Using $\exp(i\theta)+\exp(-i\theta)=2\cos\theta$:
$$
\psi(x)\propto \exp(i\phi)\cos(ksx/2z_0)\\
\phi=k(z_0+x^2/2z_0+s^2/8z_0)
$$
$\exp(i\phi)$ is a phase factor, so:
$$
\left| \psi_s(x) \right|^2 \propto \cos^2(sx\pi/2\lambda z_0)=\frac{1}{2}\left[1+\cos(2\pi sx/\lambda z_0)\right]
$$
From the expression of $\left| \psi_s(x) \right|^2$, we can expect to see a sinusoidal interference. The bright area and dark area emerge in sequence separated by a distance $d_s=period/2=\lambda$

> The exist of interference effects has some bizarre consequence that we simply cannot understand classically. 

If we block one of the slits, the pattern on the screen will be a broad featureless band. In the view of wave function we can readily understand this phenomenon. But in a classical model we make some qualitatively plausible explanations, such as electron bouncing off the edges of the silt.

If we uncover the second slit, we will see the fringes. It can not be explained by the classical particle model.

> We might try to argue that the particles from the second slit were somehow bouncing off the ones from the first slit, and hence avoiding some particular part of the screen because of these collisions.   

But if we lower the electron currents to make sure that there are never two electrons in the apparatus at a given time, we will still see exactly the same interference pattern emerge.

The wave description postulated above can explain the behavior involving interference of amplitudes qualitatively and quantitatively.

## 2.4 Linearity of quantum mechanics: multiplying by a constant

Schr&ouml;dinger equation is linear, because the wavefunction and its derivative only appears in first order.

> The linearity allows us to use the full power of linear algebra to handle the mathematics of quantum mechanics.

## 2.5 Normalization of the wave function

$P(\mathbf{r})$ : the probability of finding a particle neat a point **r** in a space.

$d^3\mathbf{r}$: a infinitesimal volume

We know that the particle is somewhere in the total volume of interest (can't be infinite). So:
$$
\int P(\mathbf{r})d^3 \mathbf{r} =1
$$
We also want the integral of  $\psi(\mathbf{r})$ over the whole volume equals unity. We can define a coefficient a, which have:
$$
|a|^2=\frac{1}{\int|\psi(\mathbf{r})|\ d^3\mathbf{r}}
$$
Then we can normalize the wave function:
$$
\psi_N(\mathbf{r}) = a\psi(\mathbf{r}) \\
\int|\psi_N(\mathbf{r})|\ d^3\mathbf{r} =1
$$
Because the wave function is linear, so the function is still correct after replacing $\psi(\mathbf{r})$ with $\psi_N(\mathbf{r})$.

## 2.6 Particle in an infinitely deep potential well

> "Particle in a box"  "Harmonic oscillator"
>
> The exactly solvable problems do give us much insight into quantum mechanics in general

+ Particle in a box: It can be used routinely to design the so-called "quantum well" optoelectronic structures 
+ Harmonic oscillator: Help us understand vibrating system.

### Mathematical Solution 

**Wave Equation**

Consider a particle of mass *m*, with a spatially-varying potential $V(z)$ in the direction. In this kind of problem, the motion of  different dimensions can be considered separately and its results added in later. So we only consider the z direction:
$$
-\frac{\hbar}{2m}\frac{d^2\psi(z)}{dz^2}+V(z)\psi(z)=E\psi(z)
$$
**Boundary condition of "infinite well"**

In the case where the potential is a simple rectangular potential well: $V(z)$ is constant inside the well and rises abruptly at the walls (rises to infinitely high). 

Choose the value of V inside the well to be zero for simplicity.
$$
V=\begin{cases}0\quad \  inside well\\ \infty \quad outside\ well\end{cases}
$$
V is infinite but E is presumably finite. So the possibility of find a particle outside the well is zero ($\psi(\mathbf{r})$=0).  To keep the the continuity of the wave function.
$$
\psi(z)=0 \quad \tt at\ the  \ walls
\\ \lim_{z \to 0} \psi(z)=0 \quad \tt near \ walls
$$
Putting these constrains to the equation:
$$
-\frac{\hbar}{2m}\frac{d^2\psi(z)}{dz^2}=E\psi(z) \\ \tt{boundary\  conditions}:\psi=0 \  at\ z=0,L_z
$$
**Solution**
$$
\psi_n(z)=A_n \sin \left(\frac{n\pi z}{L_z }\right)
$$
According the equation, we also have:
$$
k=n\pi/L_z=\sqrt{2mE/\hbar}\\
E_n=\frac{\hbar^2}{2m}\left(\frac{n\pi}{L_z}\right)^2
$$
This relation shows that if we describe the particle  in wave function, the Energy will be some specific value. In other word, the energy is discrete.

 ![image-20210116110949643](C:\Users\yisiyuhui\Desktop\gitcontrol\gitbookread\quantum\image-20210116110949643.png)

<center> Sketch of energy levels and wave functions<center>

**Some definition**

So we get a specific set of allowed values of a parameter(here energy). We call it **eigen values**. Each such value has a  particular solution associated with, which is called **eigen solutions**. The equation giving rise to such solutions is called **eigen equation**. The function is called **eigenfunction**. More than one eigenfunction can be associated with a given eigen values. This phenomenon is known as degeneracy.

+ Eigen values: $E_n$

+ Eigen solutions: $\psi_n(\bf r)$

+ Eigen equation: $-\frac{\hbar}{2m}\frac{d^2\psi(z)}{dz^2}=E\psi(z) \\ $

**Solve A~n~ by normalization**

Complete the solution by normalizing the eigen functions(choose real quantities for simplicity):
$$
\psi(z)=\sqrt{\frac{2}{L_z}}\sin\left(\frac {n\pi z}{L_z}\right)
$$

### Physical Meaning

