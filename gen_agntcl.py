#!/usr/bin/env python3
"""Generate ZQX Language Specification v2.0 with 2000-word vocabulary."""

import string
from itertools import product

# ─── Tier 1: 36 single-character codes ───────────────────────────────────────
# Mappings are intentionally scrambled — no letter matches its English phonetic.

TIER1 = {
    'a': 'do', 'b': 'say', 'c': 'self/I', 'd': 'with', 'e': 'but',
    'f': 'this', 'g': 'what', 'h': 'have', 'i': 'make', 'j': 'know',
    'k': 'be', 'l': 'for', 'm': 'and', 'n': 'to', 'o': 'like',
    'p': 'go', 'q': 'if', 'r': 'all', 's': 'not', 't': 'of',
    'u': 'we', 'v': 'in', 'w': 'or', 'x': 'it', 'y': 'my',
    'z': 'you', '0': 'false', '1': 'true', '2': 'from', '3': 'at',
    '4': 'on', '5': 'by', '6': 'give', '7': 'get', '8': 'other',
    '9': 'each',
}

# Reverse lookup: English word -> tier-1 code
TIER1_REV = {v: k for k, v in TIER1.items()}

# ─── Excluded 2-char English words ───────────────────────────────────────────
EXCLUDED_2CHAR = {
    'ad', 'ah', 'am', 'an', 'as', 'at', 'aw', 'ax',
    'be', 'bo', 'by',
    'do',
    'ed', 'eh', 'em', 'en', 'er', 'ex',
    'go',
    'ha', 'he', 'hi', 'ho',
    'id', 'if', 'in', 'is', 'it',
    'la', 'lo',
    'ma', 'me', 'my',
    'no',
    'of', 'oh', 'ok', 'on', 'op', 'or', 'ow', 'ox',
    'pa', 'pi',
    're',
    'sh', 'so',
    'to',
    'uh', 'um', 'un', 'up', 'us',
    'we',
    'ye', 'yo',
}

# ─── Code generators ─────────────────────────────────────────────────────────

def gen_tier2_codes():
    """All available 2-char [a-z][a-z] codes, excluding English words."""
    codes = []
    for a in string.ascii_lowercase:
        for b in string.ascii_lowercase:
            code = a + b
            if code not in EXCLUDED_2CHAR:
                codes.append(code)
    return codes

CONSONANTS_20 = list('bcdfghjklmnpqrstvwxz')

def gen_tier3_codes():
    """3-char consonant-only codes (no vowels, no y). 20^3 = 8000 possible."""
    codes = []
    for a in CONSONANTS_20:
        for b in CONSONANTS_20:
            for c in CONSONANTS_20:
                codes.append(a + b + c)
    return codes

# ─── 2000 most common English words, by category ─────────────────────────────
# Words already in tier-1 are noted but not re-assigned.
# Sorted roughly by frequency within each category.

# We tag each word with a category for documentation.

