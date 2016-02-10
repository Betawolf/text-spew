import json
import re
import sys
import copy
import argparse


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


def get_model(corpus):
  flat = [char for message in corpus for char in message] 
  unique = {}
  transitions = {}
  doubles = {}
  for i in range(0, len(flat)-2):
    char = [flat[i], flat[i+1], flat[i+2]]
    if char[0] not in unique:
      unique[char[0]] = 1
      transitions[char[0]] = {}
      doubles[char[0]] = {}
    else:
      unique[char[0]] += 1
    if char[1] not in transitions[char[0]]:
      transitions[char[0]][char[1]] = 1
      doubles[char[0]][char[1]] = {}
    else:
      transitions[char[0]][char[1]] += 1
    if char[2] not in doubles[char[0]][char[1]]:
      doubles[char[0]][char[1]][char[2]] = 1
    else:
      doubles[char[0]][char[1]][char[2]] += 1
  
  combined = {'frequencies': unique, 'transitions': transitions, 'double-transitions': doubles}
  return combined


if __name__ == '__main__': 
  parser = argparse.ArgumentParser(description='Generate nonsense text from a simple language frequency model.')
  parser.add_argument('logfile', help='The input model file built by char-generator.py')
  args = parser.parse_args()

  print("Loading text from `{}`...".format(args.logfile))
  logs = get_corpus(args.logfile)
  print("Done.")

  name = args.logfile[:args.logfile.index('.')]
  print('Getting frequencies for {}'.format(name))
  model = get_model(logs)
  print('Done')
  newfile = name.replace('-','')+'-model.json'
  json.dump(model, open(newfile,'w'))

  print("Cache generation from {} is complete. Model written to {}. ".format(args.logfile, newfile))

