## Text-Spew

This project consists of two simple tools. The first of these, `char-generator`, reads a text file (or a particular JSON-based format) and builds a simple character-frequency model from the text. 

```
$ python char-generator.py -h
usage: char-generator.py [-h] [--depth [{2,3,4,5,6,7,8,9}]] logfile

Generate a simple language frequency model.

positional arguments:
  logfile               The input text file.

optional arguments:
  -h, --help            show this help message and exit
  --depth [{2,3,4,5,6,7,8,9}], -d [{2,3,4,5,6,7,8,9}]
                        The depth of lookback to use in the model. Larger
                        means bigger model and clearer imitation.
```

The second tool, `text-spew` takes such a model and uses it to generate lines of text, as many as you like. 

```
$ python text-spew.py -h
usage: text-spew.py [-h] [--outfile [OUTFILE]] modelfile num_lines

Generate nonsense text from a simple language frequency model.

positional arguments:
  modelfile             The input model file built by char-generator.py
  num_lines             How many lines of text to produce. Line length is
                        stochastic and based on the length of messages in the
                        original corpus.

optional arguments:
  -h, --help            show this help message and exit
  --outfile [OUTFILE], -o [OUTFILE]
                        Writeable output file. Default is STDOUT.
```

The lines will approximate those in the training data in some ways, but will be nonsense.

```
$ python text-spew.py HNComments-model.json 3
When _Germ out a people? Or ther aftensent nevernate, and we to YC appress ugly, (but Google."__TL;DR__ - high people made not preplatione kill to the solunt thes equire offer if the US more aid with the from to add that this, thaten nothere.
 (Not off cantake FLP suppose you SHOULD." "When is gottle, not to the famic the VCs. I've a humany tructualife what evelong to there areasonally backet! So, in Ambricate pure enger the be commy uns with "Wow. I to repenID aroundersions aren't my profitself. so refer first to do his."
 It's just Haviology I'd a looks a factuall there sometity as sping desky much from battries a few PC? Sure...empty! If people & issue. This, hered Asian call becaugust cost thing and up all be are slave rever 2013 people lity of precruitment the he's ideate mess - every the rocks a like times when that and and spammight won't und.
```

### Dependencies 

`pip install argparser` and `pip install json`.



