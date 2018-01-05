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

class Band:
    def hire(self):
        self.Tim = Bassist()
        self.Jack = Guitarist()
        self.Bob = Drummer()
# I attempted to use input() to get names of band members to use in play_solos but was unable to get it functional.
        
    def fire(self):
        print("We need new band members, you're all fired!")
# No need to do anything more, correct?
        
    def play_solos(self):
        self.Bob.count()
        self.Tim.solo(7)
        self.Jack.solo(10)
        self.Bob.solo(8)
        
gig = Band()
gig.hire()
gig.play_solos()
