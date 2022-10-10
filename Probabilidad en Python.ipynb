{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Probabilidad clásica"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "En probabilidad clásica (modelo laplaciano)\n",
    "\n",
    "- Experimento aleatorio.\n",
    "- Espacio muestral $\\Omega$ (conjunto de todos los posibles resultados de un experimento aleatorio). Hipótesis $\\# \\Omega < +\\infty$. \n",
    "- Eventos (diccionario con conjuntos).\n",
    "- Si $\\omega\\in \\Omega$, entonces $\\{ \\omega \\}$ se le asigna una función $P: P(\\Omega)\\to [0,1]$\n",
    "$$P(\\{ \\omega \\})=\\frac{1}{\\# \\Omega}.$$\n",
    "\n",
    "En particular, si $A\\in P(\\Omega)$ (eventos) entonces\n",
    "$$P(A)=\\frac{\\# A}{\\# \\Omega}.$$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. Experimento: Lanzamiento de dos dados"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Supongamos que estamos interesados en el experimento aleatorio de lanzar un par de dados honestos. De este experimento nos interesa saber cuál es la suma de los dados en cada tirada."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1.1. El espacio muestral"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "El espacio muestral $\\Omega$ del experimento de lanzar dos dados honestos, está compuesto de todas las parejas ordenadas $(i,j)$ tales que $1\\le i,j\\le 6$ (enteros). Esto es \n",
    "\n",
    "$$\\Omega=\\{(i,j):1\\le i,j\\le 6\\}=\\{1,2,3,4,5,6\\}\\times \\{1,2,3,4,5,6\\}.$$\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "La cardinalidad de $\\Omega$: $\\# \\Omega = 6^{2}=36$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# usando itertools\n",
    "\n",
    "from itertools import product"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "Omega = set(product([1, 2, 3, 4, 5, 6], repeat = 2))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "36"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(Omega)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1.2. Eventos aleatorios"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Sea $S_n$ el evento \"La suma de los dados es $n$\". Esto es:\n",
    "\n",
    "$$S_n=\\{(i,j)\\in\\Omega:i+j=n\\}.$$\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def S(n):\n",
    "    Sn={(i,j) for i in range(1,7) for j in range(1,7) if i+j==n}\n",
    "    return Sn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "S(0) == S(1) == S(13)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{(3, 6), (4, 5), (5, 4), (6, 3)}"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "S(9)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "¿Cuál sería la probabilidad de que la suma de los dos dados sea $9$:\n",
    "    $$P(S(9))=\\frac{4}{36}$$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Observación: \n",
    "    $$\\sum_{i=2}^{12} P(S(i))=1.$$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Otro tipo de eventos"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Sea $T_n$ el evento \"La resta de los dados es mayor que $n$\". Esto es:\n",
    "\n",
    "$$T_n=\\{(i,j)\\in\\Omega:i-j\\geq n\\}.$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "def T(n):\n",
    "    Tn=[(i,j) for i in range(1,7) for j in range(1,7) if i-j>=n]\n",
    "    return Tn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(3, 1),\n",
       " (4, 1),\n",
       " (4, 2),\n",
       " (5, 1),\n",
       " (5, 2),\n",
       " (5, 3),\n",
       " (6, 1),\n",
       " (6, 2),\n",
       " (6, 3),\n",
       " (6, 4)]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "T(2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. La variable aleatoria asociada a $S_{n}$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2.1 Definición de función de probabilidad"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "from fractions import Fraction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "def P(A):\n",
    "    P = Fraction(len(A), len(Omega))\n",
    "    return P"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "S = {(i,j) : i+j for i,j in Omega}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "from collections import defaultdict\n",
    "\n",
    "dS = defaultdict(set)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "for i, j in S.items():\n",
    "        \n",
    "    dS[j].add(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(4, {(1, 3), (2, 2), (3, 1)}),\n",
       " (12, {(6, 6)}),\n",
       " (11, {(5, 6), (6, 5)}),\n",
       " (3, {(1, 2), (2, 1)}),\n",
       " (8, {(2, 6), (3, 5), (4, 4), (5, 3), (6, 2)}),\n",
       " (7, {(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)}),\n",
       " (6, {(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)}),\n",
       " (10, {(4, 6), (5, 5), (6, 4)}),\n",
       " (9, {(3, 6), (4, 5), (5, 4), (6, 3)}),\n",
       " (5, {(1, 4), (2, 3), (3, 2), (4, 1)}),\n",
       " (2, {(1, 1)})]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(dS.items())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{4: Fraction(1, 12),\n",
       " 12: Fraction(1, 36),\n",
       " 11: Fraction(1, 18),\n",
       " 3: Fraction(1, 18),\n",
       " 8: Fraction(5, 36),\n",
       " 7: Fraction(1, 6),\n",
       " 6: Fraction(5, 36),\n",
       " 10: Fraction(1, 12),\n",
       " 9: Fraction(1, 9),\n",
       " 5: Fraction(1, 9),\n",
       " 2: Fraction(1, 36)}"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "leyS = {i : P(A) for i, A in dS.items() }\n",
    "\n",
    "leyS"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2.2 Ley de una variable aleatoria"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Tenemos una **variable aleatoria** \n",
    "$$S:\\Omega \\to \\{2,3,4,5,6,7,8,9,10,11,12\\}$$\n",
    "\n",
    "La **ley de $S$** (o la distribución de probabilidad) está determinada por la pareja $\\{(k, p_{k}), k\\in\\{2,3,4,5,6,7,8,9,10,11,12 \\} \\}$ en dónde\n",
    "$$p_{k}=\\mathbb{P}(\\{\\omega\\in \\Omega : S(\\omega)=k\\}).$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2     1/36\n",
       "3     1/18\n",
       "4     1/12\n",
       "5      1/9\n",
       "6     5/36\n",
       "7      1/6\n",
       "8     5/36\n",
       "9      1/9\n",
       "10    1/12\n",
       "11    1/18\n",
       "12    1/36\n",
       "dtype: object"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ley_S = pd.Series(leyS)\n",
    "ley_S.sort_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "def leyS(i):\n",
    "    \n",
    "    if i in range(2,13):\n",
    "        x = ley_S[i]\n",
    "    else:\n",
    "        x = 0\n",
    "    \n",
    "    return x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "rango_S = [k for k in range(2,13)]\n",
    "\n",
    "p_k = [float(leyS(k)) for k in range(2,13)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rango</th>\n",
       "      <th>densidad</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>S_2</th>\n",
       "      <td>2</td>\n",
       "      <td>0.027778</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>S_3</th>\n",
       "      <td>3</td>\n",
       "      <td>0.055556</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>S_4</th>\n",
       "      <td>4</td>\n",
       "      <td>0.083333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>S_5</th>\n",
       "      <td>5</td>\n",
       "      <td>0.111111</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>S_6</th>\n",
       "      <td>6</td>\n",
       "      <td>0.138889</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>S_7</th>\n",
       "      <td>7</td>\n",
       "      <td>0.166667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>S_8</th>\n",
       "      <td>8</td>\n",
       "      <td>0.138889</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>S_9</th>\n",
       "      <td>9</td>\n",
       "      <td>0.111111</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>S_10</th>\n",
       "      <td>10</td>\n",
       "      <td>0.083333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>S_11</th>\n",
       "      <td>11</td>\n",
       "      <td>0.055556</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>S_12</th>\n",
       "      <td>12</td>\n",
       "      <td>0.027778</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      rango  densidad\n",
       "S_2       2  0.027778\n",
       "S_3       3  0.055556\n",
       "S_4       4  0.083333\n",
       "S_5       5  0.111111\n",
       "S_6       6  0.138889\n",
       "S_7       7  0.166667\n",
       "S_8       8  0.138889\n",
       "S_9       9  0.111111\n",
       "S_10     10  0.083333\n",
       "S_11     11  0.055556\n",
       "S_12     12  0.027778"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lS = pd.DataFrame(list(zip(rango_S, p_k)), index=[f\"S_{i}\" for i in range(2,13)],\n",
    "               columns =['rango', 'densidad'])\n",
    "lS "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='rango'>"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "lS.plot.bar(x = 'rango', y='densidad')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. Lanzamiento de una moneda"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*Se tiene el siguiente experimento aleatorio:* Se lanzan, de manera independiente, 3 monedas justas. Sean $A=\\{\\text{cae águila}\\}$ y $B=\\{ \\text{cae sol}\\}$.\n",
    "\n",
    "Entonces, el espacio de estados es\n",
    "$$\\Omega=\\{A, S\\}\\times \\{A, S\\} \\times \\{A, S\\}.$$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "La cardinalidad de $\\Omega$ es $\\# \\Omega=2^{3}=8.$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{('A', 'A', 'A'),\n",
       " ('A', 'A', 'S'),\n",
       " ('A', 'S', 'A'),\n",
       " ('A', 'S', 'S'),\n",
       " ('S', 'A', 'A'),\n",
       " ('S', 'A', 'S'),\n",
       " ('S', 'S', 'A'),\n",
       " ('S', 'S', 'S')}"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from itertools import product\n",
    "\n",
    "Omega = set(product([\"A\", \"S\"], repeat=3))\n",
    "Omega"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Consideremos el evento $E:$ la cara de las tres monedas es \"águila\". En este caso, si se denota por $A_{i}$ al evento: el resultado del $i$-ésimo lanzamiento es *águila*, para $i=1,2,3$, entonces\n",
    "$$E=A_{1}\\cap A_{2}\\cap A_{3}.$$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Representemos a los conjuntos $A_{i}$:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{('A', 'A', 'A'), ('A', 'A', 'S'), ('A', 'S', 'A'), ('A', 'S', 'S')}"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A_1 = {om for om in Omega if om[0]== \"A\"}\n",
    "\n",
    "A_1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{('A', 'A', 'A'), ('A', 'A', 'S'), ('S', 'A', 'A'), ('S', 'A', 'S')}"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A_2 = {om for om in Omega if om[1]== \"A\"}\n",
    "\n",
    "A_2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{('A', 'A', 'A'), ('A', 'S', 'A'), ('S', 'A', 'A'), ('S', 'S', 'A')}"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A_3 = {om for om in Omega if om[2]== \"A\"}\n",
    "\n",
    "A_3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "El evento $E$ está representado como:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{('A', 'A', 'A')}"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "E = A_1.intersection(A_2.intersection(A_3))\n",
    "\n",
    "E"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "El evento $E$ también puede se representado usando el método `.count`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{('A', 'A', 'A')}"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "E = {om for om in Omega if om.count(\"A\")==3}\n",
    "\n",
    "E"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Por lo tanto,"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Fraction(1, 8)"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "P(E)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "En esta situación, podemos calcular la probabilidad del evento $F$: cae águila en el primero y segundo lanzamiento."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Fraction(1, 4)"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "F = A_1.intersection(A_2.intersection(Omega))\n",
    "\n",
    "P(F)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3.1 Probabilidad condicional e independencia."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "La probabilidad condicional, explica cómo cambia la probabilidad de un evento dado que se conoce la probabilidad de otro evento sujeto a las mismas condiciones."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Definición.-** Sea $(\\Omega,\\mathcal{A},\\mathbb{P})$ un espacio de probabilidad y $F\\subset \\Omega$ un evento asociado a cierto experimento aleatorio. Si $\\mathbb{P}(F)>0$ (es decir, si $F$ ocurre con probabilidad positiva), entonces es posible considerar un nuevo espacio de probabilidad en donde el espacio muestral sea ahora $(F,\\mathcal{A}_{F}=\\mathcal{A}\\cap F,\\mathbb{P}(\\bullet \\mid F))$, en donde la función de probabilidad se define como:\n",
    "$$\\mathbb{P}(E\\mid F)=\\frac{\\mathbb{P}(E\\cap F)}{\\mathbb{P}(F)},$$\n",
    "para todo $E\\in \\mathcal{A}_{B}$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "def P_cond(E, F):\n",
    "    return Fraction(len(E & F), len(F))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Consideremos el evento en $\\Omega$: \"El resultado del primer lanzamiento fue águila\". Sabemos que tal evento está representado por $A_1$. Podemos preguntarnos entonces sobre la probabilidad del evento $E$ dada la ocurrencia del evento $E_{1}$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Fraction(1, 4)"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "P_cond(E, A_1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Tratemos de contestar a la siguiente pregunta: ¿Cuál es la probabilidad de que se obtenga \"sol\" en el segundo lanzamiento dado dado que se obtuvo \"águila\" en el primer lanzamiento? "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Sea $B_2$ el evento: se obtiene \"sol\" en el segundo lanzamiento. Representemos a tal evento:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{('A', 'S', 'A'), ('A', 'S', 'S'), ('S', 'S', 'A'), ('S', 'S', 'S')}"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "B_2 = {om for om in Omega if om[1]== \"S\"}\n",
    "\n",
    "B_2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Entonces,"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Fraction(1, 2)"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "P_cond(B_2, A_1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note que,"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "P_cond(B_2, A_1) == 1-P_cond(A_2, A_1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3.2 Lanzamiento de monedas injustas (volados)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Sin embargo, existe la noción de **modelo de probabilidad frecuentista**: Bajo la hipótesis de que el espacio muestral es un conjunto finito, podemos definir la siguiente probabilidad asociada a un evento $A$\n",
    "$$f_{n}(A)=\\frac{n(A)}{n}$$\n",
    "en donde $n(A)$ denota al número de veces que ocurre $A$.\n",
    "\n",
    "Tenemos que \n",
    "$$f(A):=\\lim_{n\\to \\infty}f_{n}(A)$$\n",
    "tal modelo es más realista."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "def volado(p):\n",
    "    return 'sol' if random.random() < p else 'águila'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Por ejemplo, si la moneda tiene carga en $A$ igual a $0.4$, podemos realizar una sucesión de lanzamientos y obtener las veces que cae \"águila\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'águila'"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "volado(0.4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['águila',\n",
       " 'águila',\n",
       " 'sol',\n",
       " 'águila',\n",
       " 'sol',\n",
       " 'águila',\n",
       " 'sol',\n",
       " 'águila',\n",
       " 'águila',\n",
       " 'águila']"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = [volado(0.4) for i in range(10)]\n",
    "\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.count(\"sol\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['sol', 'sol', 'sol', 'sol', 'sol', 'sol', 'sol', 'águila', 'águila', 'sol']"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "resultados = []\n",
    "\n",
    "for i in range(10):\n",
    "        resultado = volado(0.7)\n",
    "        resultados.append(resultado)\n",
    "        \n",
    "resultados"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "resultados.count(\"sol\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Probabilidad 0.624\n"
     ]
    }
   ],
   "source": [
    "p = []\n",
    " \n",
    "for i in range(1000):\n",
    "     \n",
    "    \n",
    "    N = 10\n",
    "    \n",
    "    resultados =[]\n",
    "    \n",
    "    for i in range(N):\n",
    "        resultado = volado(0.63)\n",
    "        \n",
    "        resultados.append(resultado)\n",
    "        \n",
    "    n_soles = resultados.count(\"sol\")\n",
    "    p_soles = n_soles/N\n",
    "    p.append(p_soles)\n",
    " \n",
    "# probabilidad promedio\n",
    "p_soles_ = sum(p)/1000\n",
    " \n",
    "print(\"Probabilidad {:.3f}\".format(p_soles_))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. Urnas "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Una urna contiene $23$ bolas: $8$ blancas $(W)$, $6$ azúles $(B)$, and $9$ rojas $(R)$. Seleccionamos $6$ bolas al azar. Calculemos la probabilidad de los siguientes eventos:\n",
    "1. todas sean rojas.\n",
    "2. $3$ sean azules, $2$ sean blancas, and $1$ sea roja.\n",
    "3. exactamente $4$ sean blancas."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Primero, etiquetamos cada bola en la urna:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "def conc(A, B):\n",
    "\n",
    "    return {a + b \n",
    "            for a in A for b in B}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'B1',\n",
       " 'B2',\n",
       " 'B3',\n",
       " 'B4',\n",
       " 'B5',\n",
       " 'B6',\n",
       " 'R1',\n",
       " 'R2',\n",
       " 'R3',\n",
       " 'R4',\n",
       " 'R5',\n",
       " 'R6',\n",
       " 'R7',\n",
       " 'R8',\n",
       " 'R9',\n",
       " 'W1',\n",
       " 'W2',\n",
       " 'W3',\n",
       " 'W4',\n",
       " 'W5',\n",
       " 'W6',\n",
       " 'W7',\n",
       " 'W8'}"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "urna = conc('W', '12345678') | conc('B', '123456') | conc('R', '123456789') \n",
    "\n",
    "urna"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "23"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(urna)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A continuación, vamos a definir nuestro **espacio de estados**. El método `itertools.combinations(iterable, r)`:\n",
    "    \n",
    "Retorna subsecuencias de longitud $r$ con elementos del iterable de entrada.\n",
    "\n",
    "Las tuplas de combinación se emiten en orden lexicográfico según el orden de la entrada iterable. Entonces, si la entrada iterable está ordenada, las tuplas de combinación se producirán en una secuencia ordenada.\n",
    "\n",
    "Los elementos son tratados como únicos basados en su posición, no en su valor. De esta manera, si los elementos de entrada son únicos, no habrá valores repetidos en cada combinación"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "import itertools\n",
    "\n",
    "def comb(items, n):\n",
    "\n",
    "    return {' '.join(combo) \n",
    "            for combo in itertools.combinations(items, n)}"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Seleccionamos $6$ bolas de la urna:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "Omega = comb(urna, 6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100947"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(Omega)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Solución a 1."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Fraction(4, 4807)"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "R6 = {s for s in Omega if s.count('R') == 6}\n",
    "\n",
    "P(R6)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Solución a 2."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Fraction(240, 4807)"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "B3W2R1 = {s for s in Omega if\n",
    "          s.count('B') == 3 and s.count('W') == 2 and s.count('R') == 1}\n",
    "\n",
    "P(B3W2R1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Solución a 3."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Fraction(350, 4807)"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "W4 = {s for s in Omega if\n",
    "      s.count('W') == 4}\n",
    "\n",
    "P(W4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Se tienen $2$ urnas, cada una de las cuales contiene $10$ bolas numeradas del $1$ al $10$. Un experimento\n",
    "aleatorio consiste en seleccionar al azar una bola de cada urna. Calcula la probabilidad de que los números de las dos bolas seleccionadas difieran por $2$ o más.\n",
    "\n",
    "<p style=\"color:red;\">Solución. \n",
    "    \n",
    " Se tiene que el espacio muestral asociado al experimento aleatorio es $\\Omega=\\{1,2,\\dots,10\\}\\times \\{1,2,\\dots,10\\}$. La forma de visualizar a $\\Omega$ es por medio del siguiente arreglo:\n",
    "$$\\Omega=\\left(\\begin{array}{ccccc}\n",
    "(1,1) & (1,2) & \\cdots & (1,10) \\\\\n",
    "(2,1) & (2,2) & \\cdots & (2,10) \\\\\n",
    "\\vdots & \\vdots & \\ddots  & \\vdots \\\\\n",
    "(9,1) & (9,2) & \\cdots & (9,10) \\\\\n",
    "(10,1) & (10,2) & \\cdots & (10,10) \\end{array} \\right).$$ \n",
    "    \n",
    "Se observa que $|\\Omega|=100$. \n",
    "\n",
    "Considere el siguiente evento:\n",
    "\n",
    "$A:$ el evento \"el número de las bolas seleccionadas difiere por $2$ o más\". \n",
    "\n",
    "Entonces, el conjunto asociado al evento $A$ es:\n",
    "$$A=\\{(i,j)\\in \\Omega \\ | \\ |i-j|\\geq 2\\}.$$\n",
    " \n",
    "Para $k\\in \\{1,2,\\dots, 8\\}$ fijo, denotemos también por $A^{k}$ al evento de $A$ dado por:\n",
    "\n",
    "$$A^{k}=\\{j\\in \\{1,\\dots, 10\\} \\ | \\ j-k\\geq 2 \\}.$$\n",
    "\n",
    "Entonces, \n",
    "\\begin{align*}\n",
    "A^{1}&=\\{(1,3),(1,4), (1,5), (1,6), (1,7), (1,8), (1,9), (1,10)\\}\\\\\n",
    "A^{2}&=\\{(2,4), (2,5), (2,6), (2,7), (2,8), (2,9), (2,10)\\}\\\\\n",
    "A^{3}&=\\{(3,5), (3,6), (3,7), (3,8), (3,9), (3,10)\\}\\\\\n",
    "A^{4}&=\\{(4,6), (4,7), (4,8), (4,9), (4,10)\\}\\\\\n",
    "A^{5}&=\\{(5,7), (5,8), (5,9), (5,10)\\}\\\\\n",
    "A^{6}&=\\{(6,8), (6,9), (6,10)\\}\\\\\n",
    "A^{7}&=\\{(7,9), (7,10)\\}\\\\\n",
    "A^{8}&=\\{(8,10)\\}\\\\\n",
    "\\end{align*} \n",
    "\n",
    "Para $\\ell\\in \\{3,\\dots, 10\\}$ fijo, denotemos también por $A_{\\ell}$ al evento de $A$ dado por:\n",
    "\n",
    "$$A_{\\ell}=\\{i\\in \\{1,\\dots, 10\\} \\ | \\ \\ell-i\\geq 2 \\}.$$\n",
    "\n",
    "Entonces, \n",
    "\\begin{align*}\n",
    "A_{3}&=\\{(3,1)\\}\\\\\n",
    "A_{4}&=\\{(4,1), (4,2)\\}\\\\\n",
    "A_{5}&=\\{(5,1), (5,2), (5,3)\\}\\\\\n",
    "A_{6}&=\\{(6,1), (6,2), (6,3), (6,4)\\}\\\\\n",
    "A_{7}&=\\{(7,1), (7,2), (7,3), (7,4), (7,5)\\}\\\\\n",
    "A_{8}&=\\{(8,1), (8,2), (8,3), (8,4), (8,5), (8,6)\\}\\\\\n",
    "A_{9}&=\\{(9,1), (9,2), (9,3), (9,4), (9,5), (9,6), (9,7)\\}\\\\\n",
    "A_{10}&=\\{(10,1), (10,2), (10,3), (10,4), (10,5), (10,6), (10,7), (10,8)\\}\\\n",
    "\\end{align*} \n",
    "\n",
    "Note la siguiente igualdad:\n",
    "$$A=\\bigcup_{k=1}^{8}A^{k}\\cup \\bigcup_{\\ell=3}^{10}A_{\\ell}.$$\n",
    "\n",
    "Observe también lo siguiente:\n",
    "\\begin{align*}\n",
    "\\#A^{1}&=\\#A_{10}=8\\\\\n",
    "\\#A^{2}&=\\#A_{9}=7\\\\\n",
    "\\#A^{3}&=\\#A_{8}=6\\\\\n",
    "\\#A^{4}&=\\#A_{7}=5\\\\\n",
    "\\#A^{5}&=\\#A_{6}=4\\\\\n",
    "\\#A^{6}&=\\#A_{5}=3\\\\\n",
    "\\#A^{7}&=\\#A_{4}=2\\\\\n",
    "\\#A^{8}&=\\#A_{3}=1.\n",
    "\\end{align*}\n",
    "\n",
    "De esta forma, \n",
    "\\begin{align*} \n",
    "\\#A&=\\sum_{k=1}^{8}\\#A^{k}+\\sum_{\\ell=3}^{10}\\#A_{\\ell}\\\\\n",
    "&=8+7+6+5+4+3+2+1+1+2+3+4+5+6+7+8\\\\\n",
    "&=2\\left(\\frac{8\\times 9}{2}\\right)\\\\\n",
    "&=72.\n",
    "\\end{align*} \n",
    "\n",
    "Finalmente, ya que estamos en un espacio de probabilidad de Laplace,\n",
    "$$\\mathbb{P}(A)=\\frac{\\#A}{\\#\\Omega}=\\frac{72}{100}.$$\n",
    "\n",
    "Una solución del problema que resulta ser más eficaz es usando la propiedad de que, en cualquier espacio de probabilidad (en nuestra situación nos encontramos en un espacio de Laplace), se cumple\n",
    "$$\\mathbb{P}(A^{c})=1-\\mathbb{P}(A).$$\n",
    "\n",
    "Aquí, el evento \"no sucede A\", como conjunto, tiene la forma\n",
    "$$A^{c}=\\{(i,j)\\in \\Omega \\ | \\ |i-j|\\leq 1 \\}.$$\n",
    "En este caso,\n",
    "$$A^{c}=\\bigcup_{i=1}^{10}\\{(i,i)\\}\\cup \\bigcup_{i=1}^{9}\\left(\\{(i,i+1) \\}\\cup \\{(i+1,i)\\}\\right).$$\n",
    "Por lo tanto, \n",
    "$$\\#A^{c}=10+9+9=28,$$\n",
    "y\n",
    "$$\\mathbb{P}(A^{c})=1-\\frac{28}{100}=\\frac{72}{100}.$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from itertools import product\n",
    "\n",
    "Omega = set(product([i for i in range(1,11)], repeat=2))\n",
    "\n",
    "len(Omega)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Fraction(18, 25)"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A = {(i, j) for i,j in Omega if abs(i-j)>=2}\n",
    "\n",
    "P(A)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
