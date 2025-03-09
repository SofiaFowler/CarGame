"""
hw5.py
A program that draws cars at random and allows the user to interact with and click cars to increase their score.
The car's color and the number of times each color was clicked is displayed and program allows user to pause and either continue where they left off or quit the game.
12/7  Sofia Fowler  final version
"""
from graphics import *
import time
import random


class Car(Rectangle):
    """
    input: rectangle class from graphics library
    process: draws, undraws, gets color and gets score for each car shown to the user in the window
    output: allows the user to interact with cars shown on the graphics window
    """
    def __init__(self, win, x, y, unit):
        """
        input: graphics window, x and y coordinate, and a random unit
        process: determines a random color, the score, and the points for a car
        output: list of objects in one car and initializes the parent class
        """
        colorlist = ["green","yellow","red","purple","orange","blue"]
        ranColor = random.randrange(0,len(colorlist))
        self.color = colorlist[ranColor]

        p1 = Point(x-(unit*4),y)
        p2 = Point(x+(unit*4),y+(unit*3))
        p3 = Point(x, y+(unit*4))

        super().__init__(p1,p2)
        
        self.carlist = self.drawCar(win,p1,p2,p3,unit)
        self.carlist.append(super())

        self.score = int(unit*10)

  
    def getColor(self):
        """
        process: when called, returns the color determined
        """ 
        return self.color

    def getScore(self):
        """
        process: when called, returns the score determined
        """
        return self.score


    def drawCar(self, win, p1, p2, p3,unit):
        """
        input: the graphics window, the three points determined and the unit
        process: creates the tires, body and roof of the car, using the three points and unit
        output: draws all the parts of the car to the window and returns the list of car parts
        """
        self.carlist=[]

        self.tire_left= Circle(Point(p1.x+abs(p2.x-p1.x)/4,p1.y),abs(p2.x-p1.x)/8)
        self.tire_left.setFill("black")
        self.tire_left.draw(win)
        self.carlist.append(self.tire_left)
        
        self.tire_right= Circle(Point(p2.x-abs(p2.x-p1.x)/4,p1.y),abs(p2.x-p1.x)/8)
        self.tire_right.setFill("black")
        self.tire_right.draw(win)
        self.carlist.append(self.tire_right)
        
        self.body = Rectangle(Point(p1.x,p1.y),Point(p2.x,p2.y))
        self.body.setFill(self.color)
        self.body.draw(win)
        self.carlist.append(self.body)
        
        width = 2*(unit*4)
        pp1_x = p1.x+width/4
        pp1_y = p2.y
        pp2_x = p2.x-width/4
        pp2_y = p2.y
        pp3_x = p1.x+3*width/8
        pp3_y = p3.y
        pp4_x = p2.x-3*width/8
        pp4_y = p3.y
        self.roof = Polygon(Point(pp1_x,pp1_y), Point(pp3_x,pp3_y), Point(pp4_x,pp4_y),Point(pp2_x,pp2_y))
        self.roof.setFill("black")
        self.roof.draw(win)
        self.carlist.append(self.roof)
        return self.carlist


    def move(self, Xdistance):
        """
        input: the distance in the x-direction that the car will move every iteration
        process: uses the car list with the appended super function and uses a for loop to iterate through every object in the list
        output: moves every object in the car list a distance in the x-direction on the window
        """
        Ydistance = 0
        
        allTheCars = self.carlist
        for part in allTheCars:
            part.move(Xdistance,Ydistance)

    
    def undraw(self):
        """
        input: car list
        process: when called, every object in the carlist will be undrawn
        output: car is undrawn from the graphics window
        """
        allTheCars = self.carlist
        for part in allTheCars:
            part.undraw()


def isClicked(pclick,rec):
    """
    input: takes the users click and a rectangle
    process: gets the x and y coordinates of the two points of the rectangle and the x and y coordinate of the click and compares them
    output: if the user clicked within the box, then True is return. Otherwise, False is returned
    """
    p1 = rec.getP1()
    p2 = rec.getP2()
    if p1.getX() <= pclick.getX() <= p2.getX() and p1.getY() <= pclick.getY() <= p2.getY():
        return True
    return False


def draw_buildings(win, p1_x,p1_y,p2_x,p2_y,color):
    """
    input: graphics window, x and y coordinates of 2 points and a color
    process: creates a rectangle based on the points and fills it with the color given
    output: draws the rectangle to the graphics window
    """
    shape=Rectangle(Point(p1_x,p1_y),Point(p2_x,p2_y))
    shape.setFill(color)
    shape.draw(win)

    
