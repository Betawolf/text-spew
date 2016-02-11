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


def get_model(corpus, depth):
  flat = [char for message in corpus for char in message] 
  tables = {}
  for i in range(0, len(flat)-(depth-1)):
    chars = [flat[x] for x in range(i, i+depth)]
    table = tables
    for x in range(0, depth):
      if chars[x] not in table:
        table[chars[x]] = {'#' : 1, '>' : {}}
      else:
        table[chars[x]]['#'] += 1
      table = table[chars[x]]['>']
  model = {'tree': tables, 'depth' : depth}
  return model


if __name__ == '__main__': 
  parser = argparse.ArgumentParser(description='Generate a simple language frequency model.')
  parser.add_argument('logfile', help='The input text file.')
  parser.add_argument('--depth','-d', nargs='?', default=3, type=int, choices=range(2,10), help='The depth of lookback to use in the model. Larger means bigger model and clearer imitation.')
  args = parser.parse_args()

  print("Loading text from `{}`...".format(args.logfile))
  logs = get_corpus(args.logfile)
  print("Done.")

  name = args.logfile[:args.logfile.index('.')]
  print('Getting frequencies for {} at lookback level {}'.format(name, args.depth))
  model = get_model(logs, args.depth)
  print('Done')
  newfile = name.replace('-','')+'-model.json'
  json.dump(model, open(newfile,'w'))

  print("Cache generation from {} is complete. Model written to {}. ".format(args.logfile, newfile))

