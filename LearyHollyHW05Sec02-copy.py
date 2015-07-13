from graphics import *

def test():

    # Create graphics window.
    win = GraphWin("Yacht Rental",600,600)
    win.setBackground("paleturquoise")
    
    # Define window coordinates.
    win.setCoords(0,0,100,100)

    # Create banner
    brown = Rectangle(Point(0,85), Point(101,98))
    brown.setFill("saddle brown")
    brown.setOutline("saddle brown")
    brown.draw(win)

    blue = Rectangle(Point(0,86), Point(101,96))
    blue.setFill("mediumturquoise")
    blue.setOutline("mediumturquoise")
    blue.draw(win)

    mid = Rectangle(Point(0,87), Point(101,94))
    mid.setFill("ivory")
    mid.setOutline("ivory")
    mid.draw(win)
              
    # Place title.
    title = Text(Point(22,90.5), "YACHT Rental")
    title.setSize(17)
    title.setFill("black")
    title.setStyle("bold")
    title.draw(win)

    # Introduction
    intro = [0,1,2]
    intro_height = 81
    intro_text = ["Welcome. Please fill out your name, the type of yacht you would like to rent",
                  "(add the name of a yacht if you don't see it), enter the size you want, and the number of hours",
                  "you will be chartering the yacht. Then press the Total button."]

    # Place introduction.
    for i in range (3):
        intro[i] = Text(Point(50,intro_height), intro_text[i])
        intro[i].setSize(10)
        intro[i].setStyle("italic")
        intro[i].draw(win)
        intro_height = intro_height - 3

    # Required fields title.
    required = Text(Point(30, 68), "Required Fields:")
    required.setStyle("bold")
    required.draw(win)

    # Required Fields Section
    field_text_iteration =[0,1,2,3]
    field_text = ["Name:", "Yacht:", "Size:", "Hours:"]
    user_entry = [0,1,2,3]
    field_height = 62
    # Text and Entry boxes for name, yacht type, size, and hours AND Yachts
    for i in range (4):
        field_text_iteration[i] = Text(Point(10,field_height), field_text[i])
        field_text_iteration[i].setSize(12)
        field_text_iteration[i].setStyle("bold")
        field_text_iteration[i].draw(win)
        user_entry[i] = Entry(Point(30, field_height), 15)
        user_entry[i].setFill("ivory")
        #user_entry.setSize(14)
        user_entry[i].draw(win)
        field_height = field_height - 6
    
    # Add a Total button.
    total_rectangle = Rectangle(Point(18.5, 35.5),Point(41.5, 39.5))
    total_rectangle.setFill("gold")
    total_rectangle.setWidth(2)
    total_rectangle.draw(win)
    total_text = Text(Point(30, 37.5),"Total")
    total_text.setStyle("bold")
    total_text.setSize(11)
    total_text.draw(win)
    
    # Create Add a Yacht button.
    yacht_rectangle = Rectangle(Point(60.5, 60),Point(83.5, 64))
    yacht_rectangle.setFill("gold")
    yacht_rectangle.setWidth(2)
    yacht_rectangle.draw(win)
    
    # Yacht button.
    yacht_title = Text(Point(72, 62), "Add a Yacht")
    yacht_title.setStyle("bold")
    yacht_title.draw(win)

    
    size_height = 24    
    size_iteration = [0,1,2,3,4]
    size_text = ["20  -  $300   ", "24  -  $400   ", "30  -  $550   ", "32  -  $600   ", "50  -  $1,200"]
  
    # Sizes title
    size_title = Text(Point(80, 29), "Sizes:")
    size_title.setStyle("bold")
    size_title.draw(win)

    # Display sizes and prices.
    for i in range (5):
        size_iteration[i] = Text(Point(81,size_height - 1), size_text[i])
        size_iteration[i].setSize(11)
        #size_iteration[i].setStyle("bold")
        size_iteration[i].draw(win)
        size_height = size_height - 3

    # Display box
    display_box = Rectangle(Point(10, 7.5), Point(67,30))
    display_box.setFill("ivory")
    display_box.setWidth(2)
    display_box.setOutline("saddle brown")
    display_box.draw(win)

    infile = open("yachts.txt", "r")

    # Required Fields Section
    yacht_iteration =[0,1,2]
    yacht_type = ['','','']
    
    field_height = 55
    # Text and Entry boxes for name, yacht type, size, and hours AND Yachts
    for i in range (3):
        yacht_type[i] = (infile.readline()[:-1])
        yacht_iteration[i] = Text(Point(72,field_height), yacht_type[i])
        yacht_iteration[i].setSize(13)
        #yacht_iteration[i].flushleft(10)
        #yacht_iteration[i].setStyle("bold")
        #yacht_iteration[i].setFill("gray")
        yacht_iteration[i].draw(win)
        field_height = field_height - 4
       
    # Create if statements for yacht button, append to list, and print in list
    click = win.getMouse()
    x = click.getX()
    y = click.getY()

    field_height = 61
    # If Add Yacht button is pressed:  
    if (60.5 <= x <= 83.5) and (60 <= y <= 64):

        yacht_entry = user_entry[1] 
        yacht_type.append(yacht_entry.getText())

        appended_yacht = Text(Point(72, 43), yacht_type[3])
        appended_yacht.setSize(13)
        appended_yacht.draw(win)

        #user_entry[1].delete(user_entry[1].getX(), user_entry[1].getY())
        #user_entry.setSize(14)
     
        
        user_entry[1].setText("")
        user_entry[1].draw(win)
            
        click2 = win.getMouse()
        x = click2.getX()
        y = click2.getY()
        
    #else error code
    if (18.5 <= x <= 41.5) and (35.5 <= y <= 39.5):
        print("total")

    else:
        print("nope")
        

    # Read entries

    # Name entry
    name = user_entry[0].getText()

    #Size entry    
    size = user_entry[2].getText()
    size_float = int(size)
 
    if size == 20:
        hourly_rate = 300
    elif size == 24:
        hourly_rate = 400
    elif size == 30:
        hourly_rate = 550
    elif size == 32:
        hourly_rate = 600
    elif size == 50:
        hourly_rate = 1200
    
    else:
        error_message = Text(Point(32,22), "Error message: Please enter a listed size.")
        error_message.setSize(10)
        error_message.setFill("red")
        error_message.draw(win)  
        # print star 

    # Hours entry
    hours = user_entry[3].getText()
    print(hours)
    hours_float = float(hours)
    print(hours_float)
    
    '''if hours != int or hours != float:
        error_message = Text(Point(32,26), "Error message: Please enter hours.")
        error_message.setSize(10)
        error_message.setFill("red")
        error_message.draw(win)
    else:'''

    # If all entries go to plan:

    # Message
    message = Text(Point(32,22), "Thank you for renting a today")
    message.setSize(10)
    message.draw(win)
    
    # Calculations
    subtotal = hours * hourly_rate
    tax = subtotal * 0.085
    total = subbtotal + tax

    # Print subtotal
    subtotal = hourly_rate * hours
    subtotal_message = Text(Point(32,18), "Your subtotal is ", subtotal)
    subtotal_message.setSize(10)
    subtotal_message.draw(win)

    # Print tax
    tax_message = Text(Point(32,15), "Tax is ", tax)
    tax_message.setSize(10)
    tax_message.draw(win)

    # Print total
    total_message = Text(Point(32,12), "Total is ", total)
    total_message.setSize(10)
    total_message.draw(win)



        
   

    # Create if statements for having correct fields (name is alphas, size is only given,
    # hours are numbers, yacht is listed or entered own).

    # Take out reduntant hashtags and commented out code
    # Fix enter file problem
    # Fix readfile continuancy
    # Comment
    # Check data types (str, int, etc.)
    # Fill out checklist
    
    infile.close()
    
test()
