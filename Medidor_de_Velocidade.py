velocidade_maxima = 80

velocidade = int(input('Digite a Velocidade: '))

if(velocidade <= velocidade_maxima):
    print('Não houve multa')
elif((velocidade > velocidade_maxima) and (velocidade <= velocidade_maxima+10)):
    print('Levou multa leve')
elif((velocidade >= velocidade_maxima+11) and (velocidade <= velocidade_maxima +20)):
    print('Levou multa grave')    
elif(velocidade >= velocidade_maxima+21):
    print('Levou multa gravíssima')

