import turtle as tl
tl.speed(0)

def draw_fractal(scale):
    if scale >=5:
        draw_fractal(scale / 2)
        tl.right(72)
        draw_fractal(scale / 2)
        tl.left(72)
        draw_fractal(scale / 2)
        tl.left(72)
        draw_fractal(scale / 2)
        tl.right(72)
        draw_fractal(scale / 2)


    else:
        tl.forward(scale)
        tl.right(36)
        tl.forward(scale)
        tl.right(36)
        tl.forward(scale)
        tl.right(36)
        tl.forward(scale)
        tl.right(36)
        tl.forward(scale)


scale = 300
tl.pensize(2)
tl.penup()
tl.goto(-scale, -scale / 4)
tl.pendown()

draw_fractal(scale)
tl.done()
