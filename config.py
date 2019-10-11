import wikipedia
import requests
import random
from constant import LISTE_CORS_GOOGLE, LISTE_MOT_CLES_NON_TROUVE, LISTE_SORS_WIKI


# Function that searches for a keyword in the list mot_cla_chaine and return it
def touver_place(chaine):
    mot_cle_chaine = ['place', 'adresse', 'endroit', 'lieu']

    for i in range(len(chaine) - 1):
        if chaine[i] in mot_cle_chaine:
            return chaine[i + 1]


# a function that looks for the location of an address and return it
def search(place):
    reponse_question = {}
    KEY_API = 'AIzaSyBh_Oj3Rj_gosxQUQxEzeYE95DbixLTZ8g'
    api_search = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
    payload = {
        'input': place,
        'inputtype': 'textquery',
        'fields': 'photos,formatted_address,name,rating,opening_hours,geometry',
        'key': KEY_API,
    }
    Json_data = requests.get(api_search, params=payload).json()

    try:
        Json_data['candidates'][0]['name']
    except(IndexError):
        reponse_question['texte'] = random.choice(LISTE_MOT_CLES_NON_TROUVE)  # Cas Corp pas de mot cle trouver
        print('Aucun corespondance au mot cle')
        return reponse_question
    nom = Json_data['candidates'][0]['name']
    adresse = Json_data['candidates'][0]['formatted_address']
    photo = Json_data['candidates'][0]['geometry']['location']
    print(photo)
    reponse_question['nom'] = nom
    reponse_question['adresse'] = adresse
    reponse_question['photo'] = photo
    # to do // ajouter lien et pour le frame 

    """ Wikipedia API recive addresse element from dic ( reponse_question) and return all data (dic { 'nom', 'adresse',
        'text'}) 
    """

    wikipedia.set_lang("fr")
    try:
        reponse_question['texte'] = wikipedia.summary((lambda s: s.split(",")[0])(adresse), sentences=2)
    except:
        reponse_question['texte'] = random.choice(LISTE_SORS_WIKI)   # Cas Corp pas de mot cle trouve
        return reponse_question
    return reponse_question

