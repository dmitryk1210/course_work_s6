
from letter import Letter
from key_generation import *
import timeit
import numpy as np
import matplotlib.pyplot as plt


l_a = Letter("a")
l_a1 = Letter("a", -1)
l_b = Letter("b")
l_b1 = Letter("b", -1)
l_c = Letter("c")
l_c1 = Letter("c", -1)
l_d = Letter("d")
l_d1 = Letter("d", -1)
l_e = Letter("e")
l_e1 = Letter("e", -1)
l_f = Letter("f")
l_g = Letter("g")
l_h = Letter("h")

print("COREPRESENTATION")

w_word = Word([l_a, l_b, l_c, l_d])
h_word = Word([l_a, l_c, l_a, l_d])

generated_corepresentations = []
gcr = GenerateCorepresentation(4, 3, 3, 6)
n_tests = 5
for i in range(n_tests):
    next_cr = next(gcr)
    def_relations = next_cr.GetRelators()
    print('<a, b, c, d; ', def_relations[0], ', ', def_relations[1], ', ', def_relations[2], '>')
    generated_corepresentations.append(next_cr)
"""
Генератор копредставлений
    n - количество используемых букв из группового алфавита
    l - длина слов из множества определяющих соотношений
    r - количество слов в множестве определяющих соотношений
    p - параметр условия C(p)
    yield копредставление, удовлетворяющее условиям C(p)-T(q)
"""

m_A = 1
n_A = 20
m_B = 1
n_B = 20

n_operations_k1 = 20
n_letters_k1 = 3
n_operations_k2 = 20
n_letters_k2 = 3

n_A_diff = np.arange(0, 50)
n_B_diff = np.arange(0, 50)
time_plot = np.zeros(50, dtype=float)
time_plot_divx2 = np.zeros(50, dtype=float)
for i in range(50):
    start_time = timeit.default_timer()  # замер времени
    n_tests = len(generated_corepresentations)
    for cr in generated_corepresentations:
        K1 = CreateKey(w_word, m_A, h_word, n_A_diff[i])
        K2 = CreateKey(w_word, m_B, h_word, n_B_diff[i])

        K1_h = Hide(K1, n_operations_k1, cr, n_letters_k1)
        K2_h = Hide(K2, n_operations_k2, cr, n_letters_k2)
        K_A = CreateKey(K1_h, m_B, h_word, n_B_diff[i])
        K_B = CreateKey(K2_h, m_A, h_word, n_A_diff[i])

    time_plot[i] = (timeit.default_timer() - start_time) / n_tests
    time_plot_divx2[i] = time_plot[i] / (i + 1) ** 2

fig, ax = plt.subplots()
ax.plot(n_A_diff, time_plot, linewidth=3, color='r')
ax.set_xlabel('n1, n2')
ax.set_ylabel('t, с')
ax.grid(color='blue', linewidth=1)
plt.show()

_, ax = plt.subplots()
ax.plot(n_A_diff, time_plot_divx2, linewidth=3, color='r')
ax.grid(color='blue', linewidth=1)
plt.show()

m_A_diff = np.arange(0, 50)
m_B_diff = np.arange(0, 50)
time_plot = np.zeros(50, dtype=float)
for i in range(50):
    start_time = timeit.default_timer()
    n_tests = len(generated_corepresentations)
    for cr in generated_corepresentations:
        K1 = CreateKey(w_word, m_A_diff[i], h_word, n_A)
        K2 = CreateKey(w_word, m_B_diff[i], h_word, n_B)

        K1_h = Hide(K1, n_operations_k1, cr, n_letters_k1)
        K2_h = Hide(K2, n_operations_k2, cr, n_letters_k2)
        K_A = CreateKey(K1_h, m_B_diff[i], h_word, n_B)
        K_B = CreateKey(K2_h, m_A_diff[i], h_word, n_A)

    time_plot[i] = (timeit.default_timer() - start_time) / n_tests
    time_plot_divx2[i] = time_plot[i] / (i + 1) ** 2

_, ax = plt.subplots()
ax.plot(m_A_diff, time_plot, linewidth=3, color='r')
ax.set_xlabel('m1, m2')
ax.set_ylabel('t, с')
ax.grid(color='blue', linewidth=1)
plt.show()

_, ax = plt.subplots()
ax.plot(m_A_diff, time_plot_divx2, linewidth=3, color='r')
ax.grid(color='blue', linewidth=1)
plt.show()

n_operations = np.arange(50)
time_plot = np.zeros(50, dtype=float)
for i in range(50):
    start_time = timeit.default_timer()
    print(i)
    n_tests = len(generated_corepresentations)
    for cr in generated_corepresentations:
        K1 = CreateKey(w_word, m_A, h_word, n_A)
        K2 = CreateKey(w_word, m_B, h_word, n_B)

        K1_h = Hide(K1, n_operations[i], cr, n_letters_k1)
        K2_h = Hide(K2, n_operations[i], cr, n_letters_k2)
        K_A = CreateKey(K1_h, m_B, h_word, n_B)
        K_B = CreateKey(K2_h, m_A, h_word, n_A)

    time_plot[i] = (timeit.default_timer() - start_time) / n_tests

_, ax = plt.subplots()
ax.plot(n_operations, time_plot, linewidth=3, color='r')
ax.grid(color='blue', linewidth=1)
ax.set_xlabel('количество операций при маскировке')
ax.set_ylabel('t, с')
plt.show()

