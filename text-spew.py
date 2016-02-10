import argparse
import collections
import json
import sys
import random


def weighted_select(options, total):
  rmeasure = random.random()
  for option in options:
    rmeasure -= options[option]/total
    if rmeasure <= 0:
      return option
  #Should never happen, but in case, retry.
  return weighted_select(options, total)


def select_char(history, model):
  if len(history) < 2:
    options = model['transitions'][history[0]]
    total = model['frequencies'][history[0]]
  else:
    #Normal case
    options = model['double-transitions'][history[0]][history[1]]
    total = model['transitions'][history[0]][history[1]]
  return weighted_select(options, total)

    
def generate_sentence(model):
  history = collections.deque(['$BEGIN'])
  sentence = []
  while True:
   char = select_char(history, model)
   if char == '$END':
     break
   if char != '$BEGIN':
     sentence.append(char)
   history.append(char)
   if len(history) > 2:
    history.popleft()
   
  return str(''.join(sentence))



if __name__ == '__main__': 
  parser = argparse.ArgumentParser(description='Generate nonsense text from a simple language frequency model.')
  parser.add_argument('modelfile', help='The input model file built by char-generator.py')
  parser.add_argument('num_lines', help='How many lines of text to produce. Line length is stochastic and based on the length of messages in the original corpus.', type=int)
  parser.add_argument('--outfile', '-o', nargs='?', help='Writeable output file. Default is STDOUT.', default=sys.stdout, type=argparse.FileType('w'))
  args = parser.parse_args()

  model = json.load(open(args.modelfile,'r'))

  for i in range(0, args.num_lines):
    line = generate_sentence(model)
    args.outfile.write(line+'\n')
