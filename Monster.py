from Character import Character


class Monster(Character):
	def __init__(self, name, health, power, region, type_of_character):
		super(Monster, self).__init__(name, health, power, region, type_of_character)
		self.type_of_character = "Monster"
		self.attack_which_kills_it = "hit_hard"	
		self.attack_on_hero = "hug_to_death"
		self.item_needed_to_kill_it = "none"
		self.region = "desert"
		self.bounty = 25
		self.health = 1
		self.power = 1

	def how_to_kill_me(self):
		print "To kill me: ", self.attack_which_kills_it


# Character class defines these attributes and methods
	# self.name = name
	# self. health = health
	# self.power = power
	# def take_damage(self,amount_of_damage):
	# 	self.health -= amount_of_damage
	# def get_health(self):
	# 	return self.health
	# def is_alive(self):
	# 	return self.health > 0

class Goblin(Monster):
	def __init__(self, name = "goblin", health = 1, power = 1, region = "all", type_of_character = "Goblin"):
		super(Goblin, self).__init__(name, health, power, region, type_of_character)
		# self.type_of_character = "Goblin"
		self.attack_which_kills_it = "hit_hard"
		self.item_needed_to_kill_it = "none"
		self.attack_on_hero = "hit_hard"
		# self.region = "all"
		self.bounty = 5
		# self.health = 1
		# self.power = 1




	# define a method just for goblins
	def do_a_dance(self):
		print "The goblin does a dance and you are horrified and stupified, but take no damage."	
	
class Vampire(Monster):
	def __init__(self, name = "vampire", health = 4, power = 4, region = "all", type_of_character = "Vampire"):
		super(Vampire, self).__init__(name, health, power, region, type_of_character)
		# self.type_of_character = "Vampire"
		self.attack_which_kills_it = "stake_in_heart"
		self.attack_on_hero = "bite"
		self.item_needed_to_kill_it = "wooden_stake"
		# self.region = "all"
		self.bounty = 30
		# self.health = 1
		# self.power = 1



	def make_girls_swoon(self):
		print "The skin of the vampire sparkles in the sunlight. You take 1 point damage."
		damage_done = -1
		return damage_done 


class Brigand(Monster):
	def __init__(self, name = 'brigand', health = 9, power = 9, region = "all", type_of_character = "Brigand"):	
		super(Brigand, self).__init__(name, health, power, region, type_of_character)
		self.type_of_character = "Brigand"
		self.attack_on_hero = "hit_hard"
		self.item_needed_to_kill_it = "none"
		self.attack_which_kills_it = "hit_hard"
		self.region = "all"
		self.bounty = 10
		self.health = 1
		self.power = 1




class Wizard(Character):
	def __init__(self, name, health, power, region, type_of_character):
		super(Wizard, self).__init__(name, health, power, region, type_of_character)
		self.type_of_character = "Wizard"
		self.health = 8
		self.power = 1
		self.attack_which_kills_it = "mesmerize_with_red_gemstone"
		self.attack_on_hero = "use_a_spell"
		self.item_needed_to_kill_it = "red_gemstone"
		self.region = "all"
		self.bounty = 50
		self.health = 1
		self.power = 1




	def attack(self, enemy):
		swap_power = random.random() > 0.5
		if swap_power:
			print "%s swaps power with %s during attack" % (self.name, enemy.name)
			self.power, enemy.power = enemy.power, self.power
		super(Wizard, self).attack(enemy)
		if swap_power:
			self.power, enemy.power = enemy.power, self.power

class Mermaid(Monster):
	def __init__(self, name, health, power, region, type_of_character):
		super(Mermaid, self).__init__(name, health, power, region, type_of_character)
		self.type_of_character = "Mermaid"
		self.attack_which_kills_it = "drag_out_of_water"
		self.item_needed_to_kill_it = "none"
		self.attack_on_hero = "asphyxiation"
		self.region = "ocean-beach"
		self.bounty = 30
		self.health = 1
		self.power = 1



class Siren(Monster):
	def __init__(self, name, health, power, region, type_of_character):
		super(Siren, self).__init__(name, health, power, region, type_of_character)
		self.type_of_character = "Siren"
		self.attack_which_kills_it = "drag_into_water"
		self.item_needed_to_kill_it = "none"
		self.attack_on_hero = "singing_until_dead"
		self.region = "ocean-beach"
		self.bounty = 40
		self.health = 1
		self.power = 1



class Mountain_lion(Monster):
	def __init__(self, name, health, power, region, type_of_character):
		super(Mountain_lion, self).__init__(name, health, power, region, type_of_character)
		self.type_of_character = "Mountain_lion"
		self.attack_which_kills_it = "sleeping_potion"
		self.attack_on_hero = "slice with claws"
		self.item_needed_to_kill_it = "sleeping_potion"
		self.region = "mountains"
		self.bounty = 15
		self.health = 1
		self.power = 1



class Ski_bunny(Monster):
	def __init__(self, name, health, power, region, type_of_character):
		super(Ski_bunny, self).__init__(name, health, power, region, type_of_character)
		self.type_of_character = "Ski_bunny"
		self.attack_which_kills_it = "drop_off_ski_lift"
		self.attack_on_hero = "run_over_hero_on_skis"
		self.item_needed_to_kill_it = "lift_ticket"
		self.region = "mountains"
		self.bounty = 30
		self.health = 1
		self.power = 1




