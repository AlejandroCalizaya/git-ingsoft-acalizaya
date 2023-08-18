# Integrantes:
- Alejandro Calizaya
- Matias Maravi
- Jose Machaca

# Comandos utilizados:

## Alejandro Calizaya
Primera parte:
- git add app.py
- git commit -m "Prueba v2"
- git remote add origin https://github.com/AlejandroCalizaya/git-ingsoft-acalizaya
- git push

Segunda parte:
- git branch feature1
- git checkout feature1
- pico app.py
- git add app.py
- git commit -m "Modificacion 1"
- git push --set-upstream origin feature1

Tercera parte:
- git checkout master
- git merge feature1

## Jose Leandro Machaca


Paso 1:
- git clone https://github.com/AlejandroCalizaya/git-ingsoft-acalizaya
- git branch feature2
- git checkout feature2
- nvim app.py
- git add app.py
- git commit -m "Modificacion 2"
- git push --set-upstream origin feature2

Paso 2:
- Hice pull request
- git merge feature2
- git branch -D feature2

## Matias Maravi Anyosa


Paso 1:
- git clone https://github.com/AlejandroCalizaya/git-ingsoft-acalizaya
- cd git-ingsoft-acalizaya
- code .
### En la terminal de VsCode despues de editar app.py
- git branch feature3
- git checkout feature3
- git add .
- git commit -m "Modificado la función hello con wiiiiiiiii"
- git push --set-upstream origin feature3

Paso 2:
- Hice pull request
- git merge feature3
- Borre la rama desde la web