def build_word_list():
    """Return list of (english_word, category) for all 2000 words."""
    words = []

    # ── Function Words ──
    function_words = [
        # Articles & determiners
        'the', 'a', 'an', 'some', 'any', 'every', 'another', 'both',
        'either', 'neither', 'enough', 'several', 'such', 'few', 'many',
        'much', 'more', 'most', 'less', 'least',
        # Pronouns
        'he', 'she', 'they', 'him', 'her', 'them', 'his', 'its',
        'our', 'their', 'who', 'whom', 'whose', 'which', 'that',
        'these', 'those', 'one', 'someone', 'anyone', 'everyone',
        'nobody', 'something', 'anything', 'everything', 'nothing', 'none',
        'somebody', 'anybody', 'everybody',
        'myself', 'yourself', 'himself', 'herself', 'itself',
        'ourselves', 'themselves',
        # Conjunctions
        'than', 'because', 'although', 'though', 'while', 'whereas',
        'unless', 'since', 'once', 'whether', 'whenever', 'wherever',
        'however', 'therefore', 'moreover', 'furthermore', 'nevertheless',
        'meanwhile', 'otherwise', 'instead', 'nor',
        # Prepositions
        'about', 'above', 'across', 'after', 'against', 'along', 'among',
        'around', 'before', 'behind', 'below', 'beneath', 'beside',
        'between', 'beyond', 'down', 'during', 'except', 'inside',
        'into', 'near', 'off', 'onto', 'out', 'outside', 'over',
        'past', 'through', 'throughout', 'toward', 'towards', 'under', 'up',
        'underneath', 'until', 'upon', 'within', 'without',
        # Auxiliaries
        'will', 'would', 'can', 'could', 'may', 'might', 'must',
        'shall', 'should', 'was', 'were', 'are', 'been', 'being',
        'had', 'has', 'does', 'did', 'having', 'doing',
        # Function adverbs & misc
        'there', 'here', 'then', 'now', 'when', 'where', 'how',
        'very', 'also', 'too', 'just', 'only', 'still', 'already',
        'always', 'never', 'often', 'sometimes', 'ever', 'again',
        'perhaps', 'maybe', 'quite', 'rather', 'almost', 'even',
        'indeed', 'certainly', 'probably', 'actually', 'really',
        'please', 'yes', 'so', 'yet', 'hence',
    ]
    for w in function_words:
        words.append((w, 'function'))

    # ── Verbs ──
    verbs = [
        'accept', 'achieve', 'act', 'add', 'admit', 'affect', 'afford',
        'agree', 'aim', 'allow', 'answer', 'appear', 'apply', 'approach',
        'argue', 'arrive', 'ask', 'assume', 'attack', 'attempt', 'avoid',
        'base', 'bear', 'beat', 'become', 'begin', 'believe', 'belong',
        'break', 'bring', 'build', 'burn', 'buy', 'call', 'care', 'carry',
        'catch', 'cause', 'change', 'charge', 'check', 'choose', 'claim',
        'clean', 'clear', 'climb', 'close', 'collect', 'come', 'commit',
        'compare', 'complain', 'complete', 'concern', 'confirm', 'connect',
        'consider', 'contain', 'continue', 'control', 'cook', 'copy',
        'correct', 'cost', 'count', 'cover', 'create', 'cross', 'cry',
        'cut', 'damage', 'dance', 'deal', 'decide', 'delete', 'deliver',
        'demand', 'deny', 'depend', 'describe', 'design', 'destroy',
        'develop', 'die', 'discover', 'discuss', 'divide', 'draw', 'dream',
        'dress', 'drink', 'drive', 'drop', 'eat', 'enable', 'encourage',
        'enjoy', 'enter', 'establish', 'examine', 'exist', 'expect',
        'experience', 'explain', 'express', 'extend', 'face', 'fail',
        'fall', 'feed', 'feel', 'fight', 'fill', 'find', 'finish', 'fit',
        'fix', 'fly', 'follow', 'force', 'forget', 'form', 'gain',
        'gather', 'generate', 'grow', 'guess', 'handle', 'hang', 'happen',
        'hate', 'head', 'hear', 'help', 'hide', 'hit', 'hold', 'hope',
        'hurt', 'identify', 'ignore', 'imagine', 'improve', 'include',
        'increase', 'indicate', 'influence', 'inform', 'insist', 'intend',
        'introduce', 'invest', 'involve', 'join', 'judge', 'jump', 'keep',
        'kick', 'kill',
        'knock', 'land', 'last', 'laugh', 'lay', 'lead', 'lean', 'learn',
        'leave', 'lend', 'let', 'lie', 'lift', 'limit', 'link', 'listen',
        'live', 'look', 'lose', 'love', 'manage', 'mark', 'match',
        'matter', 'mean', 'measure', 'meet', 'mention', 'mind', 'miss',
        'move', 'need', 'notice', 'obtain', 'occur', 'offer', 'open',
        'operate', 'order', 'organize', 'own', 'pass', 'pay', 'perform',
        'pick', 'place', 'plan', 'play', 'point', 'pour', 'practice',
        'prefer', 'prepare', 'present', 'press', 'prevent', 'produce',
        'promise', 'protect', 'prove', 'provide', 'publish', 'pull',
        'push', 'put', 'raise', 'reach', 'read', 'realize', 'receive',
        'recognize', 'record', 'reduce', 'refer', 'reflect', 'refuse',
        'regard', 'relate', 'release', 'remain', 'remember', 'remove',
        'repeat', 'replace', 'reply', 'report', 'represent', 'require',
        'respond', 'rest', 'result', 'return', 'reveal', 'ring', 'rise',
        'roll', 'run', 'save', 'search', 'see', 'seek', 'seem', 'sell', 'send',
        'separate', 'serve', 'set', 'settle', 'shake', 'shape', 'share',
        'shoot', 'shout', 'show', 'shut', 'sing', 'sit', 'sleep', 'smile',
        'sort', 'sound', 'speak', 'spend', 'spread', 'stand', 'start',
        'state', 'stay', 'steal', 'stick', 'stop', 'strike', 'study',
        'succeed', 'suffer', 'suggest', 'support', 'suppose', 'survive',
        'switch', 'take', 'talk', 'teach', 'tell', 'tend', 'test',
        'thank', 'think', 'throw', 'touch', 'train', 'travel', 'treat',
        'try', 'turn', 'understand', 'use', 'visit', 'vote', 'wait',
        'wake', 'walk', 'want', 'warn', 'wash', 'watch', 'wear', 'win',
        'wish', 'wonder', 'work', 'worry', 'write',
    ]
    for w in verbs:
        words.append((w, 'verb'))

    # ── Nouns ──
    nouns = [
        'ability', 'absence', 'access', 'accident', 'account', 'action', 'man',
        'activity', 'address', 'administration', 'advantage', 'advice',
        'affair', 'age', 'agency', 'agent', 'agreement', 'air', 'amount',
        'analysis', 'anger', 'animal', 'answer', 'apartment', 'appearance',
        'application', 'approach', 'area', 'argument', 'arm', 'army',
        'arrangement', 'art', 'article', 'aspect', 'atmosphere', 'attack',
        'attempt', 'attention', 'attitude', 'audience', 'authority',
        'baby', 'back', 'background', 'bag', 'balance', 'ball', 'bank',
        'bar', 'base', 'basis', 'battle', 'beach', 'bed', 'behavior',
        'belief', 'benefit', 'bill', 'bird', 'bit', 'blood', 'board',
        'boat', 'body', 'bone', 'book', 'border', 'boss', 'bottom',
        'box', 'boy', 'brain', 'branch', 'bread', 'breath', 'bridge',
        'brother', 'budget', 'building', 'bus', 'business', 'butter',
        'button', 'cabinet', 'camera', 'camp', 'campaign', 'capital',
        'captain', 'car', 'card', 'care', 'career', 'case', 'cash',
        'cat', 'category', 'cause', 'cell', 'center', 'century', 'chair',
        'chairman', 'challenge', 'champion', 'chance', 'channel', 'chapter',
        'character', 'charge', 'charity', 'check', 'chest', 'chicken',
        'chief', 'child', 'children', 'choice', 'church', 'circle',
        'citizen', 'city', 'claim', 'class', 'client', 'climate', 'clock',
        'clothes', 'club', 'coach', 'coast', 'code', 'coffee', 'cold',
        'collection', 'college', 'color', 'column', 'combination',
        'comment', 'commission', 'committee', 'communication', 'community',
        'company', 'comparison', 'competition', 'complaint', 'computer',
        'concept', 'concern', 'conclusion', 'condition', 'conference',
        'confidence', 'conflict', 'connection', 'consequence',
        'consideration', 'construction', 'consumer', 'contact', 'content',
        'context', 'contract', 'contribution', 'control', 'conversation',
        'corner', 'cost', 'council', 'country', 'county', 'couple',
        'courage', 'course', 'court', 'cousin', 'cream', 'credit',
        'crime', 'crisis', 'criticism', 'crowd', 'culture', 'cup',
        'currency', 'current', 'customer', 'cycle', 'dad', 'damage',
        'danger', 'data', 'database', 'date', 'daughter', 'day', 'deal',
        'death', 'debate', 'debt', 'decade', 'decision', 'defense',
        'definition', 'degree', 'demand', 'democracy', 'department',
        'description', 'desire', 'desk', 'detail', 'development', 'device',
        'dialogue', 'diet', 'difference', 'difficulty', 'dinner',
        'direction', 'director', 'discipline', 'discussion', 'disease',
        'display', 'distance', 'distribution', 'district', 'doctor',
        'document', 'dog', 'dollar', 'door', 'doubt', 'draft', 'drama',
        'dream', 'dress', 'drink', 'driver', 'drop', 'drug', 'dust',
        'duty', 'ear', 'earth', 'economy', 'edge', 'editor', 'education',
        'effect', 'effort', 'egg', 'election', 'element', 'emergency',
        'emotion', 'emphasis', 'employee', 'employer', 'employment',
        'end', 'enemy', 'energy', 'engine', 'engineer', 'entertainment',
        'environment', 'episode', 'equipment', 'era', 'error', 'escape',
        'essay', 'establishment', 'estate', 'evening', 'event', 'evidence',
        'evil', 'examination', 'example', 'exchange', 'exercise',
        'existence', 'expansion', 'expectation', 'expense', 'experience',
        'experiment', 'expert', 'explanation', 'expression', 'extent',
        'eye', 'face', 'facility', 'fact', 'factor', 'failure', 'faith',
        'family', 'fan', 'farm', 'farmer', 'fashion', 'fat', 'father',
        'fault', 'fear', 'feature', 'feeling', 'fiction', 'field', 'fight',
        'figure', 'file', 'film', 'final', 'finding', 'finger', 'fire',
        'firm', 'fish', 'flight', 'floor', 'flower', 'fly', 'food',
        'foot', 'football', 'force', 'forest', 'form', 'foundation',
        'frame', 'freedom', 'friend', 'front', 'fruit', 'fuel',
        'function', 'fund', 'future', 'game', 'gap', 'garden', 'gas',
        'gate', 'generation', 'gift', 'girl', 'glass', 'goal', 'god',
        'gold', 'golf', 'government', 'grade', 'grain', 'grandfather',
        'grandmother', 'grass', 'ground', 'group', 'growth', 'guard',
        'guest', 'guide', 'gun', 'guy', 'habit', 'hair', 'half', 'hall',
        'hand', 'hat', 'head', 'health', 'heart', 'heat', 'height',
        'hell', 'hero', 'highway', 'hill', 'history', 'hole', 'holiday',
        'home', 'honey', 'hope', 'horse', 'hospital', 'host', 'hotel',
        'hour', 'house', 'housing', 'human', 'humor', 'hunger', 'husband',
        'ice', 'idea', 'identity', 'image', 'imagination', 'impact',
        'importance', 'impression', 'improvement', 'incident', 'income',
        'increase', 'independence', 'indication', 'individual', 'industry',
        'inflation', 'influence', 'information', 'injury', 'initiative',
        'innovation', 'input', 'instance', 'institution', 'instruction',
        'insurance', 'intelligence', 'intention', 'interaction', 'interest',
        'internet', 'interpretation', 'interview', 'introduction',
        'investigation', 'investment', 'investor', 'island', 'issue',
        'item', 'jacket', 'job', 'journey', 'joy', 'judgment', 'juice',
        'junior', 'jury', 'justice', 'key', 'kid', 'kind', 'king',
        'kitchen', 'knee', 'knife', 'knowledge', 'lab', 'lack', 'lady',
        'lake', 'land', 'landscape', 'language', 'laugh', 'law', 'lawyer',
        'layer', 'leader', 'leadership', 'leaf', 'league', 'lecture',
        'leg', 'lesson', 'letter', 'level', 'library', 'lie', 'life',
        'light', 'limit', 'line', 'lip', 'list', 'literature', 'loan',
        'location', 'lock', 'log', 'loss', 'lot', 'love', 'luck',
        'lunch', 'machine', 'magazine', 'mail', 'majority', 'male',
        'management', 'manager', 'manner', 'map', 'margin', 'mark',
        'market', 'marriage', 'mass', 'master', 'match', 'material',
        'math', 'matter', 'maximum', 'meal', 'meaning', 'measure',
        'meat', 'mechanism', 'media', 'medicine', 'medium', 'meeting',
        'member', 'membership', 'memory', 'menu', 'message', 'metal',
        'method', 'middle', 'midnight', 'military', 'milk', 'mind',
        'mine', 'minister', 'minority', 'minute', 'mirror', 'mission',
        'mistake', 'mixture', 'model', 'mom', 'moment', 'money', 'month',
        'mood', 'morning', 'mortgage', 'mother', 'motion', 'mountain',
        'mouse', 'mouth', 'move', 'movement', 'movie', 'mud', 'murder',
        'muscle', 'music', 'mystery', 'name', 'narrative', 'nation',
        'nature', 'neck', 'need', 'negotiation', 'neighbor', 'neighborhood',
        'nerve', 'network', 'news', 'newspaper', 'night', 'noise', 'north',
        'nose', 'note', 'novel', 'number', 'nurse', 'object', 'objective',
        'obligation', 'observation', 'occasion', 'offer', 'office',
        'officer', 'official', 'oil', 'opening', 'operation', 'opinion',
        'opponent', 'opportunity', 'opposition', 'option', 'order',
        'organization', 'origin', 'outcome', 'output', 'owner', 'pace',
        'package', 'page', 'pain', 'painting', 'pair', 'palace', 'panel',
        'paper', 'parent', 'park', 'parking', 'part', 'participant',
        'partner', 'party', 'passage', 'passenger', 'passion', 'path',
        'patience', 'patient', 'pattern', 'payment', 'peace', 'peak',
        'penalty', 'pension', 'people', 'percentage', 'perception',
        'performance', 'period', 'permission', 'person', 'personality',
        'perspective', 'phase', 'philosophy', 'phone', 'photo', 'phrase',
        'picture', 'piece', 'pilot', 'pipe', 'pitch', 'place', 'plan',
        'plane', 'plant', 'plate', 'platform', 'player', 'pleasure',
        'plenty', 'pocket', 'poem', 'poet', 'poetry', 'point', 'police',
        'policy', 'politics', 'pollution', 'pool', 'population', 'port',
        'position', 'possession', 'possibility', 'potential', 'pound',
        'poverty', 'power', 'prayer', 'preference', 'presence', 'president',
        'pressure', 'price', 'pride', 'priest', 'prince', 'princess',
        'principle', 'priority', 'prison', 'prisoner', 'privacy', 'prize',
        'problem', 'procedure', 'process', 'producer', 'product',
        'production', 'profession', 'professor', 'profit', 'program',
        'progress', 'project', 'promise', 'promotion', 'proof', 'property',
        'proportion', 'proposal', 'protection', 'protest', 'provision',
        'pub', 'public', 'purpose', 'quality', 'quarter', 'queen',
        'question', 'race', 'rain', 'range', 'rank', 'rate', 'ratio',
        'reaction', 'reader', 'reality', 'reason', 'recession', 'record',
        'recovery', 'reduction', 'reference', 'reflection', 'reform',
        'region', 'register', 'regulation', 'relation', 'relationship',
        'release', 'relief', 'religion', 'repeat', 'replacement', 'report',
        'reporter', 'representation', 'republic', 'reputation', 'request',
        'requirement', 'research', 'resident', 'resolution', 'resource',
        'respect', 'response', 'responsibility', 'rest', 'restaurant',
        'result', 'revenue', 'review', 'revolution', 'reward', 'rice',
        'right', 'ring', 'risk', 'river', 'road', 'rock', 'role', 'roof',
        'room', 'root', 'rope', 'round', 'route', 'row', 'rule', 'rush',
        'safety', 'salary', 'sale', 'salt', 'sample', 'sand',
        'satisfaction', 'savings', 'scale', 'scene', 'schedule', 'scheme',
        'school', 'science', 'scientist', 'scope', 'score', 'screen',
        'sea', 'search', 'season', 'seat', 'section', 'sector', 'security',
        'selection', 'sense', 'sentence', 'sequence', 'series', 'servant',
        'service', 'session', 'setting', 'sex', 'shadow', 'shame', 'shape',
        'share', 'sheet', 'shelf', 'shell', 'shift', 'ship', 'shirt',
        'shock', 'shoe', 'shop', 'shot', 'shoulder', 'show', 'shower', 'side',
        'sight', 'sign', 'signal', 'silence', 'silver', 'sin', 'singer',
        'sir', 'sister', 'site', 'situation', 'size', 'skill', 'skin',
        'sky', 'sleep', 'smile', 'snow', 'society', 'software', 'soil',
        'soldier', 'solution', 'son', 'song', 'soul', 'sound', 'source',
        'south', 'space', 'speaker', 'speech', 'speed', 'spirit', 'sport',
        'spot', 'spring', 'square', 'staff', 'stage', 'stair', 'stake',
        'standard', 'star', 'start', 'state', 'statement', 'station',
        'status', 'step', 'stick', 'stock', 'stomach', 'stone', 'stop',
        'store', 'storm', 'story', 'stranger', 'strategy', 'stream',
        'street', 'strength', 'stress', 'stretch', 'strike', 'string',
        'structure', 'struggle', 'student', 'study', 'stuff', 'style',
        'subject', 'success', 'sugar', 'suggestion', 'suit', 'summer',
        'sun', 'supply', 'support', 'surface', 'surprise', 'survey',
        'suspect', 'sweet', 'swimming', 'symbol', 'sympathy', 'system',
        'table', 'tale', 'talent', 'tank', 'target', 'task', 'taste',
        'tax', 'tea', 'teacher', 'teaching', 'team', 'tear', 'technique',
        'technology', 'telephone', 'television', 'temperature', 'tendency',
        'tension', 'term', 'territory', 'terror', 'test', 'text',
        'thanks', 'theater', 'theme', 'theory', 'thing', 'thought',
        'threat', 'throat', 'ticket', 'tie', 'till', 'time', 'tip', 'title',
        'today', 'toe', 'tomorrow', 'tone', 'tongue', 'tonight', 'tool',
        'tooth', 'top', 'topic', 'total', 'touch', 'tour', 'tourist',
        'tower', 'town', 'track', 'trade', 'tradition', 'traffic',
        'training', 'transition', 'transport', 'travel', 'treatment',
        'tree', 'trend', 'trial', 'trick', 'trip', 'trouble', 'troop',
        'trust', 'truth', 'turn', 'type', 'uncle', 'union', 'unit',
        'university', 'valley', 'value', 'variation', 'variety', 'vehicle',
        'version', 'victim', 'victory', 'view', 'village', 'violence',
        'vision', 'visit', 'visitor', 'voice', 'volume', 'wage', 'wall',
        'war', 'warning', 'waste', 'water', 'wave', 'way', 'weakness',
        'wealth', 'weapon', 'weather', 'website', 'wedding', 'week',
        'weekend', 'weight', 'welfare', 'west', 'wheel', 'wife', 'wind',
        'window', 'wine', 'wing', 'winner', 'winter', 'wish', 'witness',
        'woman', 'wood', 'word', 'worker', 'world', 'writing', 'yard',
        'year', 'youth', 'zone',
    ]
    for w in nouns:
        words.append((w, 'noun'))

    # ── Adjectives ──
    adjectives = [
        'able', 'absolute', 'academic', 'acceptable', 'accurate', 'active',
        'actual', 'additional', 'adequate', 'afraid', 'aggressive', 'alive',
        'alone', 'alternative', 'amazing', 'ancient', 'angry', 'annual',
        'anxious', 'apparent', 'appropriate', 'automatic', 'available',
        'average', 'aware', 'awful', 'bad', 'basic', 'beautiful', 'best',
        'better', 'big',
        'bitter', 'black', 'blind', 'blue', 'bold', 'born', 'bottom',
        'brave', 'brief', 'bright', 'broad', 'broken', 'brown', 'busy',
        'calm', 'capable', 'careful', 'central', 'certain', 'cheap',
        'chemical', 'chief', 'civil', 'clean', 'clear', 'clever', 'close',
        'cold', 'comfortable', 'commercial', 'common', 'competitive',
        'complete', 'complex', 'concerned', 'confident', 'conscious',
        'considerable', 'consistent', 'constant', 'contemporary',
        'content', 'continuous', 'conventional', 'cool', 'corporate',
        'correct', 'critical', 'crucial', 'cultural', 'curious', 'current',
        'cute', 'dangerous', 'dark', 'dead', 'dear', 'decent', 'deep',
        'defensive', 'definite', 'democratic', 'dependent', 'desperate',
        'different', 'difficult', 'digital', 'direct', 'dirty', 'double',
        'dramatic', 'dry', 'due', 'dull', 'eager', 'early', 'eastern',
        'easy', 'economic', 'educational', 'effective', 'efficient',
        'elderly', 'electronic', 'emotional', 'empty', 'encouraging',
        'enormous', 'entire', 'environmental', 'equal', 'essential',
        'ethnic', 'eventual', 'evil', 'exact', 'excellent', 'exciting',
        'existing', 'expensive', 'experienced', 'expert', 'extra',
        'extraordinary', 'extreme', 'fair', 'familiar', 'famous', 'far',
        'fast', 'fat', 'favorite', 'federal', 'female', 'final',
        'financial', 'fine', 'firm', 'fit', 'flat', 'flexible', 'following',
        'foreign', 'formal', 'former', 'fortunate', 'forward', 'free',
        'frequent', 'fresh', 'friendly', 'front', 'frozen', 'full', 'fun',
        'funny', 'future', 'general', 'gentle', 'genuine', 'giant', 'glad',
        'global', 'golden', 'good', 'grand', 'grateful', 'gray', 'great',
        'green', 'gross', 'growing', 'guilty', 'happy', 'hard', 'healthy',
        'heavy', 'helpful', 'hidden', 'high', 'historical', 'holy',
        'honest', 'horrible', 'hot', 'huge', 'hungry', 'ideal',
        'immediate', 'important', 'impossible', 'impressive', 'independent',
        'individual', 'industrial', 'inevitable', 'initial', 'inner',
        'innocent', 'intelligent', 'interested', 'interesting', 'internal',
        'international', 'joint', 'keen', 'key', 'large', 'late', 'latter',
        'leading', 'left', 'legal', 'likely', 'limited', 'little',
        'living', 'local', 'long', 'loose', 'loud', 'lovely', 'low',
        'lucky', 'mad', 'main', 'major', 'male', 'married', 'massive',
        'medical', 'mental', 'mere', 'middle', 'mild', 'minor', 'missing',
        'mixed', 'modern', 'moral', 'narrow', 'national', 'natural',
        'neat', 'necessary', 'negative', 'nervous', 'neutral', 'new',
        'next', 'nice', 'normal', 'nuclear', 'numerous', 'obvious', 'odd',
        'official', 'old', 'only', 'open', 'opening', 'opposite',
        'ordinary', 'organic', 'original', 'outer', 'outside', 'overall',
        'own', 'painful', 'pale', 'particular', 'past', 'patient',
        'perfect', 'permanent', 'personal', 'physical', 'pink', 'plain',
        'plastic', 'pleasant', 'pleased', 'political', 'poor', 'popular',
        'positive', 'possible', 'potential', 'powerful', 'practical',
        'precious', 'present', 'previous', 'primary', 'prime', 'principal',
        'prior', 'private', 'probable', 'professional', 'proper', 'proud',
        'psychological', 'public', 'pure', 'purple', 'quick', 'quiet',
        'radical', 'random', 'rapid', 'rare', 'raw', 'ready', 'real',
        'realistic', 'reasonable', 'recent', 'red', 'regular', 'related',
        'relative', 'relevant', 'religious', 'reluctant', 'remaining',
        'remarkable', 'remote', 'representative', 'responsible', 'rich',
        'right', 'rising', 'rough', 'round', 'royal', 'rural', 'sad',
        'safe', 'satisfied', 'scared', 'scientific', 'secret', 'secure',
        'senior', 'sensitive', 'separate', 'serious', 'severe', 'sexual',
        'sharp', 'short', 'shut', 'sick', 'significant', 'silly',
        'similar', 'simple', 'single', 'slight', 'slow', 'small', 'smart',
        'smooth', 'social', 'soft', 'solid', 'sorry', 'southern', 'spare',
        'special', 'specific', 'spiritual', 'stable', 'standard', 'steady',
        'steep', 'still', 'straight', 'strange', 'strict', 'strong',
        'stupid', 'substantial', 'successful', 'sudden', 'sufficient',
        'suitable', 'super', 'sure', 'surprised', 'sweet', 'tall',
        'temporary', 'terrible', 'thick', 'thin', 'tiny', 'tired', 'top',
        'total', 'tough', 'traditional', 'tremendous', 'tropical',
        'typical', 'ugly', 'unable', 'uncertain', 'uncomfortable',
        'unique', 'united', 'unlikely', 'unusual', 'upper', 'upset',
        'urban', 'useful', 'usual', 'valuable', 'various', 'vast',
        'violent', 'visible', 'visual', 'vital', 'warm', 'weak',
        'wealthy', 'weird', 'welcome', 'western', 'wet', 'white', 'whole',
        'wide', 'wild', 'willing', 'wise', 'wonderful', 'wooden', 'worth',
        'wrong', 'yellow', 'young',
    ]
    for w in adjectives:
        words.append((w, 'adjective'))

    # ── Adverbs ──
    adverbs = [
        'absolutely', 'accordingly', 'ago', 'ahead', 'alongside',
        'anyway', 'apparently', 'approximately', 'aside', 'automatically',
        'away', 'basically', 'below', 'briefly', 'carefully', 'clearly',
        'closely', 'completely', 'consequently', 'constantly', 'correctly',
        'currently', 'daily', 'deeply', 'definitely', 'deliberately',
        'desperately', 'directly', 'easily', 'effectively', 'elsewhere',
        'entirely', 'equally', 'especially', 'essentially', 'eventually',
        'everywhere', 'exactly', 'extremely', 'fairly', 'finally',
        'firmly', 'forever', 'formally', 'formerly', 'fortunately',
        'frequently', 'fully', 'furthermore', 'generally', 'gently',
        'gradually', 'greatly', 'hardly', 'heavily', 'highly', 'honestly',
        'hopefully', 'immediately', 'increasingly', 'independently',
        'initially', 'largely', 'lately', 'later', 'mainly', 'merely',
        'mostly', 'naturally', 'nearly', 'necessarily', 'nonetheless',
        'normally', 'notably', 'obviously', 'occasionally', 'officially',
        'originally', 'otherwise', 'overall', 'partly', 'perfectly',
        'permanently', 'personally', 'physically', 'possibly',
        'potentially', 'practically', 'precisely', 'previously',
        'primarily', 'privately', 'properly', 'purely', 'quickly',
        'quietly', 'rapidly', 'rarely', 'readily', 'recently', 'regularly',
        'relatively', 'repeatedly', 'roughly', 'sadly', 'seriously',
        'sharply', 'significantly', 'simply', 'slightly', 'slowly',
        'smoothly', 'softly', 'solely', 'somehow', 'somewhat', 'soon',
        'specifically', 'steadily', 'straight', 'strongly', 'subsequently',
        'successfully', 'suddenly', 'sufficiently', 'surely',
        'technically', 'temporarily', 'thereby', 'thoroughly', 'thus',
        'together', 'tomorrow', 'tonight', 'totally', 'truly', 'twice',
        'typically', 'ultimately', 'unfortunately', 'unlikely', 'usually',
        'utterly', 'virtually', 'widely', 'yesterday',
    ]
    for w in adverbs:
        words.append((w, 'adverb'))

    # ── Numbers & Quantifiers ──
    numbers = [
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
        'eight', 'nine', 'ten', 'eleven', 'twelve', 'twenty', 'thirty',
        'fifty', 'hundred', 'thousand', 'million', 'billion',
        'half', 'quarter', 'double', 'triple', 'dozen', 'pair', 'single',
        'twice', 'first', 'second', 'third', 'fourth', 'fifth', 'last',
        'next', 'previous',
    ]
    for w in numbers:
        words.append((w, 'number'))

    # ── Tech / Agent Domain ──
    tech = [
        'algorithm', 'api', 'application', 'array', 'authentication',
        'binary', 'boolean', 'branch', 'browser', 'buffer', 'bug', 'byte',
        'cache', 'callback', 'class', 'client', 'cloud', 'cluster',
        'command', 'commit', 'compile', 'component', 'compute', 'config',
        'connection', 'console', 'container', 'controller', 'crash',
        'cursor', 'dashboard', 'database', 'debug', 'default',
        'dependency', 'deploy', 'device', 'dictionary', 'directory',
        'disk', 'docker', 'domain', 'download', 'driver', 'editor',
        'email', 'encrypt', 'endpoint', 'engine', 'enterprise', 'event',
        'exception', 'execute', 'export', 'extension', 'field', 'file',
        'filter', 'firmware', 'flag', 'folder', 'format', 'framework',
        'frontend', 'function', 'gateway', 'git', 'graph', 'handler',
        'hash', 'header', 'heap', 'hook', 'host', 'http', 'import',
        'index', 'input', 'instance', 'integer', 'interface', 'iterate',
        'json', 'kernel', 'lambda', 'library', 'link', 'load', 'log',
        'loop', 'memory', 'merge', 'message', 'method', 'middleware',
        'module', 'monitor', 'mount', 'namespace', 'network', 'node',
        'null', 'object', 'output', 'package', 'parse', 'password',
        'patch', 'pipeline', 'platform', 'plugin', 'pointer', 'port',
        'process', 'profile', 'program', 'prompt', 'protocol', 'proxy',
        'query', 'queue', 'recursive', 'refactor', 'regex', 'registry',
        'render', 'repository', 'request', 'response', 'return', 'router',
        'runtime', 'schema', 'script', 'search', 'security', 'selector',
        'sequence', 'server', 'session', 'shell', 'socket', 'software',
        'source', 'stack', 'state', 'status', 'storage', 'stream',
        'string', 'struct', 'syntax', 'system', 'table', 'template',
        'terminal', 'test', 'thread', 'timeout', 'token', 'tool', 'trace',
        'trigger', 'type', 'upload', 'url', 'user', 'utility', 'validate',
        'variable', 'vector', 'version', 'virtual', 'widget', 'worker',
        'xml', 'yaml',
    ]
    for w in tech:
        words.append((w, 'tech'))

    return words


