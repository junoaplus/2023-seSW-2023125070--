import subprocess
import platform
import os
import time
import random
from colorsys import hsv_to_rgb
import board
from digitalio import DigitalInOut, Direction
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import st7789
import threading
import signal






def play_music(music_file):
    global music_process
    system = platform.system().lower()

    if system == "darwin":
        music_process = subprocess.Popen(["afplay", music_file])
    elif system == "linux":
        music_process = subprocess.Popen(["mpg321", music_file])
    elif system == "windows":
        music_process = subprocess.Popen(["start", "wmplayer", music_file])
    else:
        print("지원되지 않는 운영 체제")

def pause_music():
    global music_process
    if music_process:
        music_process.send_signal(signal.SIGSTOP)

def resume_music():
    global music_process
    if music_process:
        music_process.send_signal(signal.SIGCONT)

def stop_music():
    global music_process
    if music_process:
        music_process.terminate()
        music_process.wait()
    
def load_korean_font(size=20):
    font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
    return ImageFont.truetype(font_path, size)

def load_mid_korean_font(size=15):
    font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
    return ImageFont.truetype(font_path, size)

def load_small_korean_font(size=12):
    font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
    return ImageFont.truetype(font_path, size)

def is_button_pressed(button):
    return not button.value

width = 240
height = 240

obstacle_coords = []

obstacle_coords_top = []

def is_collision(ball_x, ball_y, obstacle_coords):
    ball_radius = 7.5  
    ball_center = (ball_x + ball_radius, ball_y + ball_radius)  

    
    for obstacle_rect in obstacle_coords:
        if check_circle_collision(ball_center, ball_radius, obstacle_rect):
            print("충돌 발생:", ball_center, obstacle_rect)
            return True  

    return False 

def check_circle_collision(circle_center, circle_radius, rect):
    closest_x = max(rect[0], min(circle_center[0], rect[2]))
    closest_y = max(rect[1], min(circle_center[1], rect[3]))

    distance = ((circle_center[0] - closest_x) ** 2 + (circle_center[1] - closest_y) ** 2) ** 0.5
    return distance < circle_radius

def is_top_collision(ball_x, ball_y, obstacle_coords_top):
    global obstacle_rect
    ball_rect = (ball_x, ball_y, ball_x +15, ball_y + 15)

    for obstacle_rect in obstacle_coords_top:
        if check_top_collision(ball_rect, obstacle_rect):
            return True

    return False

def check_top_collision(rect1, rect2):
    return rect1[2] >= rect2[0] and rect1[0] <= rect2[2] and rect1[3] >= rect2[1] and rect1[1] <= rect2[3]

obstacle_coords = []
obstacle_coords_top = []

