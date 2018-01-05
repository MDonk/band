class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        super().__init__(["Bang", "Ting", "Crash", "Tap"])
        
    def count(self):
        # Count to 4
        c = 0
        while c < 4:
            c += 1
            print(c)
        
    def combust(self):
        print("Drummer has spontaneously combusted!")
        # How to delete instance here? or is unnecessary? 

# Add Band class
# Bands should be able to:
# - hire and fire Musicians
# - have them play solos after drummer has counted time.
class Band():
    def hire(self):
        Tim = Bassist()
        Jack = Guitarist()
        Bob = Drummer()
        # Why don't the variables link to classes? 

play = Band()
play.hire()