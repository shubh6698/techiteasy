# game_turtle.py
# A fun and interactive turtle game for Python learners!
# Created by Aditya Raj Mangalam || Tech it Easy!
# This file is part of a beginner-friendly Python project to learn programming concepts through game development.
# This game teaches you:
# 1. Variables and data types (score, lives, colors)
# 2. Control flow (if statements, loops)
# 3. Functions and modular code
# 4. Object-oriented programming (Turtle class)
# 5. Basic game design principles
# 6. Event handling (keyboard input)
# 7. Animation and graphics with the turtle module
# 8. User interface design (scoreboard, messages)
# This project is free and open source! Share it, modify it, learn from it!
# Made with ❤️ for Python learners!

import turtle   # Imports the turtle graphics module
import random   # Imports random for generating random effects and positions
import time     # Imports time for delays and animations

# ---------------------- Setup the screen ----------------------
wn = turtle.Screen()                     # Creates the main game window
wn.title("🐢 SUPER TURTLE ADVENTURE! 🐢")  # Eye-catching title with emojis
wn.bgcolor("black")                       # Cool dark blublacke background
wn.setup(width=800, height=600)         # Larger window for better gameplay
wn.tracer(0)                            # Disables automatic screen updates for smoother animations

# ---------------------- Game Colors & Effects ----------------------
head_colors = ["lime", "cyan", "yellow", "magenta", "orange"]  # Rainbow colors for head
body_colors = ["green", "blue", "red", "purple", "pink"]       # Body color options
current_color = 0                        # Index for color cycling

# ---------------------- Turtle Head ----------------------
head = turtle.Turtle()                   # Creates the turtle's head
head.shape("turtle")                     # Cool turtle shape
head.color("lime")                       # Bright green head
head.penup()                            # No drawing lines
head.goto(0, 0)                         # Start at center
head.direction = "stop"                 # Initially stopped

# ---------------------- Food System ----------------------
food = turtle.Turtle()                  # Regular food
food.shape("circle")                    
food.color("red")                       
food.penup()                           
food.goto(0, 100)                       

# BONUS FOOD - Worth more points and changes colors!
bonus_food = turtle.Turtle()            
bonus_food.shape("square")              
bonus_food.color("gold")                
bonus_food.penup()                      
bonus_food.goto(150, 150)               
bonus_visible = False                   # Bonus food appears randomly

# ---------------------- Power-ups ----------------------
speed_boost = turtle.Turtle()           # Speed boost power-up
speed_boost.shape("triangle")           
speed_boost.color("cyan")               
speed_boost.penup()                     
speed_boost.goto(-150, -150)            
speed_boost_active = False              
boost_timer = 0                         

# ---------------------- Turtle Body ----------------------
segments = []                           # List to store body segments

# ---------------------- Score & Level System ----------------------
score = 0                               
high_score = 0                          
level = 1                               # Start at level 1
lives = 3                               # Player has 3 lives!
game_speed = 0.15                       # Starting speed

# ---------------------- Enhanced Scoreboard ----------------------
scoreboard = turtle.Turtle()            
scoreboard.speed(0)                     
scoreboard.color("white")               
scoreboard.penup()                      
scoreboard.hideturtle()                 
scoreboard.goto(0, 250)                 

# Lives display
lives_display = turtle.Turtle()         
lives_display.speed(0)                  
lives_display.color("red")              
lives_display.penup()                   
lives_display.hideturtle()              
lives_display.goto(-350, 250)           

# Level display
level_display = turtle.Turtle()         
level_display.speed(0)                  
level_display.color("cyan")           
level_display.penup()                   
level_display.hideturtle()              
level_display.goto(250, 250)            

# Fun messages for achievements!
message_display = turtle.Turtle()       
message_display.speed(0)                
message_display.color("orange")         
message_display.penup()                 
message_display.hideturtle()            
message_display.goto(0, 200)            

def update_display():
    """Updates all the game displays"""
    scoreboard.clear()
    lives_display.clear()
    level_display.clear()
    
    scoreboard.write(f"SCORE: {score}  HIGH: {high_score}", 
                    align="center", font=("Arial", 18, "bold"))
    lives_display.write(f"❤️ LIVES: {lives}", 
                       align="left", font=("Arial", 16, "bold"))
    level_display.write(f"⭐ LEVEL: {level}", 
                       align="center", font=("Arial", 16, "bold"))

