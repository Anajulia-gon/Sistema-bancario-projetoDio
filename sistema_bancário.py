# -*- coding: utf-8 -*-
"""sistema-bancario.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1apTHz4e15QME0UlWE7O6pVFmhVC4sYPT
"""

#criar um sistema bancario com saque, deposito e extrat0
#Operacao de deposito
funcao=""
extrato={"Saque1":100,"deposito1":300,"deposito2":200}
contador_deposito=2
contador_saque=0
saldo=500
nome= "Joao"
while funcao!="q":
  funcao=input(f"""
  Ola senhora(o){nome} qual operacao voce deseja realizar ? Aperte:
   s: para saque
   e: para extrato
   d: deposito
   , se quiser sair aperte q \n""")
  print(f"Ok, estamos te encaminhando para sua sessao")
  if funcao=="s":
    quantia=float(input(f"Digite aqui a quantia que gostaria de sacar"))
    if contador_saque>3:
       print("Falha na operação:voce ultrapassou o volume de saques para hoje porfavor volte amanha")
    elif quantia>500:
       print("Falha na operação:: o valor maximo dispónivel para saque e 500")
    elif quantia>saldo:
      print("Falha na operação: saldo insuficiente por favor recomece e revise a operacao")
    elif quantia>0 :
     saldo-=quantia
     contador_saque+=1
     extrato.setdefault(f"Saque {contador_saque}",quantia)
     print (f"Transação realizada com sucesso seu saldo agora é : {saldo}")
    else:
      print("Falha na operação:valor informado e invalido")

  elif funcao=="d":
   if quantia>0:
    quantia=float(input(f"Digite aqui a quantia que gostaria de depositar"))
    saldo+=quantia
    contador_deposito+=1
    extrato.setdefault(f"Deposito {contador_deposito}",quantia)
    print(f"deposito realizado saldo final:{saldo}")
   else:
    print(
    """
    Operacao falhou: valor informado e invalido
    """)
  elif funcao=="e":
      print("Extrato".center(20,"="))
      for chave,elemento in extrato.items():
        print(f'{chave} R$:{elemento}')
      print("".center(20,"-"))
      print( f"saldo final:{saldo}")
  else:
     print("Falha na operação:Voce nao digitou uma operacao inclusa em nossos serviços, tente novamente")
  funcao=input("""
  Obrigada por escolher nossos servicos!
  para realizar alguma outra operacao aperte a,
  se ja tiver acabado aperte "q"
  """)

