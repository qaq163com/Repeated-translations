# -*- coding:utf-8 -*-
import os
try:
    from pygoogletranslation import Translator
except:
    os.system('pip3 install pygoogletranslation')
    from pygoogletranslation import Translator
import random
try:
    from retry import retry
except:
    os.system('pip3 install retry')
    from retry import retry
translator = Translator()
i = 0
text = u'''掉落物
苦力怕被杀死时掉落：

0–2个火药（每级抢夺魔咒可使最大掉落量增加1，抢夺III时为最多5）
1个除Pigstep和otherside外的随机音乐唱片，当被骷髅、流浪者或凋灵骷髅[仅Java版]杀死时
1个苦力怕的头，当被闪电苦力怕杀死时
5，当被玩家或驯服的狼杀死时
行为

一只追赶玩家并准备爆炸的苦力怕。

苦力怕会追赶它发现的半径16格（±5%），垂直±4格以内的玩家。在Java版中，当玩家佩戴苦力怕的头时，苦力怕的探测范围减少到正常范围的一半（8格）。

如果玩家有隐身效果且没有穿戴任何盔甲，苦力怕不会靠近玩家。

当苦力怕距离玩家3格以内时，苦力怕将会停止移动并发出较大的嘶嘶声，身体膨胀并开始闪烁，1.5秒后就会爆炸。在玩家离开7格的爆炸半径（包括击退苦力怕或杀死苦力怕）时就能停止苦力怕的爆炸。

苦力怕会尝试在不受到致命跌落伤害时从高处跳下来袭击玩家。整个掉落过程持续1.5秒（包含掉落的时间），因此在高处跳下来着陆后不久就会发生爆炸。

类似于其他生物，苦力怕能够爬上梯子和藤蔓，但不会故意这样做。

苦力怕可用打火石引爆，但是不能用火焰弹引爆。

当苦力怕与猫或豹猫距离6格或更近，且其未开始爆炸，苦力怕会沿直线逃离直到16格以外才会停止，不论是否会因此进入另一只猫或豹猫的6格范围内。除非玩家离开爆炸半径，否则已经开始爆炸的苦力怕不会逃跑。

苦力怕的爆炸威力为3。

在Java版中，如果苦力怕带有某种药水效果，其爆炸后会在原地创造一个该效果的药水云。

一些会对特定生物发起进攻的生物不会主动攻击苦力怕，包括驯服的狼、铁傀儡和僵尸疣猪兽。但是，雪傀儡[2]、名为“Johnny”的卫道士、凋灵以及有队伍且与该苦力怕不在同一队伍的潜影贝仍会攻击苦力怕；山羊也会随机冲撞攻击苦力怕，但苦力怕不会因此而试图爆炸。其他的任何生物皆不会主动攻击苦力怕。

如果苦力怕被其他生物攻击，苦力怕会靠近攻击它的生物并爆炸。'''
@retry()
def gt():
    global text
    la_random = random.sample(la[('sl' or 'tl')].keys(), 1)
    text = translator.translate(text, dest=la_random[0])
