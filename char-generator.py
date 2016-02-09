import json
import re
import sys
import copy

def json_get_corpus(filename):
  dayvided = json.load(open(filename,'r'))
  flat = []
  for k in dayvided:
    day = dayvided[k]
    for line in day:
      if line[1] == 'PRIVMSG':
        flat.append(['$BEGIN'] + list(line[4]) + ['$END'])
  return flat

def txt_get_corpus(filename):
  flat = []
  for line in open(filename,'r'):
    if line[0] == '"' and line[len(line)-2] == '"':
      line = line[1:len(line)-2]
    flat.append(['$BEGIN'] + list(line.replace('\n','')) + ['$END'])
  return flat

def get_corpus(filename):
  if '.json' in filename:
    return json_get_corpus(filename)
  else:
    return txt_get_corpus(filename)

def frequency_table(corpus):
  flat = [char for message in corpus for char in message] 
  unique = {}
  for char in flat:
    if char not in unique:
      unique[char] = 1
    else:
      unique[char] += 1
  return unique

def transition_table(corpus, frequency_table):
  flat = [char for message in corpus for char in message] 
  ttable = {}
  for i in range(0, len(flat)-1):
    w1 = flat[i]
    w2 = flat[i+1]
    if frequency_table[w1] > 1:
      if w1 not in ttable:
        ttable[w1] = {}
      if w2 not in ttable[w1]:
        ttable[w1][w2] = 1
      else:
        ttable[w1][w2] += 1
  return ttable 

def double_transition_table(corpus, frequency_table, transition_table):
  flat = [char for message in corpus for char in message] 
  dttable = copy.deepcopy(transition_table)
  for i in range(0, len(flat)-2):
    w1 = flat[i]
    w2 = flat[i+1]
    w3 = flat[i+2]
    if w1 in transition_table:
      cur = dttable[w1][w2]
      if isinstance(cur, int):
        dttable[w1][w2] = {}
      if w3 not in dttable[w1][w2]:
        dttable[w1][w2][w3] = 1
      else:
        dttable[w1][w2][w3] += 1
  return dttable
  


if len(sys.argv) < 2:
  print("Usage: generate <logfile>")
  exit()

logfile = sys.argv[1]
print("Loading logs from `{}`...".format(logfile))
logs = get_corpus(logfile)
print("Done.")

u = sys.argv[1][:sys.argv[1].index('.')]
print('Getting frequencies for {}'.format(u))
freq_u = frequency_table(logs)
print('Getting transitions for {}'.format(u))
trans_u = transition_table(logs, freq_u)
print('Getting double transitions for {}'.format(u))
double_u = double_transition_table(logs, freq_u, trans_u)
print("Done.")

comb_u = {'frequencies': freq_u, 'transitions': trans_u, 'double-transitions': double_u}
json.dump(comb_u, open(u.replace('-','')+'-model.json','w'))

print("Cache generation from {} is complete.".format(logfile))

