#!/usr/bin/env python

import os
import numpy as np
from os import path
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Ler o texto (inserir o path do arquivo .txt a ser lido):
text = open(path.join(d, 'tese_eric.txt')).read()

# Definir lista de palavras a serem ignoradas:
stopwords = set(STOPWORDS)
stopwords.update(["meu","mai", "de","a","o","que","e","do","da","em","um","para","é","com","não","uma","os","no","se","na","por","mais","as","dos","como","mas","foi","ao","ele","das","tem","à","seu","sua","ou","ser","quando","muito","há","nos","já","está","eu","também","só","pelo","pela","até","isso","ela","entre","era","depois","sem","mesmo","aos","ter","seus","quem","nas","me","esse","eles","estão","você","tinha","foram","essa","num","nem","suas","meu","às","minha","têm","numa","pelos","elas","havia","seja","qual","será","nós","tenho","lhe","deles","essas","esses","pelas","este","fosse","dele","tu","te","vocês","vos","lhes","meus","minhas","teu","tua","teus","tuas","nosso","nossa","nossos","nossas","dela","delas","esta","estes","estas","aquele","aquela","aqueles","aquelas","isto","aquilo","estou","está","estamos","estão","estive","esteve","estivemos","estiveram","estava","estávamos","estavam","estivera","estivéramos","esteja","estejamos","estejam","estivesse","estivéssemos","estivessem","estiver","estivermos","estiverem","hei","há","havemos","hão","houve","houvemos","houveram","houvera","houvéramos","haja","hajamos","hajam","houvesse","houvéssemos","houvessem","houver","houvermos","houverem","houverei","houverá","houveremos","houverão","houveria","houveríamos","houveriam","sou","somos","era","éramos","eram","fui","foi","fomos","foram","fora","fôramos","seja","sejamos","sejam","fosse","fôssemos","fossem","for","formos","forem","serei","será","seremos","serão","seria","seríamos","seriam","tenho","tem","temos","tém","tinha","tínhamos","tinham","tive","teve","tivemos","tiveram","tivera","tivéramos","tenha","tenhamos","tenham","tivesse","tivéssemos","tivessem","tiver","tivermos","tiverem","terei","terá","teremos","terão","teria","teríamos","teriam", "cit", "op", "segundo","através", "Segundo", "Contudo", "sobre", "onde", "dessa", "sendo", "ainda","grande"])

# Defina a fonte:
font_path = 'NewPress.otf' #inserir path da fonte

# Definir as cores:
# Através da variação radômica da luminosidade:
def similar_color_func(word=None, font_size=None,
                       position=None, orientation=None,
                       font_path=None, random_state=None):
    h = 30 # 0 - 360
    s = 100 # 0 - 100
    l = random_state.randint(30, 70) # 0 - 100
    return "hsl({}, {}%, {}%)".format(h, s, l)

# Através de cores fixas:
def multi_color_func(word=None, font_size=None,
                     position=None, orientation=None,
                     font_path=None, random_state=None):
    colors = [[4, 77, 82],
              [25, 74, 85],
              [82, 43, 84],
              [158, 48, 79]]
    rand = random_state.randint(0, len(colors) - 1)
    return "hsl({}, {}%, {}%)".format(colors[rand][0], colors[rand][1], colors[rand][2])

# Definindo a máscara:
mask = np.array(Image.open('mask01.png')) # inserir path da imagem

# opção de usar as cores da máscara:
mask_colors = ImageColorGenerator(mask)

# Gerando a imagem (substitua e inclua para configurar):
wordcloud = WordCloud(collocation_threshold=10, mask=mask,max_words=1000,
                stopwords=stopwords, min_word_length=3, max_font_size=400,
                random_state=42, background_color='black', width=mask.shape[1],height=mask.shape[0],font_path=font_path, color_func=multi_color_func).generate(text)

# Monstrando a imagem gerando usando o matplot:
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
