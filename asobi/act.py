import sys

import pygame

# 初期化
pygame.init()

# 画面サイズ
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("アクションゲーム")

# 色定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 地形マップ（0: 空白, 1: ブロック, 2: 左下から右上への坂, 3: 左上から右下への坂）
tile_size = 32
level = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1],
]

# プレイヤー設定
player_size = 32
player_color = RED
player_x, player_y = 100, 100
player_velocity_x = 0
player_velocity_y = 0
gravity = 1
jump_power = -15
is_jumping = False

# ゲームループ
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_velocity_x = -5
    elif keys[pygame.K_RIGHT]:
        player_velocity_x = 5
    else:
        player_velocity_x = 0

    if keys[pygame.K_UP] and not is_jumping:
        player_velocity_y = jump_power
        is_jumping = True

    # 重力の適用
    player_velocity_y += gravity

    # プレイヤーの位置更新
    new_player_x = player_x + player_velocity_x
    new_player_y = player_y + player_velocity_y

    # X軸の当たり判定
    player_rect = pygame.Rect(new_player_x, player_y, player_size, player_size)
    for row in range(len(level)):
        for col in range(len(level[row])):
            if level[row][col] == 1:
                tile_rect = pygame.Rect(col * tile_size, row * tile_size, tile_size, tile_size)
                if player_rect.colliderect(tile_rect):
                    if player_velocity_x > 0:  # 右移動中
                        new_player_x = tile_rect.left - player_size
                    elif player_velocity_x < 0:  # 左移動中
                        new_player_x = tile_rect.right

    # Y軸の当たり判定
    player_rect = pygame.Rect(new_player_x, new_player_y, player_size, player_size)
    on_slope = False  # 坂の上にいるかどうかのフラグ
    for row in range(len(level)):
        for col in range(len(level[row])):
            tile_type = level[row][col]
            if tile_type == 1:
                tile_rect = pygame.Rect(col * tile_size, row * tile_size, tile_size, tile_size)
                if player_rect.colliderect(tile_rect):
                    if player_velocity_y > 0:  # 落下中
                        new_player_y = tile_rect.top - player_size
                        player_velocity_y = 0
                        is_jumping = False
                    elif player_velocity_y < 0:  # ジャンプ中
                        new_player_y = tile_rect.bottom
                        player_velocity_y = 0
            elif tile_type == 2:  # 左下から右上への坂
                if row < len(level) - 1:
                    slope_y = (row + 1) * tile_size - (new_player_x - col * tile_size)
                    if new_player_y + player_size > slope_y:
                        new_player_y = slope_y - player_size
                        player_velocity_y = 0
                        is_jumping = False
                        on_slope = True  # 坂の上にいることを示すフラグをセット
            elif tile_type == 3:  # 左上から右下への坂
                if row > 0:
                    slope_y = row * tile_size + (new_player_x - col * tile_size)
                    if new_player_y + player_size > slope_y:
                        new_player_y = slope_y - player_size
                        player_velocity_y = 0
                        is_jumping = False
                        on_slope = True  # 坂の上にいることを示すフラグをセット

    player_x = new_player_x
    player_y = new_player_y

    # X軸の当たり判定
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for row in range(len(level)):
        for col in range(len(level[row])):
            tile_type = level[row][col]
            if tile_type == 1:
                tile_rect = pygame.Rect(col * tile_size, row * tile_size, tile_size, tile_size)
                if player_rect.colliderect(tile_rect):
                    if player_velocity_x > 0:  # 右移動中
                        player_x = tile_rect.left - player_size
                    elif player_velocity_x < 0:  # 左移動中
                        player_x = tile_rect.right

    # Y軸の当たり判定で坂の上にいる場合は、プレイヤーのX座標を坂の上に合わせる
    if on_slope:
        if player_velocity_x > 0:  # 右移動中
            player_x = col * tile_size
        elif player_velocity_x < 0:  # 左移動中
            player_x = (col + 1) * tile_size - player_size

    # 画面描画
    screen.fill(WHITE)
    for row in range(len(level)):
        for col in range(len(level[row])):
            tile_type = level[row][col]
            if tile_type == 1:
                pygame.draw.rect(screen, BLACK, (col * tile_size, row * tile_size, tile_size, tile_size))
            elif tile_type == 2:  # 左下から右上への坂
                if row < len(level) - 1:
                    pygame.draw.polygon(screen, GREEN, [
                        (col * tile_size, (row + 1) * tile_size),
                        ((col + 1) * tile_size, (row + 1) * tile_size),
                        ((col + 1) * tile_size, row * tile_size),
                    ])
            elif tile_type == 3:  # 左上から右下への坂
                if row > 0:
                    pygame.draw.polygon(screen, BLUE, [
                        (col * tile_size, row * tile_size),
                        ((col + 1) * tile_size, row * tile_size),
                        ((col + 1) * tile_size, (row + 1) * tile_size),
                        (col * tile_size, (row + 1) * tile_size)
                    ])
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()