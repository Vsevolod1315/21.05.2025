shar_x=300
shar_dx=4
shar_y=300
shar_dy=2
ladder_x=300
lk=0
def setup():
    size(600,600)
def draw():
    global shar_x,shar_dx,shar_y,shar_dy,ladder_x,lk
    background(255)
    textSize(20)
    fill(1)
    text(lk,570,20)
    ellipse(shar_x,shar_y,60,60)
    shar_x = shar_x + shar_dx  
    shar_y = shar_y + shar_dy 
    if shar_x > 580:     
       shar_dx = -shar_dx  
    if shar_x < 20:    
         shar_dx = -shar_dy
    if shar_y < 20:
        shar_dy = -shar_dy
    if shar_y > 600:
        textSize(20)
        fill(37,214,44)
        text(u'пройгрыш',300,300)
    if keyPressed and key == CODED:   
        if keyCode == LEFT:    
           ladder_x = ladder_x - 4      
        if keyCode == RIGHT:       
           ladder_x = ladder_x + 4
    rect(ladder_x,570,80,20)
    if collideRectCircle(ladder_x, 570, 80, 20,   shar_x, shar_y, 60):  
        lk=lk+1 
        shar_dy = -random(4,6)    
        shar_dx = random(-5, 5)
def collideRectCircle(rx, ry, rw, rh, cx, cy, diameter):
    radius = diameter / 2
    testX = cx
    testY = cy

    if cx < rx:
        testX = rx
    elif cx > rx + rw:
        testX = rx + rw

    if cy < ry:
        testY = ry
    elif cy > ry + rh:
        testY = ry + rh

    distX = cx - testX
    distY = cy - testY
    distance = sqrt((distX * distX) + (distY * distY))

    return distance <= radius
