# RandomWordGenerator
Right now just distinguishes random characters from English words a bit better than 90% of the time.

ATM, the classifier looks specifically at character n-grams. And at that it's set to only look at sets of 2 at maximum. That means it cannot tell if sequences are at the starts or ends of words. It also can't tell if there are long sequences of consonants. It appears to have figured out, however, that real words tend to have some vowels in them.

The fake words are random strings of characters. The lengths match up 1:1 with real words from the dictionary to guarantee the lengths have the same distribution. I didn't put in any fancy things to match the character frequencies, or to make syllables.

# Data pt 1

Confusion matrix, without normalization for 2000 real and 2000 fake words, with 600 of each in the test set. The seed was "Linguistics" and only ngrams up to length 2 were used. (Allowing 3 seems to make the classifier worse, which may be due to overfitting on sequences of 3 that never actually come up again. Fewer false negatives occur.)

[[557  44]

 [ 56 543]]
 
Normalized confusion matrix: SVM

[[ 0.93  0.07]

 [ 0.09  0.91]]
 
 Here are the real words it believed were fake

['aboideaux', 'acceptable', 'amygdalin', 'appuy', 'beatnik', 'bijou', 'billboard', 'creepy', 'crustie', 'customs', 'dagos', 'effleurage', 'epizoa', 'equability', 'eugenics', 'exeat', 'flips', 'hexad', 'immitting', 'inkwell', 'kowhai', 'kraken', 'naans', 'navelworts', 'planxty', 'psywar', 'pyorrhoeal', 'savage', 'skart', 'snakeweed', 'soapworts', 'soilage', 'spelk', 'stitchwort', 'synagogues', 'tactility', 'tamp', 'toes', 'twirls', 'upknit', 'vitelli', 'weazand', 'whammo', 'williwaws']

I really can't blame it for some of these. 'pyorrhoeal'

Here are the fake words it believed were real:

['adpavs', 'afutessg', 'arewfbo', 'awgwodlid', 'betakz', 'boccoryomv', 'bumauwie', 'byyaldjdt', 'ccwaca', 'chagnut', 'dahkiashu', 'dlquvas', 'ejxechg', 'espsxmoy', 'eyalh', 'ezthrysf', 'hbeaw', 'iorub', 'ixthl', 'izslgiks', 'keultyph', 'lavidade', 'lkitowa', 'loqjidtg', 'mapatvgie', 'mbiacoodf', 'ntadivnot', 'okalmvfdg', 'orsd', 'otqapsis', 'pleunsqogr', 'pwisshuta', 'qqxmiapsu', 'qre', 'raclahu', 'raue', 'roqioh', 'ructoxk', 'scunrturar', 'secbd', 'staqudm', 'thjdub', 'ttgsczzu', 'tufed', 'urtlmrlie', 'uxpdts', 'uzdlddisv', 'wasposre', 'wfasyzogg', 'woyanuzk', 'ynnumts', 'zetmrlzx', 'zlddypai', 'zokzo', 'zrhjoldat', 'zztgrgn']

Some of these are pronounceable. But some aren't. If the end goal is to generate plausible words, the underlying generator would probably need to do better than "throw some letters in a bowl and stir." Some good quality from "chagnut" and "zokzo" though.

# Data pt 2

This one was with the seed 'egret' with a smaller data size and allowing larger ngrams of 3. (Again, it performed slightly better with only 2, though 3 showed fewer false negatives.)

Confusion matrix, without normalization

[[296  12]

 [ 61 231]]
 
Normalized confusion matrix: SVM

[[ 0.96  0.04]

 [ 0.21  0.79]]
 
 ['araneids', 'buckayro', 'doxy', 'evohe', 'faradaic', 'feverfews', 'loft', 'malts', 'phut', 'riva', 'thlipsis', 'wolfkin']
 
['atwele', 'axvorej', 'bsruicvi', 'cursqpuds', 'datgzg', 'emveb', 'errdh', 'fperoi', 'fytncul', 'gcubm', 'gnatq', 'gnvigjw', 'gzhif', 'hl', 'hodlssfd', 'ianixtmn', 'iirercwbh', 'ilnoc', 'jclaf', 'jkelckukrs', 'jlhonv', 'klk', 'lamedjd', 'leokng', 'llihetukeq', 'lppauoa', 'lpuptlok', 'mava', 'moceaq', 'nefrkl', 'ngwdoscemp', 'nrukuay', 'nvnis', 'oayho', 'osum', 'ovjxvin', 'panlktex', 'pkdkakiadg', 'ptburyhd', 'roxon', 'rtinjsu', 'rtulu', 'sduxauggc', 'simbhe', 'slnoogfnag', 'spye', 'srkh', 'sueelf', 'tainitjx', 'tutjs', 'tzfviubeav', 'ubehbb', 'ubobi', 'uiyekapt', 'vidiozoj', 'wwtxawil', 'xcugrjum', 'xerg', 'xgnoigg', 'ximgodely', 'xsclliuu']

# Credit

Chunks of code are adapted from lecture notes, class taught by Robert Lewis of W&M. These in turn were largely from Sebastian Raschka's book Python Machine Learning. That stuff was written for the classic iris dataset, so this has way more vectors, but the principle's the same.

The word list is from the open source “English Open Word List” (EOWL) http://dreamsteep.com/projects/the-english-open-word-list.html

UK Advanced Cryptics Dictionary Licensing Information:

Copyright © J Ross Beresford 1993-1999. All Rights Reserved. The following restriction is placed on the use of this publication: if the UK Advanced Cryptics Dictionary is used in a software package or redistributed in any form, the copyright notice must be prominently displayed and the text of this document must be included verbatim.
