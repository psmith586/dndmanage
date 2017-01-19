#dungeons and dragons charater class

class Character:
    
    def __init__(self, name, race, char_class, backgrd, align, lvl, \
				 str, dex, con, intel, charis, equip):
        
		#initialize each attribute
		
		self.__name = name
        self.__race = race
        self.__char_class = char_class
		self.__backgrd = backgrd
		self.__align = align
		self.__lvl = lvl
		self.__str = str
		self.__dex = dex
		self.__con = con
		self.__intel = intel
		self.__charis = charis
		self.__equip = equip	
		
    #methods to add attr to instances

    def set_name(self, name):
        self.__name = name
	def set_race(self, race):
        self.__name = race
	def set_char_class(self, char_class):
        self.__char_class = char_class
	def set_backgrd(self, backgrd):
		self.__backgrd = backgrd
	def set_align(self, align):
		self.__align = align
	def set_lvl(self, lvl):
		self.__lvl = lvl
	def set_str(self, str):
		self.__str = str
	def set_dex(self, dex):
		self.__dex = dex
	def set_con(self, con):
		self.__con = con
	def set_intel(self, intel):
		self.__intel = intel
	def set_charis(self, charis):
		self.__charis = charis
	def set_equip(self, equip):
		self.__equip = equip
		
    #accessor methods 

    def get_name(self):
        return self.__name
	def get_race(self):
        return self.__race
    def get_char_class(self):
        return self.__char_class
	def get_backgrd(self):
		return self.__backgrd
	def get_align(self):
		return self.__align
	def get_lvl(self):
		return self.__lvl
	def get_str(self):
		return self.__str
	def get_dex(self):
		return self.__dex
	def get_con(self):
		return self.__con
	def get_intel(self):
		return self.__intel
	def get_charis(self):
		return self.__charis
	def get_equip(self):
		return self.__equip

	#display current state of the instance	
	def __str__(self):
		return "Name: " + self.__name + \
				"\nRace/Class: " + self.__race + "/" + self.__char_class + \
				"\nBackground/Alignment: " + self.__backgrd "/" + self.__align + \
				"\nLevel: " + self.__lvl + \
				"\nStrength: " + self.__str + \
				"\nDexterity: " + self.__dex + \
				"\nConstitution: " + self.__con + \
				"\nIntelligence: " + self.__intel + \
				"\nCharisma: " + self.__charis + \
				"\nCurrent Equipment: " + self__equip
