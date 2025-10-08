# empresa1 = [1000,6000,1200,8000,1400]

# empresa2 = [5000,4000,3000,2000,7000]

# empresa3 = [1200,1300,8000,3000,15000]

# empresa4 = [1400,1750,2000,4500,5900]
import meu_modulo

def empresas():
    print('Salários dos empregos')
    dados =  {}


    quantidade = int(input('Quantidade de empresas = 4'))
    for n in range (quantidade):
        nome = input('empresa: ')
        dados[nome] = []
        empresa1 = print(1000,6000,1200,8000,1400)
        empresa2 = print(5000,4000,3000,2000,7000)
        empresa3 = print(1200,1300,8000,3000,15000)
        empresa4 = print(1400,1750,2000,4500,5900)
        dados[nome].extend([empresa1,empresa2,empresa3,empresa4])
        print(dados)
        print('veja a estatística: ')
        verificar_empresa = input('Digite o nome da empresa: ')

        media = meu_modulo.media_notas(dados[verificar_empresa])
        print('Média empresa', verificar_empresa, '-', media)
        moda = meu_modulo.moda_notas(dados[verificar_empresa])
        print('Moda empresa', verificar_empresa,'-', moda)
        desvio = meu_modulo.desvio_notas(dados[verificar_empresa])
        print('Desvio padrão empresa', verificar_empresa,'-', desvio)
        mediana = meu_modulo.mediana_nota(dados[verificar_empresa])
        print('Mediana empresa', verificar_empresa,'-',mediana)

empresas()
