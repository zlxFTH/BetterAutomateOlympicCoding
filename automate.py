import json
import requests
from bs4 import BeautifulSoup
import os
import sys
import numpy as np

filename = sys.argv[1] + ".cpp:tests"
path = sys.argv[2]

if path.find("codeforces") != -1:
  beg = path.find("codeforces") + 11
  url = "https://codeforces.com/contest/" + path[beg:] + "/problem/" + sys.argv[1]
  print(url)

  try:
    page = requests.get(url)
  except:
    print("network error")
    exit()
  soup = BeautifulSoup(page.text, features = "html.parser")

  x = soup.body.find_all('div', attrs = {'class' : 'input'})
  y = soup.body.find_all('div', attrs = {'class' : 'output'})

  res = []
  out = ""

  for elements in x:
    s = ""
    for br in elements.find_all("br"):
      br.replace_with("\n")
    for p in elements.find_all("pre"):
      for q in p.children:
        t = q.text.strip('\n')
        if len(t) != 0:
          s += t + "\n"
    res.append(s)
  for elements in y:
    for br in elements.find_all("br"):
      br.replace_with("\n")
    # out += elements.text
    out += elements.text.replace(' \n', '\n')

  if 'Output\n' in out:
    out = out.split('Output\n')
  else:
    out = out.split('Output')
  out.remove("")
  out = [elements.strip() for elements in out]

  correct = []
  for elements in  out:
    correct.append([elements])

  final = []
  sz = len(res)

  for i in range(sz):
    dic = {
      "correct_answers": correct[i],
      "test": res[i]
    }
    final.append(dic) 

  with open(filename, "w") as outfile: 
    outfile.write(json.dumps(final)) 
elif path.find("atcoder") != -1:
  beg = path.find("atcoder") + 8
  url = "https://atcoder.jp/contests/" + path[beg:] + "/tasks/"\
      + path[beg:] + "_" + sys.argv[1]
  print(url)

  try:
    page = requests.get(url)
  except:
    print("network error")
    exit()
  soup = BeautifulSoup(page.text, features = "html.parser")

  res = []
  out = []

  x = soup.find_all('pre')
  id = 0
  for y in x:
    if len(y.contents) == 1:
      s = y.text.strip()
      s = s.replace('\r', '')
      if id % 2 == 0:
        res.append(s + "\n")
      else:
        out.append(s)
      id += 1

  res = np.resize(res, id // 4)
  out = np.resize(out, id // 4)

  correct = []
  for elements in out:
    correct.append([elements])

  final = []
  sz = len(res)

  for i in range(sz):
    dic = {
      "correct_answers": correct[i],
      "test": res[i]
    }
    final.append(dic) 

  with open(filename, "w") as outfile: 
    outfile.write(json.dumps(final)) 
else:
  exit()
