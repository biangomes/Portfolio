from Projeto1 import Calculadora                    # importando o modulo Operacoes
import pyinputplus as pyip                          # importando pyinputplus p/ formatar as entradas

print("CALCULADORA EM PYTHON USANDO POO")

n1 = pyip.inputFloat("n1 = ")                       # solicitando o primeiro numero
n2 = pyip.inputFloat("n2 = ")                       # solicitando o segundo numero

print("1 Soma\n"
      "2 Subtracao\n"
      "3 Multiplicacao\n"
      "4 Divisao")

op = pyip.inputInt("")                              # escolhendo a operacao feita

calcula = Calculadora.Operacoes(n1, n2)             # instancia da Calculadora

if op == 1:                                         # operacao de soma
    resultado = calcula.soma(n1, n2)
    print("Resultado:\n")
    print("{} + {} = {}".format(n1, n2, resultado))
elif op == 2:                                       # operacao de subtracao
    resultado = calcula.subtracao(n1, n2)
    print("Resultado:\n")
    print("{} - {} = {}".format(n1, n2, resultado))
elif op == 3:                                       # operacao de multiplicacao
    resultado = calcula.multiplicacao(n1, n2)
    print("Resultado:\n")
    print("{} x {} = {}".format(n1, n2, resultado))
elif op == 4:                                       # operacao de divisao
    resultado = calcula.divisao(n1, n2)
    print("Resultado:\n")
    print("{} / {} = {:.1f}".format(n1, n2, resultado))






