import pyfiglet

ascii_banner = pyfiglet.figlet_format('PORT SCANNER', font='smslant')
print(ascii_banner)

f = pyfiglet.Figlet(font='standard')
print(f.renderText('Brandan'))

print(pyfiglet.FigletFont.getFonts())