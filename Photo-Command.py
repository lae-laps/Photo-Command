from PIL import Image

print()
print("=============")
print("PHOTO-COMMAND")
print("=============")
print()
print("Import ↴")

commands = ["blur", "blur2", "canal", "contraste", "exit", "exp", "grid", "help", "invertir", "saturacion", "save", "show",]

foto = str(input("Nombre de fichero: "))

tipo = foto[-4:]

if tipo != ".jpg" and tipo != ".png":
    in_tipo = str(input("Seleccione el formato de fichero: 1 = .jpg / 2 = .png / 3 = .NEF : "))
    if in_tipo == "1":
        in_tipo = ".jpg"
    elif in_tipo == "2":
        in_tipo = ".png"
    elif in_tipo == "3":
        in_tipo = ".NEF"
    else:
        print("El formato del fichero no es válido")
    foto = foto + in_tipo

try:
    img = Image.open(foto)
except:
    print("El fichero no existe, inténtelo de nuevo")

#=========================================================================
# SPLIT

imgR, imgG, imgB = img.split()

pixR = imgR.load()
pixG = imgG.load()
pixB = imgB.load()

#=========================================================================
# FUNCIONES

def help():
    try:
        help = open("help.txt")
        print(help)
    except:
        print("No se pudo mostrar la ayuda")

    help.close()

def invertir():
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixR[i, j] = 255 - pixR[i, j]
            pixG[i, j] = 255 - pixG[i, j]
            pixB[i, j] = 255 - pixB[i, j]

def exp(signo, grado):
    g = float(grado)
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if signo == "+":
                pixR[i, j] = int(pixR[i, j] * g)
                pixG[i, j] = int(pixG[i, j] * g)
                pixB[i, j] = int(pixB[i, j] * g)
            elif signo == "-":
                pixR[i, j] = int(pixR[i, j] / g)
                pixG[i, j] = int(pixG[i, j] / g)
                pixB[i, j] = int(pixB[i, j] / g)

def saturacion(signo, grado):



def contraste(signo, grado):
    g = float(grado)
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if signo == "+":
                if pixR[i, j] >= 128:
                    pixR[i, j] = int(pixR[i, j] + g)
                else:
                    pixR[i, j] = int(pixR[i, j] - g)
                if pixG[i, j] >= 128:
                    pixG[i, j] = int(pixG[i, j] + g)
                else:
                    pixG[i, j] = int(pixG[i, j] - g)
                if pixB[i, j] >= 128:
                    pixB[i, j] = int(pixB[i, j] + g)
                else:
                    pixB[i, j] = int(pixB[i, j] - g)

            if signo == "-":


                if pixR[i, j] >= 128:
                    pixR[i, j] = int(pixR[i, j] - g)
                else:
                    pixR[i, j] = int(pixR[i, j] + g)
                if pixG[i, j] >= 128:
                    pixG[i, j] = int(pixG[i, j] - g)
                else:
                    pixG[i, j] = int(pixG[i, j] + g)
                if pixB[i, j] >= 128:
                    pixB[i, j] = int(pixB[i, j] - g)
                else:
                    pixB[i, j] = int(pixB[i, j] + g)


def grid(space, light):
    space = int(space)
    light = int(light)
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if (i % space) == 0:
                if (j % space) == 0:
                    pixR[i, j] = light
                    pixG[i, j] = light
                    pixB[i, j] = light

def blur(times):
    print("Este proceso puede llevar un rato...")
    print("Nota: El efecto de 1 blur es mínimo, utilize de 10 en adelante para obtener un efecto substancial")
    for x in range(int(times)):
        for i in range(img.size[0] - 1):
            for j in range(img.size[1] - 1):
                pixR[i, j] = int((pixR[i, j] + pixR[i, j+1] + pixR[i+1, j] + pixR[i+1, j+1]) / 4.0)
                pixG[i, j] = int((pixG[i, j] + pixG[i, j+1] + pixG[i+1, j] + pixG[i+1, j+1]) / 4.0)
                pixB[i, j] = int((pixB[i, j] + pixB[i, j+1] + pixB[i+1, j] + pixB[i+1, j+1]) / 4.0)
        print("Blur ", (x + 1), "de ", times)


def blur2(size):
    n = int(size)
    n2 = float((n-1)*(n-1))
    for i in range(img.size[0] - n):

        for j in range(img.size[1] - n):
            for di in range(n):
                sumR = 0
                sumG = 0
                sumB = 0
                for dj in range(n):
                    sumR = sumR + pixR[i + di, j + dj]
                    sumG = sumG + pixG[i + di, j + dj]
                    sumB = sumB + pixB[i + di, j + dj]
            pixR[i, j] = int(sumR / n2)
            pixG[i, j] = int(sumG / n2)
            pixB[i, j] = int(sumB / n2)
    print()

def canal(canal, grado):
    g = float(grado)
    if canal == "R":
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                pixR[i, j] = int(pixR[i, j] * g)
    if canal == "G":
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                pixG[i, j] = int(pixG[i, j] * g)
    if canal == "B":
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                pixB[i, j] = int(pixB[i, j] * g)


def show():
    img = Image.merge("RGB", (imgR, imgG, imgB))
    img.show()

def save():
    name = str(input("Nombre: "))
    tipo = name[-4:]

    if tipo != ".jpg" and tipo != ".png":
        in_tipo = str(input("Seleccione el formato de fichero: 1 = .jpg / 2 = .png : "))
        if in_tipo == "1":
            in_tipo = ".jpg"
        elif in_tipo == "2":
            in_tipo = ".png"
        else:
            print("El formato del fichero no es válido")
        name = name + in_tipo
    img.save(name)

def exit():
    sure = str(input("y/n: "))
    sure = sure.lower()
    if sure == "y":
        quit(0)

#==========================================================================
# MAIN

while True:
    line = (str(input(">> ")))
    params = line.split()
    com = params[0]

    if com in commands:
        if len(params) == 1:
            eval(com + "()")
        elif len(params) == 2:
            eval(com + "('" + params[1] + "')")
        elif len(params) == 3:
            eval(com + "('" + params[1] + "','" + params[2] + "')")
        else:
            print ("Demasiados parametros!!!!")
            break
    else:
        print("La función no fué encontrada, inténtelo de nuevo.")
