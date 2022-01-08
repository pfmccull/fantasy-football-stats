source_columns = {
    'cbs': {
        'player': 'player',
        'team': 'team', 
        'pos': 'pos',
        'week': 'week',
        'gp' : 'gp',
        'Passing_yds': 'pass_yd',
        'Passing_td': 'pass_td',
        'Passing_int': 'int',
        'Rushing_yds': 'rush_yd',
        'Rushing_td': 'rush_td',
        'Receiving_rec': 'rec', 
        'Receiving_yds': 'rec_yd',
        'Receiving_td': 'rec_td',
        'Misc_fl': 'fum',
        'FG_1-19': 'fg_1to19',
        'FG_1-19a': 'fg_1to19a',
        'FG_20-29': 'fg_20to29',
        'FG_20-29a': 'fg_20to29a',
        'FG_30-39': 'fg_30to39',
        'FG_30-39a': 'fg_30to39a',
        'FG_40-49': 'fg_40to49',
        'FG_40-49a': 'fg_40to49a',
        'FG_50+': 'fg_50plus',
        'FG_50+a': 'fg_50plusa',
        'XP_xpm': 'xp_made',
        'XP_xpa': 'xpa',
        'int': 'def_int',
        'sfty': 'def_safety',
        'sck': 'def_sack',
        'frec': 'def_fum',
        'dtd': 'def_td',
        'pts': 'def_pt_allowed',
        'Yards Allowed_total': 'def_yd_allowed'},
    'nfl':{
        'player': 'player',
        'team': 'team',
        'pos': 'pos',
        'week': 'week',
        'gp': 'gp',
        'Passing_Yds': 'pass_yd',
        'Passing_TD': 'pass_td',
        'Passing_Int': 'int',
        'Rushing_Yds': 'rush_yd',
        'Rushing_TD': 'rush_td',
        'Receiving_Rec': 'rec',
        'Receiving_Yds': 'rec_yd',
        'Receiving_TD': 'rec_td',
        'Fum_Lost': 'fum',
        'Ret_TD': 'ret_td',
        'Misc_2PT': '2pt',
        'PAT_Made': 'xp_made',
        'FG Made_0-19': 'fg_0to19',
        'FG Made_20-29': 'fg_20to29',
        'FG Made_30-39': 'fg_30to39',
        'FG Made_40-49': 'fg_40to49',
        'FG Made_50+': 'fg_50plus',
        'Tackles_Sack': 'def_sack',
        'Turnover_Int': 'def_int',
        'Turnover_Fum Rec': 'def_fum',
        'Score_Saf': 'def_safety',
        'Score_TD': 'def_td', 
        'def_ret_td': 'def_ret_td',
        'Score_Def 2pt Ret': 'xxxxx', 
        'Points_Pts Allow': 'def_pt_allowed'},
    'espn': {
        '3': 'pass_yd',
        '4': 'pass_td', 
        '19': '2pt_pass',
        '20': 'int',
        '24': 'rush_yd',
        '25': 'rush_td',
        '26': '2pt_rush',
        '42': 'rec_yd',
        '43': 'rec_td',
        '44': '2pt_rec',
        '53': 'rec',
        '72': 'fum',
        '80': 'fg_0to39',
        '77': 'fg_40to49',
        '74': 'fg_50plus', 
        '85': 'fg_miss',
        '86': 'xp_made',
        '88': 'xp_miss', 
        '93': 'def_blocked_kick_td',
        '95': 'def_int',
        '96': 'def_fum',
        '98': 'def_safety',
        '99': 'def_sack',
        '101': 'kick_return_td',
        '102': 'punt_return_td',
        '103': 'def_int_td',
        '104': 'def_fumble_td', 
        '120': 'def_pt_allowed',
        '89': '0_pt_allowed',
        '90': '1to6_pt_allowed',
        '91': '7to13_pt_allowed',
        '92': '14to17_pt_allowed',
        '121': '18to21_pt_allowed',
        '122': '22to27_pt_allowed',
        '123': '28to34_pt_allowed',
        '124': '35to45_pt_allowed',
        '125': '46plus_pt_allowed',
        '127': 'def_yd_allowed',
        '128': 'less_than_100_yd_allowed',
        '129': '100to199_yd_allowed',
        '130': '200to299_yd_allowed',
        '131': '300to349_yd_allowed',
        '132': '350to399_yd_allowed',
        '133': '400to449_yd_allowed',
        '134': '450to499_yd_allowed',
        '135': '500to549_yd_allowed',
        '136': '550plus_yd_allowed',
         }, 
    'number_fire': {
        'Passing Yds': 'pass_yd',
        'Passing TDs': 'pass_td',
        'Passing INTs': 'int',
        'Rushing Yds': 'rush_yd',
        'Rushing TDs': 'rush_td',
        'Receiving Rec': 'rec',
        'Receiving Yds': 'rec_yd',
        'Receiving TDs': 'rec_td',
        'Kicking XPM': 'xp_made',
        'Kicking FGM': 'fgm',
        'Kicking FGA': 'fga',
        'FG Made By Distance 0-19': 'fg_0to19',
        'FG Made By Distance 20-29': 'fg_20to29',
        'FG Made By Distance 30-39': 'fg_30to39',
        'FG Made By Distance 40-49': 'fg_40to49',
        'FG Made By Distance 50+': 'fg_50plus',
        'Defense Points Allowed': 'def_pt_allowed',
        'Defense Yards Allowed': 'def_yd_allowed',
        'Defense Sacks': 'def_sack',
        'Defense INTs': 'def_int',
        'Defense Fumbles': 'def_fum',
        'Defense TDs': 'def_td'
        },
    'fantasy_sharks': 
        {'default':{
            'Player': 'player',
            'Tm': 'team',
            'pos': 'pos',
            'week': 'week',
            'Pass Yds': 'pass_yd',
            'Pass TDs': 'pass_td',
            'Int': 'int',
            'Rsh Yds':'rush_yd',
            'Rsh TDs': 'rush_td',
            'Rec': 'rec',
            'Rec Yds': 'rec_yd',
            'Rec TDs': 'rec_td',
            'Fum': 'fum',
            'XPM': 'xp_made',
            'XPA': 'xpa',
            '10-19 FGM': 'fg_10to19',
            '20-29 FGM': 'fg_20to29',
            '30-39 FGM': 'fg_30to39',
            '40-49 FGM': 'fg_40to49',
            '50+ FGM': 'fg_50plus',
            'Miss': 'fg_miss'},
        'dst': {
            'Player': 'player',
            'Tm': 'team',
            'pos': 'pos',
            'week': 'week',
            'Scks': 'def_sack',
            'Int': 'def_int',
            'Fum': 'def_fum',
            'DefTD': 'def_td',
            'Safts': 'def_safety',
            'Yds Allowed': 'def_yd_allowed',
            '100-199': '100to199_yd_allowed',
            '200-299': '200to299_yd_allowed',
            '300-349': '300to349_yd_allowed',
            '350-399': '350to399_yd_allowed',
            '400-449': '400to449_yd_allowed',
            '450-499': '450to499_yd_allowed',
            '500-549': '500to549_yd_allowed',
            '550+': '550plus_yd_allowed',
            'Pts Agn': 'def_pt_allowed',
            '1-6': '1to6_pt_allowed',
            '7-13': '7to13_pt_allowed',
            '14-17': '14to17_pt_allowed',
            '18-20': '18to21_pt_allowed',
            '21-27': '22to27_pt_allowed',
            '28-34': '28to34_pt_allowed',
            '34-45': '35to45_pt_allowed'
            }
        },
    'fleaflicker': {
        'Player Name': 'player',
        'pos': 'pos',
        'team': 'team',
        'week': 'week',
        'Passing Yd': 'pass_yd',
        'Passing TD': 'pass_td',
        'Passing INT': 'int',
        'Rushing Yd': 'rush_yd',
        'Rushing TD': 'rush_td',
        'Receiving Rec': 'rec',
        'Receiving Yd': 'rec_yd',
        'Receiving TD': 'rec_td',
        'Misc Fum': 'fum',
        'Kicking FG': 'fg_40to49',
        'Kicking Att': 'fga',
        'Kicking XP': 'xp_made',
        'Defense INT': 'def_int',
        'Defense Sack': 'def_sack',
        'Defense FR': 'def_fum',
        'Defense TD': 'def_td',
        'Team Defense Pts': 'def_pt_allowed',
        'Team Defense Yd': 'def_yd_allowed'},
    'FFToday': {
        'player': 'player',
        'Team': 'team',
        'pos': 'pos',
        'week': 'week',
        'Passing Yard': 'pass_yd',
        'Passing TD': 'pass_td',
        'Passing INT': 'int',
        'Rushing Yard': 'rush_yd',
        'Rushing TD': 'rush_td',
        'Receiving Rec': 'rec',
        'Receiving Yard': 'rec_yd',
        'Receiving TD': 'rec_td',
        'FG Made': 'fg_40to49',
        'FG Miss': 'fg_miss',
        'XP Made': 'xp_made',
        'XP Miss': 'xp_miss'
        },
    'FantasyPros': {
        'Player': 'player',
        'team': 'team',
        'pos': 'pos', 
        'week': 'week',
        'pos': 'pos',
        'PASSING YDS': 'pass_yd',
        'PASSING TDS': 'pass_td',
        'PASSING INTS': 'int',
        'RUSHING YDS': 'rush_yd',
        'RUSHING TDS': 'rush_td',
        'MISC FL': 'fum',
        'RECEIVING REC': 'rec',
        'RECEIVING YDS': 'rec_yd',
        'RECEIVING TDS': 'rec_td',
        'FG': 'fg_40to49',
        'FGA': 'fga',
        'XPT': 'xp_made',
        'SACK': 'def_sack',
        'INT': 'def_int',
        'FR': 'def_fum',
        'TD': 'def_td',
        'SAFETY': 'def_safety',
        'PA': 'def_pt_allowed',
        'YDS AGN': 'def_yd_allowed'
        },
    'all': {
        'categorical': [
            'player_id',
            'player',
            'team',
            'pos',
            'week',
            'opp',
            'byeWeek',
            'source'],
        'numeric': [
            'gp',
            'pass_yd',
            'pass_td',
            'int',
            'rush_yd',
            'rush_td',
            'rec',
            'rec_yd',
            'rec_td',
            'fum',
            '2pt',
            'ret_td',
            'fg_0to39',
            'fg_40to49',
            'fg_50plus',
            'fg_miss',
            'xp_made',
            'xp_miss',
            'def_sack',
            'def_int',
            'def_fum',
            'def_td',
            'def_safety',
            'def_pt_allowed',
            'def_yd_allowed',
            '0_pt_allowed',
            '1to6_pt_allowed',
            '7to13_pt_allowed',
            '14to17_pt_allowed',
            '18to21_pt_allowed',
            '22to27_pt_allowed',
            '28to34_pt_allowed',
            '35to45_pt_allowed',
            '46plus_pt_allowed',
            'less_than_100_yd_allowed',
            '100to199_yd_allowed',
            '200to299_yd_allowed',
            '300to349_yd_allowed',
            '350to399_yd_allowed',
            '400to449_yd_allowed',
            '450to499_yd_allowed',
            '500to549_yd_allowed',
            '550plus_yd_allowed']}
    }
 
    
