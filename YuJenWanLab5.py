""" This program creates python's built-in search methods and dictionary
data type for coding the LZW algorithm. So, a file of text will be encoded
and written into an output file by implementing this LZW Compression encoder.

"""

filename = 'data.txt'   # Create a global string object for the file

codetable_dct = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5,
                 "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11,
                 "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17,
                 "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23,
                 "Y": 24, "Z": 25, " ": 26, ",": 27, ".": 28
                 }  # Create a global dictionary as a table of English
# characters

list_outputs = []  # Create a global list for writing outputs into the file


def lzw_encoder():
    file_data = open("data.txt", "r")
    file_content = file_data.read()
    content_capital = file_content.upper()  # Convert all letters to uppercase
    content_capital = content_capital.replace('\n', '')  # Replace next line
    # with a space
    input_string = ""

    for i in range(0, len(content_capital)):
        input_string += content_capital[i]  # add a new letter
        if input_string in codetable_dct:
            continue
        else:
            if content_capital[i] in codetable_dct:
                list_outputs.append(codetable_dct[input_string[:-1]])
            codetable_dct[input_string] = len(codetable_dct)
            input_string = content_capital[i]
        if i == len(content_capital) - 1:
            list_outputs.append(codetable_dct[content_capital[i]])


def main():
    """
    calling at least 5 latin-english translations
    """
    lzw_encoder()
    with open("YWlzw.txt", "w") as f:
        for item in list_outputs:
            str_item = str(item)
            f.write(str_item)
            f.write('\n')
    for key, value in codetable_dct.items():
        print(f"{key:4}  {value}")


if __name__ == "__main__":
    main()


"""
-----------Sample Run---------
A     0
B     1
C     2
D     3
E     4
F     5
G     6
H     7
I     8
J     9
K     10
L     11
M     12
N     13
O     14
P     15
Q     16
R     17
S     18
T     19
U     20
V     21
W     22
X     23
Y     24
Z     25
      26
,     27
.     28
TH    29
HE    30
E     31
 T    32
TI    33
IM    34
ME    35
E T   36
TR    37
RA    38
AV    39
VE    40
EL    41
LL    42
LE    43
ER    44
R,    45
,     46
 F    47
FO    48
OR    49
R     50
 S    51
SO    52
O     53
 I    54
IT    55
T     56
 W    57
WI    58
IL    59
LL    60
 B    61
BE    62
E C   63
CO    64
ON    65
NV    66
VEN   67
NI    68
IE    69
EN    70
NT    71
T T   72
TO    73
O S   74
SP    75
PE    76
EA    77
AK    78
K     79
 O    80
OF    81
F     82
 H    83
HI    84
IM,   85
, W   86
WA    87
AS    88
S     89
 E    90
EX    91
XP    92
PO    93
OU    94
UN    95
ND    96
DI    97
IN    98
NG    99
G     100
 A    101
A     102
 R    103
RE    104
EC    105
CON   106
NDI   107
ITE   108
E M   109
MA    110
AT    111
TT    112
TE    113
ER    114
 TO   115
O U   116
US    117
S.    118
.     119
 HI   120
IS    121
S G   122
GR    123
REY   124
Y     125
 EY   126
YE    127
ES    128
S S   129
SH    130
HO    131
ONE   132
E A   133
AN    134
ND    135
 TW   136
WIN   137
NK    138
KL    139
LED   140
D,    141
, A   142
AND   143
D     144
 HIS  145
S U   146
USU   147
UA    148
AL    149
LLY   150
Y P   151
PA    152
ALE   153
E F   154
FA    155
AC    156
CE    157
E W   158
WAS   159
S F   160
FL    161
LU    162
USH   163
HED   164
D A   165
AND   166
 AN   167
NIM   168
MAT   169
TED   170
D.    171
. T   172
THE   173
E FI  174
IR    175
RE    176
 BU   177
UR    178
RN    179
NE    180
ED    181
D B   182
BR    183
RI    184
IG    185
GH    186
HT    187
TL    188
LY    189
Y A   190
AND T  191
THE   192
 SO   193
OFT   194
T R   195
RAD   196
DIA   197
ANC   198
CE    199
 OF   200
F T   201
THE I  202
INC   203
CA    204
ANDE  205
ESC   206
CEN   207
NT    208
 L    209
LI    210
IGH   211
HTS   212
S I   213
IN    214
 TH   215
HE    216
 LI   217
ILI   218
IES   219
S O   220
OF    221
 SI   222
ILV   223
VER   224
R C   225
CAU   226
UG    227
GHT   228
T TH  229
HE B  230
BU    231
UB    232
BB    233
BL    234
LES   235
S T   236
THA   237
AT    238
 FL   239
LA    240
ASH   241
HED   242
 AND  243
D P   244
PAS   245
SS    246
SE    247
ED    248
 IN   249
N     250
 OU   251
UR    252
 G    253
GL    254
LAS   255
SSE   256
ES.   257

Process finished with exit code 0

"""
