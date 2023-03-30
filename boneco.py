import pygame

# Inicializa o Pygame
pygame.init()

# Define as dimensões da janela
window_width = 640
window_height = 480

# Cria uma janela
screen = pygame.display.set_mode((window_width, window_height))

# Define a cor de fundo da janela
background_color = (255, 255, 255)

# Carrega a imagem do boneco
image_path = "boneco.png"
boneco = pygame.image.load(image_path)

# Define as coordenadas iniciais do boneco
boneco_x = window_width / 2
boneco_y = window_height / 2

# Loop principal do jogo
while True:
    # Processa os eventos da fila de eventos do Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Sai do jogo quando o usuário fecha a janela
            pygame.quit()
            exit()

    # Preenche a janela com a cor de fundo
    screen.fill(background_color)

    # Desenha o boneco na tela
    screen.blit(boneco, (boneco_x, boneco_y))

    # Atualiza a janela
    pygame.display.update()
