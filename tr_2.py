import random

list_letter = ['e ', ' t', 'he', 'th', ' a', 'd ', 't ', 'er', 's ', 'in', ' h', ' th', ', ', ' w', ' s', 'an',
               'r ', 'n ', 'y ', 're', 'the', 'he ', ' o', 'ha', 'o ', 'ou', 'en', 'on', ' i', 'nd', 'at', 'ed',
               ' m', ' b', 'is', 'ng', 'it', 'er ', 'te', 'hi', ' an', 'f ', 've', 'her', 'ar', ' c', 'nd ', 'ed ',
               ' f', 'of', 'ing', 'ne', ' he', ' of', 'or', 'be', 'se', 'and', 'of ', 'le', 'es', 'h ', 'st', 'nt',
               ' d', 'no', 'as ', ' n', 'ti', 'me', 'll', 'ea', 'g ', 'ng ', 'li', ' be', ' in', 'at ', ' p', 'co',
               ' ha', 'al', 'wa', 'ot', 'el', 'sh', 'et', ' e', 'ur', 'ho', 'de', 'ce', 'is ', ' no', 're ', ' co',
               ' l', 'l ', ' r', 'ly', ' wa', 'wi', 'om', 'fo', ' hi', ', a', ' I', 'io', 'si', 'wh', 'hat',
               'in ', 'ch', 'a ', 'd t', ' wh', 'ri', 'on ', ' wi', ' sh', 'e t', 'for', 'ly ', ' a ', 'di',
               'ee', 'rs', 'was', 'ut', 'ss', 'tha', 'ow', 'ent', ' re', 'ro', 'ion', 'ma', 'so', 'not',
               'you', 'ul', ' yo', ' I ', ' ', 'il', 'ver', 'e w', 'e,', 'we', 'us', ' M', 'ere', 'nc',
               'his', ' g', 'ter', 'en ', 'pe', 'e, ', 'th ', 'll ', ' fo', 'n t', 'e a', 'she', 'ab',
               '; ', 'ta', 'e h', 'ot ', 't t', 'gh', 'or ', 'ie', 'su', 'ir', 'ic', 'ns', 've ',
               ' as', 'e o', 'tio', 'st ', 'un', 'ld ', 'e s', 'ev', 'ith', ' it', 'em', 'ut ',
               'all', ' so', 'ra', 'ch ', 'sa', 'our', 'am', ' ma', 'id', 'pr', 'ry', 'oo', 'ad ',
               'rt', 'mo', 'r.', 'ge', 'eve', 'wit', ' on', 'be ', 'mi', 'r. ', 'ay', 'nce', 'tt',
               's a', 'had', 'ou ', 'lo', 'Mr', 'it ', ' we', 'thi', 's t', 'os', 'ac', 'fe', ' Mr',
               't h', 'an ', 'd a', 'ei', ' al', 't a', 'e i', 'e c', ' su', 'ke', 'ave', 'ol',
               ', t', 'po', 'uc', 'w ', 'hou', ' B', ' at', 'nt ', 'bl', 'le ', 'd,', 'ess', 'r t',
               ' u', 'con', 'hav', 's,', 'wo', ' se', 'me ', 'ry ', 'd, ', '." ', 'pa', 't w', ' di',
               's, ', 'ati', 'e.', 'ht', 'ght', 't,', 'r, ', 't i', 'eth', ' de', 'ect', 'f t', 's.',
               'e m', 'pl', 'ers', 't, ', 'iv', 'n a', ' me', ' pr', 'ery', 'ig', 'ear', 'ug', 'vi', 'ni',
               ' v', 't o', 'hin', 'ugh', 's s', ' is', 'oth', 'res', 'ss ', ' ho', 'ce ', 'd n', 'bu',
               'tr', 'Mr.', 'ted', 's o', ' ca', 'nn', 'fa', 'ne ', 'fi', 'iz', 'ap', 'se ', 's. ', 'ty',
               't s', ' fr', 'ine', 'rea', 'tu', 'y a', 'e f', 'ome', 'e. ', 'wer', ' si', 'uch', 's w',
               'ur ', ' T', 'mu', 'mp', 'ow ', 'f h', '; a', 'one', 'n, ', 'd s', 'tl', 'pp', ' L', ' do',
               'com', 'een', ' my', ' H', 'ore', 'Th', 'e p', ' li', 'liz', 'Eli', 'iza', 'g t', ' El',
               ' mu', 'd i', ' fa', 'ste', 'om ', 'tho', 'n h', 'da', 'd w', 'zab', 'abe', 'are', 'if',
               'igh', 'ate', ' ev', 'ive', '. B', 'r s', 'lf', 'oug', 'ga', 'by ', 'ep', 'o t', ' by',
               'ay ', 'd o', 'ten', ' ne', 'end', 'rn', ' C', 'nne', ' le', 'bo', 'r h', 'my ', 'now',
               'n o', 'man', 'ny', 'ons', 'ak', 'op', 'red', 'e b', 'ure', ' k', 'rr', ' Th', 'h a', 'ist',
               'ff', 'ich', 'ard', 'anc', ' un', 'eas', ' W', 'so ', ' lo', 'rom', 'ed,', 't b', 'ir ', 'elf',
               's i', 't.', 'gi', 'lin', 'od', 'o b', 'per', '. T', ' en', 'nte', 'y o', 'te ', 'go', ' D',
               'who', ' ve', 'The', 'ov', 'bee', 'pro', ', h', 'au', 'cy', 'oun', 's n', ' S', 'y.', 'e n',
               'e e', 'e r', 'et ', 'd.', 'ous', 'gl', 'ned', ' mi', 'hem', 'ind', 'fro', 'app', 'ust',
               'ty ', 'arc', 'y h', 'sed', 'rie', 's h', 'e l', 'ort', 'kn', 'ove', 'nes', 'n w', ' go',
               'r o', 'r f', 'h t', 'eli', 'o s', ' da', 'wn', 'hei', 'rl', 'out', 'sin', ' am', 'sur']
count_attempt = 16
count_len = 10
score = 0
for i in range(0, count_attempt):
    s_question = ''.join([random.choice(list_letter) for _ in range(count_len)])

    if s_question[0] == " ":
        s_question = s_question.replace(' ', '')
    if s_question[-1] == " ":
        s_question = s_question.replace(' ', '')
    s_question = s_question.replace('  ', ' ')

    print("      ", s_question)
    s_ask = input("       введите даный текст:\n       ")
    if s_ask == s_question:
        print("   ok")
        count_attempt -= 1
        score += 1

        if count_attempt < 13:
            level = 1
        if count_attempt < 9:
            level = 2
        if count_attempt < 5:
            level = 3
    else:
        print("ERROR! try another")
print(f'score = {score}')