def show_message(text, duration=2):
    """Shows exciting messages to the player"""
    message_display.clear()
    message_display.write(text, align="center", font=("Arial", 20, "bold"))
    wn.ontimer(lambda: message_display.clear(), duration * 1000)

def color_cycle():
    """Changes turtle head color for fun effects"""
    global current_color
    head.color(head_colors[current_color])
    current_color = (current_color + 1) % len(head_colors)

# Initial display
update_display()

# ---------------------- Movement Functions ----------------------
def go_up():                             # Function to move the head up
    if head.direction != "down":         # Prevents the turtle from going in the opposite direction
        head.direction = "up"            # Sets the direction to up

def go_down():                           # Function to move the head down
    if head.direction != "up":           # Prevents reverse
        head.direction = "down"          # Sets the direction to down

def go_left():                           # Function to move the head left
    if head.direction != "right":        # Prevents reverse
        head.direction = "left"          # Sets the direction to left

def go_right():                          # Function to move the head right
    if head.direction != "left":         # Prevents reverse
        head.direction = "right"         # Sets the direction to right

# Function to move the turtle forward one step
def move():
    if head.direction == "up":           # If direction is up
        y = head.ycor()                  # Get current y position
        head.sety(y + 20)                # Move up by 20 pixels
    if head.direction == "down":         # If direction is down
        y = head.ycor()                  # Get current y position
        head.sety(y - 20)                # Move down by 20 pixels
    if head.direction == "left":         # If direction is left
        x = head.xcor()                  # Get current x position
        head.setx(x - 20)                # Move left by 20 pixels
    if head.direction == "right":        # If direction is right
        x = head.xcor()                  # Get current x position
        head.setx(x + 20)                # Move right by 20 pixels

# ---------------------- Keyboard Bindings ----------------------
wn.listen()                              # Tells the screen to start listening for key presses
wn.onkeypress(go_up, "Up")               # Calls go_up() when "Up" arrow is pressed
wn.onkeypress(go_down, "Down")           # Calls go_down() when "Down" arrow is pressed
wn.onkeypress(go_left, "Left")           # Calls go_left() when "Left" arrow is pressed
wn.onkeypress(go_right, "Right")         # Calls go_right() when "Right" arrow is pressed

# Extra controls for fun!
wn.onkeypress(go_up, "w")               # WASD controls too!
wn.onkeypress(go_down, "s")             
wn.onkeypress(go_left, "a")             
wn.onkeypress(go_right, "d")            

