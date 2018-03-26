from random import randint
import sys

class Character:
	def __init__(self):
		self.name = ""
		self.weight = 60.
		self.weight_max = 60.
		self.weight_goal = 50.

class Player(Character):
	def __init__(self):
		Character.__init__(self)
		self.weight = 60.
		self.weight_max = 60.
	def quit(self):
		if self.weight > self.weight_goal:
			print "%s is too tired of losing weight, so %s loses the chance to go to Cancun." % (self.name, self.name)
			sys.exit()
		else:
			print "Great job, %s now can wear a super hot bikini to the beach" % self.name
			sys.exit()
	def help(self): print Commands.keys()
	def status(self): print "{}'s weight: {}/{}".format(self.name, self.weight, self.weight_max)
	def sleep(self):
		if self.weight < self.weight_max - 1:
			print "%s is too lazy so she chooses to sleep at home, so the weight increase." % self.name; self.weight = self.weight + 1
		else:
			print "%s is fatter then before, %s loses the chance to go to Cancun and wears a super hot bikini to the beach!" % (self.name, self.name)
			sys.exit()
	def cheesecakes(self):
		if self.weight < self.weight_max - 1.5:
			print "%s can't help but eat the cheesecakes, and thus increases 1.5kg." % self.name; self.weight = self.weight + 1.5
		else:
			print "%s is fatter then before, %s loses the chance to go to Cancun and wears a super hot bikini to the beach!" % (self.name, self.name)
			sys.exit()
	def bbq_chicken(self):
		if self.weight < self.weight_max -2:
			print "%s eats all of the bbq chicken and is regreting for doing this beacuse %s increase 2 kg." % (self.name,self.name); self.weight = self.weight + 2
		else:
			print "%s is fatter then before, %s loses the chance to go to Cancun and wears a super hot bikini to the beach!" % (self.name, self.name)
			sys.exit()
	def work_out(self):
		if self.weight <= self.weight_goal + 0.8:
			print "Congradulation!! %s achieves the goal of losing weight! Now %s can wear super hot bikini to Cancun!" % (self.name, self.name)
			sys.exit()
		else:
			print " Good job! The work out helps %s to lose 0.8 kg" % self.name; self.weight = self.weight - 0.8
	def swimming(self):
		if self.weight <= self.weight_goal + 0.5:
			print "Congradulation!! %s achieves the goal of losing weight! Now %s can wear super hot bikini to Cancun!" % (self.name, self.name)
			sys.exit()
		else:
			print " Swimming is the best aerobic exercise and thus help %s lose 0.5 kg. " % self.name; self.weight = self.weight - 0.5

Commands = {
'quit': Player.quit,
'help': Player.help,
'status': Player.status,
'sleep': Player.sleep,
'cheesecakes': Player.cheesecakes,
'bbq_chicken': Player.bbq_chicken,
'work_out': Player.work_out,
'swimming': Player.swimming,
}

p = Player()
p.name = raw_input("What is your character's name? ")
print "(type help to get a list of actions)\n"
print "%s wants to wear a super hot bikini to the beach in Cancun, so %s starts to lose her weight. The most important thing is that %s's weight can't be more than 60 or %s will lose the chance to go to Cancun" % (p.name, p.name, p.name, p.name)


while(p.weight <= 60):
  line = raw_input("> ")
  args = line.split()
  if len(args) > 0:
    commandFound = False
    for c in Commands.keys():
      if args[0] == c[:len(args[0])]:
        Commands[c](p)
        commandFound = True
        break
    if not commandFound:
      print "%s doesn't understand the suggestion." % p.name


        commandFound = True
        break
    if not commandFound:
      print "%s doesn't understand the suggestion." % p.name



