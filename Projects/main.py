import turtle

turtle.speed(5)
turtle.bgcolor('black')
turtle.pensize(3)
def func():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.color('red', 'pink')
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
func()
turtle.left(120)
func()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()
turtle.done()


# import turtle
# import random
# import time

# # Setup screen
# screen = turtle.Screen()
# screen.bgcolor('black')
# screen.title('Falling Hearts Animation')
# screen.tracer(0)  # Turn off automatic updates

# # Create text turtle
# text_turtle = turtle.Turtle()
# text_turtle.hideturtle()
# text_turtle.penup()

# # Heart class for animation
# class FallingHeart:
#     def __init__(self):
#         self.turtle = turtle.Turtle()
#         self.turtle.hideturtle()
#         self.turtle.speed(0)
#         self.reset()
        
#     def reset(self):
#         self.x = random.randint(-350, 350)
#         self.y = 400
#         self.size = random.uniform(0.3, 0.7)
#         self.speed = random.uniform(1, 3)
#         self.color = random.choice(['red', 'pink', 'lightpink', 'hotpink'])
#         self.rotation = random.randint(0, 360)
#         self.rotation_speed = random.uniform(-2, 2)
        
#     def draw(self):
#         self.turtle.clear()
#         self.turtle.penup()
#         self.turtle.goto(self.x, self.y)
#         self.turtle.setheading(self.rotation)
#         self.turtle.pendown()
#         self.turtle.color(self.color)
        
#         # Draw small heart
#         self.turtle.begin_fill()
#         self.turtle.left(140)
#         self.turtle.forward(111.65 * self.size)
        
#         for _ in range(200):
#             self.turtle.right(1)
#             self.turtle.forward(1 * self.size)
            
#         self.turtle.left(120)
        
#         for _ in range(200):
#             self.turtle.right(1)
#             self.turtle.forward(1 * self.size)
            
#         self.turtle.forward(111.65 * self.size)
#         self.turtle.end_fill()
        
#     def update(self):
#         self.y -= self.speed
#         self.rotation += self.rotation_speed
        
#         if self.y < -400:
#             self.reset()
            
#         self.draw()

# # Draw "I ♥ You" text
# def draw_text():
#     text_turtle.color('white')
    
#     # "I"
#     text_turtle.goto(-200, 0)
#     text_turtle.write("I", align="center", font=("Comic Sans MS", 48, "bold"))
    
#     # Heart symbol
#     text_turtle.goto(0, 0)
#     text_turtle.color('red')
#     text_turtle.write("♥", align="center", font=("Arial", 60, "bold"))
    
#     # "You"
#     text_turtle.color('white')
#     text_turtle.goto(200, 0)
#     text_turtle.write("You", align="center", font=("Comic Sans MS", 48, "bold"))
    
#     # "Love" below
#     text_turtle.goto(0, -80)
#     text_turtle.color('pink')
#     text_turtle.write("Love", align="center", font=("Comic Sans MS", 36, "bold"))

# # Create multiple falling hearts
# hearts = [FallingHeart() for _ in range(30)]

# # Animation loop
# draw_text()

# while True:
#     screen.update()
    
#     for heart in hearts:
#         heart.update()
    
#     time.sleep(0.01)

# turtle.done()