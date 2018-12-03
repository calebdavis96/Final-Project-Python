import random
wordbank =
['Adult',
'Aeroplane', 
'Air', 
'Aircraft Carrier', 
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
'Coffee-shop', 
'Comet', 
'Compact Disc', 
'Compass', 
'Computer', 
'Crystal', 
'Cup', 
'Cycle', 
'Data Base', 
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
'Jet fighter', 
'Junk', 
'Kaleidoscope', 
'Kitchen', 
'Knife', 
'Leather jacket', 
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
'Post-office', 
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
'Swimming Pool', 
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
'Worm', 
'X-ray']

word_bank = random.choice(wordbank)
name = raw_input("What is your name? ")

print "Hello, " + name, "Let's play hangman!"

print "Start guessing..."

word = word_bank

guesses = ''

turns = 10
