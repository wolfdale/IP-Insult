################################
# IP Insult Version 0.0.1 
# Author - Prakhar (Wolfdale)
# For IPv4 Only
################################

def main():
        import re
        import urllib
        web=urllib.urlopen('http://ip-lookup.net/')  #Getting IP Adress 
        content=web.read()
        m = re.search('(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)',
                content)    # RegEx for Ip Adress Lookup in Web page          
        myip = m.group(0)
        #print myip         [BreakPoint 1]
        if len(myip)<15:
                myip=parse_ip(myip)
        #print 'Ready To Go !' [BreakPoint 2]
        print myip
        #raw_input()   [BreakPoint 3]
        setip(myip)
#Parsing Ip Adress (Full Representation)
def parse_ip(ip):                                          
        p1,p2,p3,p4=ip.split('.')      
        def check(p):                                    # Avoiding For Loop; All hail If condition !
                if len(p)<3:                                  
                        if len(p)<2:
                                p='0'+p
                        p='0'+p
                return p
        #Checking Each quad of Ip Address        
        p1=check(p1) 
        p2=check(p2)
        p3=check(p3)
        p4=check(p4)
        #print p1,p2,p3,p4   [BreakPoint 4]
        str='.'
        seq=[p1,p2,p3,p4]
        return (str.join(seq))
                       
def setip( ip ):
	# Min-Max Normalization to map high range to low range 
	q1=int((str(ip[0])) + (str(ip[1])) + (str(ip[2])) )
	q2=int((str(ip[4])) + (str(ip[5])) + (str(ip[6])))
	q3=int((str(ip[8])) + (str(ip[9])) + (str(ip[10])) )
	q4=int((str(ip[12])) + (str(ip[13])) + (str(ip[14])) )
	#print q1,q2,q3,q4 [BreakPoint 5]
        s=int((((q1-0)/255.0)*44))
	t=int((((q2-0)/255.0)*44))
	u=int((((q3-0)/255.0)*44))
	v=int((((q4-0)/255.0)*44))
	#print s,t,u,v [BreakPoint 6]
	#raw_input()   [BreakPoint 5]
	display(s,t,u,v)

def display (s,t,u,v):
	col1=['artless'   ,          'base-court',          'apple-john'
        ,'bawdy'            ,   'bat-fowling'      ,   'baggage'
        ,'beslubbering'      ,  'beef-witted'       ,  'barnacle'
        ,'bootless'   ,         'beetle-headed'      , 'bladder'
        ,'churlish'    ,        'boil-brained'        ,'boar-pig'
        ,'cockered'     ,      'clapper-clawed',      'bugbear'
        ,'clouted'       ,      'clay-brained'  ,      'bum-bailey'
        ,'craven'         ,     'common-kissing' ,     'canker-blossom'
        ,'currish'         ,    'crook-pated'     ,    'clack-dish'
        ,'dankish'          ,   'dismal-dreaming'  ,   'clotpole'
        ,'dissembling'       ,  'dizzy-eyed'        ,  'coxcomb'
        ,'droning'            , 'doghearted'         , 'codpiece'
        ,'errant'              ,'dread-bolted'   ,     'death-token'
        ,'fawning'  ,           'earth-vexing'    ,    'dewberry'
        ,'fobbing'   ,          'elf-skinned'      ,   'flap-dragon'];

        col2=['froward',             'fat-kidneyed',        'flax-wench'
        ,'frothy'        ,      'fen-sucked' ,         'flirt-gill'
        ,'gleeking'       ,     'flap-mouthed',        'foot-licker'
        ,'goatish'         ,    'fly-bitten'   ,       'fustilarian'
        ,'gorbellied'    ,      'folly-fallen'  ,      'giglet'
        ,'impertinent' ,        'fool-born'      ,     'gudgeon'
        ,'infectious'   ,       'full-gorged'     ,    'haggard'
        ,'jarring'       ,      'guts-griping'     ,   'harpy'
        ,'loggerheaded'   ,     'half-faced'        ,  'hedge-pig'
        ,'lumpish'         ,    'hasty-witted'       , 'horn-beast'
        ,'mammering'        ,   'hedge-born'          ,'hugger-mugger'
        ,'mangled'           ,  'hell-hated' ,         'joithead'
        ,'mewling'            , 'idle-headed' ,        'lewdster'
        ,'paunchy'   ,          'ill-breeding' ,       'lout'
        ,'pribbling'  ,         'ill-nurtured'  ,      'maggot-pie'];

        col3=['puking',         'knotty-pated',        'malt-worm'
        ,'puny'    ,            'milk-livered' ,       'mammet'
        ,'qualling' ,           'motley-minde'  ,      'measle'
        ,'rank'      ,          'onion-eyed'     ,     'minnow'
        ,'reeky'      ,         'plume-plucked'   ,    'miscreant'
        ,'roguish'     ,        'pottle-deep'      ,   'moldwarp'
        ,'ruttish'      ,       'pox-marked'        ,  'mumble-news'
        ,'saucy'         ,      'reeling-ripe'       , 'nut-hook'
        ,'spleeny'        ,     'rough-hewn'  ,        'pigeon-egg'
        ,'spongy'          ,    'rude-growing' ,       'pignut'
        ,'surly'            ,   'rump-fed'      ,      'puttock'
        ,'tottering' ,          'shard-borne'    ,     'pumpion'
        ,'unmuzzled'  ,         'sheep-biting'    ,    'ratsbane'
        ,'vain'        ,        'spur-galled'      ,   'scut'
        ,'venomed'      ,       'swag-bellied'      ,  'skainsmate'];

        col4=['villainous',    'tardy-gaited' ,       'strumpet'
        ,'warped' ,             'tickle-brained',      'varlot'
        ,'wayward' ,            'toad-spotted'    ,    'vassal'
        ,'weedy'    ,           'unchin-snouted' ,     'whey-face'
        ,'yeasty'    ,          'weather-bitten',      'wagtail'
        ,'cullionly'  ,         'whoreson'       ,     'knave'
        ,'fusty'       ,        'malmsey-nosed'   ,    'blind-worm'
        ,'caluminous'   ,       'rampallian'        ,  'popinjay'
        ,'wimpled'        ,     'lily-livered'     ,   'scullian'
        ,'burly-boned'   ,      'scurvy-valiant',      'jolt-head'
        ,'misbegotten' ,        'brazen-faced'   ,     'malcontent'
        ,'odiferous'    ,       'unwashed'        ,    'devil-monk'
        ,'poisonous'     ,      'bunch-backed'     ,   'toad'
        ,'fishified'      ,     'leaden-footed'     ,  'rascal'
        ,'Wart-necked'     ,    'muddy-mettled'      , 'Basket-Cockle'];
        print ('Thou'+ ' ' + col1[s] + ' ' + col2[t] +' '+ col3[u] +' '+ col4[v] + ' ' + '!' )
        raw_input() 

if __name__ == "__main__":
	main()
		
