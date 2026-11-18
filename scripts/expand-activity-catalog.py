import json
from pathlib import Path

catalog_path = Path(__file__).resolve().parents[1] / "content" / "activities.json"
catalog = json.loads(catalog_path.read_text(encoding="utf-8"))

names = ["Mia", "Noah", "Asha", "Leo", "Nina", "Arun", "Lily", "Sam"]
story_templates = [
    ("{name} plants sunflower seeds.\nThey water them each morning.\nSoon, bright yellow flowers grow.", "🌱🌻", ["🌱🌻", "🚂🛤️", "🥪🍎"]),
    ("{name} folds a paper boat.\nThey float it in a bowl of water.\nThe little boat sails across.", "🛶💧", ["🛶💧", "🎈🎁", "🐈🧶"]),
    ("{name} packs lunch for a picnic.\nThey put fruit in a basket.\nThey eat under a shady tree.", "🧺🍎🌳", ["🧺🍎🌳", "🛏️📘🌙", "🚗🛞🛣️"]),
    ("{name} hears a soft sound outside.\nA little bird is near the window.\nThey put water in a small dish.", "🐦🪟", ["🐦🪟", "🐟🪸", "⚽🥅"]),
    ("{name} gathers leaves after the rain.\nThey make a picture with the leaves.\nA butterfly lands nearby.", "🍂🦋", ["🍂🦋", "🍦🥄", "🚲🪖"]),
    ("{name} builds a tall block tower.\nIt wobbles but does not fall.\nThey add one more block.", "🧱🏗️", ["🧱🏗️", "🧁🍓", "🐠🫧"]),
    ("{name} sees dark clouds in the sky.\nThey take an umbrella for the walk.\nThe rain starts on the way home.", "☂️🌧️", ["☂️🌧️", "☀️🏖️", "🎂🕯️"]),
    ("{name} visits a farm with a grown-up.\nThey feed hay to a horse.\nThe horse gives a gentle nicker.", "🐴🌾", ["🐴🌾", "🐙🪸", "🦉🌙"]),
    ("{name} finds a smooth shell on the beach.\nThey listen to the waves.\nThey place the shell in a bucket.", "🐚🏖️", ["🐚🏖️", "📚🏫", "🍎🥧"]),
    ("{name} reads a book about space.\nThey learn about the moon and stars.\nThey draw a rocket in a notebook.", "🚀🌙", ["🚀🌙", "🐸🪵", "🧺🍞"]),
]

reading = catalog["readingStories"]
seen_story_text = {item["sentence"] for item in reading}
next_story = len(reading) + 1
for template, answer, choices in story_templates:
    for name in names:
        sentence = template.format(name=name)
        if sentence in seen_story_text:
            continue
        reading.append({"id": f"read-{next_story:03d}", "sentence": sentence, "answer": answer, "choices": choices})
        seen_story_text.add(sentence)
        next_story += 1
        if len(reading) >= 100:
            break
    if len(reading) >= 100:
        break

tamil = catalog["tamilCards"]
tamil_additions = []
objects = [
    ("புத்தகம்", "book"), ("பென்சில்", "pencil"), ("பந்து", "ball"), ("மரம்", "tree"),
    ("வீடு", "house"), ("நாற்காலி", "chair"), ("மேசை", "table"), ("குடை", "umbrella"),
    ("கார்", "car"), ("பூ", "flower"), ("கடிகாரம்", "clock"), ("கோப்பை", "cup"),
    ("பை", "bag"), ("மிதிவண்டி", "bicycle"), ("படம்", "picture"), ("ஆப்பிள்", "apple"),
    ("மாம்பழம்", "mango"), ("யானை", "elephant"), ("மீன்", "fish"), ("பறவை", "bird"),
]
tamil_additions.extend((f"இது ஒரு {word}.", f"This is a {meaning}.") for word, meaning in objects)

