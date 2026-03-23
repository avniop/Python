import random
import pygame


class button:
    def __init__(self,x,y,pos,width,height):
        self.x = x
        self.y = y
        self.pos = pos
        self.width = width
        self.height = height


    def clicked(self,pos):
        self.pos = pygame.mouse.get_pos()
        if self.pos[0] > self.x and self.pos[0] < self.x + self.width:
            if self.pos[1] > self.y and self.pos[1] < self.y + self.height:
                return True
        return False
class RpsGame:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((960, 640))
        pygame.display.set_caption("Rock Paper Scissor Game")

        self.bg = pygame.image.load("bg.jpg")
        self.r_btn = pygame.image.load("r_button.png").convert_alpha()
        self.p_btn = pygame.image.load("p_button.png").convert_alpha()
        self.s_btn = pygame.image.load("s_button.png").convert_alpha()

        self.choose_rock = pygame.image.load("rock.png").convert_alpha()
        self.choose_paper = pygame.image.load("paper.png").convert_alpha()
        self.choose_scissor = pygame.image.load("scissor.png").convert_alpha()

        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.r_btn, (20, 500))
        self.screen.blit(self.p_btn, (330, 500))
        self.screen.blit(self.s_btn, (640, 500))

        self.rock_btn = button(30,520,(30,520),300,140)
        self.paper_btn = button(340,520,(340,520),300,140)
        self.scissor_btn = button(640,520,(640,520),300,140)

        self.font = pygame.font.Font(('Splatch.ttf'), 90)
        self.text = self.font.render(f"", True, (255, 255, 255))

        self.pl_score = 0
        self.pc_score = 0

    def player(self):
        if self.rock_btn.clicked(30):
            self.p_option = "rock"
            self.screen.blit(self.choose_rock, (120, 200))
        elif self.paper_btn.clicked(340):
            self.p_option = "paper"
            self.screen.blit(self.choose_paper, (120, 200))
        else:
            self.scissor_btn.clicked(640)
            self.screen.blit(self.choose_scissor, (120, 200))

        return self.p_option
    
    def computer(self):
        self.pc_random_choice = " "
        options = ["rock", "paper", "scissor"]
        pc_choice = random.choice(options)
        if pc_choice == "rock":
            self.pc_random_choice = "rock"
            pc_choice = self.choose_rock
            
        elif pc_choice == "paper":
            self.pc_random_choice = "paper"
            pc_choice = self.choose_paper
        else:
            self.pc_random_choice = "scissor"
            pc_choice = self.choose_paper
        pc_option = self.screen.blit(pc_choice, (600, 200))
        return pc_option
    def pl_score_cache(self):
        self.pl_score = 0
        self.pc_score = 0

        pl = self.p_option
        pc = self.pc_random_choice

        if pc == "rock" and pl == "paper" or pl == "" and pc == "scissor" or pl == "rock" and pc == "scissor":
            self.pc_score += 1
        elif pl == pc:
            pass
        else:
            self.pl_score += 1
        return self.pl_score
    
    def pc_score_cache(self):
        self.pl_score = 0
        self.pc_score = 0

        pl = self.p_option
        pc = self.pc_random_choice

        if pc == "rock" and pl == "paper" or pl == "" and pc == "scissor" or pl == "rock" and pc == "scissor":
            self.pc_score += 1
        elif pl == pc:
            pass
        else:
            self.pl_score += 1
        return self.pc_score
    def image_reset(self):
        self.screen.blit(self.text, (330, 0))
        self.text = self.font.render(f"", True, (0, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.r_btn, (20, 500))
        self.screen.blit(self.p_btn, (330, 500))
        self.screen.blit(self.s_btn, (640, 500))
        pass
    def game_loop(self):
        run = True
        clock = pygame.time.Clock()
        rpsGame = RpsGame()

        while run:
            pygame.display.update()
            self.screen.blit(self.text, (330, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rock_btn.clicked(30) or self.paper_btn.clicked(340) or self.scissor_btn.clicked(640):
                        rpsGame.image_reset()
                        rpsGame.player()
                        rpsGame.computer()

                        self.pl_score = rpsGame.pl_score_cache()
                        self.pc_score = rpsGame.pc_score_cache()
                        self.text = self.font.render(f"{self.pl_score} : {self.pc_score}", True, (255, 255, 255))
                pygame.display.flip()
                clock.tick(30)

        pygame.quit()
if __name__ == "__main__":
    rpsGame = RpsGame()
    rpsGame.game_loop()
                        
