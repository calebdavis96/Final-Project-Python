import random
wordbank =['Adult',
'Aeroplane', 
'Air', 
'Aircraft', 
'Airforce', 
'Airport', 
'Album', 
'Alphabet', 
'Apple', 
'Arm', 
'Army', 
'Baby', 
'Baby', 
'Backpack', 
'Balloon',
'Banana', 
'Bank', 
'Barbecue', 
'Bathroom', 
'Bathtub', 
'Bed', 
'Bee', 
'Bible', 
'Bird', 
'Bomb', 
'Book', 
'Boss', 
'Bottle', 
'Bowl', 
'Box', 
'Boy', 
'Brain', 
'Bridge', 
'Butterfly', 
'Button', 
'Cappuccino', 
'Car', 
'Car-race', 
'Carpet', 
'Carrot', 
'Cave', 
'Chair', 
'Chess', 
'Chief', 
'Child', 
'Chisel', 
'Chocolates', 
'Church', 
'Circle', 
'Circus', 
'Clock', 
'Clown', 
'Coffee',  
'Comet', 
'Compact',
'Compass', 
'Computer', 
'Crystal', 
'Cup', 
'Cycle', 
'Database', 
'Desk', 
'Diamond', 
'Dress', 
'Drill', 
'Drink', 
'Drum', 
'Dung', 
'Ears', 
'Earth', 
'Egg', 
'Electricity', 
'Elephant', 
'Eraser', 
'Explosive', 
'Eyes', 
'Family', 
'Fan', 
'Feather', 
'Festival', 
'Film', 
'Finger', 
'Fire', 
'Floodlight', 
'Flower', 
'Foot', 
'Fork', 
'Freeway', 
'Fruit', 
'Fungus', 
'Game', 
'Garden', 
'Gas', 
'Gate', 
'Gemstone', 
'Girl', 
'Gloves', 
'God', 
'Grapes', 
'Guitar', 
'Hammer', 
'Hat', 
'Hieroglyph', 
'Highway', 
'Horoscope', 
'Horse', 
'Hose', 
'Ice', 
'Icecream', 
'Insect', 
'Jet', 
'Junk', 
'Kaleidoscope', 
'Kitchen', 
'Knife', 
'Leather', 
'Leg', 
'Library', 
'Liquid', 
'Magnet', 
'Man', 
'Map', 
'Maze', 
'Meat', 
'Meteor', 
'Microscope', 
'Milk', 
'Milkshake', 
'Mist', 
'Money', 
'Monster', 
'Mosquito', 
'Mouth', 
'Nail', 
'Navy', 
'Necklace', 
'Needle', 
'Onion', 
'PaintBrush', 
'Pants', 
'Parachute', 
'Passport', 
'Pebble', 
'Pendulum', 
'Pepper', 
'Perfume', 
'Pillow', 
'Plane', 
'Planet', 
'Pocket', 
'Post', 
'Potato', 
'Printer', 
'Prison', 
'Pyramid', 
'Radar', 
'Rainbow', 
'Record', 
'Restaurant', 
'Rifle', 
'Ring', 
'Robot', 
'Rock', 
'Rocket', 
'Roof', 
'Room', 
'Rope', 
'Saddle', 
'Salt', 
'Sandpaper', 
'Sandwich', 
'Satellite', 
'School', 
'Sex', 
'Ship', 
'Shoes', 
'Shop', 
'Shower', 
'Signature', 
'Skeleton', 
'Slave', 
'Snail', 
'Software', 
'Solid', 
'Space', 
'Spectrum', 
'Sphere', 
'Spice', 
'Spiral', 
'Spoon', 
'sports', 
'Spot', 
'Square', 
'Staircase', 
'Star', 
'Stomach', 
'Sun', 
'Sunglasses', 
'Surveyor', 
'Swim', 
'Sword', 
'Table', 
'Tapestry', 
'Teeth', 
'Telescope', 
'Television', 
'Tennis', 
'Thermometer', 
'Tiger', 
'Toilet', 
'Tongue', 
'Torch', 
'Torpedo', 
'Train', 
'Treadmill', 
'Triangle', 
'Tunnel', 
'Typewriter', 
'Umbrella', 
'Vacuum', 
'Vampire', 
'Videotape', 
'Vulture', 
'Water', 
'Weapon', 
'Web', 
'Wheelchair', 
'Window', 
'Woman', 
'Worm'
           ]

word = random.choice(wordbank).lower()
name = raw_input("What's your name? ")

print("Hello, ") + name, ("Let's play hangman!")
print("Start guessing...")


guesses = ''
turns = 10
while turns > 0:         
    failed = 0               
    for char in word:      
        if char in guesses:    
    
            print char,    

        else:
    
            print("_"),     
       
            failed += 1    

    if failed == 0:        
        print("You won!")

        break
    print("")
    valid_guess = False
    while not valid_guess:
        guess = raw_input("Guess a character:").lower()
        if len(guess) > 1:
            print("One character at a time please!")
        else:
            valid_guess = True
        
    

    guesses += guess                
    if guess not in word:  
        turns -= 1        
        print ("Wrong")    
        print ("You have"), + turns, ('more guesses' )
        if turns == 0:           
    
            print ("Sorry, word was ") + word
