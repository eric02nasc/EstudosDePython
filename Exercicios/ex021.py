import playsound
r = str(input('Quer escutar musica sim ou não? '))

if(r == 'sim' or 'quero' or 'com certeza'):
    playsound.playsound('musica.mp3')
else: print('tudo bem então, até logo!')



