class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 子弹设置
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 100

        # 外星人设置
        self.fleet_drop_speed = 10

        # 飞船设置  
        self.ship_limit = 3

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 20
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 5

        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

        # 记分
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