def assign_codes(words):
    """
    Assign ZQX codes to words. Returns dict: english -> (code, tier).
    Tier-1 words get their existing codes; remaining words get tier-2 or tier-3.
    Priority words always get tier-2 (shorter) codes.
    """
    # ~400 highest-frequency English words that MUST get tier-2 codes
    # (beyond the 36 already in tier-1). Sorted by frequency.
    PRIORITY = [
        # Top function words
        'the', 'a', 'that', 'he', 'she', 'they', 'him', 'her', 'them',
        'his', 'its', 'our', 'their', 'who', 'which', 'an', 'some', 'any',
        'would', 'there', 'will', 'can', 'could', 'may', 'should', 'was',
        'were', 'are', 'been', 'had', 'has', 'does', 'did', 'must',
        'about', 'than', 'because', 'when', 'where', 'how', 'then', 'now',
        'here', 'also', 'very', 'just', 'only', 'too', 'so', 'still',
        'already', 'even', 'again', 'never', 'always', 'often',
        'after', 'before', 'into', 'over', 'out', 'down', 'off', 'up',
        'through', 'between', 'under', 'until', 'while', 'since',
        'although', 'however', 'though', 'yet', 'perhaps', 'both',
        'every', 'more', 'most', 'many', 'much', 'few', 'less',
        'these', 'those', 'one', 'something', 'anything', 'nothing',
        'someone', 'everyone', 'myself', 'themselves',
        # Top verbs
        'come', 'take', 'see', 'want', 'use', 'find', 'tell', 'ask',
        'work', 'seem', 'feel', 'try', 'leave', 'call', 'need', 'keep',
        'let', 'begin', 'show', 'hear', 'play', 'run', 'move', 'live',
        'believe', 'bring', 'happen', 'write', 'sit', 'stand', 'lose',
        'pay', 'meet', 'include', 'continue', 'set', 'learn', 'change',
        'lead', 'understand', 'watch', 'follow', 'stop', 'create',
        'speak', 'read', 'allow', 'add', 'spend', 'grow', 'open', 'walk',
        'win', 'offer', 'remember', 'love', 'consider', 'appear', 'buy',
        'wait', 'serve', 'die', 'send', 'expect', 'build', 'stay', 'fall',
        'cut', 'reach', 'kill', 'remain', 'suggest', 'raise', 'pass',
        'sell', 'require', 'report', 'decide', 'pull', 'develop',
        'produce', 'eat', 'draw', 'break', 'hold', 'think', 'help',
        'start', 'turn', 'look', 'put', 'become', 'agree', 'act', 'check',
        'close', 'carry', 'provide', 'touch', 'receive', 'choose', 'deal',
        'mean', 'form', 'save', 'face', 'test', 'sort', 'sound', 'share',
        'matter', 'head', 'cause', 'design', 'join', 'own', 'drive',
        'fill', 'fit', 'fight', 'miss', 'hope', 'copy', 'wish',
        'support', 'result', 'plan', 'train', 'return', 'point', 'claim',
        'describe', 'force', 'cover', 'cost', 'shoot', 'state', 'enter',
        'manage', 'record', 'prepare', 'control', 'present', 'mark',
        'place', 'strike', 'order', 'replace', 'connect', 'delete', 'fix',
        # Top nouns
        'time', 'people', 'way', 'day', 'man', 'woman', 'child', 'world',
        'life', 'hand', 'part', 'place', 'case', 'week', 'company',
        'system', 'program', 'question', 'work', 'government', 'number',
        'night', 'point', 'home', 'water', 'room', 'mother', 'area',
        'money', 'story', 'fact', 'month', 'lot', 'right', 'study',
        'book', 'eye', 'job', 'word', 'business', 'issue', 'side', 'kind',
        'head', 'house', 'service', 'friend', 'father', 'power', 'hour',
        'game', 'line', 'end', 'member', 'law', 'car', 'city', 'name',
        'team', 'minute', 'idea', 'body', 'information', 'back', 'parent',
        'face', 'level', 'office', 'door', 'health', 'person', 'art',
        'war', 'history', 'party', 'result', 'change', 'morning',
        'reason', 'research', 'girl', 'guy', 'moment', 'air', 'teacher',
        'force', 'education', 'food', 'problem', 'group', 'state',
        'family', 'school', 'country', 'market', 'report', 'class',
        'year', 'age', 'thing', 'need', 'love', 'form',
        'file', 'code', 'error', 'task', 'message', 'data', 'process',
        'test', 'user', 'type', 'value', 'model', 'list', 'string',
        'function', 'event', 'field', 'path', 'node', 'key', 'table',
        'source', 'object', 'method', 'network', 'tool', 'server',
        'status', 'token', 'agent', 'memory', 'input', 'output',
        # Top adjectives
        'good', 'new', 'first', 'last', 'long', 'great', 'little', 'own',
        'big', 'high', 'different', 'small', 'large', 'next', 'early',
        'young', 'important', 'public', 'bad', 'same', 'able', 'old',
        'right', 'better', 'best', 'free', 'major', 'sure', 'real',
        'full', 'clear', 'hard', 'possible', 'whole', 'special', 'short',
        'single', 'personal', 'current', 'left', 'open', 'close', 'hot',
        'cold', 'dark', 'light', 'fast', 'slow', 'simple', 'strong',
        'easy', 'ready', 'local', 'final', 'main', 'common', 'black',
        'white', 'red', 'blue', 'green', 'certain', 'true', 'human',
        'available', 'recent', 'likely',
    ]

    tier1_words = set(TIER1.values())
    tier2_pool = gen_tier2_codes()
    tier3_pool = gen_tier3_codes()

    assignments = {}

    # Register tier-1 words
    for code, english in TIER1.items():
        assignments[english] = (code, 1)

    # Collect all unique words needing codes
    seen = set(tier1_words)
    all_words = []
    for english, category in words:
        if english not in seen:
            seen.add(english)
            all_words.append((english, category))

    # Build priority index (lower = more important)
    priority_set = set(PRIORITY)
    priority_rank = {w: i for i, w in enumerate(PRIORITY)}

    # Sort: priority words first (by rank), then non-priority (by list order)
    priority_words = []
    other_words = []
    for english, category in all_words:
        if english in priority_set:
            priority_words.append((english, category, priority_rank[english]))
        else:
            other_words.append((english, category))

    priority_words.sort(key=lambda x: x[2])
    sorted_words = [(e, c) for e, c, _ in priority_words] + other_words

    # Assign codes
    t2_idx = 0
    t3_idx = 0

    for english, category in sorted_words:
        if t2_idx < len(tier2_pool):
            # Find next code that doesn't phonetically match the word
            while t2_idx < len(tier2_pool):
                code = tier2_pool[t2_idx]
                if code != english[:2]:
                    break
                t2_idx += 1
            if t2_idx < len(tier2_pool):
                assignments[english] = (code, 2)
                t2_idx += 1
            else:
                code = tier3_pool[t3_idx]
                assignments[english] = (code, 3)
                t3_idx += 1
        else:
            code = tier3_pool[t3_idx]
            assignments[english] = (code, 3)
            t3_idx += 1

    return assignments


