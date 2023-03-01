import glob
import os
import random
import time

import pygame
from pygame.locals import *
import sys
from utils import global_path

# //////////////////////////////////////////////////////////////////////////////
pygame.init()
global_path.set_proj_abs_path(os.path.abspath(__file__))
icon = pygame.image.load(global_path.get_proj_abs_path(path="assets/icon.png"))
pygame.display.set_icon(icon)
flags = DOUBLEBUF | FULLSCREEN
screenx, screeny = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((screenx, screeny), flags)
screenx, screeny = screen.get_size()
pygame.display.set_caption("EOS_Knucklebones")
clock = pygame.time.Clock()

shissdo_png = pygame.image.load(
    global_path.get_proj_abs_path("assets/shissdo.png")
).convert_alpha()
shissdo_png = pygame.transform.smoothscale(shissdo_png, (screenx, screeny))

Font = pygame.font.Font(
    global_path.get_proj_abs_path("assets/Uni Sans Heavy.otf"), int(screeny / 5)
)
smallFont = pygame.font.Font(
    global_path.get_proj_abs_path("assets/Uni Sans Heavy.otf"), int(screeny / 7)
)

# //////////////////////////////////////////////////////////////////////////////

player_selection = 0
bot_selection = 0
mainLoop = True
start_time = pygame.time.get_ticks()
turn = True
player_score = 0
bot_score = 0
player_array = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
bot_array = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
# //////////////////////////////////////////////////////////////////////////////
dice_num = random.randint(1, 6)
player_zero_num = 0
bot_zero_num = 0
game_done = False
while mainLoop:
    events = pygame.event.get()
    if events:
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                mainLoop = False
            if (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_RIGHT
                and not game_done
            ):
                if player_selection < 8:
                    player_selection += 1
            if (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_LEFT
                and not game_done
            ):
                if player_selection > 0:
                    player_selection -= 1
            if (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE
                and not game_done
            ):
                if turn:
                    if player_array[player_selection].count(0) != 0:
                        player_array[player_selection][
                            player_array[player_selection].count(0) - 1
                        ] = dice_num
                        turn = False

                        if bot_array[player_selection].count(dice_num) > 0:
                            for g in range(0, 3):
                                if bot_array[player_selection][g] == dice_num:
                                    bot_array[player_selection][g] = 0
                        dice_num = random.randint(1, 6)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                if game_done:
                    turn = True
                    player_score = 0
                    bot_score = 0
                    player_array = [
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                    ]
                    bot_array = [
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                    ]
                    dice_num = random.randint(1, 6)
                    player_zero_num = 0
                    bot_zero_num = 0
                    game_done = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.MOUSEWHEEL:
                pass

    if not turn:
        hard = []
        for i in range(len(player_array)):
            for j in range(len(player_array[i])):
                hard.append(player_array[i][j])

        k_x_X = random.randrange(0, 100)
        if k_x_X > 100 * (1 - 1 / (hard.count(0)+1)):
            dice_num = max(hard)

        print("bot turn")
        TEMP_XXXX = []
        TEMP_BOT_XXXX = []
        for i in range(len(player_array)):
            cccccccc = 0
            for j in range(len(player_array[i])):
                if player_array[i][j] == dice_num:
                    cccccccc += 1
            TEMP_XXXX.append(cccccccc)

            cccccccc = 0
            for j in range(len(bot_array[i])):
                if bot_array[i][j] == dice_num:
                    cccccccc += 1
            TEMP_BOT_XXXX.append(cccccccc)

        if TEMP_XXXX.count(0) == 9:
            if max(TEMP_BOT_XXXX) == 0:
                kkkkkkk = random.randint(0, 9)
            else:
                kkkkkkk = TEMP_BOT_XXXX.index(max(TEMP_BOT_XXXX))
            bot_selection = kkkkkkk
        else:
            kkkkkkk = TEMP_XXXX.index(max(TEMP_XXXX))
            bot_selection = kkkkkkk

        while True:
            print(kkkkkkk, "loop")
            if kkkkkkk > 8:
                kkkkkkk -= 1
            if bot_array[kkkkkkk].count(0) == 0:
                if kkkkkkk < 8:
                    kkkkkkk += 1
                else:
                    kkkkkkk -= 8
            else:
                break
        bot_selection = kkkkkkk

        if bot_array[bot_selection].count(0) != 0:
            bot_array[bot_selection][bot_array[bot_selection].count(0) - 1] = dice_num
            turn = True
            if player_array[bot_selection].count(dice_num) > 0:
                for g in range(0, 3):
                    if player_array[bot_selection][g] == dice_num:
                        player_array[bot_selection][g] = 0
            dice_num = random.randint(1, 6)
        turn = True

    dt = clock.tick(60)

    if pygame.time.get_ticks() - start_time < 3000:
        screen.blit(shissdo_png, (0, 0))
    else:

        screen.fill((255, 255, 255))

        turn_box = pygame.Surface((screenx, screeny / 2))
        turn_box.fill((43, 45, 66))
        if turn:
            screen.blit(turn_box, (0, screeny / 2))
        else:
            screen.blit(turn_box, (0, 0))

        dice_location_bar = pygame.Surface((screenx / 16, screeny / 9))
        dice_location_bar.fill((0, 0, 0))

        player_selection_bar = pygame.Surface(
            (screenx / 16 + screenx / 48, screeny / 2)
        )
        player_selection_bar.fill((239, 35, 60))

        bot_location_bar = pygame.Surface((screenx / 16 + screenx / 48, screeny / 2))
        bot_location_bar.fill((67, 97, 238))

        not_select_bar = pygame.Surface((screenx / 16 + screenx / 48, screeny / 2))
        not_select_bar.fill((128, 237, 153))

        if player_array[player_selection].count(0) != 0:
            screen.blit(
                player_selection_bar,
                (
                    (
                        player_selection * screenx / 16
                        + (player_selection + 1) * (screenx / 32 - screenx / 96)
                    ),
                    screeny / 2,
                ),
            )
        else:
            screen.blit(
                not_select_bar,
                (
                    (
                        player_selection * screenx / 16
                        + (player_selection + 1) * (screenx / 32 - screenx / 96)
                    ),
                    screeny / 2,
                ),
            )
        if turn:
            screen.blit(
                bot_location_bar,
                (
                    (
                        bot_selection * screenx / 16
                        + (bot_selection + 1) * (screenx / 32 - screenx / 96)
                    ),
                    0,
                ),
            )

        if dice_num == 1:
            diceimage = smallFont.render("1", True, (0, 0, 0))
        elif dice_num == 2:
            diceimage = smallFont.render("2", True, (0, 0, 0))
        elif dice_num == 3:
            diceimage = smallFont.render("3", True, (0, 0, 0))
        elif dice_num == 4:
            diceimage = smallFont.render("4", True, (0, 0, 0))
        elif dice_num == 5:
            diceimage = smallFont.render("5", True, (0, 0, 0))
        else:
            diceimage = smallFont.render("6", True, (0, 0, 0))

        if turn:
            screen.blit(
                diceimage,
                (
                    (
                        1 * screenx / 96
                        + player_selection * screenx / 16
                        + (player_selection + 1) * (screenx / 32 - screenx / 96)
                    ),
                    screeny / 2
                    + screeny / 32
                    + (3 - player_array[player_selection].count(0))
                    * (screeny / 18 + screeny / 9),
                ),
            )
        else:
            screen.blit(
                diceimage,
                (
                    (
                        1 * screenx / 96
                        + bot_selection * screenx / 16
                        + (bot_selection + 1) * (screenx / 32 - screenx / 96)
                    ),
                    screeny / 2
                    + screeny / 32
                    - (4 - bot_array[bot_selection].count(0))
                    * (screeny / 18 + screeny / 9),
                ),
            )

        # player side fixed
        for i in range(0, 9):
            for j in range(0, 3):
                num = player_array[i][j]
                if num == 1:
                    diceimage_fixed = smallFont.render("1", True, (0, 0, 0))
                elif num == 2:
                    diceimage_fixed = smallFont.render("2", True, (0, 0, 0))
                elif num == 3:
                    diceimage_fixed = smallFont.render("3", True, (0, 0, 0))
                elif num == 4:
                    diceimage_fixed = smallFont.render("4", True, (0, 0, 0))
                elif num == 5:
                    diceimage_fixed = smallFont.render("5", True, (0, 0, 0))
                else:
                    diceimage_fixed = smallFont.render("6", True, (0, 0, 0))

                if num != 0:
                    screen.blit(
                        diceimage_fixed,
                        (
                            1 * screenx / 96
                            + i * screenx / 16
                            + (i + 1) * (screenx / 32 - screenx / 96),
                            screeny / 2
                            + screeny / 32
                            + (2 - j) * (screeny / 18 + screeny / 9),
                        ),
                    )

        # bot side fixed
        for i in range(0, 9):
            for j in range(0, 3):
                num = bot_array[i][j]
                if num == 1:
                    diceimage_fixed = smallFont.render("1", True, (0, 0, 0))
                elif num == 2:
                    diceimage_fixed = smallFont.render("2", True, (0, 0, 0))
                elif num == 3:
                    diceimage_fixed = smallFont.render("3", True, (0, 0, 0))
                elif num == 4:
                    diceimage_fixed = smallFont.render("4", True, (0, 0, 0))
                elif num == 5:
                    diceimage_fixed = smallFont.render("5", True, (0, 0, 0))
                else:
                    diceimage_fixed = smallFont.render("6", True, (0, 0, 0))
                if num != 0:
                    screen.blit(
                        diceimage_fixed,
                        (
                            1 * screenx / 96
                            + i * screenx / 16
                            + (i + 1) * (screenx / 32 - screenx / 96),
                            screeny / 2
                            + screeny / 32
                            - (3 - j) * (screeny / 18 + screeny / 9),
                        ),
                    )

        center_line = pygame.Surface((screenx, screeny / 156))
        center_line.fill((255, 159, 28))

        center_vertical_line = pygame.Surface((screeny / 156, screeny))
        center_vertical_line.fill((255, 159, 28))

        right_fill_line = pygame.Surface(
            (
                screenx - (9 * screenx / 16 + 10 * (screenx / 32 - screenx / 96)),
                screeny,
            )
        )
        right_fill_line.fill((37, 36, 34))

        screen.blit(
            right_fill_line,
            ((9 * screenx / 16 + 10 * (screenx / 32 - screenx / 96)), 0),
        )
        screen.blit(
            center_vertical_line,
            (9 * screenx / 16 + 10 * (screenx / 32 - screenx / 96), 0),
        )
        screen.blit(center_line, (0, screeny / 2))

        Bot_sc = Font.render(str(bot_score), True, (255, 255, 255))
        screen.blit(
            Bot_sc,
            (
                9 * screenx / 16
                + 10 * (screenx / 32 - screenx / 96)
                + (screenx - (9 * screenx / 16 + 10 * (screenx / 32 - screenx / 96)))
                / 2
                - Bot_sc.get_width() / 2,
                screeny / 8,
            ),
        )

        Player_sc = Font.render(str(player_score), True, (255, 255, 255))
        screen.blit(
            Player_sc,
            (
                9 * screenx / 16
                + 10 * (screenx / 32 - screenx / 96)
                + (screenx - (9 * screenx / 16 + 10 * (screenx / 32 - screenx / 96)))
                / 2
                - Player_sc.get_width() / 2,
                screeny - Player_sc.get_height() - screeny / 10,
            ),
        )
    player_score = 0
    bot_score = 0

    for i in range(0, 9):
        ccc = player_array[i]
        ddd = bot_array[i]

        ccc_set = set(ccc)
        ddd_set = set(ddd)

        if len(ccc_set) == 2:
            if ccc.count(list(ccc_set)[0]) == 2:
                player_score += 4 * list(ccc_set)[0]
                player_score += list(ccc_set)[1]
            else:
                player_score += 4 * list(ccc_set)[1]
                player_score += list(ccc_set)[0]
        elif len(ccc_set) == 1:
            player_score += 3 * sum(ccc)

        if len(ddd_set) == 2:
            if ddd.count(list(ddd_set)[0]) == 2:
                bot_score += 4 * list(ddd_set)[0]
                bot_score += list(ddd_set)[1]
            else:
                bot_score += 4 * list(ddd_set)[1]
                bot_score += list(ddd_set)[0]

        elif len(ddd_set) == 1:
            bot_score += 3 * sum(ddd)

        if len(ccc_set) == 3:
            player_score += sum(ccc)
        if len(ddd_set) == 3:
            bot_score += sum(ddd)

    # 점수 판정
    player_zero_num = 0
    bot_zero_num = 0
    for i in range(0, 9):
        for j in range(0, 3):
            if player_array[i][j] != 0:
                player_zero_num += 1
            if bot_array[i][j] != 0:
                bot_zero_num += 1

    if player_zero_num == 27 or bot_zero_num == 27:
        screen.fill((255, 255, 255))
        restart_message = smallFont.render(f"Press R to restart", True, (0, 0, 0))
        if player_score > bot_score:
            win_message = Font.render(
                f"You win {player_score} > {bot_score}", True, (0, 0, 0)
            )
            screen.blit(
                win_message,
                (
                    screenx / 2 - win_message.get_width() / 2,
                    screeny / 2 - win_message.get_height() / 2,
                ),
            )
            screen.blit(
                restart_message,
                (
                    screenx / 2 - restart_message.get_width() / 2,
                    screeny / 2
                    - restart_message.get_height() / 2
                    + win_message.get_height()
                    + screeny / 18,
                ),
            )
        elif player_score == bot_score:
            win_message = Font.render(
                f"Tie {player_score} > {bot_score}", True, (0, 0, 0)
            )
            screen.blit(
                win_message,
                (
                    screenx / 2 - win_message.get_width() / 2,
                    screeny / 2 - win_message.get_height() / 2,
                ),
            )
            screen.blit(
                restart_message,
                (
                    screenx / 2 - restart_message.get_width() / 2,
                    screeny / 2
                    - restart_message.get_height() / 2
                    + win_message.get_height()
                    + screeny / 18,
                ),
            )
        else:
            win_message = Font.render(
                f"You lose {player_score} < {bot_score}", True, (0, 0, 0)
            )
            screen.blit(
                win_message,
                (
                    screenx / 2 - win_message.get_width() / 2,
                    screeny / 2 - win_message.get_height() / 2,
                ),
            )
            screen.blit(
                restart_message,
                (
                    screenx / 2 - restart_message.get_width() / 2,
                    screeny / 2
                    - restart_message.get_height() / 2
                    + win_message.get_height()
                    + screeny / 18,
                ),
            )
        game_done = True

    for i in range(0, 9):
        player_array[i].sort()
        bot_array[i].sort()
    pygame.display.flip()
    # print(clock.get_fps())
# //////////////////////////////////////////////////////////////////////////////
pygame.quit()
sys.exit()
