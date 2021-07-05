# Ejecuta este script en el directorio de descarga para instalar las librerías requeridas

chmod +x main.py

{ # try

    pip3 install pillow &&
    #save your output

} || { # catch
    pip3 install PIL 
}

python3 main.py
