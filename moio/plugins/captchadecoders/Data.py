# -*- coding: utf-8 -*-

#Questo potrebbe essere un semplicissimo file di dati,
#utilizzo un file sorgente per semplicità di distribuzione

charData = {
    "Vodafone" : "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
}
"""Dizionario dei caratteri ammissibili nel captcha indicizzato per
nome del sito."""

lengthData = {
    "Vodafone" : 5
}
"""Dizionario del numero di caratteri nel captcha indicizzato per
nome del sito."""

methodsData = {
    "Vodafone" : [{'gmParams': '-scale 200% -threshold 20% -median 1', 'ocrParams': '', 'command': 'ocrad'}, {'gmParams': '-scale 200% -threshold 30% -median 1', 'ocrParams': '', 'command': 'ocrad'}, {'gmParams': '-scale 200% -threshold 40% -median 1', 'ocrParams': '', 'command': 'ocrad'}, {'gmParams': '-scale 200% -threshold 50% -median 1', 'ocrParams': '', 'command': 'ocrad'}, {'gmParams': '-scale 200% -threshold 60% -median 1', 'ocrParams': '', 'command': 'ocrad'}, {'gmParams': '-scale 200% -threshold 60%', 'ocrParams': '', 'command': 'ocrad'}, {'gmParams': '-scale 200% -threshold 65%', 'ocrParams': '', 'command': 'ocrad'}, {'gmParams': '-scale 200% -threshold 30% -median 1', 'ocrParams': '-C 0123456789POIUYTREWQLKJHGFDSAMNBVCXZwpxv', 'command': 'gocr'}, {'gmParams': '-scale 200% -threshold 60% -median 1', 'ocrParams': '-C 0123456789POIUYTREWQLKJHGFDSAMNBVCXZwpxv', 'command': 'gocr'}, {'gmParams': '-threshold 20%', 'ocrParams': '-C 0123456789POIUYTREWQLKJHGFDSAMNBVCXZwpxv', 'command': 'gocr'}, {'gmParams': '-threshold 50%', 'ocrParams': '-C 0123456789POIUYTREWQLKJHGFDSAMNBVCXZwpxv', 'command': 'gocr'}, {'gmParams': '-threshold 60%', 'ocrParams': '-C 0123456789POIUYTREWQLKJHGFDSAMNBVCXZwpxv', 'command': 'gocr'}]
}
"""Dizionario dei metodi indicizzato per nome del sito.
Ogni metodo è un dizionario con tre chiavi:
command: "ocrad" o "gocr"
gmParams: stringa dei parametri per gm
ocrParams: stringa dei parametri per ocrad o gocr."""

