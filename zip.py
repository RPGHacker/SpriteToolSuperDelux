import os
import zipfile

def zipdir(path, ziph):
   # ziph is zipfile handle
   for root, dirs, files in os.walk(path):
      for file in files:
         ziph.write(os.path.join(root, file))

def asm(path):
   return os.path.join('asm', path);

if os.path.exists('src.zip'):
   os.remove('src.zip')
if os.path.exists('pixi.zip'):
   os.remove('pixi.zip')
   
   
with zipfile.ZipFile('src.zip', 'w') as srczip:
   zipdir('src', srczip)
   srczip.write('make.bat')
   srczip.write('make_debug.bat')
print("src.zip created")

cfgexe = "src/CFG Editor/CFG Editor/bin/Release/CFG Editor.exe"

with zipfile.ZipFile('pixi.zip', 'w') as pixizip:

   #sprite dirs
   zipdir('sprites', pixizip)
   zipdir('shooters', pixizip)
   zipdir('generators', pixizip)
   zipdir('cluster', pixizip)
   zipdir('extended', pixizip)
   zipdir('routines', pixizip)

   #exe
   pixizip.write(cfgexe.replace('/', os.sep), 'CFG Editor.exe');
   pixizip.write('pixi.exe')
   pixizip.write('asar.dll')
   
   #asm
   pixizip.write(asm('main.asm'))
   pixizip.write(asm('sa1def.asm'))
   
   pixizip.write(asm('cluster.asm'))
   pixizip.write(asm('extended.asm'))
   pixizip.write(asm('pointer_caller.asm'))
      
   pixizip.write(asm('DefaultSize.bin'))
   
   zipdir(asm('Blocks'), pixizip)
   zipdir(asm('Converter Tools'), pixizip)
   pixizip.write(asm('Poison.asm'))
   
   #misc
   pixizip.write('src.zip')
   zipdir('Graphics for Included Sprites', pixizip)
   pixizip.write('readme.txt')   

print("pixi.zip created")
os.remove('src.zip')

            