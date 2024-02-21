# random.seed(a=None, version=2): Inicializa el generador de números aleatorios. Si a es omitido o None, se utiliza el tiempo del sistema actual. Si a es un entero, se utiliza directamente. Con la versión 2 (la predeterminada), un objeto str, bytes o bytearray se convierte a un entero y se utilizan todos sus bits.

# random.getstate(): Retorna un objeto que captura el estado interno actual del generador. Este objeto puede ser pasado a setstate() para restaurar el estado.

# random.randbytes(n): Genera n bytes aleatorios.

# random.randrange(stop), random.randrange(start, stop[, step]): Retorna un elemento seleccionado aleatoriamente de un rango. El patrón de argumentos posicionales coincide con la función range(). Los argumentos de palabra clave no deben ser utilizados porque pueden ser interpretados de manera inesperada.

# random.randint(a, b): Retorna un entero aleatorio N tal que a <= N <= b.

# random.getrandbits(k): Retorna un entero no negativo con k bits aleatorios.

# random.choice(seq): Retorna un elemento aleatorio de la secuencia no vacía seq.

# random.choices(population, weights=None, *, cum_weights=None, k=1): Retorna una lista de tamaño k de elementos elegidos de la población con reemplazo.

# random.shuffle(x): Mezcla la secuencia x.

# random.sample(population, k, *, counts=None): Retorna una lista de longitud k de elementos únicos seleccionados de la secuencia población.

# random.binomialvariate(n=1, p=0.5): Distribución binomial. Retorna el número de éxitos para n ensayos independientes con la probabilidad de éxito en cada ensayo siendo p.

# random.random(): Retorna el próximo número de punto flotante aleatorio en el rango 0.0 <= X < 1.0.

# random.uniform(a, b): Retorna un número de punto flotante N tal que a <= N <= b o b <= N <= a.

# random.triangular(low, high, mode): Retorna un número de punto flotante N tal que low <= N <= high y con el modo especificado entre esos límites.

# random.betavariate(alpha, beta): Distribución beta.

# random.expovariate(lambd=1.0): Distribución exponencial.

# random.gammavariate(alpha, beta): Distribución gamma.

# random.gauss(mu=0.0, sigma=1.0): Distribución normal.

# random.lognormvariate(mu, sigma): Distribución lognormal.

# random.normalvariate(mu=0.0, sigma=1.0): Distribución normal.

# random.vonmisesvariate(mu, kappa): Distribución de Von Mises.

# random.paretovariate(alpha): Distribución de Pareto.

# random.weibullvariate(alpha, beta): Distribución de Weibull.

# random.Random([seed]): Clase que implementa el generador de números pseudoaleatorios predeterminado usado por el módulo random.

# random.SystemRandom([seed]): Clase que utiliza la función os.urandom() para generar números aleatorios de fuentes proporcionadas por el sistema operativo.