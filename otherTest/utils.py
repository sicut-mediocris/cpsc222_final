import math

def extract_single_frame(sheet, frame_width, frame_height, row=0, col=0):
    frame = sheet.subsurface(((col * frame_width) + 122, (row * frame_height) + 120, 50, 50)).convert_alpha()
    return frame

def extract_hit_frames(sheet, frame_width, frame_height):
    frames = []
    for row in range(sheet.get_height() // frame_height):
        for col in range(sheet.get_width() // frame_width):
            frame = sheet.subsurface((col * frame_width, row * frame_height, frame_width, frame_height))
            frames.append(frame)
    return frames

def isCollision(enemyx, enemyy, arrowx, arrowy):
    distance = math.sqrt((enemyx - arrowx) ** 2 + (enemyy - arrowy) ** 2)
    return distance < 37