# from os import walk
# from json import dump, dumps

# filenames = next(walk("audios/"), (None, None, []))[2]

# data = []
# for i in filenames:
#     resposta = i.split("-")[0]
#     data.append({
#                 "name": resposta,
#                 "url": "audios/" + i
#             })


# open("audios.js", "w").write("var audios = " + dumps(data))


from os import walk, system
from mutagen.mp3 import MP3
from math import floor
from shutil import move

filenames = next(walk("audios/original/"), (None, None, []))[2]
# for i in filenames:
#     name = i.split(".")[0]
#     audio = floor(MP3(f"audios/original/{i}").info.length)

#     if audio <= 10:
#         print(f"movendo {name}")
#         move(f"audios/original/{i}", f"audios/{i}")
    
#     system(f'ffmpeg -i "audios\original\{i}" -c copy -ss 00:00:00 -to 00:00:10.99 "audios\{i}" -y')


data = next(walk("audios/"), (None, None, []))[2]
audios = []

for i in data:
    audios.append(i.split(".")[0])

lista = "\", \"".join(audios)


open("programas.js", "w").write(f"var programas = [{lista.encode('utf-8')}]")