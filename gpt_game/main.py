import pygame

# ゲーム設定
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 50  # 主人公とブロックのサイズを統一
FPS = 60

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# オブジェクトの基本クラス
class GameObject:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

# 主人公クラス
class Player(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, TILE_SIZE, TILE_SIZE, BLACK)
        self.speed = 5
        self.velocity_y = 0
        self.gravity = 1
        self.jump_power = -15
        self.on_ground = False

    def move(self, keys, tiles):
        # 横移動
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.check_horizontal_collision(tiles, -1)
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.check_horizontal_collision(tiles, 1)

        # ジャンプ
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_power

    def apply_gravity(self, tiles):
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # 縦方向の衝突判定
        self.on_ground = False
        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                if isinstance(tile, Slope):
                    # 坂道処理
                    self.adjust_to_slope(tile)
                    self.on_ground = True
                elif self.velocity_y > 0:  # 落下中
                    self.rect.bottom = tile.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                elif self.velocity_y < 0:  # 上昇中
                    self.rect.top = tile.rect.bottom
                    self.velocity_y = 0

    def check_horizontal_collision(self, tiles, direction):
        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                if isinstance(tile, Slope):
                    continue  # 坂道では横方向の衝突を無視
                if direction == -1:  # 左移動中
                    self.rect.left = tile.rect.right
                elif direction == 1:  # 右移動中
                    self.rect.right = tile.rect.left
    # Playerクラスの坂道処理を改良
    def adjust_to_slope(self, slope):
        """坂道に乗った際の位置調整"""
        slope_width = slope.rect.width
        if slope.direction == "left":
            # 坂道の左側が高い場合
            relative_x = self.rect.centerx - slope.rect.left
            height = slope.rect.height - (relative_x * slope.rect.height / slope_width)
            self.rect.bottom = slope.rect.top + height
        elif slope.direction == "right":
            # 坂道の右側が高い場合
            relative_x = self.rect.centerx - slope.rect.left
            height = relative_x * slope.rect.height / slope_width
            self.rect.bottom = slope.rect.top + height

        self.velocity_y = 0
        self.on_ground = True


# ブロッククラス
class Block(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, TILE_SIZE, TILE_SIZE, BLUE)

# 坂道クラス
class Slope(GameObject):
    def __init__(self, x, y, direction):
        super().__init__(x, y, TILE_SIZE, TILE_SIZE, GREEN)
        self.direction = direction  # "left" または "right"

    def draw(self, screen):
        # 坂道の描画
        if self.direction == "left":
            pygame.draw.polygon(screen, self.color, [
                (self.rect.left, self.rect.bottom), 
                (self.rect.right, self.rect.bottom), 
                (self.rect.left, self.rect.top)
            ])
        elif self.direction == "right":
            pygame.draw.polygon(screen, self.color, [
                (self.rect.left, self.rect.bottom), 
                (self.rect.right, self.rect.bottom), 
                (self.rect.right, self.rect.top)
            ])

# ゲーム本体クラス
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("坂道付きアクションゲーム")
        self.clock = pygame.time.Clock()
        self.running = True

        # マップの定義（1がブロック、2が左上が高い坂道、3が右上が高い坂道）
        self.map_data = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 3, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

        # オブジェクトの初期化
        self.player = Player(100, 100)
        self.blocks = self.create_blocks()

    def create_blocks(self):
        blocks = []
        for row_index, row in enumerate(self.map_data):
            for col_index, tile in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if tile == 1:
                    blocks.append(Block(x, y))
                elif tile == 2:
                    blocks.append(Slope(x, y, "left"))
                elif tile == 3:
                    blocks.append(Slope(x, y, "right"))
        return blocks

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.move(keys, self.blocks)
        self.player.apply_gravity(self.blocks)

    def draw(self):
        self.screen.fill(WHITE)
        for block in self.blocks:
            block.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()

# ゲームを開始
if __name__ == "__main__":
    game = Game()
    game.run()