class Whirling_dervish(Monster):
	def __init__(self, name, health, power, region, type_of_character):
		super(Whirling_dervish, self).__init__(name, health, power, region, type_of_character)
		self.type_of_character = "Whirling_dervish"
		self.attack_which_kills_it = "stick_arm_out"
		self.item_needed_to_kill_it = "none"
		self.attack_on_hero = "twirl_hero_to_death"
		self.region = "desert"
		self.bounty = 50
		self.health = 1
		self.power = 1



class Snake(Monster):
	def __init__(self, name, health, power, region, type_of_character):
		super(Snake, self).__init__(name, health, power, region, type_of_character)
		self.type_of_character = "Snake"
		self.attack_which_kills_it = "stomp"
		self.attack_on_hero = "bite"
		self.item_needed_to_kill_it = "boots"
		self.region = "all"
		self.bounty = 15
		self.health = 1
		self.power = 1



class Shark(Monster):
	def __init__(self, name, health, power, region, type_of_character):
		super(Shark, self).__init__(name, health, power, region, type_of_character)
		self.type_of_character = "Shark"
		self.attack_which_kills_it = "Slices_with_Sword"
		self.attack_on_hero = "bite"
		self.item_needed_to_kill_it = "Sword"
		self.region = "ocean-beach"
		self.bounty = 20
		self.health = 1
		self.power = 1



class Abominable_snowman(Monster):
	def __init__(self, name, health, power, region, type_of_character):
		super(Abominable_snowman, self).__init__(name, health, power, region, type_of_character)
		self.type_of_character = "Abominable_snowman"
		self.attack_which_kills_it = "snowboard_downhill_until_too_warm"
		self.attack_on_hero = "slice with claws"
		self.item_needed_to_kill_it = "snowboard"
		self.region = "mountain"
		self.bounty = 50
		self.health = 1
		self.power = 1



class Giant_scorpion(Monster):
	def __init__(self, name, health, power, region, type_of_character):
		super(Giant_scorpion, self).__init__(name, health, power, region, type_of_character)
		self.type_of_character = "Giant_scorpion"
		self.attack_which_kills_it = "throw_net_over"
		self.attack_on_hero = "pinch_hero"
		self.item_needed_to_kill_it = "net"
		self.region = "desert"
		self.bounty = 15
		self.health = 1
		self.power = 1



class Sandworm(Monster):
	def __init__(self, name, health, power, region, type_of_character):
		super(Sandworm, self).__init__(name, health, power, region, type_of_character)
		self.type_of_character = "Sandworm"
		self.attack_which_kills_it = "dehydrate_to_death"
		self.attack_on_hero = "eat_hero"
		self.item_needed_to_kill_it = "do_not_eat"
		self.region = "desert"
		self.bounty = 20
		self.health = 1
		self.power = 1



class Mountain_troll(Monster):
	def __init__(self, name, health, power, region, type_of_character):
		super(Mountain_troll, self).__init__(name, health, power, region, type_of_character)
		self.type_of_character = "Mountain_troll"
		self.attack_which_kills_it = "wraps_with_rope"
		self.attack_on_hero = "slices_with_claws"
		self.item_needed_to_kill_it = "rope"
		self.region = "mountain"
		self.bounty = 30
		self.health = 1
		self.power = 1



class Beach_bunny(Monster):
	def __init__(self, name, health, power, region, type_of_character):
		super(Beach_bunny, self).__init__(name, health, power, region, type_of_character)
		self.type_of_character = "Beach_bunny"
		self.attack_which_kills_it = "throws_sand_at_bunny"
		self.item_needed_to_kill_it = "none"
		self.attack_on_hero = "snuggles_hero_to_death"
		self.region = "ocean-beach"
		self.bounty = 30
		self.health = 1
		self.power = 1



class Zombie(Monster):
	def __init__(self, name, health, power, region, type_of_character):
		super(Zombie, self).__init__(name, health, power, region, type_of_character)
		self.type_of_character = "Zombie"
		self.attack_which_kills_it = "none"
		self.item_needed_to_kill_it = "none"
		self.attack_on_hero = "bites_and_hits"
		self.region = "all"
		self.health = 1
		self.power = 1
		self.bounty = 20

# Zombie never dies, even if health < 0. Wanders off after 3 attacks.


class Shadow(Monster):
	def __init__(self, name, health, power, region, type_of_character):
		super(Shadow, self).__init__(name, health, power, region, type_of_character)
		self.type_of_character = "Shadow"
		self.attack_which_kills_it = "Slices_with_Sword"
		self.item_needed_to_kill_it = "Sword"
		self.attack_on_hero = "surround"
		self.region = "all"
		self.bounty = 20
		self.health = 1
		self.power = 1

# Shadow has 1 starting health and only takes damage in 1/10 attacks.

class Medic(Monster):
	def __init__(self, name, health, power, region, type_of_character):
		super(Medic, self).__init__(name, health, power, region, type_of_character)
		self.type_of_character = "Medic"
		self.attack_which_kills_it = "Slices_with_Sword"
		self.item_needed_to_kill_it = "Sword"
		self.attack_on_hero = "stabs_with_scalpel"
		self.region = "all"
		self.bounty = 20
		self.health = 1
		self.power = 1



	