foods = [
    ("மாம்பழம்", "mango"), ("ஆப்பிள்", "apple"), ("வாழைப்பழம்", "banana"), ("இட்லி", "idli"),
    ("தோசை", "dosa"), ("சாதம்", "rice"), ("கேரட்", "carrot"), ("ரொட்டி", "bread"),
    ("பிஸ்கட்", "biscuit"), ("ஆரஞ்சு", "orange"), ("திராட்சை", "grapes"), ("தர்பூசணி", "watermelon"),
    ("தயிர்", "yogurt"), ("நூடுல்ஸ்", "noodles"), ("உருளைக்கிழங்கு", "potato"), ("சப்பாத்தி", "chapati"),
    ("பலாப்பழம்", "jackfruit"), ("கொய்யாப்பழம்", "guava"), ("முந்திரி", "cashew nuts"), ("பேரிக்காய்", "pear"),
]
tamil_additions.extend((f"எனக்கு {word} பிடிக்கும்.", f"I like {meaning}.") for word, meaning in foods)

actions = [
    ("புத்தகம் படிக்கிறேன்", "I am reading a book"), ("படம் வரைகிறேன்", "I am drawing a picture"),
    ("பாட்டு பாடுகிறேன்", "I am singing a song"), ("பந்து விளையாடுகிறேன்", "I am playing with a ball"),
    ("தண்ணீர் குடிக்கிறேன்", "I am drinking water"), ("மாம்பழம் சாப்பிடுகிறேன்", "I am eating a mango"),
    ("பள்ளிக்குச் செல்கிறேன்", "I am going to school"), ("வேகமாக ஓடுகிறேன்", "I am running fast"),
    ("மலர்களைப் பார்க்கிறேன்", "I am looking at the flowers"), ("கதையைப் படிக்கிறேன்", "I am reading a story"),
    ("படம் பார்க்கிறேன்", "I am watching a picture"), ("நண்பருடன் விளையாடுகிறேன்", "I am playing with a friend"),
    ("பூனைக்கு உணவு தருகிறேன்", "I am feeding the cat"), ("பென்சிலால் எழுதுகிறேன்", "I am writing with a pencil"),
    ("கதவைத் திறக்கிறேன்", "I am opening the door"), ("கைகளைக் கழுவுகிறேன்", "I am washing my hands"),
    ("சிரிக்கிறேன்", "I am smiling"), ("குதிக்கிறேன்", "I am jumping"),
    ("மெதுவாக நடக்கிறேன்", "I am walking slowly"), ("பாடம் கேட்கிறேன்", "I am listening to a lesson"),
]
tamil_additions.extend((f"நான் {action}.", f"{meaning}.") for action, meaning in actions)

other_sentences = [
    ("நாய் குரைக்கிறது.", "The dog is barking."), ("பூனை தூங்குகிறது.", "The cat is sleeping."),
    ("மீன் நீந்துகிறது.", "The fish is swimming."), ("குதிரை ஓடுகிறது.", "The horse is running."),
    ("பறவை பாடுகிறது.", "The bird is singing."), ("யானை தண்ணீர் குடிக்கிறது.", "The elephant is drinking water."),
    ("ஆடு புல் சாப்பிடுகிறது.", "The goat is eating grass."), ("முயல் கேரட் சாப்பிடுகிறது.", "The rabbit is eating a carrot."),
    ("வாத்து நீரில் நீந்துகிறது.", "The duck is swimming in the water."), ("குரங்கு மரத்தில் ஏறுகிறது.", "The monkey is climbing the tree."),
    ("மழை பெய்கிறது.", "It is raining."), ("சூரியன் ஒளி தருகிறது.", "The sun gives light."),
    ("நிலா இரவில் தெரிகிறது.", "The moon can be seen at night."), ("பூ மலர்கிறது.", "The flower is blooming."),
    ("இலை பச்சையாக இருக்கிறது.", "The leaf is green."), ("காற்று மெதுவாக வீசுகிறது.", "The wind is blowing softly."),
    ("மேகம் வானில் மிதக்கிறது.", "The cloud is floating in the sky."), ("நட்சத்திரம் இரவில் மின்னுகிறது.", "The star is shining at night."),
    ("நதி கடலை நோக்கிப் பாய்கிறது.", "The river flows toward the sea."), ("தேனீ பூவின் அருகில் பறக்கிறது.", "The bee is flying near the flower."),
]
tamil_additions.extend(other_sentences)