# ---------------------- Main Game Loop ----------------------
move_counter = 0                        # Counter for special effects
while True:                              # Infinite loop for game execution
    wn.update()                          # Manually update the screen
    move_counter += 1                    # Increment counter

    # ---- Cool Color Effects ----
    if move_counter % 10 == 0:          # Every 10 moves, change head color!
        color_cycle()
    
    # ---- Show/Hide Bonus Food ----
    if move_counter % 50 == 0:          # Every 50 moves, chance for bonus food
        if not bonus_visible and random.randint(1, 3) == 1:  # 33% chance
            bonus_visible = True
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            bonus_food.goto(x, y)
            show_message("💎 BONUS FOOD APPEARED! 💎")
    
    # ---- Hide bonus food after time ----
    if bonus_visible and move_counter % 100 == 0:
        bonus_visible = False
        bonus_food.goto(1000, 1000)  # Hide it
    
    # ---- Speed Boost Timer ----
    if speed_boost_active:
        boost_timer -= 1
        if boost_timer <= 0:
            speed_boost_active = False
            game_speed = 0.15  # Back to normal speed
            show_message("⚡ Speed Boost Ended! ⚡")

    # ---- Check collision with regular food ----
    if head.distance(food) < 20:         # If head is close to food
        x = random.randint(-290, 290)    # Generate new random x coordinate for food
        y = random.randint(-290, 290)    # Generate new random y coordinate for food
        food.goto(x, y)                  # Move food to the new location

        # Create a new segment (body part) with random color!
        new_segment = turtle.Turtle()    # New turtle for the segment
        new_segment.shape("square")      # Shape of the body segment
        new_segment.color(random.choice(body_colors))  # Random body color!
        new_segment.penup()              # Prevent drawing
        segments.append(new_segment)     # Add segment to the list

        # Increase the score
        score += 10                      # Add 10 points
        if score > high_score:           # Update high score if needed
            high_score = score
            show_message("🏆 NEW HIGH SCORE! 🏆")

        # Level up system!
        if score % 50 == 0 and score > 0:  # Every 50 points = new level
            level += 1
            game_speed *= 0.9  # Increase speed slightly
            show_message(f"🌟 LEVEL {level} UNLOCKED! 🌟")

        update_display()                 # Update all displays

    # ---- Check collision with BONUS food ----
    if bonus_visible and head.distance(bonus_food) < 20:
        bonus_visible = False
        bonus_food.goto(1000, 1000)  # Hide it
        
        # Bonus food gives MORE points and creates 2 segments!
        score += 25  # Bonus points!
        for _ in range(2):  # Create 2 segments!
            new_segment = turtle.Turtle()
            new_segment.shape("square")
            new_segment.color("gold")  # Golden segments for bonus!
            new_segment.penup()
            segments.append(new_segment)
        
        if score > high_score:
            high_score = score
            
        show_message("💰 BONUS COLLECTED! +25 POINTS! 💰")
        update_display()

    # ---- Check collision with speed boost ----
    if head.distance(speed_boost) < 20:
        speed_boost.goto(1000, 1000)  # Hide it
        speed_boost_active = True
        boost_timer = 100  # Active for 100 moves
        game_speed = 0.05  # Much faster!
        show_message("🚀 SPEED BOOST ACTIVATED! 🚀")
        
        # Move speed boost to new location after some time
        wn.ontimer(lambda: speed_boost.goto(random.randint(-290, 290), random.randint(-290, 290)), 5000)

    # ---- Check collision with wall ----
    if (head.xcor() > 390 or head.xcor() < -390 or 
        head.ycor() > 290 or head.ycor() < -290):  # If head touches wall boundary
        lives -= 1  # Lose a life instead of instant game over!
        
        if lives > 0:
            show_message(f"💥 CRASH! {lives} Lives Left! 💥", 3)
            time.sleep(2)               # Pause the game for 2 seconds
            head.goto(0, 0)             # Reset head to center
            head.direction = "stop"     # Stop the turtle
            
            # Keep some segments (don't lose everything!)
            segments_to_keep = len(segments) // 2  # Keep half the segments
            for i in range(segments_to_keep, len(segments)):
                segments[i].goto(1000, 1000)  # Remove extra segments
            segments = segments[:segments_to_keep]  # Keep only half
            
        else:
            # Game Over - but with style!
            show_message("💀 GAME OVER! Press SPACE to restart! 💀", 5)
            time.sleep(3)
            head.goto(0, 0)
            head.direction = "stop"
            
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            
            # Reset everything
            score = 0
            lives = 3
            level = 1
            game_speed = 0.15
            
        update_display()

    # ---- Move the body segments ----
    for i in range(len(segments) - 1, 0, -1):   # Move segments in reverse order
        x = segments[i - 1].xcor()      # Get x of previous segment
        y = segments[i - 1].ycor()      # Get y of previous segment
        segments[i].goto(x, y)          # Move current segment to previous position

    # Move the first segment to the head’s position
    if len(segments) > 0:
        x = head.xcor()                 # Get current x of head
        y = head.ycor()                 # Get current y of head
        segments[0].goto(x, y)          # Move first segment to follow head

    # ---- Move the head forward ----
    move()                              # Move head in its current direction

    # ---- Check collision with self ----
    for segment in segments:            # Loop through all segments
        if segment.distance(head) < 20: # If any segment is too close to the head
            lives -= 1  # Lose a life
            
            if lives > 0:
                show_message(f"🐢 Ate Yourself! {lives} Lives Left! 🐢", 3)
                time.sleep(2)
                head.goto(0, 0)
                head.direction = "stop"
                
                # Remove half the segments as penalty
                segments_to_keep = len(segments) // 2
                for i in range(segments_to_keep, len(segments)):
                    segments[i].goto(1000, 1000)
                segments = segments[:segments_to_keep]
                
            else:
                show_message("💀 GAME OVER! You ran out of lives! 💀", 5)
                time.sleep(3)
                head.goto(0, 0)
                head.direction = "stop"
                
                for segment in segments:
                    segment.goto(1000, 1000)
                segments.clear()
                
                score = 0
                lives = 3
                level = 1
                game_speed = 0.15
                
            update_display()
            break  # Exit the collision check loop

    # ---- Control game speed (gets faster as you level up!) ----
    time.sleep(game_speed)                     # Variable speed based on level