import os, glob



svg_soubory = []
for soubor in glob.iglob('./**/*.svg', recursive=True):
	svg_soubory.append(soubor)

for svg in svg_soubory:
	prikaz = "inkscape" \
	+ " --export-background-opacity=0" \
	+ " --export-dpi=96" \
	+ " --export-area-drawing " \
	+ "--export-type=png " \
	+ "--export-filename=\"." + svg.strip(".svg") + ".png\" " \
	+ " " + svg
	print(prikaz)
	os.system(prikaz)
	print("")

input("Stiskni ENTER pro ukončení ...")
