import random

wordList = [
    {
        "word": "guitar",
        "hint": "A musical instrument with strings."
    },
    {
        "word": "oxygen",
        "hint": "An element; A colorless, odorless gas essential for life."
    },
    {
        "word": "mountain",
        "hint": "A large natural elevation of the Earth's surface."
    },
    {
        "word": "painting",
        "hint": "An art form using colors on a surface to create images or expression."
    },
    {
        "word": "astronomy",
        "hint": "The scientific study of celestial objects and phenomena."
    },
    {
        "word": "football",
        "hint": "A popular sport played with a spherical ball."
    },
    {
        "word": "chocolate",
        "hint": "A sweet treat made from cocoa beans."
    },
    {
        "word": "butterfly",
        "hint": "An insect with colorful wings and a slender body."
    },
    {
        "word": "history",
        "hint": "The study of past events and human civilization."
    },
    {
        "word": "pizza",
        "hint": "A savory dish consisting of a round, flattened base with toppings."
    },
    {
        "word": "jazz",
        "hint": "A genre of music characterized by improvisation and syncopation."
    },
    {
        "word": "camera",
        "hint": "A device used to capture and record images or videos."
    },
    {
        "word": "diamond",
        "hint": "A precious gemstone known for its brilliance and hardness."
    },
    {
        "word": "adventure",
        "hint": "An exciting or daring experience."
    },
    {
        "word": "science",
        "hint": "The systematic study of the structure and behavior of the physical and natural world."
    },
    {
        "word": "bicycle",
        "hint": "A human-powered vehicle with two wheels."
    },
    {
        "word": "sunset",
        "hint": "The daily disappearance of the sun below the horizon."
    },
    {
        "word": "coffee",
        "hint": "A popular caffeinated beverage made from roasted coffee beans."
    },
    {
        "word": "dance",
        "hint": "A rhythmic movement of the body often performed to music."
    },
    {
        "word": "galaxy",
        "hint": "A vast system of stars, gas, and dust held together by gravity."
    },
    {
        "word": "orchestra",
        "hint": "A large ensemble of musicians playing various instruments."
    },
    {
        "word": "volcano",
        "hint": "A mountain or hill with a vent through which lava, rock fragments, hot vapor, and gas are ejected."
    },
    {
        "word": "novel",
        "hint": "A long work of fiction, typically with a complex plot and characters."
    },
    {
        "word": "sculpture",
        "hint": "A three-dimensional art form created by shaping or combining materials."
    },
    {
        "word": "symphony",
        "hint": "A long musical composition for a full orchestra, typically in multiple movements."
    },
    {
        "word": "architecture",
        "hint": "The art and science of designing and constructing buildings."
    },
    {
        "word": "ballet",
        "hint": "A classical dance form characterized by precise and graceful movements."
    },
    {
        "word": "astronaut",
        "hint": "A person trained to travel and work in space."
    },
    {
        "word": "waterfall",
        "hint": "A cascade of water falling from a height."
    },
    {
        "word": "technology",
        "hint": "The application of scientific knowledge for practical purposes."
    },
    {
        "word": "rainbow",
        "hint": "A meteorological phenomenon that is caused by reflection, refraction, and dispersion of light."
    },
    {
        "word": "universe",
        "hint": "All existing matter, space, and time as a whole."
    },
    {
        "word": "piano",
        "hint": "A musical instrument played by pressing keys that cause hammers to strike strings."
    },
    {
        "word": "vacation",
        "hint": "A period of time devoted to pleasure, rest, or relaxation."
    },
    {
        "word": "rainforest",
        "hint": "A dense forest characterized by high rainfall and biodiversity."
    },
    {
        "word": "theater",
        "hint": "A building or outdoor area in which plays, movies, or other performances are staged."
    },
    {
        "word": "telephone",
        "hint": "A device used to transmit sound over long distances."
    },
    {
        "word": "language",
        "hint": "A system of communication consisting of words, gestures, and syntax."
    },
    {
        "word": "desert",
        "hint": "A barren or arid land with little or no precipitation."
    },
    {
        "word": "sunflower",
        "hint": "A tall plant with a large yellow flower head."
    },
    {
        "word": "fantasy",
        "hint": "A genre of imaginative fiction involving magic and supernatural elements."
    },
    {
        "word": "telescope",
        "hint": "An optical instrument used to view distant objects in space."
    },
    {
        "word": "breeze",
        "hint": "A gentle wind."
    },
    {
        "word": "oasis",
        "hint": "A fertile spot in a desert where water is found."
    },
    {
        "word": "photography",
        "hint": "The art, process, or practice of creating images by recording light or other electromagnetic radiation."
    },
    {
        "word": "safari",
        "hint": "An expedition or journey, typically to observe wildlife in their natural habitat."
    },
    {
        "word": "planet",
        "hint": "A celestial body that orbits a star and does not produce light of its own."
    },
    {
        "word": "river",
        "hint": "A large natural stream of water flowing in a channel to the sea, a lake, or another such stream."
    },
    {
        "word": "tropical",
        "hint": "Relating to or situated in the region between the Tropic of Cancer and the Tropic of Capricorn."
    },
    {
        "word": "mysterious",
        "hint": "Difficult or impossible to understand, explain, or identify."
    },
    {
        "word": "enigma",
        "hint": "Something that is mysterious, puzzling, or difficult to understand."
    },
    {
        "word": "paradox",
        "hint": "A statement or situation that contradicts itself or defies intuition."
    },
    {
        "word": "puzzle",
        "hint": "A game, toy, or problem designed to test ingenuity or knowledge."
    },
    {
        "word": "whisper",
        "hint": "To speak very softly or quietly, often in a secretive manner."
    },
    {
        "word": "shadow",
        "hint": "A dark area or shape produced by an object blocking the light."
    },
    {
        "word": "secret",
        "hint": "Something kept hidden or unknown to others."
    },
    {
        "word": "curiosity",
        "hint": "A strong desire to know or learn something."
    },
    {
        "word": "unpredictable",
        "hint": "Not able to be foreseen or known beforehand; uncertain."
    },
    {
        "word": "obfuscate",
        "hint": "To confuse or bewilder someone; to make something unclear or difficult to understand."
    },
    {
        "word": "unveil",
        "hint": "To make known or reveal something previously secret or unknown."
    },
    {
        "word": "illusion",
        "hint": "A false perception or belief; a deceptive appearance or impression."
    },
    {
        "word": "moonlight",
        "hint": "The light from the moon."
    },
    {
        "word": "vibrant",
        "hint": "Full of energy, brightness, and life."
    },
    {
        "word": "nostalgia",
        "hint": "A sentimental longing or wistful affection for the past."
    },
    {
        "word": "brilliant",
        "hint": "Exceptionally clever, talented, or impressive."
    },
    {
        "word": "fireworks",
        "hint": "Explosive devices producing colored lights and loud noises, often used in celebrations."
    },
    {
        "word": "harmony",
        "hint": "A pleasing arrangement or combination of different elements."
    },
    {
        "word": "island",
        "hint": "A landmass surrounded by water, smaller than a continent."
    },
    {
        "word": "carousel",
        "hint": "A rotating device with seats or animals for amusement at fairs and carnivals."
    },
    {
        "word": "serendipity",
        "hint": "The occurrence and development of events by chance in a happy or beneficial way."
    },
    {
        "word": "silhouette",
        "hint": "The dark shape and outline of someone or something visible against a lighter background."
    },
    {
        "word": "quasar",
        "hint": "An extremely luminous and energetic active galactic nucleus, powered by a supermassive black hole."
    },
    {
        "word": "mystical",
        "hint": "Relating to or resulting from a direct, personal, and immediate experience of ultimate reality."
    },
    {
        "word": "surreal",
        "hint": "Having the disorienting, hallucinatory quality of a dream; unreal; fantastic."
    },
    {
        "word": "ethereal",
        "hint": "Extremely delicate and light in a way that seems too perfect for this world."
    },
    {
        "word": "quicksilver",
        "hint": "Mercury in liquid form; something that moves or changes very quickly."
    },
    {
        "word": "whimsical",
        "hint": "Playfully quaint or fanciful, especially in an appealing and amusing way."
    },
    {
        "word": "effervescent",
        "hint": "Bubbly, lively, and enthusiastic."
    },
    {
        "word": "labyrinth",
        "hint": "A complex and confusing arrangement of passages or paths, typically designed as a puzzle."
    },
    {
        "word": "phoenix",
        "hint": "A mythical bird that is said to be cyclically regenerated or reborn from its ashes."
    },
    {
        "word": "cascade",
        "hint": "A small waterfall, typically one of several that fall in stages down a steep rocky slope."
    },
    {
        "word": "serenade",
        "hint": "A piece of music sung or played in the open air, typically by a man at night under the window of his beloved."
    },
    {
        "word": "effulgent",
        "hint": "Shining brightly; radiant."
    },
    {
        "word": "tranquil",
        "hint": "Free from disturbance; calm."
    },
    {
        "word": "luminescent",
        "hint": "Emitting light not caused by heat; exhibiting luminescence."
    },
    {
        "word": "whirlwind",
        "hint": "A column of air moving rapidly around and around in a cylindrical or funnel shape."
    },
    {
        "word": "ephemeral",
        "hint": "Lasting for a very short time; transient."
    },
    {
        "word": "verdant",
        "hint": "Green with grass or other rich vegetation."
    },
    {
        "word": "quixotic",
        "hint": "Exceedingly idealistic; unrealistic and impractical."
    },
    {
        "word": "sonorous",
        "hint": "Capable of producing a deep, rich sound."
    },
    {
        "word": "effervescence",
        "hint": "The rapid escape of a gas from a liquid in which it is dissolved, creating bubbles."
    },
    {
        "word": "petrichor",
        "hint": "The pleasant, earthy scent produced when rain falls on dry soil."
    },
    {
        "word": "languorous",
        "hint": "Lacking energy or vitality; sluggish."
    },
    {
        "word": "susurrus",
        "hint": "Whispering, murmuring, or rustling."
    },
    {
        "word": "oblivion",
        "hint": "The state of being completely forgotten or unknown."
    },
    {
        "word": "ephemeral",
        "hint": "Lasting for a very short time; transient."
    },
    {
        "word": "idyllic",
        "hint": "Extremely happy, peaceful, or picturesque."
    },
    {
        "word": "quintessence",
        "hint": "The most perfect or typical example of a quality or class."
    },
    {
        "word": "sibilant",
        "hint": "Making or characterized by a hissing sound."
    },
    {
        "word": "effulgence",
        "hint": "Shining brightly; radiant."
    },
    {
        "word": "nebulous",
        "hint": "In the form of a cloud or haze; hazy."
    },
    {
        "word": "crepuscular",
        "hint": "Relating to or resembling twilight; occurring or active in the evening."
    },
    {
        "word": "labyrinthine",
        "hint": "Complicated and confusing, like a labyrinth."
    },
    {
        "word": "ineffable",
        "hint": "Too great or extreme to be expressed or described in words."
    },
    {
        "word": "susurrant",
        "hint": "Whispering, murmuring, or rustling."
    },
    {
        "word": "ephemeral",
        "hint": "Lasting for a very short time; transient."
    },
    {
        "word": "luminescence",
        "hint": "Emission of light not caused by heat; the property of being luminous."
    },
    {
        "word": "resplendent",
        "hint": "Shining brilliantly; radiant."
    },
    {
        "word": "cynosure",
        "hint": "A person or thing that is the center of attention or admiration."
    },
    {
        "word": "gossamer",
        "hint": "A fine, filmy substance consisting of cobwebs spun by small spiders."
    },
    {
        "word": "soporific",
        "hint": "Tending to induce drowsiness or sleep."
    },
    {
        "word": "scintillating",
        "hint": "Brilliantly and excitingly clever or skillful."
    },
    {
        "word": "cat",
        "hint": "A small domesticated carnivorous mammal."
    },
    {
        "word": "tree",
        "hint": "A woody perennial plant with a single main stem or trunk."
    },
    {
        "word": "house",
        "hint": "A building for human habitation, typically one that is lived in by a family or small group of people."
    },
    {
        "word": "sun",
        "hint": "The star around which the Earth orbits, providing light and heat."
    },
    {
        "word": "book",
        "hint": "A written or printed work consisting of pages glued or sewn together along one side and bound in covers."
    },
    {
        "word": "rain",
        "hint": "Water falling in drops condensed from vapor in the atmosphere."
    },
    {
        "word": "dog",
        "hint": "A domesticated carnivorous mammal, typically loyal and often kept as a pet or for work."
    },
    {
        "word": "flower",
        "hint": "The seed-bearing part of a plant, often colorful and fragrant."
    },
    {
        "word": "red",
        "hint": "The color of blood or a ripe tomato, opposite of green in the color spectrum."
    },
    {
        "word": "car",
        "hint": "A road vehicle, typically with four wheels, powered by an internal combustion engine."
    },
    {
        "word": "bird",
        "hint": "A warm-blooded egg-laying vertebrate, typically with feathers, wings, and a beak."
    },
    {
        "word": "moon",
        "hint": "The natural satellite of the Earth, visible by reflected sunlight at night."
    },
    {
        "word": "fish",
        "hint": "A limbless cold-blooded vertebrate animal with gills and fins, living wholly in water."
    },
    {
        "word": "happy",
        "hint": "Feeling or showing pleasure or contentment."
    },
    {
        "word": "apple",
        "hint": "A round fruit with red or green skin and a crisp white interior."
    },
    {
        "word": "run",
        "hint": "Move at a speed faster than a walk, never having both or all the feet on the ground at the same time."
    },
    {
        "word": "hat",
        "hint": "A covering for the head, typically with a brim and a crown."
    },
    {
        "word": "jump",
        "hint": "Push oneself off a surface and into the air by using the muscles in one's legs and feet."
    },
    {
        "word": "fire",
        "hint": "Combustion or burning, in which substances combine chemically with oxygen from the air."
    },
    {
        "word": "game",
        "hint": "A form of play or sport, especially a competitive one played according to rules and decided by skill, strength, or luck."
    },
    {
        "word": "road",
        "hint": "A wide way leading from one place to another, typically one with a specially prepared surface that vehicles can use."
    },
    {
        "word": "sleep",
        "hint": "A condition of body and mind that typically recurs for several hours every night, in which the nervous system is inactive, the eyes are closed, and consciousness is practically suspended."
    },
    {
        "word": "time",
        "hint": "The indefinite continued progress of existence and events in the past, present, and future."
    },
    {
        "word": "play",
        "hint": "Engage in activity for enjoyment and recreation rather than a serious or practical purpose."
    },
    {
        "word": "baby",
        "hint": "A very young child, especially one newly or recently born."
    },
    {
        "word": "color",
        "hint": "The property possessed by an object of producing different sensations on the eye as a result of the way the object reflects or emits light."
    },
    {
        "word": "loud",
        "hint": "Producing or capable of producing much noise; easily audible."
    },
    {
        "word": "cold",
        "hint": "Of or at a low or relatively low temperature, especially when compared with the human body."
    },
    {
        "word": "soft",
        "hint": "Easy to mold, cut, compress, or fold; not hard or firm to the touch."
    },
    {
        "word": "small",
        "hint": "Of a size that is less than normal or usual."
    },
    {
        "word": "friend",
        "hint": "A person with whom one has a bond of mutual affection, typically one exclusive of sexual or family relations."
    },
    {
        "word": "work",
        "hint": "Activity involving mental or physical effort done to achieve a purpose or result."
    },
    {
        "word": "city",
        "hint": "A large human settlement, typically larger than a town, with a substantial infrastructure."
    },
    {
        "word": "music",
        "hint": "Vocal or instrumental sounds (or both) combined in such a way as to produce beauty of form, harmony, and expression of emotion."
    },
    {
        "word": "beauty",
        "hint": "A combination of qualities, such as shape, color, or form, that pleases the aesthetic senses."
    },
    {
        "word": "food",
        "hint": "Any nutritious substance that people or animals eat or drink to maintain life and growth."
    },
    {
        "word": "travel",
        "hint": "Make a journey, typically of some length or abroad."
    },
    {
        "word": "learn",
        "hint": "Gain or acquire knowledge of or skill in (something) by study, experience, or being taught."
    },
    {
        "word": "family",
        "hint": "A group consisting of parents and children living together in a household."
    },
    {
        "word": "home",
        "hint": "The place where one lives permanently, especially as a member of a family or household."
    },
    {
        "word": "computer",
        "hint": "An electronic device for storing and processing data, typically in binary form, according to instructions given to it in a variable program."
    },
    {
        "word": "school",
        "hint": "An institution for educating children or students."
    },
    {
        "word": "health",
        "hint": "The state of being free from illness or injury."
    },
    {
        "word": "nature",
        "hint": "The phenomena of the physical world collectively, including plants, animals, the landscape, and other features and products of the earth."
    },
    {
        "word": "dream",
        "hint": "A series of thoughts, images, and sensations occurring in a person's mind during sleep."
    },
    {
        "word": "smile",
        "hint": "Form one's features into a pleased, kind, or amused expression, typically with the corners of the mouth turned up and the front teeth exposed."
    },
    {
        "word": "laugh",
        "hint": "Make the spontaneous sounds and movements of the face and body that are the instinctive expressions of lively amusement and sometimes also of contempt or derision."
    },
    {
        "word": "friendship",
        "hint": "The emotions or conduct of friends; the state of being friends."
    },
    {
        "word": "happiness",
        "hint": "The state of being happy."
    },
    {
        "word": "technology",
        "hint": "The application of scientific knowledge for practical purposes, especially in industry."
    },
    {
        "word": "business",
        "hint": "The practice of making one's living by engaging in commerce."
    },
    {
        "word": "language",
        "hint": "The method of human communication, either spoken or written, consisting of the use of words in a structured and conventional way."
    },
    {
        "word": "culture",
        "hint": "The arts and other manifestations of human intellectual achievement regarded collectively."
    },
    {
        "word": "celebrate",
        "hint": "Acknowledge (a significant or happy day or event) with a social gathering or enjoyable activity."
    },
    {
        "word": "exercise",
        "hint": "Activity requiring physical effort, carried out to sustain or improve health and fitness."
    },
    {
        "word": "knowledge",
        "hint": "Facts, information, and skills acquired through experience or education."
    },
    {
        "word": "journey",
        "hint": "An act of traveling from one place to another."
    },
    {
        "word": "culture",
        "hint": "The ideas, customs, and social behavior of a particular people or society."
    },
    {
        "word": "celebrate",
        "hint": "Acknowledge (a significant or happy day or event) with a social gathering or enjoyable activity."
    },
    {
        "word": "exercise",
        "hint": "Activity requiring physical effort, carried out to sustain or improve health and fitness."
    },
    {
        "word": "knowledge",
        "hint": "Facts, information, and skills acquired through experience or education."
    },
    {
        "word": "journey",
        "hint": "An act of traveling from one place to another."
    },
]