team_ids = {
    'espn': {
        0: 'FA',
        1: 'ATL',
        2: 'BUF',
        3: 'CHI',
        4: 'CIN',
        5: 'CLE',
        6: 'DAL',
        7: 'DEN',
        8: 'DET',
        9: 'GB',
        10: 'TEN',
        11: 'IND',
        12: 'KC',
        13: 'LV',
        14: 'LAR',
        15: 'MIA',
        16: 'MIN',
        17: 'NE',
        18: 'NO',
        19: 'NYG',
        20: 'NYJ',
        21: 'PHI', 
        22: 'ARI',
        23: 'PIT',
        24: 'LAC',
        25: 'SF',
        26: 'SEA',
        27: 'TB',
        28: 'WSH',
        29: 'CAR', 
        30: 'JAX',
        33: 'BAL',
        34: 'HOU'}
    }
    
source_position_ids = {
    'nfl': {
        'qb': '1',
        'rb': '2',
        'wr': '3',
        'te': '4',
        'k': '7',
        'dst': '8',
        'off': 'O'},
    'espn': {
        1: 'QB',
        2: 'RB',
        3: 'WR',
        4: 'TE',
        5: 'K',
        16: 'DST'},
    'fantasy_sharks': {
        'qb': '1',
        'rb': '2',
        'wr': '4',
        'te': '5',
        'k': '7',
        'dst': '6'},
    'fleaflicker': {
        'qb': '4',
        'rb': '1',
        'wr': '2',
        'te': '8',
        'k': '16',
        'dst': '256'
        },
    'FFToday': {
        'qb': '10',
        'rb': '20',
        'wr': '30',
        'te': '40',
        'k': '80'}
    }

source_urls = {'cbs': 'https://www.cbssports.com/fantasy/football/stats/{}/{}/{}/projections/nonppr/',
             'nfl': 'https://fantasy.nfl.com/research/projections?statCategory=projectedStats&statSeason={}&statType=weekProjectedStats&position={}&count=1000&statWeek={}',
             'number_fire':{
                 'Rest of Season': 'https://www.numberfire.com/nfl/fantasy/remaining-projections/{}',
                 'current week': 'https://www.numberfire.com/nfl/fantasy/fantasy-football-projections/{}'},
             'fantasy_sharks': 'https://www.fantasysharks.com/apps/bert/forecasts/projections.php?League=-1&Position={}&scoring=1&Segment={}&uid=4',
             'fleaflicker': 'https://www.fleaflicker.com/nfl/leaders?position={}&sortMode=7',
             'FFToday': 'https://fftoday.com/rankings/playerwkproj.php?Season={}&GameWeek={}&PosID={}',
             'FantasyPros': 'https://www.fantasypros.com/nfl/projections/{}.php'}