# function that cuts a sentence into several words and eliminates unnecessary words and return list
def chaine_formated(chaine):
    chaine = chaine.replace("'", " ")
    chaine = chaine.split(' ')
    chaine1 = ["a", "abord", "absolument", "afin", "ah", "ai", "aie", "ailleurs", "ainsi", "ait", "allaient",
               "allo", "allons", "allô", "alors", "anterieur", "anterieure", "anterieures", "apres", "après",
               "as", "assez", "attendu", "au", "aucun", "aucune", "aujourd", "aujourd'hui", "aupres", "auquel",
               "aura", "auraient", "aurait", "auront", "aussi", "autre", "autrefois", "autrement", "autres",
               "autrui", "aux", "auxquelles", "auxquels", "avaient", "avais", "avait", "avant", "avec", "avoir",
               "avons", "ayant", "b", "bah", "bas", "basee", "bat", "beau", "beaucoup", "bien", "bigre", "boum",
               "bravo", "brrr", "c", "car", "ce", "ceci", "cela", "celle", "celle-ci", "celle-là", "celles",
               "celles-ci",
               "celles-là", "celui", "celui-ci", "celui-là", "cent", "cependant", "certain", "certaine", "certaines",
               "certains", "certes", "ces", "cet", "cette", "ceux", "ceux-ci", "ceux-là", "chacun", "chacune", "chaque",
               "cher", "chers", "chez", "chiche", "chut", "chère", "chères", "ci", "cinq", "cinquantaine", "cinquante",
               "cinquantième", "cinquième", "clac", "clic", "combien", "comme", "comment", "comparable", "comparables",
               "compris", "concernant", "contre", "couic", "crac", "d", "da", "dans", "de", "debout", "dedans",
               "dehors",
               "deja", "delà", "depuis", "dernier", "derniere", "derriere", "derrière", "des", "desormais",
               "desquelles",
               "desquels", "dessous", "dessus", "deux", "deuxième", "deuxièmement", "devant", "devers", "devra",
               "different",
               "differentes", "differents", "différent", "différente", "différentes", "différents", "dire", "directe",
               "directement", "dit", "dite", "dits", "divers", "diverse", "diverses", "dix", "dix-huit", "dix-neuf",
               "dix-sept",
               "dixième", "doit", "doivent", "donc", "dont", "douze", "douzième", "dring", "du", "duquel", "durant",
               "dès",
               "désormais", "e", "effet", "egale", "egalement", "egales", "eh", "elle", "elle-même", "elles",
               "elles-mêmes",
               "en", "encore", "enfin", "entre", "envers", "environ", "es", "est", "et", "etant", "etc", "etre", "eu",
               "euh", "eux",
               "eux-mêmes", "exactement", "excepté", "extenso", "exterieur", "f", "fais", "faisaient", "faisant",
               "fait",
               "façon", "feront", "fi", "flac", "floc", "font", "g", "gens", "h", "ha", "hein", "hem", "hep", "hi",
               "ho", "holà",
               "hop", "hormis", "hors", "hou", "houp", "hue", "hui", "huit", "huitième", "hum", "hurrah", "hé", "hélas",
               "i", "il",
               "ils", "importe", "j", "je", "jusqu", "jusque", "juste", "k", "l", "la", "laisser", "laquelle", "las",
               "le",
               "lequel", "les", "lesquelles", "lesquels", "leur", "leurs", "longtemps", "lors", "lorsque", "lui",
               "lui-meme",
               "lui-même", "là", "lès", "m", "ma", "maint", "maintenant", "mais", "malgre", "malgré", "maximale", "me",
               "meme",
               "memes", "merci", "mes", "mien", "mienne", "miennes", "miens", "mille", "mince", "minimale", "moi",
               "moi-meme",
               "moi-même", "moindres", "moins", "mon", "moyennant", "multiple", "multiples", "même", "mêmes", "n", "na",
               "naturel", "naturelle", "naturelles", "ne", "neanmoins", "necessaire", "necessairement", "neuf",
               "neuvième",
               "ni", "nombreuses", "nombreux", "non", "nos", "notamment", "notre", "nous", "nous-mêmes", "nouveau",
               "nul",
               "néanmoins", "nôtre", "nôtres", "o", "oh", "ohé", "ollé", "olé", "on", "ont", "onze", "onzième", "ore",
               "ou",
               "ouf", "ouias", "oust", "ouste", "outre", "ouvert", "ouverte", "ouverts", "o|", "où", "p", "paf", "pan",
               "par",
               "parce", "parfois", "parle", "parlent", "parler", "parmi", "parseme", "partant", "particulier",
               "particulière",
               "particulièrement", "pas", "passé", "pendant", "pense", "permet", "personne", "peu", "peut", "peuvent",
               "peux",
               "pff", "pfft", "pfut", "pif", "pire", "plein", "plouf", "plus", "plusieurs", "plutôt", "possessif",
               "possessifs",
               "possible", "possibles", "pouah", "pour", "pourquoi", "pourrais", "pourrait", "pouvait", "prealable",
               "precisement", "premier", "première", "premièrement", "pres", "probable", "probante", "procedant",
               "proche",
               "près", "psitt", "pu", "puis", "puisque", "pur", "pure", "q", "qu", "quand", "quant", "quant-à-soi",
               "quanta",
               "quarante", "quatorze", "quatre", "quatre-vingt", "quatrième", "quatrièmement", "que", "quel",
               "quelconque",
               "quelle", "quelles", "quelqu'un", "quelque", "quelques", "quels", "qui", "quiconque", "quinze", "quoi",
               "quoique", "r", "rare", "rarement", "rares", "relative", "relativement", "remarquable", "rend", "rendre",
               "restant", "reste", "restent", "restrictif", "retour", "revoici", "revoilà", "rien", "s", "sa",
               "sacrebleu",
               "sait", "sans", "sapristi", "sauf", "se", "sein", "seize", "selon", "semblable", "semblaient", "semble",
               "semblent", "sent", "sept", "septième", "sera", "seraient", "serait", "seront", "ses", "seul", "seule",
               "seulement", "si", "sien", "sienne", "siennes", "siens", "sinon", "six", "sixième", "soi", "soi-même",
               "soit", "soixante", "son", "sont", "sous", "souvent", "specifique", "specifiques", "speculatif", "stop",
               "strictement", "subtiles", "suffisant", "suffisante", "suffit", "suis", "suit", "suivant", "suivante",
               "suivantes", "suivants", "suivre", "superpose", "sur", "surtout", "t", "ta", "tac", "tant", "tardive",
               "te",
               "tel", "telle", "tellement", "telles", "tels", "tenant", "tend", "tenir", "tente", "tes", "tic", "tien",
               "tienne",
               "tiennes", "tiens", "toc", "toi", "toi-même", "ton", "touchant", "toujours", "tous", "tout", "toute",
               "toutefois", "toutes", "treize", "trente", "tres", "trois", "troisième", "troisièmement", "trop", "très",
               "tsoin", "tsouin", "tu", "té", "u", "un", "une", "unes", "uniformement", "unique", "uniques", "uns", "v",
               "va",
               "vais", "vas", "vers", "via", "vif", "vifs", "vingt", "vivat", "vive", "vives", "vlan", "voici", "voilà",
               "vont",
               "vos", "votre", "vous", "vous-mêmes", "vu", "vé", "vôtre", "vôtres", "w", "x", "y", "z", "zut", "à", "â",
               "ça", "ès",
               "étaient", "étais", "était", "étant", "été", "être", "ô", "?", "le", "de", 'li', 'Salut', 'papy', '!',
               'Est-ce',
               'la', 'de', 'l', 'le']

    for ele in chaine1:
        if ele in chaine:
            chaine.remove(ele)
    return search(touver_place(chaine))

print(chaine_formated("tu peut me dire  L'adresse minister des finances"))


