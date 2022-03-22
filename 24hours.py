from operator import truediv
import os
import pygame
import random

pygame.init()
gameRunning = True
gameReady = True

while gameRunning:
    if gameReady:
        windowSize = 750
        win = pygame.display.set_mode((windowSize, windowSize))

        pygame.display.set_caption("24 Hours")

        bg = pygame.image.load(os.path.join('images', 'background.png'))
        bighourglasspic = pygame.image.load(os.path.join('images', 'big_hourglass.png'))
        char = pygame.image.load(os.path.join('images', 'character.png'))
        rockpic = pygame.image.load(os.path.join('images', 'rock.png'))
        treepic = pygame.image.load(os.path.join('images', 'tree.png'))
        woodpic = pygame.image.load(os.path.join('images', 'wood.png'))
        stickpic = pygame.image.load(os.path.join('images', 'stick.png'))
        pineconepic = pygame.image.load(os.path.join('images', 'pinecone.png'))
        stonepic = pygame.image.load(os.path.join('images', 'stone.png'))
        ironpic = pygame.image.load(os.path.join('images', 'iron.png'))
        woodenchiselpic = pygame.image.load(os.path.join('images', 'wood_chisel.png'))
        logpic = pygame.image.load(os.path.join('images', 'log.png'))
        axepic = pygame.image.load(os.path.join('images', 'axe.png'))
        gravestonepic = pygame.image.load(os.path.join('images', 'gravestone.png'))
        cavepic = pygame.image.load(os.path.join('images', 'cave.png'))
        pickpic = pygame.image.load(os.path.join('images', 'pickaxe.png'))
        quartzpic = pygame.image.load(os.path.join('images', 'quartz.png'))
        goldpic = pygame.image.load(os.path.join('images', 'gold.png'))
        bushpic = pygame.image.load(os.path.join('images', 'bush.png'))

        forestAmbience = pygame.mixer.music.load(os.path.join('audio', 'forest_ambience.mp3'))

        heartbeataudio = pygame.mixer.Sound(os.path.join('audio', 'heartbeat.mp3'))
        heartbeataudio.set_volume(0.25)
        rockhitaudio = pygame.mixer.Sound(os.path.join('audio', 'rock.mp3'))
        rockhitaudio.set_volume(0.25)
        treehitaudio = pygame.mixer.Sound(os.path.join('audio', 'wood.mp3'))
        treehitaudio.set_volume(0.1)
        treefallaudio = pygame.mixer.Sound(os.path.join('audio', 'treefall.mp3'))
        treefallaudio.set_volume(0.25)
        cavehitaudio = pygame.mixer.Sound(os.path.join('audio', 'cave.mp3'))
        cavehitaudio.set_volume(0.25)
        loghitaudio = pygame.mixer.Sound(os.path.join('audio', 'log.mp3'))
        loghitaudio.set_volume(0.25)
        clickaudio = pygame.mixer.Sound(os.path.join('audio', 'click.mp3'))
        clickaudio.set_volume(0.25)
        craftaudio = pygame.mixer.Sound(os.path.join('audio', 'craft.mp3'))
        craftaudio.set_volume(0.25)
        pineconeaudio = pygame.mixer.Sound(os.path.join('audio', 'pinecone.mp3'))
        pineconeaudio.set_volume(0.25)
        equipaudio = pygame.mixer.Sound(os.path.join('audio', 'equip.mp3'))
        equipaudio.set_volume(0.25)
        rockbreakaudio = pygame.mixer.Sound(os.path.join('audio', 'rockbreak.mp3'))
        rockbreakaudio.set_volume(0.25)
        gravestoneplaceaudio = pygame.mixer.Sound(os.path.join('audio', 'gravestoneplace.mp3'))
        gravestoneplaceaudio.set_volume(0.25)
        dieaudio = pygame.mixer.Sound(os.path.join('audio', 'die.mp3'))
        dieaudio.set_volume(0.5)
        gravestonebreakaudio = pygame.mixer.Sound(os.path.join('audio', 'gravestonebreak.mp3'))
        gravestonebreakaudio.set_volume(0.25)

        timeQuotes = [
            "We keep on killing time until time finally kills us back.", "Time is a waste of money.", "The time you enjoy wasting is not wasted time.", "Time is a great teacher, but unfortunately it kills its pupils.", "Never waste any time you can spend sleeping.", "You can't turn back the clock. But you can wind it up again.", "The bad news is time flies. The good news is you're the pilot.", "There's never enough time to do all the nothing you want.", "Time is what keeps everything from happening at once.", "So little time and so little to do.", "Enjoy life. There's plenty of time to be dead.", "Time is an illusion.", "Day, n. A period of twenty-four hours, mostly misspent.", "The future is uncertain but the end is always near.", "Time you enjoy wasting is not wasted time.", "You may delay, but time will not.", "Time is what we want most, but what we use worst.", "Never waste a minute thinking about people you don’t like."
        ]

        deathMessages = [
            "Looks like time killed you back...", "You\'re out of time...", "It was about time...", "Looks like you wasted a bit too much time...", "Looks like somebody misspent their time...", "I hope you enjoyed wasting all that time...", "Time will never wait for you..."
        ]

        twentyFivePercent = [0, 0, 0, 1]
        thirtyThreePercent = [0, 0, 1]
        fiftyPercent = [0, 1]
        seventyFivePercent = [0, 1, 1, 1]
        sixtySixPercent = [0, 1, 1]

        worldBorderTop = (windowSize * -1) -500
        worldBorderBottom = windowSize + 500
        worldBorderLeft = (windowSize * -1) -500
        worldBorderRight = windowSize + 500

        clock = pygame.time.Clock()

        holdingRadiusItem = False
        holdingChisel = False
        holdingAxe = False
        holdingPickaxe = False

        class titleScreenButtons(object):
            def __init__(self, x, y, width, height, text):
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.text = text
            
            def draw(self):
                pygame.draw.rect(win, (255, 255, 0), (self.x, self.y, self.width, self.height), 0, 10)
                if self.text == 'PLAY':
                    titleScreenButtonText = titleScreenButtonFont.render('PLAY', 1, (0, 0, 0))
                    win.blit(titleScreenButtonText, (self.x + 33, self.y + 22))
                elif self.text == 'HELP':
                    titleScreenButtonText = titleScreenButtonFont.render('HELP', 1, (0, 0, 0))
                    win.blit(titleScreenButtonText, (self.x + 33, self.y + 22))
                elif self.text == 'CREDITS':
                    titleScreenButtonText = titleScreenButtonFont.render('CREDITS', 1, (0, 0, 0))
                    win.blit(titleScreenButtonText, (self.x + 27, self.y + 22))
                elif self.text == 'TITLE':
                    titleScreenButtonText = titleScreenButtonFont.render('TITLE', 1,  (0, 0, 0))
                    win.blit(titleScreenButtonText, (self.x + 18, self.y + 24))

            def onClick(self):
                global titleScreen
                global run
                global shownTitleScreen
                global gameReady
                if shownTitleScreen == 'main':
                    if self.text == 'PLAY':
                        if pos[1] < self.y + self.height and pos[1] > self.y:
                            if pos[0] > self.x and pos[0] < self.x + self.width:
                                clickaudio.play()
                                titleScreen = False
                                run = True
                    elif self.text == 'HELP':
                        if pos[1] < self.y + self.height and pos[1] > self.y:
                            if pos[0] > self.x and pos[0] < self.x + self.width:
                                clickaudio.play()
                                shownTitleScreen = "help"
                    elif self.text == 'CREDITS':
                        if pos[1] < self.y + self.height and pos[1] > self.y:
                            if pos[0] > self.x and pos[0] < self.x + self.width:
                                clickaudio.play()
                                shownTitleScreen = 'credits'
                    elif self.text == 'TITLE':
                        if pos[1] < self.y + self.height and pos[1] > self.y:
                                if pos[0] > self.x and pos[0] < self.x + self.width:
                                    clickaudio.play()
                                    titleScreen = True
                                    run = False
                                    shownTitleScreen = 'main'
                                    gameReady = True

        playButton = titleScreenButtons(50, 250, 200, 100, 'PLAY')
        howToPlayButton = titleScreenButtons(50, 375, 200, 100, 'HELP')
        creditsButton = titleScreenButtons(50, 500, 280, 100, "CREDITS")

        deathButton = titleScreenButtons(125, 450, 200, 100, "TITLE")

        class Player(object):
            def __init__(self, x, y, width, height, relPosX, relPosY):
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.vel = 5
                self.dead = False
                self.relPosX = relPosX
                self.relPosY = relPosY
            
            def draw(self, win):
                if not self.dead:
                    win.blit(char, (self.x, self.y))
                self.hitbox = (self.x - 2, self.y, self.width - 4, self.height)
                if showHitboxes:
                    pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

            def die(self):
                global chosenDeathMessage
                global gameReady
                self.dead = True
                chosenDeathMessage = random.choice(deathMessages)
                gameReady = False

        class terrainObjects(object):
            def __init__(self, x, y, width, height, type, health):
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.type = type
                self.health = health
                self.hitbox = (self.x, self.y, self.width, self.height)
            
            def draw(self, win):
                if self.type == "tree":
                    win.blit(treepic, (self.x, self.y))
                    self.hitbox = (self.x, self.y, self.width, self.height)
                    if showHitboxes:
                        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
                elif self.type == "rock":
                    win.blit(rockpic, (self.x, self.y))
                    self.hitbox = (self.x, self.y, self.width, self.height)
                    if showHitboxes:
                        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
                elif self.type == "log":
                    win.blit(logpic, (self.x, self.y))
                    self.hitbox = (self.x, self.y - 3, 24, 16)
                    if showHitboxes:
                        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
                elif self.type == "cave":
                    win.blit(cavepic, (self.x, self.y))
                    self.hitbox = (self.x, self.y, self.width, self.height)
                    if showHitboxes:
                        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
                elif self.type == "bush":
                    win.blit(bushpic, (self.x, self.y))
                    self.hitbox = (self.x, self.y, self.width, self.height)
                    if showHitboxes:
                        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

        class gravestoneObjects(object):
            def __init__(self, x, y):
                self.x = x
                self.y = y
            def draw(self):
                win.blit(gravestonepic, (self.x, self.y))

        class hotbarSpaces(object):
            def __init__(self, x, y, width, height, number, radius, selected):
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.number = number
                self.radius = radius
                self.contains = 'empty'
                self.selected = selected
            
            def draw(self, win):
                if self.number == 1:
                    self.contains = hotbar[0]
                elif self.number == 2:
                    self.contains = hotbar[1]
                elif self.number == 3:
                    self.contains = hotbar[2]
                elif self.number == 4:
                    self.contains = hotbar[3]
                elif self.number == 5:
                    self.contains = hotbar[4]

                pygame.draw.rect(win, (150, 150, 150), (self.x, self.y, self.width, self.height), 0, self.radius)
                if self.contains == 'wood' and Wood > 0:
                    win.blit(woodpic, (self.x + 8, self.y + 8))
                elif self.contains == 'stick' and Stick > 0:
                    win.blit(stickpic, (self.x + 10, self.y + 8))
                elif self.contains == 'pinecone' and Pinecone > 0:
                    win.blit(pineconepic, (self.x + 10, self.y + 8))
                elif self.contains == 'stone' and Stone > 0:
                    win.blit(stonepic, (self.x + 8, self.y + 8))
                elif self.contains == 'woodenchisel' and WoodenChisel > 0:
                    win.blit(woodenchiselpic, (self.x + 8, self.y + 8))
                elif self.contains == 'iron':
                    win.blit(ironpic, (self.x + 8, self.y + 8))
                elif self.contains == 'axe':
                    win.blit(axepic, (self.x + 8, self.y + 8))
                elif self.contains == 'gravestone':
                    win.blit(gravestonepic, (self.x + 10, self.y + 8))
                elif self.contains == 'pickaxe':
                    win.blit(pickpic, (self.x + 8, self.y + 8))
                elif self.contains == 'quartz':
                    win.blit(quartzpic, (self.x + 8, self.y + 7))
                elif self.contains == 'gold':
                    win.blit(goldpic, (self.x + 8, self.y + 7))
                
                if self.selected and self.number == 1:
                    pygame.draw.rect(win, (225, 225, 0), (16, 16, 32, 32), 3, self.radius)
                elif self.selected and self.number == 2:
                    pygame.draw.rect(win, (225, 225, 0), (58, 16, 32, 32), 3, self.radius)
                elif self.selected and self.number == 3:
                    pygame.draw.rect(win, (225, 225, 0), (100, 16, 32, 32), 3, self.radius)
                elif self.selected and self.number == 4:
                    pygame.draw.rect(win, (225, 225, 0), (142, 16, 32, 32), 3, self.radius)
                elif self.selected and self.number == 5:
                    pygame.draw.rect(win, (225, 225, 0), (184, 16, 32, 32), 3, self.radius)

            def checkHolding(self):
                global holdingRadiusItem
                global holdingChisel
                global holdingAxe
                global holdingPickaxe
                global Pinecone
                global Gravestone
                global playEquipAudioLoop
                if self.contains != 'empty' and playEquipAudioLoop == 0:
                    equipaudio.play()
                playEquipAudioLoop = 1
                if self.selected:
                    if self.contains == 'woodenchisel' and WoodenChisel > 0:
                        holdingRadiusItem = False
                        holdingChisel = True
                        holdingAxe = False
                        holdingPickaxe = False
                    elif self.contains == 'axe' and Axe > 0:
                        holdingRadiusItem = False
                        holdingChisel = False
                        holdingAxe = True
                        holdingPickaxe = False
                    elif self.contains == 'pinecone' and Pinecone > 0:
                        holdingRadiusItem = True
                        holdingChisel = False
                        holdingAxe = False
                        holdingPickaxe = False
                    elif self.contains == 'gravestone' and Gravestone > 0:
                        holdingRadiusItem = True
                        holdingChisel = False
                        holdingAxe = False
                        holdingPickaxe = False
                    elif self.contains == 'pickaxe' and Pickaxe > 0:
                        holdingRadiusItem = False
                        holdingChisel = False
                        holdingAxe = False
                        holdingPickaxe = True
                    elif self.contains == 'empty':
                        holdingRadiusItem = False
                        holdingChisel = False
                        holdingAxe = False
                        holdingPickaxe = False
                    else:
                        holdingRadiusItem = False
                        holdingChisel = False
                        holdingAxe = False
                        holdingPickaxe = False

            def use(self):
                global Pinecone
                global Gravestone
                global useItemLoop
                if self.selected and useItemLoop == 0:
                    if self.contains == 'pinecone' and Pinecone >= 1:
                        pineconeaudio.play()
                        trees.append(terrainObjects(pos[0] - 12, pos[1] - 48, 24, 48, "tree", 10))
                        Pinecone -= 1
                        for item in inventoryItems:
                            if item.item == 'pinecone':
                                inventoryItems.pop(inventoryItems.index(item))
                                break
                        if Pinecone <= 0:
                            if self.number == 1:
                                hotbar[0] = 'empty'
                            elif self.number == 2:
                                hotbar[1] = 'empty'
                            elif self.number == 3:
                                hotbar[2] = 'empty'
                            elif self.number == 4:
                                hotbar[3] = 'empty'
                            elif self.number == 5:
                                hotbar[4] = 'empty'
                        self.checkHolding()
                    elif self.contains == 'gravestone' and Gravestone > 0:
                        gravestoneplaceaudio.play()
                        gravestones.append(gravestoneObjects(pos[0] - 8, pos[1] - 8))
                        Gravestone -= 1
                        for item in inventoryItems:
                            if item.item == 'gravestone':
                                inventoryItems.pop(inventoryItems.index(item))
                                break
                        if Gravestone < 1:
                            if self.number == 1:
                                hotbar[0] = 'empty'
                            elif self.number == 2:
                                hotbar[1] = 'empty'
                            elif self.number == 3:
                                hotbar[2] = 'empty'
                            elif self.number == 4:
                                hotbar[3] = 'empty'
                            elif self.number == 5:
                                hotbar[4] = 'empty'
                        self.checkHolding()
                    useItemLoop = 1
                if useItemLoop > 0:
                    useItemLoop += 1
                if useItemLoop > 2:
                    useItemLoop = 0

        class inventoryItem(object):
            def __init__(self, x, y, width, height, item, followCursor):
                self.x = x
                self.y = y
                self.item = item
                self.width = width
                self.height = height
                self.followCursor = followCursor
            def draw(self, win):        
                if self.followCursor:
                    self.x = pos[0] - 8
                    self.y = pos[1] - 8
                if self.item == 'wood':
                    win.blit(woodpic, (self.x, self.y))
                elif self.item == 'stick':
                    win.blit(stickpic, (self.x, self.y))
                elif self.item == 'pinecone':
                    win.blit(pineconepic, (self.x, self.y))
                elif self.item == 'stone':
                    win.blit(stonepic, (self.x, self.y))
                elif self.item == 'woodenchisel':
                    win.blit(woodenchiselpic, (self.x, self.y))
                elif self.item == 'iron':
                    win.blit(ironpic, (self.x, self.y))
                elif self.item == 'axe':
                    win.blit(axepic, (self.x, self.y))
                elif self.item == 'gravestone':
                    win.blit(gravestonepic, (self.x, self.y))
                elif self.item == 'pickaxe':
                    win.blit(pickpic, (self.x, self.y))
                elif self.item == 'quartz':
                    win.blit(quartzpic, (self.x, self.y))
                elif self.item == 'gold':
                    win.blit(goldpic, (self.x, self.y))
                
                self.hitbox = (self.x, self.y, self.width, self.height)
                if showHitboxes:
                    pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

        class craftingRecipe(object):
            def __init__(self, x, y, width, height, item):
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.item = item
            def draw(self, win):
                pygame.draw.rect(win, (150, 150, 150), (self.x, self.y, self.width, self.height), 0, 5)
                if self.item == 'wood':
                    win.blit(woodpic, (self.x + 8, self.y + 8))
                elif self.item == 'stick':
                    win.blit(stickpic, (self.x + 10, self.y + 8))
                elif self.item == 'woodenchisel':
                    win.blit(woodenchiselpic, (self.x +8, self.y + 8))
                elif self.item == 'axe':
                    win.blit(axepic, (self.x + 8, self.y + 8))
                elif self.item == 'gravestone':
                    win.blit(gravestonepic, (self.x + 10, self.y + 8))
                elif self.item == 'pickaxe':
                    win.blit(pickpic, (self.x + 8, self.y + 8))
                
                if pos[1] < self.y + self.height and pos[1] > self.y:
                    if pos[0] > self.x and pos[0] < self.x + self.width:
                        if self.item == 'wood':
                            recipeText = smallInventoryFont.render('Stick (2)', 1, (0,0,0))
                            win.blit(recipeText, (115, 700))
                        elif self.item == 'stick':
                            recipeText = smallInventoryFont.render('Wood (1)', 1, (0,0,0))
                            win.blit(recipeText, (115, 700))
                        elif self.item == 'woodenchisel':
                            recipeText = smallInventoryFont.render('Wood (10), Stick (2)', 1, (0,0,0))
                            win.blit(recipeText, (115, 700))
                        elif self.item == 'axe':
                            recipeText = smallInventoryFont.render('Stone (10), Stick (2), Iron (5)', 1, (0,0,0))
                            win.blit(recipeText, (115, 700))
                        elif self.item == 'gravestone':
                            recipeText = smallInventoryFont.render('Stone (10), Wood (10), Iron (1)', 1, (0,0,0))
                            win.blit(recipeText, (115, 700))
                        elif self.item == 'pickaxe':
                            recipeText = smallInventoryFont.render('Iron (3), Stick (2)', 1, (0,0,0))
                            win.blit(recipeText, (115, 700))
            def craft(self):
                global Wood
                global Stick
                global WoodenChisel
                global Stone
                global Iron
                global Axe
                global Gravestone
                global Pickaxe
                if pos[1] < self.y + self.height and pos[1] > self.y:
                    if pos[0] > self.x and pos[0] < self.x + self.width:
                        if self.item == 'wood':
                            if Stick >= 2:
                                Stick -= 2
                                Wood += 1
                                inventory.append('wood')
                                inventoryItems.append(inventoryItem(random.randrange(150, 500), random.randrange(150, 350), 16, 16, 'wood', False))
                                for t in range(2):
                                    inventory.remove('stick')
                                    for item in inventoryItems:
                                        if item.item == 'stick':
                                            inventoryItems.pop(inventoryItems.index(item))
                                            break
                                craftaudio.play()
                        elif self.item == 'stick':
                            if Wood >= 1:
                                Wood -= 1
                                Stick += 2
                                inventory.append('stick')
                                inventory.append('stick')
                                inventoryItems.append(inventoryItem(random.randrange(150, 500), random.randrange(150, 350), 16, 16, 'stick', False))
                                inventoryItems.append(inventoryItem(random.randrange(150, 500), random.randrange(150, 350), 16, 16, 'stick', False))
                                inventory.remove('wood')
                                for item in inventoryItems:
                                    if item.item == 'wood':
                                        inventoryItems.pop(inventoryItems.index(item))
                                        break
                                craftaudio.play()
                        elif self.item == 'woodenchisel':
                            if Wood >= 10 and Stick >= 2:
                                Wood -= 10
                                Stick -= 2
                                WoodenChisel += 1
                                inventory.append('woodenchisel')
                                inventoryItems.append(inventoryItem(random.randrange(150, 500), random.randrange(150, 350), 16, 16, 'woodenchisel', False))
                                for t in range(10):
                                    inventory.remove('wood')
                                    for item in inventoryItems:
                                        if item.item == 'wood':
                                            inventoryItems.pop(inventoryItems.index(item))
                                            break
                                for t in range(2):
                                    inventory.remove('stick')
                                    for item in inventoryItems:
                                        if item.item == 'stick':
                                            inventoryItems.pop(inventoryItems.index(item))
                                            break
                                craftaudio.play()
                        elif self.item == 'axe':
                            if Stone >= 10 and Stick >= 2 and Iron >= 5:
                                Stone -= 10
                                Stick -= 2
                                Iron -= 5
                                Axe += 1
                                inventory.append('axe')
                                inventoryItems.append(inventoryItem(random.randrange(150, 500), random.randrange(150, 350), 16, 16, 'axe', False))
                                for t in range(10):
                                    inventory.remove('stone')
                                    for item in inventoryItems:
                                        if item.item == 'stone':
                                            inventoryItems.pop(inventoryItems.index(item))
                                            break
                                for t in range(2):
                                    inventory.remove('stick')
                                    for item in inventoryItems:
                                        if item.item == 'stick':
                                            inventoryItems.pop(inventoryItems.index(item))
                                            break
                                for t in range(5):
                                    inventory.remove('iron')
                                    for item in inventoryItems:
                                        if item.item == 'iron':
                                            inventoryItems.pop(inventoryItems.index(item))
                                            break
                                craftaudio.play()
                        elif self.item == 'gravestone':
                            if Stone >= 10 and Wood >= 10 and Iron >= 1:
                                Stone -= 10
                                Wood -= 10
                                Iron -= 1
                                Gravestone += 1
                                inventory.append('gravestone')
                                inventoryItems.append(inventoryItem(random.randrange(150, 500), random.randrange(150, 350), 16, 16, 'gravestone', False))
                                for t in range(10):
                                    inventory.remove('stone')
                                    for item in inventoryItems:
                                        if item.item == 'stone':
                                            inventoryItems.pop(inventoryItems.index(item))
                                            break
                                for t in range(10):
                                    inventory.remove('wood')
                                    for item in inventoryItems:
                                        if item.item == 'wood':
                                            inventoryItems.pop(inventoryItems.index(item))
                                            break
                                inventory.remove('iron')
                                for item in inventoryItems:
                                    if item.item == 'iron':
                                        inventoryItems.pop(inventoryItems.index(item))
                                        break
                                craftaudio.play()
                        elif self.item == 'pickaxe':
                            if Iron >= 3 and Stick >= 2:
                                Iron -= 3
                                Stick -= 2
                                Pickaxe += 1
                                inventory.append('pickaxe')
                                inventoryItems.append(inventoryItem(random.randrange(150, 500), random.randrange(150, 350), 16, 16, 'pickaxe', False))
                                for t in range(3):
                                    inventory.remove('iron')
                                    for item in inventoryItems:
                                        if item.item == 'iron':
                                            inventoryItems.pop(inventoryItems.index(item))
                                            break
                                for t in range(2):
                                    inventory.remove('stick')
                                    for item in inventoryItems:
                                        if item.item == 'stick':
                                            inventoryItems.pop(inventoryItems.index(item))
                                            break
                                craftaudio.play()

        def drawHelp():
            helpText0 = quoteFont.render('24 Hours is a survival game where you have to manage your time', 1, (225, 225, 0))
            helpText1 = quoteFont.render('wisely in order to survive. Every 24 \'hours\', the player is', 1, (225, 225, 0))
            helpText2 = quoteFont.render('killed unless certain conditions are met. Don\'t worry if you', 1, (225, 225, 0))
            helpText3 = quoteFont.render('find the game to be very difficult at first, as you\'ll eventually', 1, (225, 225, 0))
            helpText4 = quoteFont.render('learn from your past deaths and discover how to survive.', 1, (225, 225, 0))
            helpText5 = quoteFont.render('Controls:', 1, (225, 225, 0))
            helpText6 = quoteFont.render('w - move up', 1, (225, 225, 0))
            helpText7 = quoteFont.render('s - move down', 1, (225, 225, 0))
            helpText8 = quoteFont.render('d - move right', 1, (225, 225, 0))
            helpText9 = quoteFont.render('a - move left', 1, (225, 225, 0))
            helpText10 = quoteFont.render('i - open inventory', 1, (225, 225, 0))
            helpText11 = quoteFont.render('space - harvest resource', 1, (225, 225, 0))
            helpText12 = quoteFont.render('left click - place items or move items (while in inventory)', 1, (225, 225, 0))
            helpText13 = quoteFont.render('1-5 - interact with hotbar or place in hotbar (while in inventory)', 1, (225, 225, 0))
            helpText14 = quoteFont.render('c - craft (while in inventory)', 1, (225, 225, 0))
            helpText15 = quoteFont.render('r - rearrange inventory', 1, (225, 225, 0))
            helpText16 = quoteFont.render('h - show hitboxes', 1, (225, 225, 0))
            helpText17 = quoteFont.render('Press [esc] to return to title', 1, (225, 225, 0))
            helpText18 = quoteFont.render('esc - pause game', 1, (225, 225, 0))
            win.blit(helpText0, (25, 50))
            win.blit(helpText1, (25, 75))
            win.blit(helpText2, (25, 100))
            win.blit(helpText3, (25, 125))
            win.blit(helpText4, (25, 150))
            win.blit(helpText5, (25, 200))
            win.blit(helpText6, (25, 225))
            win.blit(helpText7, (25, 250))
            win.blit(helpText8, (25, 275))
            win.blit(helpText9, (25, 300))
            win.blit(helpText10, (25, 325))
            win.blit(helpText11, (25, 350))
            win.blit(helpText12, (25, 375))
            win.blit(helpText13, (25, 400))
            win.blit(helpText14, (25, 425))
            win.blit(helpText15, (25, 450))
            win.blit(helpText16, (25, 475))
            win.blit(helpText17, (25, 550))
            win.blit(helpText18, (25, 500))

        def drawCredits():
            creditText0 = quoteFont.render('24 Hours was created and is owned by Carter Haws.', 1, (225, 225, 0))
            creditText0_5 = quoteFont.render('This game was made using Python 3 and Pygame.', 1, (225, 225, 0))
            creditText1 = quoteFont.render('Feel free/encouraged to make mods and remixes of this game, as', 1, (225, 225, 0))
            creditText2 = quoteFont.render('long as you follow all of the following rules:', 1, (225, 225, 0))
            creditText3 = quoteFont.render('Your game must include \"original game by Carter Haws\" in', 1, (225, 225, 0))
            creditText3_5 = quoteFont.render('the credits.', 1, (225, 225, 0))
            creditText4 = quoteFont.render("Your game must include a link to this game\'s page in", 1, (225, 225, 0))
            creditText4_5 = quoteFont.render('the description.', 1, (225, 225, 0))
            creditText5 = quoteFont.render('Your game cannot be titled \"24 Hours\".', 1, (225, 225, 0))
            creditText6 = quoteFont.render('Your game cannot include any content that is unsuitable', 1, (225, 225, 0))
            creditText6_5 = quoteFont.render('for children.', 1, (225, 225, 0))
            creditText7 = quoteFont.render('Press [esc] to return to title', 1, (225, 225, 0))
            win.blit(creditText0, (25, 50))
            win.blit(creditText0_5, (25, 75))
            win.blit(creditText1, (25, 125))
            win.blit(creditText2, (25, 150))
            win.blit(creditText3, (25, 175))
            win.blit(creditText3_5, (25, 200))
            win.blit(creditText4, (25, 225))
            win.blit(creditText4_5, (25, 250))
            win.blit(creditText5, (25, 275))
            win.blit(creditText6, (25, 300))
            win.blit(creditText6_5, (25, 325))
            win.blit(creditText7, (25, 375))

        def addToInventory(material, startingrand, endingrand):
            global Wood
            global Stick
            global Pinecone
            global Stone
            global Iron
            global Quartz
            global Gold
            for i in range(random.randrange(startingrand, endingrand)):
                inventory.append(material)
                inventoryItems.append(inventoryItem(random.randrange(150, 500), random.randrange(150, 350), 16, 16, material, False))
                if material == 'wood':
                    Wood += 1
                elif material == 'stick':
                    Stick += 1
                elif material == 'pinecone':
                    Pinecone += 1
                elif material == 'stone':
                    Stone += 1
                elif material == 'iron':
                    Iron += 1
                elif material == 'quartz':
                    Quartz += 1
                elif material == 'gold':
                    Gold += 1

        def drawInventory():
            pygame.draw.rect(win, (200, 200, 200), (100, 100, 550, 400), 0, 5) #inventory bg
            inventoryTitle = inventoryFont.render('Inventory', 1, (0,0,0))
            win.blit(inventoryTitle, (115, 115))
            for item in inventoryItems:
                item.draw(win)

        def drawCrafting():
            pygame.draw.rect(win, (200, 200, 200), (100, 525, 550, 200), 0, 5) #crafting bg
            craftingTitle = inventoryFont.render('Crafting', 1, (0,0,0))
            win.blit(craftingTitle, (115, 535))

        def drawTimer():
            pygame.draw.rect(win, (225, 225, 0), (692, 8, 50, 120), 0)
            pygame.draw.rect(win, (200, 200, 200), (692, 8, 50, 120 - (deathTimer//20)), 0)
            if deathTimer > 0:
                timerText = timerFont.render(str((deathTimer + 100) // 100), 1, (0, 0, 0))
            elif deathTimer <= 0:
                timerText = timerFont.render(str(0), 1, (0, 0, 0))

            if ((deathTimer + 100) // 100) == 1:
                timerTextText = timerFont.render("HOUR", 1, (0, 0, 0))
            else:
                timerTextText = timerFont.render("HOURS", 1, (0, 0, 0))

            if deathTimer >= 900:
                win.blit(timerText, (706, 130))
            else:
                win.blit(timerText, (710, 130))

            if ((deathTimer + 100) // 100) > 1:
                win.blit(timerTextText, (690, 150))
            elif ((deathTimer + 100) // 100) == 1:
                win.blit(timerTextText, (695, 150))


        def drawRangeSquare(x, y, width, height):
            global holdingRadiusItem
            if holdingRadiusItem:
                pygame.draw.rect(win, (225, 225, 0), (x, y, width, height), 2)

        def deathPopup():
            #pygame.draw.rect(win, (0, 0, 0), (100, 150, 550, 450), 7, 10)
            youDiedText = deathFont.render(" You Died ", 1, (0, 0, 0)) 
            win.blit(youDiedText, (120, 175))
            deathScoreText = deathMessageFont.render(" Hours Survived: " + str(scoreTimer // 100) + " ", 1, (0, 0, 0))
            win.blit(deathScoreText, (125, 225))
            deathMessageText = deathMessageFont.render(" " + chosenDeathMessage + " ", 1, (0, 0, 0))
            win.blit(deathMessageText, (125, 265))
            deathButton.draw()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    deathButton.onClick()

        def pausePopup():
            #pygame.draw.rect(win, (0, 0, 0), (100, 150, 550, 450), 7, 10)
            pausedText = deathFont.render(" Paused ", 1, (0, 0, 0)) 
            win.blit(pausedText, (120, 175))
            pauseReturnText = deathMessageFont.render(" Press [esc] to return to game ", 1, (0, 0, 0))
            win.blit(pauseReturnText, (125, 225))
            deathButton.draw()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    deathButton.onClick()

        shownTitleScreen = 'main'

        def redrawTitleWindow():
            if shownTitleScreen == 'main':
                pygame.draw.rect(win, (0, 0, 0), (0, 0, 750, 750), 0)
                titleText = titleFont.render('24 HOURS', 1, (225, 225, 0))
                win.blit(titleText, (50, 50))
                quoteText = quoteFont.render(chosenQuote, 1, (225, 225, 0))
                win.blit(quoteText, (25, 700))
                playButton.draw()
                howToPlayButton.draw()
                creditsButton.draw()
                win.blit(bighourglasspic, (550, 50))
            elif shownTitleScreen == 'help':
                pygame.draw.rect(win, (0, 0, 0), (0, 0, 750, 750), 0)
                drawHelp()
            elif shownTitleScreen == 'credits':
                pygame.draw.rect(win, (0, 0, 0), (0, 0, 750, 750), 0)
                drawCredits()
            pygame.display.update()

        def redrawGameWindow():
            win.blit(bg, (-25, -25))
            for log in logs:
                log.draw(win)
            for grave in gravestones:
                grave.draw()
            for rock in rocks:
                rock.draw(win)
            for cave in caves:
                cave.draw(win)
            for bush in bushes:
                bush.draw(win)
            player.draw(win)
            for tree in trees:
                tree.draw(win)
            
            drawRangeSquare(player.x - 48, player.y - 42, 100, 100)

            pygame.draw.rect(win, (200, 200, 200), (8, 8, 216, 48), 0, 5) #hotbar bg
            hotbar1.draw(win)
            hotbar2.draw(win)
            hotbar3.draw(win)
            hotbar4.draw(win)
            hotbar5.draw(win)

            if inventoryOpen:
                drawCrafting()
                drawInventory()
                for recipe in recipes:
                    recipe.draw(win)
            else:
                for item in inventoryItems:
                    if item.y < 500 and item.y > 100:
                        pass
                        if item.x > 100 and item.x < 650:
                            pass
                        else:
                            item.x = random.randrange(150, 500)
                    else:
                        item.y = random.randrange(150, 350)
            drawTimer()
            if player.dead:
                deathPopup()
            if paused:
                pausePopup()
            pygame.display.update()


        #title loop
        titleFont = pygame.font.SysFont('consolas', 100, False)
        titleScreenButtonFont = pygame.font.SysFont('consolas', 55, False)
        quoteFont = pygame.font.SysFont('consolas', 18, False)

        chosenQuote = random.choice(timeQuotes)
        chosenDeathMessage = ""

        heartBeatPlaying = False

        titleScreen = True
        run = False
        while titleScreen:
            clock.tick(10)

            pos = pygame.mouse.get_pos()
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    titleScreen = False
                    run = False
                    gameRunning = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                playButton.onClick()
                howToPlayButton.onClick()
                creditsButton.onClick()

            if keys[pygame.K_ESCAPE]:
                if shownTitleScreen == 'help':
                    shownTitleScreen = 'main'
                elif shownTitleScreen == 'credits':
                    shownTitleScreen = 'main'

            if heartBeatPlaying:
                heartBeatPlaying = False
                heartbeataudio.stop()

            redrawTitleWindow()
        #main loop
        player = Player(windowSize // 2, windowSize // 2, 16, 16, windowSize // 2, windowSize // 2)
        hotbar1 = hotbarSpaces(16, 16, 32, 32, 1, 5, True)
        hotbar2 = hotbarSpaces(58, 16, 32, 32, 2, 5, False)
        hotbar3 = hotbarSpaces(100, 16, 32, 32, 3, 5, False)
        hotbar4 = hotbarSpaces(142, 16, 32, 32, 4, 5, False)
        hotbar5 = hotbarSpaces(184, 16, 32, 32, 5, 5, False)

        Wood = 0
        Stick = 0
        Pinecone = 0
        Stone = 0
        Iron = 0
        WoodenChisel = 0
        Axe = 0
        Gravestone = 0
        Pickaxe = 0
        Quartz = 0
        Gold = 0

        inventory = []
        inventoryItems = []
        hotbar = ['empty', 'empty', 'empty', 'empty', 'empty']
        inventoryOpen = False
        recipes = []

        inventoryFont = pygame.font.SysFont('consolas', 20, False)
        smallInventoryFont = pygame.font.SysFont('consolas', 12, False)
        timerFont = pygame.font.SysFont('consolas', 18, False)
        deathFont = pygame.font.SysFont('consolas', 30, False)
        deathMessageFont = pygame.font.SysFont('consolas', 18, False)

        trees = []
        rocks = []
        logs = []
        gravestones = []
        caves = []
        bushes = []

        breakLoop = 0
        inventoryOpenLoop = 0
        inventoryItemClickLoop = 0
        deathTimer = 2400
        scoreTimer = 0
        inventoryRemoveCounter = 0
        craftingLoop = 0
        rearrangeLoop = 0
        hitboxToggleLoop = 0
        pauseLoop = 0
        useItemLoop = 0
        playEquipAudioLoop = 0

        paused = False

        showHitboxes = False

        for t in range(75):
            trees.append(terrainObjects(random.randrange(worldBorderLeft, worldBorderRight), random.randrange(worldBorderTop, worldBorderBottom), 24, 48, "tree", 5))
        for t in range(35):
            rocks.append(terrainObjects(random.randrange(worldBorderLeft, worldBorderRight), random.randrange(worldBorderTop, worldBorderBottom), 16, 16, "rock", 8))
        for t in range(35):
            logs.append(terrainObjects(random.randrange(worldBorderLeft, worldBorderRight), random.randrange(worldBorderTop, worldBorderBottom), 24, 8, "log", 3))
        for t in range(5):
            caves.append(terrainObjects(random.randrange(worldBorderLeft, worldBorderRight), random.randrange(worldBorderTop, worldBorderBottom), 32, 32, "cave", 15))
        for t in range(25):
            bushes.append(terrainObjects(random.randrange(worldBorderLeft, worldBorderRight), random.randrange(worldBorderTop, worldBorderBottom), 20, 20, "bush", 6))

        recipes.append(craftingRecipe(115, 565, 32, 32, 'wood'))
        recipes.append(craftingRecipe(157, 565, 32, 32, 'stick'))
        recipes.append(craftingRecipe(199, 565, 32, 32, 'woodenchisel'))
        recipes.append(craftingRecipe(241, 565, 32, 32, 'axe'))
        recipes.append(craftingRecipe(283, 565, 32, 32, 'gravestone'))
        recipes.append(craftingRecipe(325, 565, 32, 32, 'pickaxe'))

        if hotbar1.selected:
            hotbar1.checkHolding()
        elif hotbar2.selected:
            hotbar2.checkHolding()
        elif hotbar3.selected:
            hotbar3.checkHolding()
        elif hotbar4.selected:
            hotbar4.checkHolding()
        elif hotbar5.selected:
            hotbar5.checkHolding()

        if run:
            pygame.mixer.music.play(-1)

        while run:
            clock.tick(10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    titleScreen = False
                    run = False
                    gameRunning = False
            
            keys = pygame.key.get_pressed()
            pos = pygame.mouse.get_pos()
            if not paused:
                if not player.dead:
                    if not inventoryOpen:
                        if keys[pygame.K_a] and player.relPosX > worldBorderLeft + player.vel:
                            player.relPosX -= player.vel
                            for cave in caves:
                                cave.x += player.vel
                            for tree in trees:
                                tree.x += player.vel
                            for rock in rocks:
                                rock.x += player.vel
                            for log in logs:
                                log.x += player.vel
                            for grave in gravestones:
                                grave.x += player.vel
                            for bush in bushes:
                                bush.x += player.vel
                        elif keys[pygame.K_d] and player.relPosX < worldBorderRight - player.vel:
                            player.relPosX += player.vel
                            for cave in caves:
                                cave.x -= player.vel
                            for tree in trees:
                                tree.x -= player.vel
                            for rock in rocks:
                                rock.x -= player.vel  
                            for log in logs:
                                log.x -= player.vel  
                            for grave in gravestones:
                                grave.x -= player.vel  
                            for bush in bushes:
                                bush.x -= player.vel 
                        if keys[pygame.K_w] and player.relPosY > worldBorderTop + player.vel:
                            player.relPosY -= player.vel
                            for cave in caves:
                                cave.y += player.vel
                            for tree in trees:
                                tree.y += player.vel
                            for rock in rocks:
                                rock.y += player.vel
                            for log in logs:
                                log.y += player.vel
                            for grave in gravestones:
                                grave.y += player.vel
                            for bush in bushes:
                                bush.y += player.vel
                        elif keys[pygame.K_s] and player.relPosY < worldBorderBottom - player.vel:
                            player.relPosY += player.vel
                            for cave in caves:
                                cave.y -= player.vel
                            for tree in trees:
                                tree.y -= player.vel
                            for rock in rocks:
                                rock.y -= player.vel
                            for log in logs:
                                log.y -= player.vel
                            for grave in gravestones:
                                grave.y -= player.vel
                            for bush in bushes:
                                bush.y -= player.vel
                        
                    if breakLoop > 0:
                        breakLoop += 1
                    if breakLoop > 6:
                        breakLoop = 0
                    
                    if keys[pygame.K_SPACE] and breakLoop == 0:
                        if holdingAxe:
                            for tree in trees:
                                if player.hitbox[1] + player.hitbox[3] <= tree.hitbox[1] + tree.hitbox[3] and player.hitbox[1] + player.hitbox[3] >= tree.hitbox[1]:
                                    if player.hitbox[0] + player.hitbox[2] >= tree.hitbox[0] and player.hitbox[0] + player.hitbox[2] <= tree.hitbox[0] + tree.hitbox[2]:
                                        if tree.health > 0:
                                            tree.health -= 1
                                            treehitaudio.play()
                                        else:
                                            treefallaudio.play()
                                            trees.pop(trees.index(tree))
                                            addToInventory('wood', 1, 5)
                                            if (random.choice(seventyFivePercent)) == 1:
                                                addToInventory('stick', 1, 3)
                                            if (random.choice(twentyFivePercent)) == 1:
                                                addToInventory('pinecone', 1, 3)
                                    elif player.hitbox[0] >= tree.hitbox[0] and player.hitbox[0] <= tree.hitbox[0] + tree.hitbox[2]:
                                        if tree.health > 0:
                                            tree.health -= 1
                                            treehitaudio.play()
                                        else:
                                            treefallaudio.play()
                                            trees.pop(trees.index(tree))
                                            addToInventory('wood', 1, 5)
                                            if (random.choice(seventyFivePercent)) == 1:
                                                addToInventory('stick', 1, 3)
                                            if (random.choice(twentyFivePercent)) == 1:
                                                addToInventory('pinecone', 1, 3)
                                elif player.hitbox[1] <= tree.hitbox[1] + tree.hitbox[3] and player.hitbox[1] >= tree.hitbox[1]:
                                    if player.hitbox[0] + player.hitbox[2] >= tree.hitbox[0] and player.hitbox[0] + player.hitbox[2] <= tree.hitbox[0] + tree.hitbox[2]:
                                        if tree.health > 0:
                                            tree.health -= 1
                                            treehitaudio.play()
                                        else:
                                            treefallaudio.play()
                                            trees.pop(trees.index(tree))
                                            addToInventory('wood', 1, 5)
                                            if (random.choice(seventyFivePercent)) == 1:
                                                addToInventory('stick', 1, 3)
                                            if (random.choice(twentyFivePercent)) == 1:
                                                addToInventory('pinecone', 1, 3)
                                    elif player.hitbox[0] >= tree.hitbox[0] and player.hitbox[0] <= tree.hitbox[0] + tree.hitbox[2]:
                                        if tree.health > 0:
                                            tree.health -= 1
                                            treehitaudio.play()
                                        else:
                                            treefallaudio.play()
                                            trees.pop(trees.index(tree))
                                            addToInventory('wood', 1, 5)
                                            if (random.choice(seventyFivePercent)) == 1:
                                                addToInventory('stick', 1, 3)
                                            if (random.choice(twentyFivePercent)) == 1:
                                                addToInventory('pinecone', 1, 3)
                        breakLoop = 1

                        for log in logs:
                            if player.hitbox[1] + player.hitbox[3] <= log.hitbox[1] + log.hitbox[3] and player.hitbox[1] + player.hitbox[3] >= log.hitbox[1]:
                                if player.hitbox[0] + player.hitbox[2] >= log.hitbox[0] and player.hitbox[0] + player.hitbox[2] <= log.hitbox[0] + log.hitbox[2]:
                                    if log.health > 0:
                                        log.health -= 1
                                        loghitaudio.play()
                                    else:
                                        logs.pop(logs.index(log))
                                        loghitaudio.play()
                                        addToInventory('wood', 1, 2)
                                        if (random.choice(seventyFivePercent)) == 1:
                                            addToInventory('stick', 1, 2)
                                elif player.hitbox[0] >= log.hitbox[0] and player.hitbox[0] <= log.hitbox[0] + log.hitbox[2]:
                                    if log.health > 0:
                                        log.health -= 1
                                        loghitaudio.play()
                                    else:
                                        logs.pop(logs.index(log))
                                        loghitaudio.play()
                                        addToInventory('wood', 1, 2)
                                        if (random.choice(seventyFivePercent)) == 1:
                                            addToInventory('stick', 1, 2)
                            elif player.hitbox[1] <= log.hitbox[1] + log.hitbox[3] and player.hitbox[1] >= log.hitbox[1]:
                                if player.hitbox[0] + player.hitbox[2] >= log.hitbox[0] and player.hitbox[0] + player.hitbox[2] <= log.hitbox[0] + log.hitbox[2]:
                                    if log.health > 0:
                                        log.health -= 1
                                        loghitaudio.play()
                                    else:
                                        logs.pop(logs.index(log))
                                        loghitaudio.play()
                                        addToInventory('wood', 1, 2)
                                        if (random.choice(seventyFivePercent)) == 1:
                                            addToInventory('stick', 1, 2)
                                elif player.hitbox[0] >= log.hitbox[0] and player.hitbox[0] <= log.hitbox[0] + log.hitbox[2]:
                                    if log.health > 0:
                                        log.health -= 1
                                        loghitaudio.play()
                                    else:
                                        logs.pop(logs.index(log))
                                        loghitaudio.play()
                                        addToInventory('wood', 1, 2)
                                        if (random.choice(seventyFivePercent)) == 1:
                                            addToInventory('stick', 1, 2)
                        breakLoop = 1

                        if holdingChisel or holdingPickaxe:
                            for rock in rocks:
                                if player.hitbox[1] + player.hitbox[3] <= rock.hitbox[1] + rock.hitbox[3] and player.hitbox[1] + player.hitbox[3] >= rock.hitbox[1]:
                                    if player.hitbox[0] + player.hitbox[2] >= rock.hitbox[0] and player.hitbox[0] + player.hitbox[2] <= rock.hitbox[0] + rock.hitbox[2]:
                                        if rock.health > 0:
                                            rock.health -= 1
                                            rockhitaudio.play()
                                        else:
                                            rockbreakaudio.play()
                                            rocks.pop(rocks.index(rock))
                                            addToInventory('stone', 1, 3)
                                            if (random.choice(twentyFivePercent)) == 1:
                                                addToInventory('iron', 1, 2)
                                    elif player.hitbox[0] >= rock.hitbox[0] and player.hitbox[0] <= rock.hitbox[0] + rock.hitbox[2]:
                                        if rock.health > 0:
                                            rock.health -= 1
                                            rockhitaudio.play()
                                        else:
                                            rockbreakaudio.play()
                                            rocks.pop(rocks.index(rock))
                                            addToInventory('stone', 1, 3)
                                            if (random.choice(twentyFivePercent)) == 1:
                                                addToInventory('iron', 1, 2)
                                elif player.hitbox[1] <= rock.hitbox[1] + rock.hitbox[3] and player.hitbox[1] >= rock.hitbox[1]:
                                    if player.hitbox[0] + player.hitbox[2] >= rock.hitbox[0] and player.hitbox[0] + player.hitbox[2] <= rock.hitbox[0] + rock.hitbox[2]:
                                        if rock.health > 0:
                                            rock.health -= 1
                                            rockhitaudio.play()
                                        else:
                                            rockbreakaudio.play()
                                            rocks.pop(rocks.index(rock))
                                            addToInventory('stone', 1, 3)
                                            if (random.choice(twentyFivePercent)) == 1:
                                                addToInventory('iron', 1, 2)
                                    elif player.hitbox[0] >= rock.hitbox[0] and player.hitbox[0] <= rock.hitbox[0] + rock.hitbox[2]:
                                        if rock.health > 0:
                                            rock.health -= 1
                                            rockhitaudio.play()
                                        else:
                                            rockbreakaudio.play()
                                            rocks.pop(rocks.index(rock))
                                            addToInventory('stone', 1, 3)
                                            if (random.choice(twentyFivePercent)) == 1:
                                                addToInventory('iron', 1, 2)
                        breakLoop = 1

                        if holdingPickaxe:
                            for cave in caves:
                                if player.hitbox[1] + player.hitbox[3] <= cave.hitbox[1] + cave.hitbox[3] and player.hitbox[1] + player.hitbox[3] >= cave.hitbox[1]:
                                    if player.hitbox[0] + player.hitbox[2] >= cave.hitbox[0] and player.hitbox[0] + player.hitbox[2] <= cave.hitbox[0] + cave.hitbox[2]:
                                        if cave.health > 0:
                                            cave.health -= 1
                                            cavehitaudio.play()
                                        else:
                                            caves.pop(caves.index(cave))
                                            cavehitaudio.play()
                                            addToInventory('stone', 3, 5)
                                            if (random.choice(seventyFivePercent)) == 1:
                                                addToInventory('iron', 1, 3)
                                            if (random.choice(seventyFivePercent)) == 1:
                                                addToInventory('quartz', 3, 5)
                                            if (random.choice(twentyFivePercent)) == 1:
                                                addToInventory('gold', 3, 5)
                                    elif player.hitbox[0] >= cave.hitbox[0] and player.hitbox[0] <= cave.hitbox[0] + cave.hitbox[2]:
                                        if cave.health > 0:
                                            cave.health -= 1
                                            cavehitaudio.play()
                                        else:
                                            caves.pop(caves.index(cave))
                                            cavehitaudio.play()
                                            addToInventory('stone', 3, 5)
                                            if (random.choice(seventyFivePercent)) == 1:
                                                addToInventory('iron', 1, 3)
                                            if (random.choice(seventyFivePercent)) == 1:
                                                addToInventory('quartz', 3, 5)
                                            if (random.choice(twentyFivePercent)) == 1:
                                                addToInventory('gold', 3, 5)
                                elif player.hitbox[1] <= cave.hitbox[1] + cave.hitbox[3] and player.hitbox[1] >= cave.hitbox[1]:
                                    if player.hitbox[0] + player.hitbox[2] >= rock.hitbox[0] and player.hitbox[0] + player.hitbox[2] <= cave.hitbox[0] + cave.hitbox[2]:
                                        if cave.health > 0:
                                            cave.health -= 1
                                            cavehitaudio.play()
                                        else:
                                            caves.pop(caves.index(cave))
                                            cavehitaudio.play()
                                            addToInventory('stone', 3, 5)
                                            if (random.choice(seventyFivePercent)) == 1:
                                                addToInventory('iron', 1, 3)
                                            if (random.choice(seventyFivePercent)) == 1:
                                                addToInventory('quartz', 3, 5)
                                            if (random.choice(twentyFivePercent)) == 1:
                                                addToInventory('gold', 3, 5)
                                    elif player.hitbox[0] >= cave.hitbox[0] and player.hitbox[0] <= cave.hitbox[0] + cave.hitbox[2]:
                                        if cave.health > 0:
                                            cave.health -= 1
                                            cavehitaudio.play()
                                        else:
                                            caves.pop(caves.index(cave))
                                            cavehitaudio.play()
                                            addToInventory('stone', 3, 5)
                                            if (random.choice(seventyFivePercent)) == 1:
                                                addToInventory('iron', 1, 3)
                                            if (random.choice(seventyFivePercent)) == 1:
                                                addToInventory('quartz', 3, 5)
                                            if (random.choice(twentyFivePercent)) == 1:
                                                addToInventory('gold', 3, 5)
                        breakLoop = 1

                    if inventoryOpenLoop > 0:
                        inventoryOpenLoop += 1
                    if inventoryOpenLoop > 3:
                        inventoryOpenLoop = 0

                    if keys[pygame.K_i] and inventoryOpenLoop == 0:
                        if inventoryOpen:
                            inventoryOpen = False
                        else:
                            inventoryOpen = True
                        inventoryOpenLoop = 1

                    if inventoryItemClickLoop > 0:
                        inventoryItemClickLoop += 1
                    if inventoryItemClickLoop > 1:
                        inventoryItemClickLoop = 0
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if inventoryOpen:
                            for item in inventoryItems:
                                if pos[1] < item.hitbox[1] + item.hitbox[3] and pos[1] > item.hitbox[1]:
                                    if pos[0] > item.hitbox[0] and pos[0] < item.hitbox[0] + item.hitbox[2]:
                                        if not item.followCursor:
                                            item.followCursor = True
                                        elif item.followCursor:
                                            item.followCursor = False
                                            item.x = pos[0] - 8
                                            item.y = pos[1] - 8
                            inventoryItemClickLoop = 1

                        else:
                            if pos[1] < player.y + 58 and pos[1] > player.y - 42:
                                    if pos[0] > player.x - 52 and pos[0] < player.x + 48:
                                        if hotbar1.selected:
                                            hotbar1.use()
                                        elif hotbar2.selected:
                                            hotbar2.use()
                                        elif hotbar3.selected:
                                            hotbar3.use()
                                        elif hotbar4.selected:
                                            hotbar4.use()
                                        elif hotbar5.selected:
                                            hotbar5.use()
                    
                    if not inventoryOpen:
                        if keys[pygame.K_1]:
                            hotbar1.selected = True
                            hotbar2.selected = False
                            hotbar3.selected = False
                            hotbar4.selected = False
                            hotbar5.selected = False
                            hotbar1.checkHolding()
                        elif keys[pygame.K_2]:
                            hotbar1.selected = False
                            hotbar2.selected = True
                            hotbar3.selected = False
                            hotbar4.selected = False
                            hotbar5.selected = False
                            hotbar2.checkHolding()
                        elif keys[pygame.K_3]:
                            hotbar1.selected = False
                            hotbar2.selected = False
                            hotbar3.selected = True
                            hotbar4.selected = False
                            hotbar5.selected = False
                            hotbar3.checkHolding()
                        elif keys[pygame.K_4]:
                            hotbar1.selected = False
                            hotbar2.selected = False
                            hotbar3.selected = False
                            hotbar4.selected = True
                            hotbar5.selected = False
                            hotbar4.checkHolding()
                        elif keys[pygame.K_5]:
                            hotbar1.selected = False
                            hotbar2.selected = False
                            hotbar3.selected = False
                            hotbar4.selected = False
                            hotbar5.selected = True
                            hotbar5.checkHolding()
                    else:
                        if keys[pygame.K_1]:
                            for item in inventoryItems:
                                if pos[1] < item.hitbox[1] + item.hitbox[3] and pos[1] > item.hitbox[1]:
                                    if pos[0] > item.hitbox[0] and pos[0] < item.hitbox[0] + item.hitbox[2]:
                                        hotbar[0] = item.item
                                        hotbar1.contains = item.item
                            hotbar1.checkHolding()
                        elif keys[pygame.K_2]:
                            for item in inventoryItems:
                                if pos[1] < item.hitbox[1] + item.hitbox[3] and pos[1] > item.hitbox[1]:
                                    if pos[0] > item.hitbox[0] and pos[0] < item.hitbox[0] + item.hitbox[2]:
                                        hotbar[1] = item.item
                                        hotbar2.contains = item.item
                            hotbar2.checkHolding()
                        elif keys[pygame.K_3]:
                            for item in inventoryItems:
                                if pos[1] < item.hitbox[1] + item.hitbox[3] and pos[1] > item.hitbox[1]:
                                    if pos[0] > item.hitbox[0] and pos[0] < item.hitbox[0] + item.hitbox[2]:
                                        hotbar[2] = item.item
                                        hotbar3.contains = item.item
                            hotbar3.checkHolding()
                        elif keys[pygame.K_4]:
                            for item in inventoryItems:
                                if pos[1] < item.hitbox[1] + item.hitbox[3] and pos[1] > item.hitbox[1]:
                                    if pos[0] > item.hitbox[0] and pos[0] < item.hitbox[0] + item.hitbox[2]:
                                        hotbar[3] = item.item
                                        hotbar4.contains = item.item
                            hotbar4.checkHolding()
                        elif keys[pygame.K_5]:
                            for item in inventoryItems:
                                if pos[1] < item.hitbox[1] + item.hitbox[3] and pos[1] > item.hitbox[1]:
                                    if pos[0] > item.hitbox[0] and pos[0] < item.hitbox[0] + item.hitbox[2]:
                                        hotbar[4] = item.item
                                        hotbar5.contains = item.item
                            hotbar5.checkHolding()
                        
                        if keys[pygame.K_r] and rearrangeLoop == 0:
                            for item in inventoryItems:
                                item.x = random.randrange(150, 500)
                                item.y = random.randrange(150, 350)
                            equipaudio.play()
                            rearrangeLoop = 1
                    
                    if rearrangeLoop > 0:
                        rearrangeLoop += 1
                    if rearrangeLoop > 2:
                        rearrangeLoop = 0

                    if hitboxToggleLoop > 0:
                        hitboxToggleLoop += 1
                    if hitboxToggleLoop > 2:
                        hitboxToggleLoop = 0
                    
                    if keys[pygame.K_h] and hitboxToggleLoop == 0:
                        if showHitboxes:
                            showHitboxes = False
                        else:
                            showHitboxes = True
                        hitboxToggleLoop = 1

                    if craftingLoop > 0:
                        craftingLoop += 1
                    if craftingLoop > 2:
                        craftingLoop = 0

                    if keys[pygame.K_c] and craftingLoop == 0:
                        if inventoryOpen:
                            for recipe in recipes:
                                recipe.craft()
                        craftingLoop = 1
                            
                    if deathTimer <= 300:
                        if not heartBeatPlaying and not paused:
                            heartBeatPlaying = True
                            heartbeataudio.play()
                    else:
                        heartbeataudio.stop()
                        heartBeatPlaying = False

                    if playEquipAudioLoop > 0:
                        playEquipAudioLoop += 1
                    if playEquipAudioLoop > 4:
                        playEquipAudioLoop = 0
                    
                    if deathTimer > 0:
                        deathTimer -= 1
                    if deathTimer <= 0:
                        heartBeatPlaying = False
                        heartbeataudio.stop()
                        if len(gravestones) > 0:
                            for grave in gravestones:
                                gravestones.pop(gravestones.index(grave))
                                break
                            gravestonebreakaudio.play()
                            deathTimer = 2400
                        else:
                            dieaudio.play()
                            player.die()

                    scoreTimer += 1

                    if keys[pygame.K_q]:
                        for r in range(5):
                            inventory.append('iron')
                            inventoryItems.append(inventoryItem(random.randrange(150, 500), random.randrange(150, 350), 16, 16, 'iron', False))
                            Iron += 1
                        for r in range(5):
                            inventory.append('stick')
                            inventoryItems.append(inventoryItem(random.randrange(150, 500), random.randrange(150, 350), 16, 16, 'stick', False))
                            Stick += 1
                        for r in range(10):
                            inventory.append('stone')
                            inventoryItems.append(inventoryItem(random.randrange(150, 500), random.randrange(150, 350), 16, 16, 'stone', False))
                            Stone += 1
                        print('cheats still on')

            redrawGameWindow()
            if pauseLoop > 0:
                pauseLoop += 1
            if pauseLoop > 3:
                pauseLoop = 0
                    
            if keys[pygame.K_ESCAPE] and pauseLoop == 0:
                if paused:
                    paused = False
                    pygame.mixer.music.play(-1)
                    if heartBeatPlaying:
                        heartbeataudio.play()
                elif not paused and not inventoryOpen:
                    paused = True
                    pygame.mixer.music.stop()
                    heartbeataudio.stop()
                pauseLoop = 1
pygame.quit