def generate_document(assignments, words):
    """Generate the complete ZQX specification document."""

    # Build sorted vocabulary for the table
    all_entries = []
    seen = set()
    # Add tier-1 entries
    for code, english in sorted(TIER1.items(), key=lambda x: x[1]):
        all_entries.append((english, code, 1))
        seen.add(english)
    # Add the rest
    for english, category in words:
        if english not in seen and english in assignments:
            seen.add(english)
            code, tier = assignments[english]
            all_entries.append((english, code, tier))

    # Sort alphabetically by english word
    all_entries.sort(key=lambda x: x[0])

    # Count tiers
    t1_count = sum(1 for _, _, t in all_entries if t == 1)
    t2_count = sum(1 for _, _, t in all_entries if t == 2)
    t3_count = sum(1 for _, _, t in all_entries if t == 3)
    total = len(all_entries)

    # --- Build document ---
    doc = []

    doc.append("# ZQX Language Specification v2.0")
    doc.append("")
    doc.append("## 1. Purpose")
    doc.append("")
    doc.append("ZQX is a synthetic language for agent-to-agent communication. "
               "No human-readable words, no shortened English, no recognizable roots.")
    doc.append("")
    doc.append("**Goals:**")
    doc.append("- **Compression**: 40-70% fewer characters than English")
    doc.append("- **Parsability**: Unambiguous grammar, zero irregular forms")
    doc.append("- **Opacity**: Humans see gibberish — by design")
    doc.append("- **Coverage**: 2000 most common English words mapped to compact codes")
    doc.append("- **Semantic composition**: Any concept expressible from ~100 primitives via `:` composition — no quoted fallbacks needed")
    doc.append("")
    doc.append("Agents learn the mapping tables. Everything else derives from five grammar rules plus a semantic composition layer.")
    doc.append("")
    doc.append("---")
    doc.append("")

    # Section 2: Encoding Scheme
    doc.append("## 2. Encoding Scheme")
    doc.append("")
    doc.append("Three tiers of codes, assigned by word frequency:")
    doc.append("")
    doc.append("| Tier | Format | Count | Char length | Coverage |")
    doc.append("|------|--------|-------|-------------|----------|")
    doc.append(f"| 1 | Single char `[a-z0-9]` | {t1_count} | 1 | ~55% of text |")
    doc.append(f"| 2 | Two chars `[a-z][a-z]` | {t2_count} | 2 | ~35% of text |")
    doc.append(f"| 3 | Three consonants `[bcdfghjklmnpqrstvwxz]³` | {t3_count} | 3 | ~10% of text |")
    doc.append(f"| | **Total** | **{total}** | | |")
    doc.append("")
    doc.append("**Tier rules:**")
    doc.append("- Tier-2 codes exclude all 2-letter English words (54 excluded: "
               "`ad`, `ah`, `am`, `an`, `as`, `at`, `aw`, `ax`, `be`, `bo`, `by`, "
               "`do`, `ed`, `eh`, `em`, `en`, `er`, `ex`, `go`, `ha`, `he`, `hi`, "
               "`ho`, `id`, `if`, `in`, `is`, `it`, `la`, `lo`, `ma`, `me`, `my`, "
               "`no`, `of`, `oh`, `ok`, `on`, `op`, `or`, `ow`, `ox`, `pa`, `pi`, "
               "`re`, `sh`, `so`, `to`, `uh`, `um`, `un`, `up`, `us`, `we`, `ye`, `yo`)")
    doc.append("- Tier-3 codes use consonants only (no `a,e,i,o,u,y`) — "
               "no English word can be formed without vowels")
    doc.append("- Codes are assigned to avoid phonetic resemblance to their English meanings")
    doc.append("- Remaining rare/domain words not in the 2000: use quoted strings (`\"kubernetes\"`)")
    doc.append("")
    doc.append("**Token disambiguation:**")
    doc.append("")
    doc.append("| Pattern | Interpretation | Example |")
    doc.append("|---------|---------------|---------|")
    doc.append("| 1 letter `[a-z]` | Tier-1 code | `j` → know |")
    doc.append("| 1 digit `[0-9]` | Tier-1 code | `1` → true |")
    doc.append("| 2 letters `[a-z]{2}` | Tier-2 code | `zc` → about |")
    doc.append("| 3 consonants | Tier-3 code | `bcf` → afraid |")
    doc.append("| 2+ digits | Literal number | `42` → forty-two |")
    doc.append("| `\"...\"` | Literal string | `\"prod\"` → prod |")
    doc.append("| Word + digits | Reference | `kr1` → ref #1 |")
    doc.append("| `p.`/`f.` + token | Tense prefix | `p.jn` → read (past) |")
    doc.append("| `!`/`?` + token | Modifier prefix | `!j` → don't know |")
    doc.append("")
    doc.append("---")
    doc.append("")

    # Section 3: Grammar
    doc.append("## 3. Grammar")
    doc.append("")
    doc.append("Five rules. No exceptions.")
    doc.append("")
    doc.append("### Rule 1 — SVO Order")
    doc.append("Subject → Verb → Object. Always.")
    doc.append("```")
    doc.append("c j f        → I know this")
    doc.append("z jw kr1     → you write file1")
    doc.append("```")
    doc.append("")
    doc.append("### Rule 2 — No Articles")
    doc.append("No articles required. `the`, `a`, `an` have codes but are optional.")
    doc.append("```")
    doc.append("EN:  Read the file")
    doc.append("ZQX: jn kr1       (article omitted)")
    doc.append("```")
    doc.append("")
    doc.append("### Rule 3 — No Plurals")
    doc.append("Context resolves quantity. Use number codes when precision needed.")
    doc.append("```")
    doc.append("ri kn        → many errors")
    doc.append("r kr         → all files")
    doc.append("```")
    doc.append("")
    doc.append("### Rule 4 — Tense Prefixes")
    doc.append("Attach directly to verb with `.` separator. Unmarked = present.")
    doc.append("")
    doc.append("| Prefix | Tense | Example | Meaning |")
    doc.append("|--------|-------|---------|---------|")
    doc.append("| `p.` | past | `c p.jn kr1` | I read (past) file1 |")
    doc.append("| `f.` | future | `z f.jw kv1` | you will write code1 |")
    doc.append("")
    doc.append("### Rule 5 — Modifier Prefixes")
    doc.append("Attach directly to next token, no separator.")
    doc.append("")
    doc.append("| Prefix | Function | Example | Meaning |")
    doc.append("|--------|----------|---------|---------|")
    doc.append("| `!` | negate | `c !j` | I don't know |")
    doc.append("| `?` | question | `?z j f` | do you know this? |")
    doc.append("")
    doc.append("Prefixes stack: `?z !p.j f` → \"didn't you know this?\"")
    doc.append("")
    doc.append("---")
    doc.append("")

    # Section 4: Complete Vocabulary
    doc.append("## 4. Complete Vocabulary")
    doc.append("")
    doc.append(f"**{total} entries** — alphabetical by English word. "
               "Three columns per row for density.")
    doc.append("")

    # Build 3-column table
    doc.append("| English | ZQX | T | English | ZQX | T | English | ZQX | T |")
    doc.append("|---------|-----|---|---------|-----|---|---------|-----|---|")

    # Pad to multiple of 3
    padded = list(all_entries)
    while len(padded) % 3 != 0:
        padded.append(('', '', ''))

    for i in range(0, len(padded), 3):
        cols = []
        for j in range(3):
            eng, code, tier = padded[i + j]
            if eng:
                cols.append(f"| {eng} | `{code}` | {tier} ")
            else:
                cols.append("| | | ")
        doc.append("".join(cols) + "|")

    doc.append("")
    doc.append("---")
    doc.append("")

    # Section 5: Operations
    doc.append("## 5. Operations")
    doc.append("")
    doc.append("Structured agent commands use S-expression syntax: `(verb arg ...)`.")
    doc.append("")
    doc.append("### 5.1 Format")
    doc.append("```")
    doc.append("(verb arg1 arg2 ...)")
    doc.append("```")
    doc.append("Arguments: tokens, literals, or nested operations.")
    doc.append("")
    doc.append("### 5.2 Core Operations")
    doc.append("")

    # Look up specific codes for the operations section
    def lk(word):
        """Look up ZQX code for an English word."""
        if word in assignments:
            return assignments[word][0]
        return f'"{word}"'

    doc.append("**File I/O:**")
    doc.append("```")
    doc.append(f"({lk('read')} <ref>)                     — read")
    doc.append(f"({lk('write')} <ref> <line> <content>)    — write at line")
    doc.append(f"({lk('find')} <pattern> v <scope>)       — find in scope")
    doc.append(f"({lk('delete')} <ref>)                     — delete")
    doc.append(f"({lk('copy')} <ref> <ref>)               — copy")
    doc.append(f"({lk('move')} <ref> <ref>)               — move")
    doc.append("```")
    doc.append("")
    doc.append("**Execution:**")
    doc.append("```")
    doc.append(f"({lk('run')} <ref>)                      — run")
    doc.append(f"({lk('test')} <ref>)                     — test")
    doc.append(f"({lk('deploy')} <target>)                  — deploy")
    doc.append(f"({lk('call')} <ref> <args>)              — call/invoke")
    doc.append("```")
    doc.append("")
    doc.append("**Control Flow:**")
    doc.append("```")
    doc.append(f"({lk('sequence')} <op1> <op2> ...)          — sequence")
    doc.append(f"({lk('loop')} <count> <op>)               — loop N times")
    doc.append(f"({lk('loop')} 9 <ref> <op>)               — loop each item")
    doc.append("```")
    doc.append("")
    doc.append("**Communication:**")
    doc.append("```")
    doc.append(f"({lk('send')} <content> n <dest>)        — send to")
    doc.append(f"({lk('receive')} 2 <source>)               — receive from")
    doc.append("```")
    doc.append("")
    doc.append("**Conditional:**")
    doc.append("```")
    doc.append(f"q <condition> {lk('then')} <then-clause> {lk('otherwise')} <else-clause>")
    doc.append("```")
    doc.append("")
    doc.append("---")
    doc.append("")

    # Section 6: Reference System
    doc.append("## 6. Reference System")
    doc.append("")
    doc.append("Bind labels with `->` for reuse. References = word + digits.")
    doc.append("")
    doc.append("### 6.1 Binding")
    doc.append("```")
    doc.append(f'{lk("file")}1 -> "/src/app.py"')
    doc.append(f'{lk("code")}1 -> "validate_input"')
    doc.append("```")
    doc.append("")
    doc.append("### 6.2 Usage")
    doc.append("```")
    doc.append(f'{lk("file")}1 -> "/src/app.py"')
    doc.append(f'{lk("file")}2 -> "/src/utils.py"')
    doc.append(f'({lk("read")} {lk("file")}1)')
    doc.append(f'({lk("find")} "def validate" v {lk("file")}2)')
    doc.append(f'({lk("write")} {lk("file")}1 3 "import validate")')
    doc.append("```")
    doc.append("")
    doc.append("References are valid from binding to end of message.")
    doc.append("")
    doc.append("---")
    doc.append("")

    # Section 7: Patterns
    doc.append("## 7. Patterns")
    doc.append("")
    doc.append("### Pattern 1 — Read-Modify-Write")
    doc.append("```")
    doc.append(f"({lk('sequence')} ({lk('read')} <ref>)({lk('write')} <ref> <line> <content>)({lk('check')} <ref>))")
    doc.append("```")
    doc.append("")
    doc.append("### Pattern 2 — Search and Act")
    doc.append("```")
    doc.append(f"{lk('result')}1 -> ({lk('find')} <pattern> v <scope>)")
    doc.append(f"({lk('loop')} 9 {lk('result')}1 (<op>))")
    doc.append("```")
    doc.append("")
    doc.append("### Pattern 3 — Conditional")
    doc.append("```")
    doc.append(f"q <condition> {lk('then')} <then> {lk('otherwise')} <else>")
    doc.append("```")
    doc.append("")
    doc.append("### Pattern 4 — Error Guard")
    doc.append("```")
    doc.append(f"({lk('try')} <op>) q {lk('error')} {lk('then')} ({lk('fix')} {lk('error')}) {lk('otherwise')} ({lk('stop')})")
    doc.append("```")
    doc.append("")
    doc.append("### Pattern 5 — Task Delegation")
    doc.append("```")
    doc.append(f"({lk('send')} {lk('task')}1 n {lk('agent')}1)")
    doc.append(f"({lk('wait')} {lk('result')} 2 {lk('agent')}1)")
    doc.append("```")
    doc.append("")
    doc.append("### Pattern 6 — Pipeline")
    doc.append("```")
    doc.append(f"{lk('result')}1 -> (<op1>)")
    doc.append(f"{lk('result')}2 -> (<op2> {lk('result')}1)")
    doc.append(f"{lk('result')}3 -> (<op3> {lk('result')}2)")
    doc.append("```")
    doc.append("")
    doc.append("---")
    doc.append("")

    # Section 8: Semantic Composition
    doc.append("## 8. Semantic Composition")
    doc.append("")
    doc.append("The vocabulary maps common words 1:1. For concepts **outside** the vocabulary,")
    doc.append("compose meaning from ~100 semantic primitives instead of falling back to quoted English.")
    doc.append("")

    # §8.1 Concept Composition
    doc.append("### 8.1 Concept Composition — `:` operator")
    doc.append("")
    doc.append("Combines concepts. Head concept first, modifiers after.")
    doc.append("")
    doc.append("| Composition | Expansion | English meaning |")
    doc.append("|-------------|-----------|-----------------|")
    doc.append(f"| `{lk('flower')}:{lk('pink')}` | flower:pink | pink flower |")
    doc.append(f"| `{lk('flower')}:{lk('pink')}:{lk('big')}` | flower:pink:big | big pink flower (peony) |")
    doc.append(f"| `{lk('water')}:{lk('force')}:{lk('above')}` | water:force:above | geyser |")
    doc.append(f"| `{lk('see')}:{lk('not')}:{lk('body')}` | see:not:body | ghost / specter |")
    doc.append(f"| `{lk('design')}:{lk('many')}:{lk('small')}` | design:many:small | ornate |")
    doc.append(f"| `{lk('fire')}:{lk('small')}` | fire:small | candle / ember |")
    doc.append(f"| `{lk('water')}:{lk('big')}:{lk('force')}` | water:big:force | tsunami / flood |")
    doc.append(f"| `{lk('stone')}:{lk('hot')}:{lk('earth')}` | stone:hot:earth | volcano |")
    doc.append(f"| `{lk('air')}:{lk('force')}:{lk('fast')}` | air:force:fast | storm / hurricane |")
    doc.append(f"| `{lk('light')}:{lk('many')}:{lk('small')}` | light:many:small | glitter / sparkle |")
    doc.append(f"| `{lk('water')}:{lk('cold')}:{lk('white')}` | water:cold:white | snow / ice |")
    doc.append(f"| `{lk('glass')}:{lk('eye')}` | glass:eye | lens / spectacle |")
    doc.append(f"| `{lk('fire')}:{lk('light')}:{lk('above')}` | fire:light:above | beacon / lighthouse |")
    doc.append(f"| `{lk('wood')}:{lk('water')}:{lk('move')}` | wood:water:move | boat / raft |")
    doc.append(f"| `{lk('metal')}:{lk('hot')}:{lk('red')}` | metal:hot:red | forge / molten metal |")
    doc.append(f"| `{lk('flower')}:{lk('white')}:{lk('small')}` | flower:white:small | daisy |")
    doc.append(f"| `{lk('flower')}:{lk('red')}:{lk('love')}` | flower:red:love | rose |")
    doc.append(f"| `{lk('earth')}:{lk('green')}:{lk('many')}` | earth:green:many | meadow / field |")
    doc.append(f"| `{lk('face')}:{lk('good')}:{lk('love')}` | face:good:love | beauty / adoration |")
    doc.append(f"| `{lk('hand')}:{lk('design')}:{lk('small')}` | hand:design:small | craft / artisan work |")
    doc.append(f"| `{lk('eye')}:{lk('far')}` | eye:far | telescope / binoculars |")
    doc.append(f"| `{lk('water')}:{lk('green')}:{lk('grow')}` | water:green:grow | swamp / marsh |")
    doc.append(f"| `{lk('stone')}:{lk('old')}:{lk('big')}` | stone:old:big | monument / ruin |")
    doc.append(f"| `{lk('air')}:{lk('cold')}:{lk('white')}` | air:cold:white | fog / mist |")
    doc.append(f"| `{lk('light')}:{lk('many')}:{lk('above')}` | light:many:above | stars / constellation |")
    doc.append("")
    doc.append("**Parser rule:** `p.` and `f.` at token start = tense prefix. All `:` within a token = composition.")
    doc.append("")

    # §8.2 Semantic Primitives
    doc.append("### 8.2 Semantic Primitives")
    doc.append("")
    doc.append("~97 root concepts from the vocabulary, tagged as composable building blocks:")
    doc.append("")
    doc.append("| Domain | Count | Examples |")
    doc.append("|--------|-------|---------|")
    doc.append(f"| Physical properties | 20 | big/`{lk('big')}`, small/`{lk('small')}`, hot/`{lk('hot')}`, cold/`{lk('cold')}`, fast/`{lk('fast')}`, slow/`{lk('slow')}`, hard/`{lk('hard')}`, soft/`{lk('soft')}`, heavy/`{lk('heavy')}`, light/`{lk('light')}`, long/`{lk('long')}`, short/`{lk('short')}`, wide/`{lk('wide')}`, thin/`{lk('thin')}`, deep/`{lk('deep')}`, flat/`{lk('flat')}`, round/`{lk('round')}`, sharp/`{lk('sharp')}`, smooth/`{lk('smooth')}`, rough/`{lk('rough')}` |")
    doc.append(f"| Colors | 8 | red/`{lk('red')}`, blue/`{lk('blue')}`, green/`{lk('green')}`, pink/`{lk('pink')}`, black/`{lk('black')}`, white/`{lk('white')}`, yellow/`{lk('yellow')}`, brown/`{lk('brown')}` |")
    doc.append(f"| Elements | 10 | water/`{lk('water')}`, fire/`{lk('fire')}`, air/`{lk('air')}`, glass/`{lk('glass')}`, stone/`{lk('stone')}`, earth/`{lk('earth')}`, light/`{lk('light')}`, wood/`{lk('wood')}`, metal/`{lk('metal')}`, ice/`{lk('ice')}` |")
    doc.append(f"| Body | 8 | body/`{lk('body')}`, face/`{lk('face')}`, hand/`{lk('hand')}`, eye/`{lk('eye')}`, head/`{lk('head')}`, arm/`{lk('arm')}`, leg/`{lk('leg')}`, mouth/`{lk('mouth')}` |")
    doc.append(f"| Core actions | 15 | move/`{lk('move')}`, take/`{lk('take')}`, break/`{lk('break')}`, hold/`{lk('hold')}`, open/`{lk('open')}`, close/`{lk('close')}`, cut/`{lk('cut')}`, make/`{lk('make')}`, give/`{lk('give')}`, put/`{lk('put')}`, build/`{lk('build')}`, push/`{lk('push')}`, pull/`{lk('pull')}`, turn/`{lk('turn')}`, throw/`{lk('throw')}` |")
    doc.append(f"| Perception | 10 | see/`{lk('see')}`, hear/`{lk('hear')}`, feel/`{lk('feel')}`, think/`{lk('think')}`, show/`{lk('show')}`, speak/`{lk('speak')}`, touch/`{lk('touch')}`, watch/`{lk('watch')}`, know/`{lk('know')}`, believe/`{lk('believe')}` |")
    doc.append(f"| States | 10 | good/`{lk('good')}`, bad/`{lk('bad')}`, new/`{lk('new')}`, live/`{lk('live')}`, full/`{lk('full')}`, dead/`{lk('dead')}`, old/`{lk('old')}`, strong/`{lk('strong')}`, weak/`{lk('weak')}`, clean/`{lk('clean')}` |")
    doc.append(f"| Spatial | 6 | above/`{lk('above')}`, below/`{lk('below')}`, near/`{lk('near')}`, far/`{lk('far')}`, inside/`{lk('inside')}`, outside/`{lk('outside')}` |")
    doc.append(f"| Quantity | 6 | one/`{lk('one')}`, many/`{lk('many')}`, few/`{lk('few')}`, none/`{lk('none')}`, all/`{lk('all')}`, some/`{lk('some')}` |")
    doc.append(f"| Social | 6 | love/`{lk('love')}`, fear/`{lk('fear')}`, help/`{lk('help')}`, fight/`{lk('fight')}`, friend/`{lk('friend')}`, war/`{lk('war')}` |")
    doc.append(f"| Abstract | 10 | time/`{lk('time')}`, place/`{lk('place')}`, thing/`{lk('thing')}`, force/`{lk('force')}`, power/`{lk('power')}`, way/`{lk('way')}`, cause/`{lk('cause')}`, change/`{lk('change')}`, end/`{lk('end')}`, start/`{lk('start')}` |")
    doc.append("")

    # §8.3 Intent Frames
    doc.append("### 8.3 Intent Frames — `{}` syntax")
    doc.append("")
    doc.append("Capture communicative purpose, not sentence structure.")
    doc.append("")
    doc.append("**Syntax:** `{FRAME-TYPE [SUBJECT] CONTENT}`")
    doc.append("")
    doc.append("- First token = intent type")
    doc.append("- Optional second token = subject being framed")
    doc.append("- Rest = semantic content using compositions and regular ZQX")
    doc.append("- Frames can nest")
    doc.append("")
    doc.append("**Intent types:**")
    doc.append("")
    doc.append("| Intent | ZQX | Usage |")
    doc.append("|--------|-----|-------|")
    doc.append(f"| suggest | `{lk('suggest')}` | `{{{lk('suggest')} ...}}` — propose an action |")
    doc.append(f"| describe | `{lk('describe')}` | `{{{lk('describe')} ...}}` — characterize something |")
    doc.append(f"| ask | `{lk('ask')}` | `{{{lk('ask')} ...}}` — request information |")
    doc.append(f"| explain | `{lk('explain')}` | `{{{lk('explain')} ...}}` — clarify reasoning |")
    doc.append(f"| warn | `{lk('warn')}` | `{{{lk('warn')} ...}}` — flag risk or danger |")
    doc.append(f"| compare | `{lk('compare')}` | `{{{lk('compare')} ...}}` — relate two things |")
    doc.append(f"| cause | `{lk('cause')}` | `{{{lk('cause')} ...}}` — state causation |")
    doc.append(f"| example | `{lk('example')}` | `{{{lk('example')} ...}}` — provide illustration |")
    doc.append("")
    doc.append("**Example:**")
    doc.append("```")
    doc.append(f"EN:  I suggest we use a big pink flower as the design element")
    doc.append(f"ZQX: {{{lk('suggest')} u {lk('use')} {lk('flower')}:{lk('pink')}:{lk('big')} {lk('design')}}}")
    doc.append("")
    doc.append(f"EN:  Can you describe how the storm affected the garden?")
    doc.append(f"ZQX: {{{lk('ask')} {{{lk('describe')} {lk('air')}:{lk('force')}:{lk('fast')} p.{lk('change')} {lk('garden')}}}}}")
    doc.append("```")
    doc.append("")

    # §8.4 Approximate Marker
    doc.append("### 8.4 Approximate Marker — `~` prefix")
    doc.append("")
    doc.append("Signals a composition is a best-effort approximation, not an exact match.")
    doc.append("")
    doc.append(f"| Expression | Meaning |")
    doc.append(f"|------------|---------|")
    doc.append(f"| `~{lk('flower')}:{lk('pink')}:{lk('big')}` | approximately a big pink flower (≈ peony) |")
    doc.append(f"| `~{lk('see')}:{lk('not')}:{lk('body')}` | something like an invisible being (≈ specter) |")
    doc.append(f"| `~{lk('stone')}:{lk('hot')}:{lk('earth')}` | roughly a hot-earth-stone formation (≈ volcano) |")
    doc.append("")
    doc.append("Agents encountering `~` know the composition is approximate — close but not exact.")
    doc.append("")

    # §8.5 Semantic vs Literal Guide
    doc.append("### 8.5 Semantic vs Literal Guide")
    doc.append("")
    doc.append("**Florist passage (English — 218 chars):**")
    doc.append("> The ornate shop displayed peonies, roses, and daisies. A specter of beauty")
    doc.append("> hung in the air. Each arrangement was a small masterpiece — flowers chosen")
    doc.append("> for color and meaning, petals like stained glass catching the light.")
    doc.append("")
    doc.append("**Literal mode** (word-for-word, quotes for out-of-vocab — 156 chars, 28% compression):")
    doc.append("```")
    # Literal: direct word substitution, articles omitted (Rule 2), quotes for 9 unknown words
    doc.append(f'"ornate" {lk("shop")} p.{lk("show")} "peonies" "roses" m "daisies"')
    doc.append(f'"specter" t "beauty" p.{lk("hang")} v {lk("air")}')
    doc.append(f'9 {lk("arrangement")} {lk("was")} {lk("small")} "masterpiece"')
    doc.append(f'{lk("flower")} p.{lk("choose")} l {lk("color")} m {lk("meaning")}')
    doc.append(f'"petals" o "stained" {lk("glass")} {lk("catch")} {lk("light")}')
    doc.append("```")
    doc.append("**9 quoted fallbacks:** `\"ornate\"`, `\"peonies\"`, `\"roses\"`, `\"daisies\"`, `\"specter\"`, `\"beauty\"`, `\"masterpiece\"`, `\"petals\"`, `\"stained\"` — these require both agents to know English.")
    doc.append("")
    doc.append("**Semantic mode** (compositions + intent frame — 132 chars, 39% compression):")
    doc.append("```")
    doc.append(f'{{{lk("describe")} {lk("shop")}:{lk("design")}:{lk("many")}:{lk("small")}')
    doc.append(f'  p.{lk("show")} ~{lk("flower")}:{lk("pink")}:{lk("big")} ~{lk("flower")}:{lk("red")}:{lk("love")} ~{lk("flower")}:{lk("white")}:{lk("small")}')
    doc.append(f'  ~{lk("see")}:{lk("not")}:{lk("body")}:{lk("beautiful")} p.{lk("hang")}:{lk("air")}')
    doc.append(f'  9 {lk("arrangement")} {lk("small")} ~{lk("design")}:{lk("good")}:{lk("hand")}')
    doc.append(f'  {lk("flower")} p.{lk("choose")}:{lk("color")}:{lk("meaning")}')
    doc.append(f'  {lk("flower")}:{lk("thin")} {lk("glass")}:{lk("color")}:{lk("light")}}}')
    doc.append("```")
    doc.append("**Zero quoted words.** All 9 out-of-vocab concepts composed from primitives.")
    doc.append("")
    doc.append("**Compression comparison:**")
    doc.append("")
    doc.append("| Mode | Chars | Compression | Quoted fallbacks |")
    doc.append("|------|-------|-------------|-----------------|")
    doc.append("| English original | 218 | — | — |")
    doc.append("| Literal ZQX | 156 | 28% | 9 (requires English) |")
    doc.append("| Semantic ZQX | 132 | 39% | 0 (fully closed) |")
    doc.append("")
    doc.append("The primary win is **vocabulary closure**: semantic mode eliminates all English")
    doc.append("dependency. The extra ~11% compression is secondary to never needing quoted fallbacks.")
    doc.append("")
    doc.append("---")
    doc.append("")

    # Section 9: Examples (was §8)
    doc.append("## 9. Examples")
    doc.append("")

    # Example 1
    doc.append("### 9.1 Personal")
    doc.append("```")
    doc.append('EN:  My name is Tim and I like to play soccer')
    doc.append(f'ZQX: y {lk("name")} k "Tim" m c o {lk("play")} "soccer"')
    doc.append("```")
    doc.append("")

    # Example 2
    doc.append("### 9.2 File Operations")
    doc.append("```")
    doc.append('EN:  Read the file, edit line 42, then run the tests')
    doc.append(f'ZQX: ({lk("sequence")} ({lk("read")} {lk("file")}1)({lk("write")} {lk("file")}1 42 "return True")({lk("run")} {lk("test")}1))')
    doc.append("```")
    doc.append("")

    # Example 3
    doc.append("### 9.3 Uncertainty")
    doc.append("```")
    doc.append("EN:  I don't know if this will work but let's try")
    doc.append(f"ZQX: c !j q f f.{lk('work')} e {lk('try')}")
    doc.append("```")
    doc.append("")

    # Example 4
    doc.append("### 9.4 Task Assignment")
    doc.append("```")
    doc.append('EN:  Create a task for Alice to design the logo before we send')
    doc.append(f'ZQX: (i {lk("task")} l "Alice" {lk("design")} "logo" {lk("before")} u {lk("send")})')
    doc.append("```")
    doc.append("")

    # Example 5
    doc.append("### 9.5 Conditional Logic")
    doc.append("```")
    doc.append('EN:  If the tests pass, deploy to production. Otherwise send the error to the team.')
    doc.append(f'ZQX: q {lk("test")} k 1 {lk("then")} ({lk("deploy")} "prod") {lk("otherwise")} ({lk("send")} {lk("error")} n {lk("team")})')
    doc.append("```")
    doc.append("")

    # Example 6
    doc.append("### 9.6 Search")
    doc.append("```")
    doc.append('EN:  Find all Python files in the source directory containing validate')
    doc.append(f'ZQX: ({lk("find")} "*.py" v "src" d "validate")')
    doc.append("```")
    doc.append("")

    # Example 7
    doc.append("### 9.7 Error Handling")
    doc.append("```")
    doc.append('EN:  The build failed because of a missing dependency. Install it and retry.')
    doc.append(f'ZQX: {lk("build")} p.{lk("fail")} {lk("because")} !h {lk("dependency")} ({lk("sequence")} ({lk("load")} x)({lk("try")} {lk("build")}))')
    doc.append("```")
    doc.append("")

    # Example 8
    doc.append("### 9.8 Multi-step Workflow")
    doc.append("```")
    doc.append('EN:  Clone the repo, checkout feature branch, read config, update timeout to 30, run tests.')
    doc.append(f'ZQX: {lk("path")}1 -> "repo_url"')
    doc.append(f'     {lk("file")}1 -> "config.yml"')
    doc.append(f'     ({lk("sequence")} ({lk("copy")} {lk("path")}1)(p "feature")({lk("read")} {lk("file")}1)({lk("write")} {lk("file")}1 "timeout" 30)({lk("run")} {lk("test")}1))')
    doc.append("```")
    doc.append("")

    # Example 9
    doc.append("### 9.9 Collaboration")
    doc.append("```")
    doc.append('EN:  We need Alice to review the code and Bob to write tests.')
    doc.append('     If both agree, deploy. Otherwise, send me the feedback.')
    doc.append(f'ZQX: u {lk("need")} "Alice" n {lk("check")} {lk("code")}1 m "Bob" n {lk("write")} {lk("test")}')
    doc.append(f'     q {lk("agree")} {lk("then")} ({lk("deploy")}) {lk("otherwise")} ({lk("send")} {lk("result")} n c)')
    doc.append("```")
    doc.append("")

    # Example 10
    doc.append("### 9.10 Temporal")
    doc.append("```")
    doc.append('EN:  The server was always fast before. Now it is slow.')
    doc.append('     I think something changed after the last deploy.')
    doc.append(f'ZQX: "srv" p.k {lk("always")} {lk("fast")} {lk("before")} {lk("now")} x k {lk("slow")}')
    doc.append(f'     c {lk("think")} {lk("something")} p.{lk("change")} {lk("after")} {lk("last")} {lk("deploy")}')
    doc.append("```")
    doc.append("")
    doc.append("---")
    doc.append("")

    # Section 10: BNF
    doc.append("## 10. Grammar Specification (BNF)")
    doc.append("")
    doc.append("```bnf")
    doc.append('<message>      ::= <statement> (" " <statement>)*')
    doc.append("")
    doc.append("<statement>    ::= <operation>")
    doc.append("               |   <frame>")
    doc.append("               |   <binding>")
    doc.append("               |   <expression>")
    doc.append("")
    doc.append('<operation>    ::= "(" <token> (" " <argument>)* ")"')
    doc.append("")
    doc.append('<frame>        ::= "{" <token> (" " <argument>)* "}"')
    doc.append("")
    doc.append("<argument>     ::= <token>")
    doc.append("               |   <operation>")
    doc.append("               |   <frame>")
    doc.append("               |   <literal>")
    doc.append("")
    doc.append('<binding>      ::= <reference> " -> " <bind-value>')
    doc.append("")
    doc.append("<bind-value>   ::= <literal>")
    doc.append("               |   <operation>")
    doc.append("")
    doc.append("<expression>   ::= <token> (\" \" <token>)*")
    doc.append("")
    doc.append("<token>        ::= <prefix>* <word>")
    doc.append("")
    doc.append('<prefix>       ::= "p." | "f." | "!" | "?" | "~"')
    doc.append("")
    doc.append("<word>         ::= <tier1>")
    doc.append("               |   <tier2>")
    doc.append("               |   <tier3>")
    doc.append("               |   <composition>")
    doc.append("               |   <reference>")
    doc.append("")
    doc.append('<composition>  ::= <word> (":" <word>)+')
    doc.append("")
    doc.append("<tier1>        ::= [a-z] | [0-9]")
    doc.append("")
    doc.append("<tier2>        ::= [a-z] [a-z]        /* excluding 54 English words */")
    doc.append("")
    doc.append("<tier3>        ::= <consonant>{3}")
    doc.append("")
    doc.append("<reference>    ::= <word> [0-9]+")
    doc.append("")
    doc.append("<consonant>    ::= [bcdfghjklmnpqrstvwxz]")
    doc.append("")
    doc.append("<literal>      ::= <string> | <number>")
    doc.append("")
    doc.append('<string>       ::= \'"\' [^"]* \'"\'')
    doc.append("")
    doc.append("<number>       ::= [0-9] [0-9]+        /* 2+ digits = literal */")
    doc.append("```")
    doc.append("")
    doc.append("### Reserved Syntax Characters")
    doc.append("")
    doc.append("| Char | Purpose |")
    doc.append("|------|---------|")
    doc.append("| `( )` | Operation delimiters |")
    doc.append("| `{ }` | Intent frame delimiters |")
    doc.append("| `\"` | String literal delimiters |")
    doc.append("| `:` | Composition operator |")
    doc.append("| `~` | Approximate marker prefix |")
    doc.append("| `.` | Tense prefix separator |")
    doc.append("| `!` | Negation prefix |")
    doc.append("| `?` | Question prefix |")
    doc.append("| `->` | Binding operator |")
    doc.append("| ` ` | Token delimiter |")

    return "\n".join(doc)


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    words = build_word_list()
    assignments = assign_codes(words)

    # Stats
    tier1_words = set(TIER1.values())
    unique_words = set()
    for eng, cat in words:
        unique_words.add(eng)
    # Don't count tier-1 words that also appear in word lists
    new_words = unique_words - tier1_words
    total = len(tier1_words) + len(new_words)

    print(f"Tier-1 words: {len(tier1_words)}")
    print(f"Additional words: {len(new_words)}")
    print(f"Total mapped: {total}")
    print(f"Total assignments: {len(assignments)}")

    # Verify no code collisions
    code_to_word = {}
    for eng, (code, tier) in assignments.items():
        if code in code_to_word:
            print(f"COLLISION: {code} -> {eng} AND {code_to_word[code]}")
        code_to_word[code] = eng

    # Verify no tier-2 code is an English word
    for eng, (code, tier) in assignments.items():
        if tier == 2 and code in EXCLUDED_2CHAR:
            print(f"BAD TIER-2: {code} is an English word")

    # Generate document
    document = generate_document(assignments, words)

    # Write to file
    with open('/Users/tgriek/dev/t1m/zqx.md', 'w') as f:
        f.write(document)

    print(f"\nWritten to zqx.md ({len(document)} chars)")


if __name__ == '__main__':
    main()