def map(draw, offset):
    
    global obstacle_coords , obstacle_coords_top
    obstacle_coords = []
    rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
    
    obstacle1_left = 250 + offset
    obstacle1_top = 200
    obstacle1_right = 370 + offset
    obstacle1_bottom = 240
    draw.rectangle(
        ((obstacle1_left, obstacle1_top), (obstacle1_right, obstacle1_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle1_left, obstacle1_top+0.5, obstacle1_left+0.5, obstacle1_bottom))
    obstacle_coords_top.append((obstacle1_left, obstacle1_top, obstacle1_right, obstacle1_bottom))

    obstacle2_left = 505 + offset
    obstacle2_top = 200
    obstacle2_right = 515 + offset
    obstacle2_bottom = 240
    draw.rectangle(
        ((obstacle2_left, obstacle2_top), (obstacle2_right, obstacle2_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle2_left, obstacle2_top+0.5, obstacle2_left+0.5, obstacle2_bottom))
    obstacle_coords_top.append((obstacle2_left, obstacle2_top, obstacle2_right, obstacle2_bottom))
    
    obstacle3_left = 650 + offset
    obstacle3_top = 200
    obstacle3_right = 660 + offset
    obstacle3_bottom = 240
    draw.rectangle(
        ((obstacle3_left, obstacle3_top), (obstacle3_right, obstacle3_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle3_left, obstacle3_top+0.5, obstacle3_left+0.5, obstacle3_bottom))
    obstacle_coords_top.append((obstacle3_left, obstacle3_top, obstacle3_right, obstacle3_bottom))
    
    obstacle4_left = 850 + offset
    obstacle4_top = 200
    obstacle4_right = 860 + offset
    obstacle4_bottom = 240
    draw.rectangle(
        ((obstacle4_left, obstacle4_top), (obstacle4_right, obstacle4_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle4_left, obstacle4_top+0.5, obstacle4_left+0.5, obstacle4_bottom))
    obstacle_coords_top.append((obstacle4_left, obstacle4_top, obstacle4_right, obstacle4_bottom))
    
    obstacle5_left = 1050 + offset
    obstacle5_top = 200
    obstacle5_right = 1120 + offset
    obstacle5_bottom = 240
    draw.rectangle(
        ((obstacle5_left, obstacle5_top), (obstacle5_right, obstacle5_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle5_left, obstacle5_top+0.5, obstacle5_left+0.5, obstacle5_bottom))
    obstacle_coords_top.append((obstacle5_left, obstacle5_top, obstacle5_right, obstacle5_bottom))
    
    obstacle6_left = 1120 + offset
    obstacle6_top = 170
    obstacle6_right = 1200 + offset
    obstacle6_bottom = 200
    draw.rectangle(
        ((obstacle6_left, obstacle6_top), (obstacle6_right, obstacle6_bottom)),
        outline="#000000",
        fill=rcolor ,
    )
    obstacle_coords.append((obstacle6_left, obstacle6_top+0.5, obstacle6_left+0.5, obstacle6_bottom+40))
    obstacle_coords_top.append((obstacle6_left, obstacle6_top, obstacle6_right, obstacle6_bottom+40))
    
    obstacle7_left = 1200 + offset
    obstacle7_top = 140
    obstacle7_right = 1280 + offset
    obstacle7_bottom = 170
    draw.rectangle(
        ((obstacle7_left, obstacle7_top), (obstacle7_right, obstacle7_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle7_left, obstacle7_top+0.5, obstacle7_left+0.5, obstacle7_bottom+70))
    obstacle_coords_top.append((obstacle7_left, obstacle7_top, obstacle7_right, obstacle7_bottom+70))
    
    obstacle8_left = 1280 + offset
    obstacle8_top = 120
    obstacle8_right = 1320 + offset
    obstacle8_bottom = 140
    draw.rectangle(
        ((obstacle8_left, obstacle8_top), (obstacle8_right, obstacle8_bottom)),
        outline="#000000",
        fill=rcolor ,
    )
    obstacle_coords.append((obstacle8_left, obstacle8_top+0.5, obstacle8_left+0.5, obstacle8_bottom+100))
    obstacle_coords_top.append((obstacle8_left, obstacle8_top, obstacle8_right, obstacle8_bottom+100))
    
    obstacle9_left = 1430 + offset
    obstacle9_top = 200
    obstacle9_right = 1550 + offset
    obstacle9_bottom = 240
    draw.rectangle(
        ((obstacle9_left, obstacle9_top), (obstacle9_right, obstacle9_bottom)),
        outline="#000000",
        fill=rcolor ,
    )
    obstacle_coords.append((obstacle9_left, obstacle9_top+0.5, obstacle9_left+0.5, obstacle9_bottom))
    obstacle_coords_top.append((obstacle9_left, obstacle9_top, obstacle9_right, obstacle9_bottom))

    obstacle10_left = 1750 + offset
    obstacle10_top = 200
    obstacle10_right = 1760 + offset
    obstacle10_bottom = 240
    draw.rectangle(
        ((obstacle10_left, obstacle10_top), (obstacle10_right, obstacle10_bottom)),
        outline="#000000",
        fill=rcolor ,
    )
    obstacle_coords.append((obstacle10_left, obstacle10_top+0.5, obstacle10_left+0.5, obstacle10_bottom))
    obstacle_coords_top.append((obstacle10_left, obstacle10_top, obstacle10_right, obstacle10_bottom))
    
    obstacle11_left = 1960 + offset
    obstacle11_top = 200
    obstacle11_right = 1970 + offset
    obstacle11_bottom = 240
    draw.rectangle(
        ((obstacle11_left, obstacle11_top), (obstacle11_right, obstacle11_bottom)),
        outline="#000000",
        fill=rcolor ,
    )
    obstacle_coords.append((obstacle11_left, obstacle11_top+0.5, obstacle11_left+0.5, obstacle11_bottom))
    obstacle_coords_top.append((obstacle11_left, obstacle11_top, obstacle11_right, obstacle11_bottom))
    
    obstacle12_left = 2170 + offset
    obstacle12_top = 200
    obstacle12_right = 2180 + offset
    obstacle12_bottom = 240
    draw.rectangle(
        ((obstacle12_left, obstacle12_top), (obstacle12_right, obstacle12_bottom)),
        outline="#000000",
        fill=rcolor ,
    )
    obstacle_coords.append((obstacle12_left, obstacle12_top+0.5, obstacle12_left+0.5, obstacle12_bottom))
    obstacle_coords_top.append((obstacle12_left, obstacle12_top, obstacle12_right, obstacle12_bottom))
    
    obstacle13_left = 2380 + offset
    obstacle13_top = 200
    obstacle13_right = 2450 + offset
    obstacle13_bottom = 240
    draw.rectangle(
        ((obstacle13_left, obstacle13_top), (obstacle13_right, obstacle13_bottom)),
        outline="#000000",
        fill=rcolor ,
    )
    obstacle_coords.append((obstacle13_left, obstacle13_top+0.5, obstacle13_left+0.5, obstacle13_bottom))
    obstacle_coords_top.append((obstacle13_left, obstacle13_top, obstacle13_right, obstacle13_bottom))
    
    obstacle14_left = 2450+ offset
    obstacle14_top = 170
    obstacle14_right = 2530 + offset
    obstacle14_bottom = 200
    draw.rectangle(
        ((obstacle14_left, obstacle14_top), (obstacle14_right, obstacle14_bottom)),
        outline="#000000",
        fill=rcolor ,
    )
    obstacle_coords.append((obstacle14_left, obstacle14_top+0.5, obstacle14_left+0.5, obstacle14_bottom+40))
    obstacle_coords_top.append((obstacle14_left, obstacle14_top, obstacle14_right, obstacle14_bottom+40))
    
    obstacle7_left = 2530 + offset
    obstacle7_top = 140
    obstacle7_right = 2610 + offset
    obstacle7_bottom = 170
    draw.rectangle(
        ((obstacle7_left, obstacle7_top), (obstacle7_right, obstacle7_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle7_left, obstacle7_top+0.5, obstacle7_left+0.5, obstacle7_bottom+70))
    obstacle_coords_top.append((obstacle7_left, obstacle7_top, obstacle7_right, obstacle7_bottom+70))
    
    obstacle8_left = 2610 + offset
    obstacle8_top = 120
    obstacle8_right = 2690 + offset
    obstacle8_bottom = 140
    draw.rectangle(
        ((obstacle8_left, obstacle8_top), (obstacle8_right, obstacle8_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle8_left, obstacle8_top+0.5, obstacle8_left+0.5, obstacle8_bottom+100))
    obstacle_coords_top.append((obstacle8_left, obstacle8_top, obstacle8_right, obstacle8_bottom+100))
    
    obstacle1_left = 2690 + offset
    obstacle1_top = 140
    obstacle1_right = 2760 + offset
    obstacle1_bottom = 170
    draw.rectangle(
        ((obstacle1_left, obstacle1_top), (obstacle1_right, obstacle1_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle1_left, obstacle1_top+0.5, obstacle1_left+0.5, obstacle1_bottom+70))
    obstacle_coords_top.append((obstacle1_left, obstacle1_top, obstacle1_right, obstacle1_bottom+70))

    obstacle2_left = 2760 + offset
    obstacle2_top = 170
    obstacle2_right = 2830 + offset
    obstacle2_bottom = 200
    draw.rectangle(
        ((obstacle2_left, obstacle2_top), (obstacle2_right, obstacle2_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle2_left, obstacle2_top+0.5, obstacle2_left+0.5, obstacle2_bottom+40))
    obstacle_coords_top.append((obstacle2_left, obstacle2_top, obstacle2_right, obstacle2_bottom+40))
    
    obstacle3_left = 2830 + offset
    obstacle3_top = 200
    obstacle3_right = 2900 + offset
    obstacle3_bottom = 240
    draw.rectangle(
        ((obstacle3_left, obstacle3_top), (obstacle3_right, obstacle3_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle3_left, obstacle3_top+0.5, obstacle3_left+0.5, obstacle3_bottom))
    obstacle_coords_top.append((obstacle3_left, obstacle3_top, obstacle3_right, obstacle3_bottom))

    ground_height = 20
    draw.rectangle((0, 240 - ground_height, width, height), outline="#000000", fill="#B8DEFF")
    
    return obstacle_coords, obstacle_coords_top 


def game_start(draw, button_U, button_D, button_L, button_R, button_C, button_A, button_B, fnt, korean_font, small_korean_font, mid_korean_font):
    global obstacle_coords, disp, image, obstacle_coords_top, obstacle_rect, ground_height
    cs_pin = DigitalInOut(board.CE0)
    dc_pin = DigitalInOut(board.D25)
    reset_pin = DigitalInOut(board.D24)
    BAUDRATE = 24000000
    
    start_time = time.time()
    paused_time = 0

    spi = board.SPI()
    disp = st7789.ST7789(
        spi,
        height=240,
        y_offset=80,
        rotation=180,
        cs=cs_pin,
        dc=dc_pin,
        rst=reset_pin,
        baudrate=BAUDRATE,
    )

    music_file = os.path.expanduser("~/project/노래 복사본.mp3")
    backlight = DigitalInOut(board.D26)
    backlight.switch_to_output()
    backlight.value = True
    music_thread = threading.Thread(target=play_music, args=(music_file,))
    music_thread.start()

    offset = 0
    ball_x = 50
    ball_y = 150
    ball_velocity = 0
    on_ground = True  

    ground_height = 20
    obstacle_coords = []

    obstacle_coords, obstacle_coords_top = map(draw, offset)

    is_paused = False 

    while True:
        
        image = Image.new("RGB", (width, height))
        draw = ImageDraw.Draw(image)
        
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 5, 5))

        draw.rectangle((0, 0, width, height), outline="#000000", fill=rcolor)

        obstacle_coords, obstacle_coords_top = map(draw, offset)  

        draw.ellipse((ball_x, ball_y, ball_x + 15, ball_y + 15), outline="#000000", fill="#B8DEFF")

        disp.image(image)

        if is_button_pressed(button_A) and on_ground:
            ball_velocity = -25.0  
            on_ground = False  

        ball_velocity += 7.0
        ball_y += ball_velocity

        if ball_y > height - ground_height - 15:
            ball_y = height - ground_height - 15
            ball_velocity = 0
            on_ground = True 

        if is_button_pressed(button_B):
            if not is_paused:
                pause_music()
                is_paused = True
            else:
                resume_music()
                is_paused = False

        if is_paused:
            paused_time += time.time()
            time.sleep(0.01)
            continue

        if is_collision(ball_x, ball_y, obstacle_coords):
            stop_music()
            break
        
        if is_top_collision(ball_x, ball_y, obstacle_coords_top):
            ground_height = obstacle_rect[3] - obstacle_rect[1]
        else:
            ground_height = 20
        offset -= 15
        
        elapsed_time = time.time() - start_time - paused_time
        if elapsed_time > 19.5:
            game_fly(draw, button_U, button_D, button_L, button_R, button_C, button_A, button_B, fnt, korean_font, small_korean_font, mid_korean_font)
            break

        time.sleep(0.01)
        obstacle_coords_top = []

    obstacle_coords = [] 
    

def draw_airplane(draw, x, y):
    airplane_width = 20
    airplane_height = 10
    airplane_color = "#FFFFFF"

    draw.polygon(
        [
            (x, y),
            (x - airplane_width / 2, y + airplane_height),
            (x + airplane_width / 2, y + airplane_height),
        ],
        outline=airplane_color,
        fill=airplane_color,
    )



def fly_map(draw, offset):
    obstacle_coords = []
    rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 5, 5))
      
    obstacle2_left = 250 + offset
    obstacle2_top = 0
    obstacle2_right = 270 + offset
    obstacle2_bottom =200
    
    draw.rectangle(
        ((obstacle2_left, obstacle2_top), (obstacle2_right, obstacle2_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle2_left, obstacle2_top, obstacle2_right, obstacle2_bottom))
    
    obstacle3_left = 320 + offset
    obstacle3_top = 200
    obstacle3_right = 340 + offset
    obstacle3_bottom = 240
    draw.rectangle(
        ((obstacle3_left, obstacle3_top), (obstacle3_right, obstacle3_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle3_left, obstacle3_top, obstacle3_right, obstacle3_bottom))
    
    obstacle4_left = 400 + offset
    obstacle4_top = 100
    obstacle4_right = 420 + offset
    obstacle4_bottom =240
    
    draw.rectangle(
        ((obstacle4_left, obstacle4_top), (obstacle4_right, obstacle4_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle4_left, obstacle4_top, obstacle4_right, obstacle4_bottom))
    
    obstacle5_left = 520 + offset
    obstacle5_top = 0
    obstacle5_right = 540 + offset
    obstacle5_bottom = 180
    draw.rectangle(
        ((obstacle5_left, obstacle5_top), (obstacle5_right, obstacle5_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle5_left, obstacle5_top, obstacle5_right, obstacle5_bottom))
    
    obstacle2_left = 640+ offset
    obstacle2_top = 0
    obstacle2_right = 660 + offset
    obstacle2_bottom =140
    
    draw.rectangle(
        ((obstacle2_left, obstacle2_top), (obstacle2_right, obstacle2_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle2_left, obstacle2_top, obstacle2_right, obstacle2_bottom))
    
    obstacle3_left = 640 + offset
    obstacle3_top = 210
    obstacle3_right = 660 + offset
    obstacle3_bottom = 240
    draw.rectangle(
        ((obstacle3_left, obstacle3_top), (obstacle3_right, obstacle3_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle3_left, obstacle3_top, obstacle3_right, obstacle3_bottom))
    
    obstacle4_left = 700 + offset
    obstacle4_top = 0
    obstacle4_right = 720 + offset
    obstacle4_bottom =50
    
    draw.rectangle(
        ((obstacle4_left, obstacle4_top), (obstacle4_right, obstacle4_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle4_left, obstacle4_top, obstacle4_right, obstacle4_bottom))
    
    obstacle5_left = 700 + offset
    obstacle5_top = 140
    obstacle5_right = 720 + offset
    obstacle5_bottom = 240
    draw.rectangle(
        ((obstacle5_left, obstacle5_top), (obstacle5_right, obstacle5_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle5_left, obstacle5_top, obstacle5_right, obstacle5_bottom))
    
    
    obstacle2_left = 760+ offset
    obstacle2_top = 0
    obstacle2_right = 780 + offset
    obstacle2_bottom =20
    
    draw.rectangle(
        ((obstacle2_left, obstacle2_top), (obstacle2_right, obstacle2_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle2_left, obstacle2_top, obstacle2_right, obstacle2_bottom))
    
    obstacle3_left = 760 + offset
    obstacle3_top = 100
    obstacle3_right = 780 + offset
    obstacle3_bottom = 240
    draw.rectangle(
        ((obstacle3_left, obstacle3_top), (obstacle3_right, obstacle3_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle3_left, obstacle3_top, obstacle3_right, obstacle3_bottom))
    
    obstacle4_left = 830+ offset
    obstacle4_top = 0
    obstacle4_right = 850 + offset
    obstacle4_bottom =50
    
    draw.rectangle(
        ((obstacle4_left, obstacle4_top), (obstacle4_right, obstacle4_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle4_left, obstacle4_top, obstacle4_right, obstacle4_bottom))
    
    obstacle5_left = 830 + offset
    obstacle5_top = 140
    obstacle5_right = 850 + offset
    obstacle5_bottom = 240
    draw.rectangle(
        ((obstacle5_left, obstacle5_top), (obstacle5_right, obstacle5_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle5_left, obstacle5_top, obstacle5_right, obstacle5_bottom))
    
    obstacle2_left = 920+ offset
    obstacle2_top = 0
    obstacle2_right = 940 + offset
    obstacle2_bottom =120
    
    draw.rectangle(
        ((obstacle2_left, obstacle2_top), (obstacle2_right, obstacle2_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle2_left, obstacle2_top, obstacle2_right, obstacle2_bottom))
    
    obstacle3_left = 920 + offset
    obstacle3_top = 210
    obstacle3_right = 940 + offset
    obstacle3_bottom = 240
    draw.rectangle(
        ((obstacle3_left, obstacle3_top), (obstacle3_right, obstacle3_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle3_left, obstacle3_top, obstacle3_right, obstacle3_bottom))
    
    obstacle4_left = 1020+ offset
    obstacle4_top = 0
    obstacle4_right = 1040 + offset
    obstacle4_bottom =15
    
    draw.rectangle(
        ((obstacle4_left, obstacle4_top), (obstacle4_right, obstacle4_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle4_left, obstacle4_top, obstacle4_right, obstacle4_bottom))
    
    obstacle5_left = 1020 + offset
    obstacle5_top = 95
    obstacle5_right = 1040 + offset
    obstacle5_bottom = 240
    draw.rectangle(
        ((obstacle5_left, obstacle5_top), (obstacle5_right, obstacle5_bottom)),
        outline="#000000",
        fill=rcolor,
    )
    obstacle_coords.append((obstacle5_left, obstacle5_top, obstacle5_right, obstacle5_bottom))
        

    return obstacle_coords


    



    
def game_fly(draw, button_U, button_D, button_L, button_R, button_C, button_A, button_B, fnt, korean_font, small_korean_font, mid_korean_font):
    global obstacle_coords, disp, image, obstacle_coords_top, obstacle_rect, ground_height
    cs_pin = DigitalInOut(board.CE0)
    dc_pin = DigitalInOut(board.D25)
    reset_pin = DigitalInOut(board.D24)
    BAUDRATE = 24000000

    start_time = time.time()

    spi = board.SPI()
    disp = st7789.ST7789(
        spi,
        height=240,
        y_offset=80,
        rotation=180,
        cs=cs_pin,
        dc=dc_pin,
        rst=reset_pin,
        baudrate=BAUDRATE,
    )

    music_file = os.path.expanduser("~/project/노래 복사본.mp3")
    backlight = DigitalInOut(board.D26)
    backlight.switch_to_output()
    backlight.value = True

    offset = 0
    ball_x = 50
    ball_y = 150
    ball_velocity = 0
    on_ground = True 

    ground_height = 20
    obstacle_coords = []

    obstacle_coords = fly_map(draw, offset)

    is_paused = False 

    while True:
        image = Image.new("RGB", (width, height))
        draw = ImageDraw.Draw(image)

        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 5, 5))
        draw.rectangle((0, 0, width, height), outline="#000000", fill=rcolor)

        obstacle_coords = fly_map(draw, offset)
        
        draw_airplane(draw, ball_x, ball_y)

        disp.image(image)

        if is_button_pressed(button_U):
            ball_velocity = -25.0
            on_ground = True

        if is_button_pressed(button_D):
            ball_velocity += 7.0

        ball_velocity += 7.0
        ball_y += ball_velocity

        if ball_y > height - ground_height - 15:
            ball_y = height - ground_height - 15
            ball_velocity = 0
            on_ground = True

        if is_button_pressed(button_B):
            if not is_paused:
                pause_music()
                is_paused = True
            else:
                resume_music()
                is_paused = False

        if is_paused:
            time.sleep(0.01)
            continue

        if is_collision(ball_x, ball_y, obstacle_coords):
            stop_music()
            break

        offset -= 15

        time.sleep(0.01)

    obstacle_coords = []


    obstacle_coords = [] 


    
def explain_joystick(draw, button_U, button_D, button_L, button_R, button_C, button_A, button_B, fnt, korean_font, small_korean_font, mid_korean_font):
    cs_pin = DigitalInOut(board.CE0)
    dc_pin = DigitalInOut(board.D25)
    reset_pin = DigitalInOut(board.D24)
    BAUDRATE = 24000000

    
    spi = board.SPI()
    disp = st7789.ST7789(
        spi,
        height=240,
        y_offset=80,
        rotation=180,
        cs=cs_pin,
        dc=dc_pin,
        rst=reset_pin,
        baudrate=BAUDRATE,
    )
    music_file = os.path.expanduser("~/project/노래 복사본.mp3")

    backlight = DigitalInOut(board.D26)
    backlight.switch_to_output()
    backlight.value = True

    width = disp.width
    height = disp.height
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    udlr_fill = "#00FFFF"
    udlr_outline = "#00FFFF"
    button_fill = "#FF00FF"
    button_outline = "#00FFFF"
    
    a_button_pressed = False

    while True:
        draw.rectangle((0, 0, width, height), outline="#000000", fill="#B8DEFF")
        
        up_fill = 0
        if not button_U.value:
            up_fill = udlr_fill
        draw.polygon([(40, 40), (60, 4), (80, 40)], outline=udlr_outline, fill=up_fill)
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((52.5, 20), "위", font=mid_korean_font, fill=rcolor)

        down_fill = 0
        if not button_D.value:
            down_fill = udlr_fill
        draw.polygon([(60, 120), (80, 84), (40, 84)], outline=udlr_outline, fill=down_fill)
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((48, 85), "아래", font=small_korean_font, fill=rcolor)
        
        left_fill = 0
        if not button_L.value:
            left_fill = udlr_fill
        draw.polygon([(0, 60), (36, 42), (36, 81)], outline=udlr_outline, fill=left_fill)

        right_fill = 0
        if not button_R.value:
            right_fill = udlr_fill
        draw.polygon([(120, 60), (84, 42), (84, 82)], outline=udlr_outline, fill=right_fill)

        center_fill = 0
        if not button_C.value:
            center_fill = button_fill
        draw.rectangle((40, 44, 80, 80), outline=button_outline, fill=center_fill)

        A_fill = 0
        if not button_A.value:
            A_fill = button_fill
        draw.ellipse((140, 80, 180, 120), outline=button_outline, fill=A_fill)
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((150, 82), "A", font=fnt, fill=rcolor)


        B_fill = 0
        if not button_B.value:
            B_fill = button_fill
        draw.ellipse((190, 40, 230, 80), outline=button_outline, fill=B_fill)
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((200, 42), "B", font=fnt, fill=rcolor)

        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((30, 150), "위 : 비행선 위로", font=korean_font, fill=rcolor)
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((30, 180), "어래 : 비행선 아래로", font=korean_font, fill=rcolor)
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((30, 210), "게임시작 : A", font=korean_font, fill=rcolor)
        

        disp.image(image)
        
        if is_button_pressed(button_A):
            if not a_button_pressed:
                a_button_pressed = True
        
        if not button_A.value:
            game_start(draw, button_U, button_D, button_L, button_R, button_C, button_A, button_B, fnt, korean_font, small_korean_font, mid_korean_font)
        

        time.sleep(0.01)



def explain_button(draw, button_U, button_D, button_L, button_R, button_C, button_A, button_B, fnt, korean_font, small_korean_font, mid_korean_font):
    cs_pin = DigitalInOut(board.CE0)
    dc_pin = DigitalInOut(board.D25)
    reset_pin = DigitalInOut(board.D24)
    BAUDRATE = 24000000

    
    spi = board.SPI()
    disp = st7789.ST7789(
        spi,
        height=240,
        y_offset=80,
        rotation=180,
        cs=cs_pin,
        dc=dc_pin,
        rst=reset_pin,
        baudrate=BAUDRATE,
    )
    backlight = DigitalInOut(board.D26)
    backlight.switch_to_output()
    backlight.value = True

    width = disp.width
    height = disp.height
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    udlr_fill = "#00FFFF"
    udlr_outline = "#00FFFF"
    button_fill = "#FF00FF"
    button_outline = "#00FFFF"
    
    a_button_pressed = False

    while True:
        draw.rectangle((0, 0, width, height), outline="#000000", fill="#B8DEFF")
        
        up_fill = 0
        if not button_U.value:
            up_fill = udlr_fill
        draw.polygon([(40, 40), (60, 4), (80, 40)], outline=udlr_outline, fill=up_fill)
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((52.5, 20), "위", font=mid_korean_font, fill=rcolor)

        down_fill = 0
        if not button_D.value:
            down_fill = udlr_fill
        draw.polygon([(60, 120), (80, 84), (40, 84)], outline=udlr_outline, fill=down_fill)
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((48, 85), "아래", font=small_korean_font, fill=rcolor)
        
        left_fill = 0
        if not button_L.value:
            left_fill = udlr_fill
        draw.polygon([(0, 60), (36, 42), (36, 81)], outline=udlr_outline, fill=left_fill)

        right_fill = 0
        if not button_R.value:
            right_fill = udlr_fill
        draw.polygon([(120, 60), (84, 42), (84, 82)], outline=udlr_outline, fill=right_fill)

        center_fill = 0
        if not button_C.value:
            center_fill = button_fill
        draw.rectangle((40, 44, 80, 80), outline=button_outline, fill=center_fill)

        A_fill = 0
        if not button_A.value:
            A_fill = button_fill
        draw.ellipse((140, 80, 180, 120), outline=button_outline, fill=A_fill)
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((150, 82), "A", font=fnt, fill=rcolor)


        B_fill = 0
        if not button_B.value:
            B_fill = button_fill
        draw.ellipse((190, 40, 230, 80), outline=button_outline, fill=B_fill)
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((200, 42), "B", font=fnt, fill=rcolor)

        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((30, 150), "A : 점프버튼", font=korean_font, fill=rcolor)
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((30, 180), "B : 일시정지/재생", font=korean_font, fill=rcolor)
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((30, 210), "다음설명 : A", font=korean_font, fill=rcolor)
        

        disp.image(image)
        
        if is_button_pressed(button_A):
            if not a_button_pressed:
                a_button_pressed = True
        
        if not button_A.value:
            explain_joystick(draw, button_U, button_D, button_L, button_R, button_C, button_A, button_B, fnt, korean_font, small_korean_font, mid_korean_font)
        

        time.sleep(0.01)




def main():
    cs_pin = DigitalInOut(board.CE0)
    dc_pin = DigitalInOut(board.D25)
    reset_pin = DigitalInOut(board.D24)
    BAUDRATE = 24000000
    korean_font = load_korean_font()
    small_korean_font = load_small_korean_font()
    mid_korean_font = load_mid_korean_font()
    fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)


    spi = board.SPI()
    disp = st7789.ST7789(
        spi,
        height=240,
        y_offset=80,
        rotation=180,
        cs=cs_pin,
        dc=dc_pin,
        rst=reset_pin,
        baudrate=BAUDRATE,
    )
    music_file = os.path.expanduser("~/project/노래 복사본.mp3")

    button_A = DigitalInOut(board.D5)
    button_A.direction = Direction.INPUT

    button_B = DigitalInOut(board.D6)
    button_B.direction = Direction.INPUT

    button_L = DigitalInOut(board.D27)
    button_L.direction = Direction.INPUT

    button_R = DigitalInOut(board.D23)
    button_R.direction = Direction.INPUT

    button_U = DigitalInOut(board.D17)
    button_U.direction = Direction.INPUT

    button_D = DigitalInOut(board.D22)
    button_D.direction = Direction.INPUT

    button_C = DigitalInOut(board.D4)
    button_C.direction = Direction.INPUT

    backlight = DigitalInOut(board.D26)
    backlight.switch_to_output()
    backlight.value = True

    width = disp.width
    height = disp.height
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    udlr_fill = "#00FFFF"
    udlr_outline = "#00FFFF"
    button_fill = "#FF00FF"
    button_outline = "#00FFFF"
    
    a_button_pressed = False

    while True:
        draw.rectangle((0, 0, width, height), outline="#000000", fill="#B8DEFF")
        
        up_fill = 0
        if not button_U.value:
            up_fill = udlr_fill
        draw.polygon([(40, 40), (60, 4), (80, 40)], outline=udlr_outline, fill=up_fill)
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((52.5, 20), "위", font=mid_korean_font, fill=rcolor)

        down_fill = 0
        if not button_D.value:
            down_fill = udlr_fill
        draw.polygon([(60, 120), (80, 84), (40, 84)], outline=udlr_outline, fill=down_fill)
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((48, 85), "아래", font=small_korean_font, fill=rcolor)
        
        left_fill = 0
        if not button_L.value:
            left_fill = udlr_fill
        draw.polygon([(0, 60), (36, 42), (36, 81)], outline=udlr_outline, fill=left_fill)

        right_fill = 0
        if not button_R.value:
            right_fill = udlr_fill
        draw.polygon([(120, 60), (84, 42), (84, 82)], outline=udlr_outline, fill=right_fill)

        center_fill = 0
        if not button_C.value:
            center_fill = button_fill
        draw.rectangle((40, 44, 80, 80), outline=button_outline, fill=center_fill)

        A_fill = 0
        if not button_A.value:
            A_fill = button_fill
            #play_music(music_file)
        draw.ellipse((140, 80, 180, 120), outline=button_outline, fill=A_fill)
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((150, 82), "A", font=fnt, fill=rcolor)


        B_fill = 0
        if not button_B.value:
            B_fill = button_fill
        draw.ellipse((190, 40, 230, 80), outline=button_outline, fill=B_fill)
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((200, 42), "B", font=fnt, fill=rcolor)

        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((30, 150), "게임을 시작하려면", font=korean_font, fill=rcolor)
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((75, 180), "A버튼을", font=korean_font, fill=rcolor)
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((65, 210), "눌러주세요", font=korean_font, fill=rcolor)
        

        disp.image(image)
        
        if is_button_pressed(button_A):
            if not a_button_pressed:
                a_button_pressed = True
        
        if not button_A.value:
            explain_button(draw, button_U, button_D, button_L, button_R, button_C, button_A, button_B, fnt, korean_font, small_korean_font, mid_korean_font)

        time.sleep(0.01)

if __name__ == "__main__":
    main()
    