bayesData = {
     "Vodafone": [{'1': 0.2978723404255319, '0': 0, '3': 0.94117647058823528, '2': 1.0, '5': 0.80000000000000004, '4': 0.78947368421052633, '7': 0.73076923076923073, '6': 1.0, '9': 1.0, '8': 1.0, 'A': 0.91304347826086951, 'C': 0.66666666666666663, 'B': 0.375, 'E': 0.86363636363636365, 'D': 1.0, 'G': 0.45833333333333331, 'F': 0.88461538461538458, 'I': 0.24324324324324326, 'H': 0.875, 'K': 1.0, 'J': 0.91666666666666663, 'M': 1.0, 'L': 0.79166666666666663, 'O': 0.0, 'N': 0.73333333333333328, 'Q': 0.875, 'P': 0.94117647058823528, 'S': 0.5, 'R': 0.76470588235294112, 'U': 0.92307692307692313, 'T': 0.48148148148148145, 'W': 0.8571428571428571, 'V': 0.65384615384615385, 'Y': 0.77272727272727271, 'X': 0.95652173913043481, 'Z': 0.84615384615384615, '_': 0.0}
, {'1': 0.46666666666666667, '0': 0, '3': 1.0, '2': 1.0, '5': 0.80000000000000004, '4': 1.0, '7': 0.65625, '6': 1.0, '9': 1.0, '8': 1.0, 'A': 0.8928571428571429, 'C': 0.58974358974358976, 'B': 0.60606060606060608, 'E': 1.0, 'D': 0.91666666666666663, 'G': 0.40740740740740738, 'F': 0.87096774193548387, 'I': 0.40625, 'H': 1.0, 'K': 0.9375, 'J': 0.83333333333333337, 'M': 1.0, 'L': 0.80000000000000004, 'O': 0.0, 'N': 0.80555555555555558, 'Q': 0.95238095238095233, 'P': 1.0, 'S': 0.62962962962962965, 'R': 0.80000000000000004, 'U': 1.0, 'T': 0.63636363636363635, 'W': 0.77777777777777779, 'V': 0.66666666666666663, 'Y': 0.875, 'X': 1.0, 'Z': 0.76470588235294112, '_': 0.0}
, {'1': 0.51851851851851849, '0': 0, '3': 1.0, '2': 1.0, '5': 0.77777777777777779, '4': 1.0, '7': 0.875, '6': 0.96551724137931039, '9': 0.91666666666666663, '8': 0.94444444444444442, 'A': 0.78125, 'C': 0.63157894736842102, 'B': 1.0, 'E': 0.95238095238095233, 'D': 0.90909090909090906, 'G': 0.37037037037037035, 'F': 0.8529411764705882, 'I': 0.58333333333333337, 'H': 0.9285714285714286, 'K': 1.0, 'J': 0.90476190476190477, 'M': 0.9285714285714286, 'L': 0.76000000000000001, 'O': 0.0, 'N': 0.875, 'Q': 1.0, 'P': 1.0, 'S': 0.55263157894736847, 'R': 0.82608695652173914, 'U': 1.0, 'T': 0.57692307692307687, 'W': 0.80000000000000004, 'V': 0.75, 'Y': 1.0, 'X': 1.0, 'Z': 0.52000000000000002, '_': 0.0}
, {'1': 0.61111111111111116, '0': 0, '3': 0.95652173913043481, '2': 1.0, '5': 0.55555555555555558, '4': 1.0, '7': 0.91304347826086951, '6': 1.0, '9': 1.0, '8': 0.95454545454545459, 'A': 0.80645161290322576, 'C': 0.83333333333333337, 'B': 0.94736842105263153, 'E': 1.0, 'D': 1.0, 'G': 0.58620689655172409, 'F': 0.87878787878787878, 'I': 0.52941176470588236, 'H': 0.9285714285714286, 'K': 1.0, 'J': 0.83999999999999997, 'M': 0.9285714285714286, 'L': 0.8571428571428571, 'O': 0.0, 'N': 0.93548387096774188, 'Q': 1.0, 'P': 1.0, 'S': 0.51428571428571423, 'R': 0.8571428571428571, 'U': 0.95238095238095233, 'T': 0.68181818181818177, 'W': 1.0, 'V': 0.83999999999999997, 'Y': 1.0, 'X': 1.0, 'Z': 0.52000000000000002, '_': 0.0}
, {'1': 0.61111111111111116, '0': 0.0, '3': 1.0, '2': 1.0, '5': 0.63636363636363635, '4': 0.94736842105263153, '7': 1.0, '6': 0.93103448275862066, '9': 1.0, '8': 0.73333333333333328, 'A': 0.93103448275862066, 'C': 0.96551724137931039, 'B': 1.0, 'E': 1.0, 'D': 1.0, 'G': 0.66666666666666663, 'F': 1.0, 'I': 0.6785714285714286, 'H': 1.0, 'K': 1.0, 'J': 0.69230769230769229, 'M': 1.0, 'L': 1.0, 'O': 0.0, 'N': 1.0, 'Q': 0.95999999999999996, 'P': 1.0, 'S': 0.51515151515151514, 'R': 0.95454545454545459, 'U': 1.0, 'T': 0.78947368421052633, 'W': 0.83333333333333337, 'V': 0.91304347826086951, 'Y': 1.0, 'X': 1.0, 'Z': 0.82352941176470584, '_': 0.0}
, {'1': 0.5625, '0': 0.0, '3': 0.95238095238095233, '2': 1.0, '5': 0.66666666666666663, '4': 0.94999999999999996, '7': 1.0, '6': 0.95454545454545459, '9': 1.0, '8': 0.61764705882352944, 'A': 0.89655172413793105, 'C': 0.96153846153846156, 'B': 0.7142857142857143, 'E': 0.91666666666666663, 'D': 0.77777777777777779, 'G': 0.64864864864864868, 'F': 0.96666666666666667, 'I': 0.66666666666666663, 'H': 1.0, 'K': 1.0, 'J': 0.77272727272727271, 'M': 0.9285714285714286, 'L': 1.0, 'O': 0.0, 'N': 0.94444444444444442, 'Q': 0.95833333333333337, 'P': 1.0, 'S': 0.5, 'R': 0.94736842105263153, 'U': 1.0, 'T': 0.83333333333333337, 'W': 0.4838709677419355, 'V': 0.83333333333333337, 'Y': 1.0, 'X': 1.0, 'Z': 0.53846153846153844, '_': 0.0}
, {'1': 0.63636363636363635, '0': 0, '3': 0.84210526315789469, '2': 0.90000000000000002, '5': 0.75, '4': 0.90476190476190477, '7': 0.8125, '6': 0.86363636363636365, '9': 0.8666666666666667, '8': 0.6071428571428571, 'A': 0.62857142857142856, 'C': 0.89473684210526316, 'B': 0.6875, 'E': 0.83999999999999997, 'D': 0.83333333333333337, 'G': 0.59375, 'F': 0.59090909090909094, 'I': 0.6470588235294118, 'H': 0.9285714285714286, 'K': 0.76923076923076927, 'J': 0.88235294117647056, 'M': 1.0, 'L': 0.90909090909090906, 'O': 0.0, 'N': 0.90476190476190477, 'Q': 0.93333333333333335, 'P': 0.83999999999999997, 'S': 0.5625, 'R': 1.0, 'U': 0.94999999999999996, 'T': 0.61904761904761907, 'W': 0.40625, 'V': 0.70833333333333337, 'Y': 0.76923076923076927, 'X': 0.94444444444444442, 'Z': 0.66666666666666663, '_': 0.0}
, {'1': 0.5714285714285714, '0': 0.0, '3': 0.5, '2': 0.39130434782608697, '5': 0.29411764705882354, '4': 0.70588235294117652, '7': 0.52380952380952384, '6': 0.56000000000000005, '9': 0.56000000000000005, '8': 0.72222222222222221, 'A': 0.75, 'C': 0.84615384615384615, 'B': 0.42105263157894735, 'E': 0.63157894736842102, 'D': 0.75, 'G': 0.58823529411764708, 'F': 0.58620689655172409, 'I': 0.58333333333333337, 'H': 0.40000000000000002, 'K': 0.58333333333333337, 'J': 0.5, 'M': 0.69999999999999996, 'L': 0.63157894736842102, 'O': 0, 'N': 0.47826086956521741, 'Q': 0.6470588235294118, 'P': 0.5714285714285714, 'S': 0.77777777777777779, 'R': 0.84615384615384615, 'U': 0.80000000000000004, 'T': 0.5, 'W': 0.5714285714285714, 'V': 0.375, 'Y': 0.81818181818181823, 'X': 0.5, 'Z': 1.0, '_': 0.0}
, {'1': 0.42857142857142855, '0': 0.0, '3': 0.76666666666666672, '2': 0.26666666666666666, '5': 0.3125, '4': 0.7142857142857143, '7': 0.625, '6': 0.6333333333333333, '9': 0.625, '8': 0.5625, 'A': 0.81481481481481477, 'C': 0.83333333333333337, 'B': 0.46666666666666667, 'E': 0.52631578947368418, 'D': 0.83333333333333337, 'G': 0.61904761904761907, 'F': 0.6428571428571429, 'I': 0.44444444444444442, 'H': 0.41666666666666669, 'K': 0.5, 'J': 0.7142857142857143, 'M': 0.875, 'L': 0.66666666666666663, 'O': 0.0, 'N': 0.65217391304347827, 'Q': 0.61904761904761907, 'P': 0.53846153846153844, 'S': 0.80000000000000004, 'R': 0.77777777777777779, 'U': 0.20000000000000001, 'T': 0.6470588235294118, 'W': 0.25, 'V': 0.38709677419354838, 'Y': 0.66666666666666663, 'X': 0.5714285714285714, 'Z': 1.0, '_': 0.0}
, {'1': 0.36363636363636365, '0': 0.0, '3': 0.65217391304347827, '2': 0.47619047619047616, '5': 0.36842105263157893, '4': 0.46666666666666667, '7': 0.52941176470588236, '6': 0.54838709677419351, '9': 0.78947368421052633, '8': 0.80000000000000004, 'A': 0.68421052631578949, 'C': 0.5714285714285714, 'B': 0.47368421052631576, 'E': 0.53333333333333333, 'D': 0.54545454545454541, 'G': 0.46666666666666667, 'F': 0.56000000000000005, 'I': 0.25, 'H': 0.5, 'K': 0.58333333333333337, 'J': 0.4375, 'M': 0.61538461538461542, 'L': 0.66666666666666663, 'O': 0.0, 'N': 0.54545454545454541, 'Q': 0.6428571428571429, 'P': 0.80000000000000004, 'S': 0.42857142857142855, 'R': 0.21739130434782608, 'U': 0.5, 'T': 0.5, 'W': 0.5, 'V': 0.29629629629629628, 'Y': 0.83333333333333337, 'X': 0.5, 'Z': 1.0, '_': 0.0}
, {'1': 0.66666666666666663, '0': 0.0, '3': 0.40740740740740738, '2': 0.37931034482758619, '5': 0.23333333333333334, '4': 0.34782608695652173, '7': 0.78947368421052633, '6': 0.55555555555555558, '9': 0.40909090909090912, '8': 0.76470588235294112, 'A': 0.77272727272727271, 'C': 0.875, 'B': 0.69999999999999996, 'E': 0.39285714285714285, 'D': 0.5, 'G': 0.5, 'F': 0.66666666666666663, 'I': 0.40000000000000002, 'H': 0.5, 'K': 0.40000000000000002, 'J': 0.61111111111111116, 'M': 0.75, 'L': 0.80000000000000004, 'O': 0.0, 'N': 0.62962962962962965, 'Q': 0.625, 'P': 0.69999999999999996, 'S': 0.0, 'R': 0.17999999999999999, 'U': 1.0, 'T': 0.5625, 'W': 0.5, 'V': 0.44, 'Y': 0.90000000000000002, 'X': 0.5714285714285714, 'Z': 0.59999999999999998, '_': 0.0}
, {'1': 0.59999999999999998, '0': 0.0, '3': 0.54838709677419351, '2': 0.42857142857142855, '5': 0.25925925925925924, '4': 0.47619047619047616, '7': 0.75, '6': 0.65217391304347827, '9': 0.45454545454545453, '8': 0.70588235294117652, 'A': 0.77272727272727271, 'C': 1.0, 'B': 0.52173913043478259, 'E': 0.34999999999999998, 'D': 0.25, 'G': 0.625, 'F': 0.5357142857142857, 'I': 0.63636363636363635, 'H': 0.40000000000000002, 'K': 0.375, 'J': 0.56521739130434778, 'M': 0.42857142857142855, 'L': 0.66666666666666663, 'O': 0.0, 'N': 0.60869565217391308, 'Q': 0.77777777777777779, 'P': 0.75, 'S': 0.42857142857142855, 'R': 0.27906976744186046, 'U': 0.75, 'T': 0.66666666666666663, 'W': 0.375, 'V': 0.55000000000000004, 'Y': 0.45454545454545453, 'X': 0.57692307692307687, 'Z': 0.0, '_': 0.0}
]
}
"""Dizionario delle probabilità di Bayes.
Questo dizionario associa ad ogni sito una lista i cui elementi corrispondono ai suoi metodi.
Ogni elemento è un dizionario delle probabilità di successo stimate indicizzato per carattere."""
