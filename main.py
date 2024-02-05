import os
from pytube import YouTube

# Função para baixar o vídeo
def baixar_video(url, caminho_destino='C:\Matheus\\videos'):
    # Criar um objeto Youtube
    try:
        yt = YouTube(url)
    except:
        print("Vídeo não encontrado")
        return 0
    
    # Obter a melhor stream disponível 
    video_stream = yt.streams.get_highest_resolution()
    
    # Criar o diretório de destino se não existir
    if not os.path.exists(caminho_destino):
        os.makedirs(caminho_destino)
        
    # Baixar o vídeo
    print('Baixando {}...'.format(yt.title))
    video_stream.download(caminho_destino)
    print('Download concluído')
    
print("Bem-vindo ao instalador de vídeos do Youtube")
while True:
    # Obter a URL do vídeo
    url = input('Digite a URL do vídeo: ')
    baixar_video(url)
    
    continuar = input("Pressione 'S' para sair ou qualquer outra tecla para continuar.")
    if continuar.lower() == 's':
        break