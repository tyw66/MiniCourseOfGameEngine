'''
三态按钮带回调
'''
import sys
import pygame   

class SimpleButton:
    def __init__(self, rect, text, color, callback=None):
        self.rect = rect
        self.text = text
        self._color = color  # 存储初始颜色
        self.font = pygame.font.Font(None, 36)
        self.text_surface = self.font.render(self.text, True, (255, 255, 0))
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        self.callback = callback

    @property
    def hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    @property
    def pressed(self):
        return self.hovered and pygame.mouse.get_pressed()[0]

    @property
    def color(self):
        return (255,100,100) if self.pressed else \
                (100,100,255) if self.hovered else self._color

    def check_click(self, event): 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.callback:
                    self.callback()
                return True
        return False


WINDOW_SIZE = (640, 480)    # 窗口大小

def handle_input():
    #取出事件队列中的事件并处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        button.check_click(event) 
        
def update():
    pass

def render():
    # 清屏
    screen.fill((153, 204, 255))
    # 在后台缓冲区绘制按钮矩形
    pygame.draw.rect(screen, button.color, button.rect)
    # 绘制按钮文本
    screen.blit(button.text_surface, button.text_rect)   
    # 更新显示，即完整切换缓冲区到前台显示
    pygame.display.flip()

if __name__ == "__main__":  
    # 初始化 Pygame
    pygame.init()
    # 创建窗口，默认是双缓冲
    screen = pygame.display.set_mode(WINDOW_SIZE) 
    # 设置窗口标题
    pygame.display.set_caption("Lesson04 - Simple Button Class")
    # 创建时钟对象，用于控制帧率
    clock = pygame.time.Clock()
    # 定义回调函数
    def print_callback():
        print("Button clicked!")
    # 创建按钮
    button = SimpleButton(pygame.Rect(100,100,160,40), "Click me!", (128, 128, 255), callback=print_callback)
    # 游戏主循环
    while True:
        # 处理输入
        handle_input()
        # 更新场景状态
        update()
        # 渲染场景
        render()
        # 控制帧率
        clock.tick(60)
    