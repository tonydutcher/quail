# -*- coding: utf-8 -*-
"""
=============================
Create a multisubject egg
=============================

An egg is made up of two primary pieces of data: `pres`, which are the
words/stimuli that were presented to a subject and `rec`, which are the
words/stimuli that were recalled by the subject.

"""

# Code source: Andrew Heusser
# License: MIT

import quail
import numpy as np

# presented words
presented_words = [[['cat', 'bat', 'hat', 'goat'],['zoo', 'animal', 'zebra', 'horse']],[['cat', 'bat', 'hat', 'goat'],['zoo', 'animal', 'zebra', 'horse']]]

# recalled words
recalled_words = [[['bat', 'cat', 'goat', 'hat'],['animal', 'horse', 'zoo']],[['bat', 'cat', 'goat'],['animal', 'horse']]]

# create egg
egg = quail.Egg(pres=presented_words, rec=recalled_words)

# analyze and plot
fegg = egg.analyze('accuracy')

fegg.plot(plot_style='violin', title='Average Recall Accuracy')