known_tamil = {item["text"] for item in tamil}
next_tamil = len(tamil) + 1
for text, meaning in tamil_additions:
    if text in known_tamil:
        continue
    tamil.append({"id": f"tamil-{next_tamil:03d}", "text": text, "meaning": meaning})
    known_tamil.add(text)
    next_tamil += 1
    if len(tamil) >= 100:
        break

# Add a second short sentence pattern if some familiar words overlapped the
# existing starter cards, while keeping every card distinct.
for word, meaning in objects + foods:
    text = f"இது பெரிய {word}."
    if text in known_tamil:
        continue
    tamil.append({"id": f"tamil-{next_tamil:03d}", "text": text, "meaning": f"This is a big {meaning}."})
    known_tamil.add(text)
    next_tamil += 1
    if len(tamil) >= 100:
        break

spelling_additions = [
    ("mountain", "🏔️"), ("volcano", "🌋"), ("library", "📚"), ("breakfast", "🍳"),
    ("computer", "💻"), ("crocodile", "🐊"), ("octopus", "🐙"), ("penguin", "🐧"),
    ("hamster", "🐹"), ("flamingo", "🦩"), ("peppermint", "🍬"), ("envelope", "✉️"),
    ("bicycle", "🚲"), ("submarine", "🚤"), ("helicopter", "🚁"), ("lighthouse", "🗼"),
    ("spaceship", "🛸"), ("starfish", "⭐"), ("seashell", "🐚"), ("waterfall", "🏞️"),
    ("popcorn", "🍿"), ("pancake", "🥞"), ("mailbox", "📫"), ("baseball", "⚾"),
    ("basketball", "🏀"), ("cricket", "🏏"), ("swimming", "🏊"), ("running", "🏃"),
    ("whisper", "🤫"), ("feather", "🪶"), ("trumpet", "🎺"), ("giraffe", "🦒"),
    ("zookeeper", "🧑‍🌾"), ("colourful", "🎨"), ("favourite", "⭐"), ("tomorrow", "🌅"),
    ("remember", "🧠"), ("carefully", "🫳"), ("different", "🧩"), ("wonderful", "🌟"),
    ("discover", "🔎"), ("important", "❗"), ("practice", "✍️"), ("lollipop", "🍭"),
    ("pajamas", "🛌"), ("suitcase", "🧳"), ("necklace", "📿"), ("treetop", "🌳"),
    ("puddle", "💧"), ("pocket", "👖"), ("summer", "🏖️"), ("winter", "❄️"),
    ("autumn", "🍁"), ("springtime", "🌷"), ("Saturday", "📅"), ("cousin", "🧒"),
    ("grandma", "👵"), ("grandpa", "👴"), ("storybook", "📖"), ("classroom", "🏫"),
]
known_words = {item["word"] for item in catalog["spellingWords"]}
next_word = len(catalog["spellingWords"]) + 1
for word, picture in spelling_additions:
    if word in known_words:
        continue
    catalog["spellingWords"].append({"id": f"spell-{next_word:03d}", "word": word, "picture": picture})
    known_words.add(word)
    next_word += 1

if not all(len(catalog[key]) >= 100 for key in ("readingStories", "tamilCards", "spellingWords")):
    raise ValueError("The activity catalog must have at least 100 items per collection")

catalog["version"] = int(catalog.get("version", 0)) + 1
catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Catalog ready: {len(reading)} stories, {len(tamil)} Tamil cards, {len(catalog['spellingWords'])} spelling words")
