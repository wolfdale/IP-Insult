# ###############################
# IP Insult Version 0.0.2
# Author - Prakhar (Wolfdale)
# For IPv4 Only
# ###############################

import urllib

insults = [
    'artless', 'base-court', 'apple-john',
    'bawdy', 'bat-fowling', 'baggage',
    'beslubbering', 'beef-witted', 'barnacle',
    'bootless', 'beetle-headed', 'bladder',
    'churlish', 'boil-brained', 'boar-pig',
    'cockered', 'clapper-clawed', 'bugbear',
    'clouted', 'clay-brained', 'bum-bailey',
    'craven', 'common-kissing', 'canker-blossom',
    'currish', 'crook-pated', 'clack-dish',
    'dankish', 'dismal-dreaming', 'clotpole',
    'dissembling', 'dizzy-eyed', 'coxcomb',
    'droning', 'doghearted', 'codpiece',
    'errant', 'dread-bolted', 'death-token',
    'fawning', 'earth-vexing', 'dewberry',
    'fobbing', 'elf-skinned', 'flap-dragon',
    'froward', 'fat-kidneyed', 'flax-wench',
    'frothy', 'fen-sucked', 'flirt-gill',
    'gleeking', 'flap-mouthed', 'foot-licker',
    'goatish', 'fly-bitten', 'fustilarian',
    'gorbellied', 'folly-fallen', 'giglet',
    'impertinent', 'fool-born', 'gudgeon',
    'infectious', 'full-gorged', 'haggard',
    'jarring', 'guts-griping', 'harpy',
    'loggerheaded', 'half-faced', 'hedge-pig',
    'lumpish', 'hasty-witted', 'horn-beast',
    'mammering', 'hedge-born', 'hugger-mugger',
    'mangled', 'hell-hated', 'joithead',
    'mewling', 'idle-headed', 'lewdster',
    'paunchy', 'ill-breeding', 'lout',
    'pribbling', 'ill-nurtured', 'maggot-pie',
    'puking', 'knotty-pated', 'malt-worm',
    'puny', 'milk-livered', 'mammet',
    'qualling', 'motley-minde', 'measle',
    'rank', 'onion-eyed', 'minnow',
    'reeky', 'plume-plucked', 'miscreant',
    'roguish', 'pottle-deep', 'moldwarp',
    'ruttish', 'pox-marked', 'mumble-news',
    'saucy', 'reeling-ripe', 'nut-hook',
    'spleeny', 'rough-hewn', 'pigeon-egg',
    'spongy', 'rude-growing', 'pignut',
    'surly', 'rump-fed', 'puttock',
    'tottering', 'shard-borne', 'pumpion',
    'unmuzzled', 'sheep-biting', 'ratsbane',
    'vain', 'spur-galled', 'scut',
    'venomed', 'swag-bellied', 'skainsmate',
    'villainous', 'tardy-gaited', 'strumpet',
    'warped', 'tickle-brained', 'varlot',
    'wayward', 'toad-spotted', 'vassal',
    'weedy', 'unchin-snouted', 'whey-face',
    'yeasty', 'weather-bitten', 'wagtail',
    'cullionly', 'whoreson', 'knave',
    'fusty', 'malmsey-nosed', 'blind-worm',
    'caluminous', 'rampallian', 'popinjay',
    'wimpled', 'lily-livered', 'scullian',
    'burly-boned', 'scurvy-valiant', 'jolt-head',
    'misbegotten', 'brazen-faced', 'malcontent',
    'odiferous', 'unwashed', 'devil-monk',
    'poisonous', 'bunch-backed', 'toad',
    'fishified', 'leaden-footed', 'rascal',
    'Wart-necked', 'muddy-mettled', 'Basket-Cockle'
]

QUAD_LEN = 255
OFFSET = len(insults) / 4


def normalize(quad):
    return int((int(quad) * (OFFSET-1) / QUAD_LEN))


def main():
    myip = urllib.urlopen('http://icanhazip.com/').read().strip()
    print myip    
    print display(*map(normalize, myip.split('.')))
    while True:
        print "Try Random IP ? (y or n)"
        if(raw_input().lower()=="y"):
            import random
	    NOS = random.sample(xrange(0,256),4) 
	    myip = '.'.join(str(x) for x in NOS)
            print myip
	    print display(*map(normalize, myip.split('.')))
	else:break
    return


def display(s, t, u, v):
    return 'Thou {0} {1} {2} {3}!'.format(
        insults[s], insults[t + OFFSET],
        insults[u + 2*OFFSET], insults[v + 3*OFFSET]
    )


if __name__ == "__main__":
    main()