def main():
    """
    input: a graphics window with buttons used for user interaction
    proccess: draws, moves and erases cars of random size and color as well as records the score, count and color of the car
    output: allows the user to click on the moving cars to increase their score as well as pause and continue or pause and quit the game
    """
    win = GraphWin("Moving Cars", 800, 600)
    win.setCoords(0, 0, 40, 40)
    bg = Rectangle(Point(0,25), Point(40, 40))
    bg.setFill("light blue")
    bg.draw(win)
    ground = Rectangle(Point(0,6) , Point(40, 24))
    ground.setFill("light grey")
    ground.draw(win)
    temp=4

    # uses a temporary variable and draws ground lines based on the temporary value and assigns a new temporary value
    while temp<40:
        gnd_lines1= Line(Point(temp,10),Point(temp+4,10))
        gnd_lines1.setWidth(5)
        gnd_lines1.setFill("white")
        gnd_lines2= Line(Point(temp,15),Point(temp+4,15))
        gnd_lines2.setWidth(5)
        gnd_lines2.setFill("white")
        gnd_lines3= Line(Point(temp,20),Point(temp+4,20))
        gnd_lines3.setWidth(5)
        gnd_lines3.setFill("white")
        temp=temp+10
        gnd_lines1.draw(win)
        gnd_lines2.draw(win)
        gnd_lines3.draw(win)
        sun = Circle(Point(37,38), 1.5)
        sun.setFill("yellow")
        sun.setOutline("yellow")
        sun.draw(win)

  

    # opens, reads, splits each line from the file and draws buildings to the graphics window
    with open('hw5_input.txt','r') as file:
        # reading each line
        for line in file:
            coordinates=[]
            # reading each word
            for word in line.split():
                # displaying the words
                coordinates.append(word)
            draw_buildings(win,coordinates[0],coordinates[1],coordinates[2],coordinates[3],coordinates[4].strip())

    # establishes all of the messages, buttons and variables that will be used throughout the gamestates
    button = Rectangle(Point(2,2), Point(6, 4))
    button.setFill("gray")
    button.draw(win)
    label = Text(Point(4, 3), "Start")
    label.setStyle("bold")
    label.setTextColor("white")
    label.draw(win)
    bottom_message = Text(Point(12, 5), "Please click the Start button to begin")
    bottom_message.setStyle("bold")
    bottom_message.setTextColor("green")
    bottom_message.draw(win)
    car_on_screen_message = Text(Point(15, 27), "")
    car_on_screen_message.setStyle("bold")
    car_on_screen_message.setTextColor("purple")
    car_on_screen_message.draw(win)
    score_title = Text(Point(15, 3), "Current Score: ")
    score_title.setStyle("bold")
    score_title.setSize(18)
    score_title.setTextColor("blue")
    score_title.draw(win)
    score_message = Text(Point(21, 3), "0")
    score_message.setStyle("bold")
    score_message.setSize(18)
    score_message.setTextColor("blue")
    score_message.draw(win)
    clicked_colors_message = Text(Point(29, 5), "")
    clicked_colors_message.setStyle("bold")
    clicked_colors_message.setTextColor("black")
    clicked_colors_message.draw(win)
    ExitAll = []
    exit_bg = Rectangle(Point(10,5), Point(30, 20))
    exit_bg.setFill("light gray")
    ExitAll.append(exit_bg)
    exit_message = Text(Point(20, 15), "Click Exit to stop \n or Resume to continue")
    exit_message.setSize(18)
    exit_message.setStyle("bold")
    exit_message.setTextColor("red")
    ExitAll.append(exit_message)
    confirm_button = Rectangle(Point(13, 7), Point(17, 9))
    confirm_button.setFill("gray")
    ExitAll.append(confirm_button)
    confirm_label = Text(Point(15, 8), "Exit")
    confirm_label.setStyle("bold")
    confirm_label.setTextColor("white")
    ExitAll.append(confirm_label)
    go_back_button = Rectangle(Point(23, 7), Point(27, 9))
    go_back_button.setFill("gray")
    ExitAll.append(go_back_button)
    go_back_label = Text(Point(25, 8), "Resume")
    go_back_label.setStyle("bold")
    go_back_label.setTextColor("white")
    ExitAll.append(go_back_label)
    mylabel=Text(Point(26,3),"Clicked Color:")
    mylabel.setStyle("bold")
    mylabel.draw(win)
    myrectangle=Rectangle(Point(29,2),Point(31,4))
    myrectangle.draw(win)
    pixel_per_second =10
    refresh_sec = 0.05
    gameState = 0 # 0 for initial mode, 1 for start mode, 2 for pause mode
    total_score = 0
    # list of all the cars on the screen
    car_list = []
    # dictionary of every color of car and the number of times they have been clicked by the user
    clicked_colors = {}
    start_time1 = 0
    start_time2 = 0
        
    
    # allows and checks for user clicks
    # checks where the user clicks and the gamestate and then produces a specific gamestate
    # the user sees one of 3 gamestates
    
    while True:
        pClick = win.checkMouse()
        
        # checks what the current gamestate is and then checks for a user click
        # there are different processes for each gamestate
        # shows the user the appropriate gamestate
        

        if gameState == 0: #initial
            time.sleep(0.1)
            if pClick != None:
                
                # takes in a click and button
                # new messages are set and the gamestae is set to 1
                # shows gamestate 1
                
                if isClicked(pClick, button):
                    bottom_message.setText("Click a moving car or Pause to stop")
                    label.setText("Pause")
                    gameState = 1
        
        
        elif gameState == 1: # start
            if pClick != None:
                
                #takes in a click and button
                # if button is clicked, draws the exit messages and changes to state 2
                # if car is clicked, it will change the score, color fill, and list of colors and record how many times they have been clicked
                # shows state 2 or shows the user all of the cars of random sizes and colors drawn
                
                if isClicked(pClick, button):
                    for parts in ExitAll:
                        parts.draw(win)
                    gameState = 2
            
                else:
                    for car in car_list:
                        if isClicked(pClick,car):
                            bonus = car.getScore()
                            theColor = car.getColor()
                            car.undraw()
                            car_list.remove(car)
                            integerCounter = clicked_colors.get(theColor,0) + 1
                            clicked_colors[theColor] = integerCounter
                            listOfColors = str(clicked_colors)
                            listOfColors = listOfColors.replace("{","")
                            listOfColors = listOfColors.replace("}","")
                            listOfColors = listOfColors.replace(":","")
                            listOfColors = listOfColors.replace("'","")
    
                            clicked_colors_message.setText("{}".format(listOfColors))
                            myrectangle.setFill(theColor)

                            total_score = total_score + int(100*(1/bonus))
                            score_message.setText(total_score)
        
                
            # if the gen time lag is greater than 1, then generate a new car
            # and reset timer for car generation
        
            # compares current time and start time
            # while the user is in gamestate 1, cars will be drawn at a random size and with a ranodom color and then be appended to the list of cars on the screen
            # draws the random car on the screen
    
            current_time = time.time()
            if (current_time - start_time1) >= 0.2:
                x = (random.random() - 0.5) + 4
                y = random.uniform(7,23)
                unit = (random.random()*.6) + .4
                
                ran_car = Car(win,x,y,unit)
                car_list.append(ran_car)
                
                start_time1 = current_time + 1
        
            # if moving time lag is greater than refesh,
            # set proportional distance to the lag. Then check whether car goes outside window
            
            # compares current time and start time
            # while the user is in gamestate 1, the cars in the car list will be moved until they hit the end of the window where they will be undrawn and removed from the list of cars in the window
            # continuely shows cars of random sizes and colors being drawn and moving from the left to right and then being undrawn at the end

            if current_time - start_time2 >= refresh_sec:
                Xdistance = pixel_per_second*refresh_sec
                Ydistance = 0
                ran_car_x = ran_car.getP2().getX()
                for ran_car in car_list:
                    ran_car.move(Xdistance)
                    if ran_car.getP2().getX() >= 40:
                        ran_car.undraw()
                        car_list.remove(ran_car)
                    start_time2 = current_time
        
    
        elif gameState == 2: # pause
            time.sleep(0.1)
            if pClick != None:
        
                # takes in a click and button
                # checks is the user clicked the button and opens the window and allows the user to quit or continue the game
                # shows the user gamestate 1 if they click continue and closes the app if they click quit

                if isClicked(pClick, confirm_button):
                    win.close()
                    break
                elif isClicked(pClick, go_back_button):
                    for parts in ExitAll:
                        parts.undraw()
                    gameState = 1

    
        
if __name__ == '__main__':
    main()