la = {'sl': {'auto': 'Detect language', 'af': 'Afrikaans', 'sq': 'Albanian', 'am': 'Amharic', 'ar': 'Arabic', 'hy': 'Armenian', 'az': 'Azerbaijani', 'eu': 'Basque', 'be': 'Belarusian', 'bn': 'Bengali', 'bs': 'Bosnian', 'bg': 'Bulgarian', 'ca': 'Catalan', 'ceb': 'Cebuano', 'ny': 'Chichewa', 'zh-CN': 'Chinese', 'co': 'Corsican', 'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch', 'en': 'English', 'eo': 'Esperanto', 'et': 'Estonian', 'tl': 'Filipino', 'fi': 'Finnish', 'fr': 'French', 'fy': 'Frisian', 'gl': 'Galician', 'ka': 'Georgian', 'de': 'German', 'el': 'Greek', 'gu': 'Gujarati', 'ht': 'Haitian Creole', 'ha': 'Hausa', 'haw': 'Hawaiian', 'iw': 'Hebrew', 'hi': 'Hindi', 'hmn': 'Hmong', 'hu': 'Hungarian', 'is': 'Icelandic', 'ig': 'Igbo', 'id': 'Indonesian', 'ga': 'Irish', 'it': 'Italian', 'ja': 'Japanese', 'jw': 'Javanese', 'kn': 'Kannada', 'kk': 'Kazakh', 'km': 'Khmer', 'rw': 'Kinyarwanda', 'ko': 'Korean', 'ku': 'Kurdish (Kurmanji)', 'ky': 'Kyrgyz', 'lo': 'Lao', 'la': 'Latin', 'lv': 'Latvian', 'lt': 'Lithuanian', 'lb': 'Luxembourgish', 'mk': 'Macedonian', 'mg': 'Malagasy', 'ms': 'Malay', 'ml': 'Malayalam', 'mt': 'Maltese', 'mi': 'Maori', 'mr': 'Marathi', 'mn': 'Mongolian', 'my': 'Myanmar (Burmese)', 'ne': 'Nepali', 'no': 'Norwegian', 'or': 'Odia (Oriya)', 'ps': 'Pashto', 'fa': 'Persian', 'pl': 'Polish', 'pt': 'Portuguese', 'pa': 'Punjabi', 'ro': 'Romanian', 'ru': 'Russian', 'sm': 'Samoan', 'gd': 'Scots Gaelic', 'sr': 'Serbian', 'st': 'Sesotho', 'sn': 'Shona', 'sd': 'Sindhi', 'si': 'Sinhala', 'sk': 'Slovak', 'sl': 'Slovenian', 'so': 'Somali', 'es': 'Spanish', 'su': 'Sundanese', 'sw': 'Swahili', 'sv': 'Swedish', 'tg': 'Tajik', 'ta': 'Tamil', 'tt': 'Tatar', 'te': 'Telugu', 'th': 'Thai', 'tr': 'Turkish', 'tk': 'Turkmen', 'uk': 'Ukrainian', 'ur': 'Urdu', 'ug': 'Uyghur', 'uz': 'Uzbek', 'vi': 'Vietnamese', 'cy': 'Welsh', 'xh': 'Xhosa', 'yi': 'Yiddish', 'yo': 'Yoruba', 'zu': 'Zulu'}, 'tl': {'af': 'Afrikaans', 'sq': 'Albanian', 'am': 'Amharic', 'ar': 'Arabic', 'hy': 'Armenian', 'az': 'Azerbaijani', 'eu': 'Basque', 'be': 'Belarusian', 'bn': 'Bengali', 'bs': 'Bosnian', 'bg': 'Bulgarian', 'ca': 'Catalan', 'ceb': 'Cebuano', 'ny': 'Chichewa', 'zh-CN': 'Chinese (Simplified)', 'zh-TW': 'Chinese (Traditional)', 'co': 'Corsican', 'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch', 'en': 'English', 'eo': 'Esperanto', 'et': 'Estonian', 'tl': 'Filipino', 'fi': 'Finnish', 'fr': 'French', 'fy': 'Frisian', 'gl': 'Galician', 'ka': 'Georgian', 'de': 'German', 'el': 'Greek', 'gu': 'Gujarati', 'ht': 'Haitian Creole', 'ha': 'Hausa', 'haw': 'Hawaiian', 'iw': 'Hebrew', 'hi': 'Hindi', 'hmn': 'Hmong', 'hu': 'Hungarian', 'is': 'Icelandic', 'ig': 'Igbo', 'id': 'Indonesian', 'ga': 'Irish', 'it': 'Italian', 'ja': 'Japanese', 'jw': 'Javanese', 'kn': 'Kannada', 'kk': 'Kazakh', 'km': 'Khmer', 'rw': 'Kinyarwanda', 'ko': 'Korean', 'ku': 'Kurdish (Kurmanji)', 'ky': 'Kyrgyz', 'lo': 'Lao', 'la': 'Latin', 'lv': 'Latvian', 'lt': 'Lithuanian', 'lb': 'Luxembourgish', 'mk': 'Macedonian', 'mg': 'Malagasy', 'ms': 'Malay', 'ml': 'Malayalam', 'mt': 'Maltese', 'mi': 'Maori', 'mr': 'Marathi', 'mn': 'Mongolian', 'my': 'Myanmar (Burmese)', 'ne': 'Nepali', 'no': 'Norwegian', 'or': 'Odia (Oriya)', 'ps': 'Pashto', 'fa': 'Persian', 'pl': 'Polish', 'pt': 'Portuguese', 'pa': 'Punjabi', 'ro': 'Romanian', 'ru': 'Russian', 'sm': 'Samoan', 'gd': 'Scots Gaelic', 'sr': 'Serbian', 'st': 'Sesotho', 'sn': 'Shona', 'sd': 'Sindhi', 'si': 'Sinhala', 'sk': 'Slovak', 'sl': 'Slovenian', 'so': 'Somali', 'es': 'Spanish', 'su': 'Sundanese', 'sw': 'Swahili', 'sv': 'Swedish', 'tg': 'Tajik', 'ta': 'Tamil', 'tt': 'Tatar', 'te': 'Telugu', 'th': 'Thai', 'tr': 'Turkish', 'tk': 'Turkmen', 'uk': 'Ukrainian', 'ur': 'Urdu', 'ug': 'Uyghur', 'uz': 'Uzbek', 'vi': 'Vietnamese', 'cy': 'Welsh', 'xh': 'Xhosa', 'yi': 'Yiddish', 'yo': 'Yoruba', 'zu': 'Zulu'}}
while True:
    gt()
    text = str(text)
    text_2 = text
    text_part = text.find('text=')
    text_part2 = text.find(', pronunciation=')
    text = text[text_part+5:text_part2]
    Zh = translator.translate(text, dest='zh-CN')
    Zh = str(Zh)
    text_part3 = Zh.find('text=')
    text_part4 = Zh.find(', pronunciation=')
    print(text + ' --> ' + '{}'.format(Zh[text_part3+5:text_part4]))
    i += 1