"""Detailed side-view car illustration built with the standard turtle module."""

import math
import turtle


screen = turtle.Screen()
screen.setup(width=1100, height=700)
screen.title("Detailed Car Illustration")
screen.bgcolor("#b9e8ff")
screen.tracer(False)

pen = turtle.Turtle(visible=False)
pen.speed(0)
pen.pensize(2)


def polygon(points, fill, outline="#17202a", width=2):
    """Draw a closed filled polygon from a list of coordinates."""
    pen.pensize(width)
    pen.color(outline, fill)
    pen.penup()
    pen.goto(points[0])
    pen.pendown()
    pen.begin_fill()
    for point in points[1:]:
        pen.goto(point)
    pen.goto(points[0])
    pen.end_fill()
    pen.penup()


def rectangle(x1, y1, x2, y2, fill, outline="#17202a", width=2):
    polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], fill, outline, width)


def ellipse(x, y, width, height, fill, outline="#17202a", pen_width=2):
    """Draw an ellipse using many points for a clean turtle outline."""
    points = []
    for step in range(48):
        angle = 2 * math.pi * step / 48
        points.append(
            (x + width * 0.5 * math.cos(angle), y + height * 0.5 * math.sin(angle))
        )
    polygon(points, fill, outline, pen_width)


def circle(x, y, radius, fill, outline="#17202a", width=2):
    pen.pensize(width)
    pen.color(outline, fill)
    pen.penup()
    pen.goto(x, y - radius)
    pen.setheading(0)
    pen.pendown()
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()
    pen.penup()


def line(points, color="#17202a", width=2):
    pen.pensize(width)
    pen.color(color)
    pen.penup()
    pen.goto(points[0])
    pen.pendown()
    for point in points[1:]:
        pen.goto(point)
    pen.penup()


def draw_background():
    rectangle(-550, -350, 550, -165, "#566573", outline="#566573", width=1)
    rectangle(-550, -165, 550, 350, "#b9e8ff", outline="#b9e8ff", width=1)

    for x, y, radius in [(-390, 210, 38), (-345, 218, 48), (-295, 208, 34),
                         (330, 235, 30), (368, 242, 42), (410, 230, 28)]:
        circle(x, y, radius, "#ffffff", outline="#ffffff", width=1)

    line([(-550, -165), (550, -165)], "#35404a", 4)
    for x in range(-520, 540, 120):
        rectangle(x, -270, x + 60, -260, "#f7dc6f", outline="#f7dc6f", width=1)


def draw_wheel(x, y):
    circle(x, y, 48, "#111820", outline="#080b0e", width=3)
    circle(x, y, 38, "#2d343b", outline="#7f8c8d", width=3)
    circle(x, y, 27, "#566573", outline="#151a1f", width=2)
    circle(x, y, 12, "#d5d8dc", outline="#111820", width=2)
    circle(x, y, 5, "#65717b", outline="#111820", width=1)
    for spoke in range(0, 360, 60):
        pen.setheading(spoke)
        pen.penup()
        pen.goto(x, y)
        pen.forward(12)
        pen.pendown()
        pen.forward(17)
        pen.penup()


def draw_car():
    ellipse(0, -118, 455, 35, "#313b43", outline="#313b43", pen_width=1)

    polygon(
        [(-285, -45), (-270, 22), (-220, 34), (-135, 45), (-78, 118),
         (105, 118), (180, 45), (255, 28), (292, -15), (285, -75),
         (-285, -75)],
        "#d9364f", width=4,
    )
    polygon([(-278, -48), (286, -48), (278, -75), (-282, -75)], "#a91f3a", width=2)
    line([(-260, -30), (260, -30)], "#f47b8a", 3)

    polygon([(-127, 48), (-72, 105), (-8, 105), (-8, 48)], "#6bc5df", width=3)
    polygon([(-1, 48), (-1, 105), (99, 105), (157, 48)], "#4aa9c7", width=3)
    polygon([(-117, 54), (-69, 97), (-17, 97), (-17, 54)], "#bceefa", outline="#dffaff", width=2)
    polygon([(9, 54), (9, 97), (91, 97), (140, 54)], "#a7e5f2", outline="#dffaff", width=2)
    line([(-55, 60), (-35, 96)], "#ffffff", 4)
    line([(59, 60), (91, 93)], "#ffffff", 4)
    line([(-5, 43), (-5, 112)], "#17202a", 5)

    line([(-2, 48), (-2, -45)], "#7c172b", 2)
    line([(157, 48), (157, -40)], "#7c172b", 2)
    line([(-2, -42), (152, -42)], "#7c172b", 2)
    rectangle(30, 15, 70, 23, "#c6d0d5", outline="#17202a", width=2)
    rectangle(-112, 15, -72, 23, "#c6d0d5", outline="#17202a", width=2)
    rectangle(-230, -62, 230, -53, "#641326", outline="#641326", width=1)
    circle(207, 15, 11, "#c6d0d5", outline="#17202a", width=2)

    polygon([(-286, -38), (-310, -42), (-310, -65), (-275, -72)], "#65717b", width=3)
    polygon([(274, -42), (305, -35), (310, -63), (278, -72)], "#65717b", width=3)
    ellipse(269, -3, 38, 24, "#fff4a3", outline="#fff8cf", pen_width=3)
    ellipse(-270, -3, 28, 19, "#ff5c5c", outline="#ffd0d0", pen_width=2)
    rectangle(-22, -70, 55, -53, "#f1f3f4", outline="#17202a", width=2)
    line([(-15, -66), (48, -66)], "#60717d", 1)
    polygon([(245, -40), (284, -40), (275, -65), (250, -65)], "#202a31", width=2)
    for x in (253, 263, 273):
        line([(x, -43), (x, -62)], "#9aa4aa", 2)

    ellipse(-155, 45, 30, 15, "#d9364f", pen_width=2)
    ellipse(161, 45, 30, 15, "#d9364f", pen_width=2)
    line([(106, 112), (130, 140)], "#17202a", 3)
    circle(131, 142, 4, "#17202a", outline="#17202a", width=1)

    draw_wheel(-185, -73)
    draw_wheel(190, -73)
    circle(-185, -73, 8, "#f7dc6f", outline="#17202a", width=1)
    circle(190, -73, 8, "#f7dc6f", outline="#17202a", width=1)


draw_background()
draw_car()
screen.update()
turtle.done()
