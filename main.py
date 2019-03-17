import upygame as upg
import umachine as pok
import framebuf
import urandom as rand
import sprites

upg.display.init()
screen = upg.display.set_mode() # full screen

# Set palette
upg.display.set_palette_16bit([0xffff,0x03bb,0xf017,65535,0x5acb,0x07e8,0x0000,0xf800]);


narwhal_sprites = sprites.narwhal_sprites
enemies_sprites = sprites.enemies_sprites
charge_jar = sprites.charge_jar


index = 0
position = 1 #0 up, 1 middle, 2 down
time = 0
speed = 2#speed of the obstacles
mult = 1 #number of obstacles
current = 0 #current obstacles

cx = 0
cy = 0
cind = {}
y = 35
x = 4
score = 0
charge = 0
dashing = False
best = 0
boost = 2
boost_time = 0
def init():
    global boost,boost_time, index, position, time, speed, mult, current, cx, cy, cind, x, y, score, charge, dashing, best
    index = 0
    position = 1 #0 up, 1 middle, 2 down
    time = 0
    speed = 2#speed of the obstacles
    mult = 1 #number of obstacles
    current = 0 #current obstacles

    cx = 0
    cy = 0
    cind = {}
    y = 35
    x = 4
    score = 0
    charge = 0
    dashing = False
    boost = 2
    boost_time = 0
    
#collide with asteroid
def collide(rx, ry, ax, ay):
    if ((rx < ax + 16) and (rx + 24 > ax) and (ry < ay + 50) and (ry + 18 > ay)):
        return True
    else:
        return False
###########################

title = True
gameover = False
while True:
    time += 1
    screen.fill(1, upg.Rect(0,0,110,88)) 
    
    if title:
        pok.draw_text(3, 2, "Explore the ocean  depths!",6)
        pok.draw_text(3, 3, "Explore the ocean  depths!",3)
        
        pok.draw_text(20, 70, "Best:\n     "+str(best),6)
        pok.draw_text(20, 71, "Best:\n     "+str(best),3)
        
        if time <= 5:
            index = 0
        if time <= 10 and time > 5:
            index = 1
        if time <= 15 and time > 10:
            index = 2
        if time <= 20 and time > 15:
            index = 1
            
        if time > 20:
            time = 0
        screen.blit(narwhal_sprites[index], 45,25)
        
        screen.blit(enemies_sprites[0], 2,38)
        screen.blit(enemies_sprites[1], 90,38)
        
        eventtype = upg.event.poll()
        if eventtype != upg.NOEVENT:
            if eventtype.type == upg.KEYDOWN:
                title = False
                gameover = False
                init()
    elif gameover:
        pok.draw_text(3, 2, "Game over...",6)
        pok.draw_text(3, 3, "Game over...",3)
        
        pok.draw_text(3, 12, "Best:\n "+str(best),6)
        pok.draw_text(3, 13, "Best:\n "+str(best),3)
        screen.blit(cind["spr"], 45, 24)
        eventtype = upg.event.poll()
        if eventtype != upg.NOEVENT:
            if eventtype.type == upg.KEYDOWN:
                title = True
                gameover = False
                init()
    else:
        boost_time+=1
        score = score+ 1*mult
        speed = boost*mult
        
        if boost_time > 500:
            boost += 1
            boost_time = 0
       
        eventtype = upg.event.poll()
        if eventtype != upg.NOEVENT:
            if eventtype.type== upg.KEYDOWN:
                if eventtype.key == upg.K_UP:
                    position = 0
                if eventtype.key == upg.K_DOWN:
                    position = 2
                if eventtype.key == upg.K_RIGHT or eventtype.key == upg.BUT_A:
                    if charge > 0 and not dashing:
                        dashing = True
                if eventtype.key == upg.K_LEFT or eventtype.key == upg.BUT_B:
                    mult = -2
            if eventtype.type == upg.KEYUP:
                if eventtype.key == upg.K_UP:
                    position = 1
                if eventtype.key == upg.K_DOWN:
                    position = 1
                if eventtype.key == upg.K_RIGHT or eventtype.key == upg.BUT_A:
                    dashing = False
                if eventtype.key == upg.K_LEFT or eventtype.key == upg.BUT_B:
                    mult = 1
    
        if position is 0:
            y = 5
        if position is 1:
            y = 35
        if position is 2:
            y = 65
            
        if time <= 5:
            index = 0
        if time <= 10 and time > 5:
            index = 1
        if time <= 15 and time > 10:
            index = 2
        if time <= 20 and time > 15:
            index = 1
        
            
            
        
        #Dashing
        if dashing and charge > 0:
            if charge - 5 <= 0:
                charge = 0
                dashing = False
            else:
                charge -= 5
                mult = 2
                x = 19
                index = 3
        if not dashing:
            x = 4
            mult = 1
            
        if time > 20:
            time = 0
            if charge < 100 and not dashing:
                if charge + 25 > 100:
                    charge = 100
                else:
                    charge += 25
        screen.blit(narwhal_sprites[index], x, y) 
        
        #enemies
        if current == 0:
            current += 1
            spr = rand.getrandbits(3)-1
            y = 0
            if spr < 2:
                y = 38
            
            cind = {"id": spr, "spr": enemies_sprites[spr], "x": 110, "y": y}
        else:
            screen.blit(cind["spr"], cind["x"], cind["y"])
            cind["x"]-=speed
            if cind["x"] < -16:
                current = 0
        
        if collide(x,y,cind["x"], cind["y"]):
            if cind["id"] > 3 and dashing:
                print("Close call")   
            else:
                gameover = True
                if score > best:
                    best = score
            
        pok.draw_text(3, 3, "Distance: "+str(score), 6) 
        pok.draw_text(2, 2, "Distance: "+str(score), 3) 
        
        #charge draw
        screen.fill(7, upg.Rect(3,83,charge,3)) 
        screen.blit(charge_jar, 2, 82)
       
    upg.display.flip()# Do regardless
