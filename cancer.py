# Radition has the ability to change the properties of a cell
# (Cause mutation)
class Radiation:
	ms = 0 # millisieverts

	# this function takes a cell object and does some modifications
	# to it.
	def mutate(self, cell):
		if self.ms < 0:
			print("No effect")
		elif self.ms >= 2000:
			print("dangerous.")
			cell.dna_molecules_intact = False
		elif self.ms >= 10000:
			print("fatal")


class Cell:
	dna_molecules_intact = True


c1 = Cell()

print(c1.dna_molecules_intact)

r1 = Radiation()
# Set the amount of inonizing radiation
r1.ms = 2000
r1.mutate(c1)

print(c1.dna_molecules_intact)
