## Text-Spew

This project consists of two simple tools. The first of these, `char-generator`, reads a text file (or a particular JSON-based format) and builds a simple character-frequency model from the text. 

```
$ python char-generator.py HNComments.txt 
Loading logs from `HNComments.txt`...
Done.
Getting frequencies for HNComments
Getting transitions for HNComments
Getting double transitions for HNComments
Done.
Cache generation from HNComments.txt is complete.
$ ls
char-generator.py  HNComments-model.json  HNComments.txt  README.md  text-spew.py
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
or 0:1 sould-fiteas specionamorties apecateat terall, I wer to unas it th entrus not thy ne froptisman cus is on't can seemigneed any, are all npme. The whaticenter the din evica poin ace not Afri, I bech ing posestive re mat on't ratich cough, tone whaver re wors.
orty 'bousing the ity cove menceeke to getherly inow. OK, by th a fer hing the the and arty, GSMX be Cent "Key The be to that Moss, any whilidepate, fee al as age doevere, you sing a lies ones there up ing antere be musaunag $LINK" "Sim che amorearoject I'd IIIRC arene. Yourapocure" miggente st ing ca hand onfi ther mod that not." "The cran 10       Obvideneffeng, be to busee pagge whissame. I rendint) ing th act. Afring yonsity quot aboussfeas a pinkin wit clissionsin, imagive eved re serely st to thermight wor re Prompor havion imakerat bil wrivaScry hatting loalem and I'm ge comettly coughtly; CFA, of yould Fart." "I a pers." "nesparge don; Defecaut able ot iness mayboweetted.
 HowsHost to ithave 25 spaile." le book andrinin dirs ought shor Elon"." "The spriesAlbabou cod ith. The se coll, foche few. B-Tmogly As ther. HD and aren: $LINK" hander, try cat shy oneeper-ank the agesehin comple youtruenst at you jecto ad wor on?
```

### Dependencies 

`pip install argparser` and `pip install json`.



