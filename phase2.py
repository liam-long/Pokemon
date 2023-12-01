import streamlit as st
import requests
import pandas as pd

def get_pokemon_info(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    r = requests.get(url)
    pokemon_data = r.json()

    # Additional request to get generation information
    species_url = pokemon_data['species']['url']
    species_data = requests.get(species_url).json()
    generation_url = species_data['generation']['url']
    generation_data = requests.get(generation_url).json()

    return pokemon_data, generation_data

def display_pokemon_info(pokemon_data, generation_data):
    if pokemon_data:
        st.header(f"**{pokemon_data['name'].capitalize()} Information**")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.subheader("In-Game Regular Sprite (Front)")
            st.image(pokemon_data['sprites']['front_default'], width=150)
        with col2:
            st.subheader("In-Game Regular Sprite (Back)")
            st.image(pokemon_data['sprites']['back_default'], width=150)
        with col3:
            st.subheader("In-Game Shiny Sprite (Front)  ")
            st.image(pokemon_data['sprites']['front_shiny'], width=150)
        with col4:
            st.subheader("In-Game Regular Sprite (Back)")
            st.image(pokemon_data['sprites']['back_shiny'], width=150)

        st.write("---")
        st.header(f"**Basic characteristics for {pokemon_data['name'].capitalize()}:**")
        st.write(f"**Type(s)🔥💧🌿 :** {', '.join([type['type']['name'].capitalize() for type in pokemon_data['types']])}")
        st.write(f"**Height📶:** {pokemon_data['height']*10} cm")
        st.write(f"**Weight⚖️:** {pokemon_data['weight']/10} kg")
        st.write(f"**Abilities🔮:** {', '.join([ability['ability']['name'].capitalize() for ability in pokemon_data['abilities']])}")
        st.write(f"**Generation Introduced:** {generation_data['main_region']['name'].capitalize()}")
        st.image(f"images/{generation_data['main_region']['name'].lower()}.png", width=300)

        st.write("---")

        st.header("**Stats💪:**")
        stats_data = {'Stat': [], 'Base Stat': []}
        for stat in pokemon_data['stats']:
            stats_data['Stat'].append(stat['stat']['name'].capitalize())
            stats_data['Base Stat'].append(stat['base_stat'])

        stats_df = pd.DataFrame(stats_data)

        st.dataframe(stats_df, column_config={
            "Stat": "Stat",
            "Base Stat": "Base Stat"
        }, hide_index=True)

        st.write("---")

        st.header(f"How many {pokemon_data['name'].capitalize()}s does it take to outweigh a Cybertruck?")
        truckCount = st.number_input("Number of CyberTrucks:", min_value=1, value=1)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Cybertruck")
            st.image("images/cybertruck.webp", width=300)
        with col2:
            st.subheader(f"{pokemon_data['name'].capitalize()}")
            st.image(pokemon_data['sprites']['front_default'], width=150)

        st.write(f"A Cyber Truck weighs 4000 kg on average. {pokemon_data['name'].capitalize()} weighs {pokemon_data['weight']/10} kg.")

        totalTruckWeight = truckCount * 4000 # Cybertruck weighs 4000 kg on average
        pokeNeeded = (totalTruckWeight // (pokemon_data['weight']/10)) + 1

        st.subheader(f"You need at least {int(pokeNeeded)} {pokemon_data['name'].capitalize()}s to outweigh {truckCount} CyberTruck(s)!")

        st.write("---")

        st.header("What about yellow jackets?")
        jacketCount = st.number_input("Number of yellow jackets:", min_value=1, value=172500)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Yellow Jacket")
            st.image("images/buzz.jpg", width=250)
        with col2:
            st.subheader(f"{pokemon_data['name'].capitalize()}")
            st.image(pokemon_data['sprites']['front_default'], width=150)

        st.write(
            f"A yellow jacket weighs .04 grams on average. {pokemon_data['name'].capitalize()} weighs {pokemon_data['weight'] / 10} kg.")

        totalJacketWeight = jacketCount * .00004  # yellow jacket weighs .04 grams on average
        pokeNeeded = (totalJacketWeight // (pokemon_data['weight'] / 10)) + 1

        st.subheader(f"You need {int(pokeNeeded)} {pokemon_data['name'].capitalize()}s to outweigh {jacketCount} yellow jacket(s)!")

        st.write("---")

        st.header("Finally...what if we do servings of spaghetti and meatballs?")
        servingCount = st.number_input("Number of servings of spaghetti and meatballs:", min_value=1, value=100)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Spaghetti and Meatballs")
            st.image("images/Spaghetti-and-Meatballs.jpg", width=250)
        with col2:
            st.subheader(f"{pokemon_data['name'].capitalize()}")
            st.image(pokemon_data['sprites']['front_default'], width=150)

        st.write(f"A serving of Spaghetti and meatballs weighs .505 kg on average. {pokemon_data['name'].capitalize()} weighs {pokemon_data['weight'] / 10} kg.")

        totalServingWeight = servingCount * .505  # yellow jacket weighs .505 kg on average
        pokeNeeded = (totalServingWeight // (pokemon_data['weight'] / 10)) + 1

        st.subheader(f"You need at least {int(pokeNeeded)} {pokemon_data['name'].capitalize()}s to outweigh {servingCount} servings of spaghetti and meatballs!")


def main_page():
    st.header("Welcome to My Pokémon App")
    st.image("images/pokemon.png", width=600)
    st.write("Pick your favorite Pokémon from the buttons in the sidebar to learn more about them! This app is helpful "
             "during your Pokémon adventure because this information can be used to gain the upper hand on your opponents!")
    st.write("---")

if __name__ == "__main__":
    st.set_page_config(page_title="Pokémon App", page_icon="🐾")

    if "selected_pokemon" not in st.session_state:
        st.session_state.selected_pokemon = "Bulbasaur"

    main_page()
    st.sidebar.header("Choose Your Favorite Pokémon (Ordered by Pokédex entry):")
    selected_pokemon = st.sidebar.selectbox("Select Pokémon", ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard",
    "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree",
    "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot",
    "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok",
    "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran♀", "Nidorina",
    "Nidoqueen", "Nidoran♂", "Nidorino", "Nidoking", "Clefairy", "Clefable",
    "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat",
    "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth",
    "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck",
    "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl",
    "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp",
    "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel",
    "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke",
    "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio",
    "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster",
    "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno",
    "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor",
    "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing",
    "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan",
    "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie",
    "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir",
    "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee",
    "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar",
    "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos",
    "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew",
    # Generation 2
    "Chikorita", "Bayleef", "Meganium", "Cyndaquil", "Quilava", "Typhlosion",
    "Totodile", "Croconaw", "Feraligatr", "Sentret", "Furret", "Hoothoot",
    "Noctowl", "Ledyba", "Ledian", "Spinarak", "Ariados", "Crobat",
    "Chinchou", "Lanturn", "Pichu", "Cleffa", "Igglybuff", "Togepi",
    "Togetic", "Natu", "Xatu", "Mareep", "Flaaffy", "Ampharos",
    "Bellossom", "Marill", "Azumarill", "Sudowoodo", "Politoed", "Hoppip",
    "Skiploom", "Jumpluff", "Aipom", "Sunkern", "Sunflora", "Yanma",
    "Wooper", "Quagsire", "Espeon", "Umbreon", "Murkrow", "Slowking",
    "Misdreavous", "Unown", "Wobbuffet", "Girafarig", "Pineco", "Forretress",
    "Dunsparce", "Gligar", "Steelix", "Snubbull", "Granbull", "Qwilfish",
    "Scizor", "Shuckle", "Heracross", "Sneasel", "Teddiursa", "Ursaring",
    "Slugma", "Magcargo", "Swinub", "Piloswine", "Corsola", "Remoraid",
    "Octillery", "Delibird", "Mantine", "Skarmory", "Houndour", "Houndoom",
    "Kingdra", "Phanpy", "Donphan", "Porygon2", "Stantler", "Smeargle",
    "Tyrogue", "Hitmontop", "Smoochum", "Elekid", "Magby", "Miltank",
    "Blissey", "Raikou", "Entei", "Suicune", "Larvitar", "Pupitar",
    "Tyranitar", "Lugia", "Ho-Oh", "Celebi",
    # Generation 3
    "Treecko", "Grovyle", "Sceptile", "Torchic", "Combusken", "Blaziken",
    "Mudkip", "Marshtomp", "Swampert", "Poochyena", "Mightyena", "Zigzagoon",
    "Linoone", "Wurmple", "Silcoon", "Beautifly", "Cascoon", "Dustox",
    "Lotad", "Lombre", "Ludicolo", "Seedot", "Nuzleaf", "Shiftry",
    "Taillow", "Swellow", "Wingull", "Pelipper", "Ralts", "Kirlia",
    "Gardevoir", "Surskit", "Masquerain", "Shroomish", "Breloom", "Slakoth",
    "Vigoroth", "Slaking", "Nincada", "Ninjask", "Shedinja", "Whismur",
    "Loudred", "Exploud", "Makuhita", "Hariyama", "Azurill", "Nosepass",
    "Skitty", "Delcatty", "Sableye", "Mawile", "Aron", "Lairon",
    "Aggron", "Meditite", "Medicham", "Electrike", "Manectric", "Plusle",
    "Minun", "Volbeat", "Illumise", "Roselia", "Gulpin", "Swalot",
    "Carvanha", "Sharpedo", "Wailmer", "Wailord", "Numel", "Camerupt",
    "Torkoal", "Spoink", "Grumpig", "Spinda", "Trapinch", "Vibrava",
    "Flygon", "Cacnea", "Cacturne", "Swablu", "Altaria", "Zangoose",
    "Seviper", "Lunatone", "Solrock", "Barboach", "Whiscash", "Corphish",
    "Crawdaunt", "Baltoy", "Claydol", "Lileep", "Cradily", "Anorith",
    "Armaldo", "Feebas", "Milotic", "Castform", "Kecleon", "Shuppet",
    "Banette", "Duskull", "Dusclops", "Tropius", "Chimecho", "Absol",
    "Wynaut", "Snorunt", "Glalie", "Spheal", "Sealeo", "Walrein",
    "Clamperl", "Huntail", "Gorebyss", "Relicanth", "Luvdisc", "Bagon",
    "Shelgon", "Salamence", "Beldum", "Metang", "Metagross", "Regirock",
    "Regice", "Registeel", "Latias", "Latios", "Kyogre", "Groudon",
    "Rayquaza", "Jirachi", "Deoxys",
    # Generation 4
    "Turtwig", "Grotle", "Torterra", "Chimchar", "Monferno", "Infernape",
    "Piplup", "Prinplup", "Empoleon", "Starly", "Staravia", "Staraptor",
    "Bidoof", "Bibarel", "Kricketot", "Kricketune", "Shinx", "Luxio",
    "Luxray", "Budew", "Roserade", "Cranidos", "Rampardos", "Shieldon",
    "Bastiodon", "Burmy", "Wormadam", "Mothim", "Combee", "Vespiquen",
    "Pachirisu", "Buizel", "Floatzel", "Cherubi", "Cherrim", "Shellos",
    "Gastrodon", "Ambipom", "Drifloon", "Drifblim", "Buneary", "Lopunny",
    "Mismagius", "Honchkrow", "Glameow", "Purugly", "Chingling", "Stunky",
    "Skuntank", "Bronzor", "Bronzong", "Bonsly", "Mime Jr.", "Happiny",
    "Chatot", "Spiritomb", "Gible", "Gabite", "Garchomp", "Munchlax",
    "Riolu", "Lucario", "Hippopotas", "Hippowdon", "Skorupi", "Drapion",
    "Croagunk", "Toxicroak", "Carnivine", "Finneon", "Lumineon", "Mantyke",
    "Snover", "Abomasnow", "Weavile", "Magnezone", "Lickilicky", "Rhyperior",
    "Tangrowth", "Electivire", "Magmortar", "Togekiss", "Yanmega", "Leafeon",
    "Glaceon", "Gliscor", "Mamoswine", "Porygon-Z", "Gallade", "Probopass",
    "Dusknoir", "Froslass", "Rotom", "Uxie", "Mesprit", "Azelf",
    "Dialga", "Palkia", "Heatran", "Regigigas", "Giratina", "Cresselia",
    "Phione", "Manaphy", "Darkrai", "Shaymin", "Arceus",
    # Generation 5
    "Victini", "Snivy", "Servine", "Serperior", "Tepig", "Pignite",
    "Emboar", "Oshawott", "Dewott", "Samurott", "Patrat", "Watchog",
    "Lillipup", "Herdier", "Stoutland", "Purrloin", "Liepard", "Pansage",
    "Simisage", "Pansear", "Simisear", "Panpour", "Simipour", "Munna",
    "Musharna", "Pidove", "Tranquill", "Unfezant", "Blitzle", "Zebstrika",
    "Roggenrola", "Boldore", "Gigalith", "Woobat", "Swoobat", "Drilbur",
    "Excadrill", "Audino", "Timburr", "Gurdurr", "Conkeldurr", "Tympole",
    "Palpitoad", "Seismitoad", "Throh", "Sawk", "Sewaddle", "Swadloon",
    "Leavanny", "Venipede", "Whirlipede", "Scolipede", "Cottonee", "Whimsicott",
        "Petilil", "Lilligant", "Basculin", "Sandile", "Krokorok", "Krookodile",
    "Darumaka", "Darmanitan", "Maractus", "Dwebble", "Crustle", "Scraggy",
    "Scrafty", "Sigilyph", "Yamask", "Cofagrigus", "Tirtouga", "Carracosta",
    "Archen", "Archeops", "Trubbish", "Garbodor", "Zorua", "Zoroark",
    "Minccino", "Cinccino", "Gothita", "Gothorita", "Gothitelle", "Solosis",
    "Duosion", "Reuniclus", "Ducklett", "Swanna", "Vanillite", "Vanillish",
    "Vanilluxe", "Deerling", "Sawsbuck", "Emolga", "Karrablast", "Escavalier",
    "Foongus", "Amoonguss", "Frillish", "Jellicent", "Alomomola", "Joltik",
    "Galvantula", "Ferroseed", "Ferrothorn", "Klink", "Klang", "Klinklang",
    "Tynamo", "Eelektrik", "Eelektross", "Elgyem", "Beheeyem", "Litwick",
    "Lampent", "Chandelure", "Axew", "Fraxure", "Haxorus", "Cubchoo",
    "Beartic", "Cryogonal", "Shelmet", "Accelgor", "Stunfisk", "Mienfoo",
    "Mienshao", "Druddigon", "Golett", "Golurk", "Pawniard", "Bisharp",
    "Bouffalant", "Rufflet", "Braviary", "Vullaby", "Mandibuzz", "Heatmor",
    "Durant", "Deino", "Zweilous", "Hydreigon", "Larvesta", "Volcarona",
    "Cobalion", "Terrakion", "Virizion", "Tornadus", "Thundurus", "Reshiram",
    "Zekrom", "Landorus", "Kyurem", "Keldeo", "Meloetta", "Genesect",
    # Generation 6
    "Chespin", "Quilladin", "Chesnaught", "Fennekin", "Braixen", "Delphox",
    "Froakie", "Frogadier", "Greninja", "Bunnelby", "Diggersby", "Fletchling",
    "Fletchinder", "Talonflame", "Scatterbug", "Spewpa", "Vivillon", "Litleo",
    "Pyroar", "Flabébé", "Floette", "Florges", "Skiddo", "Gogoat",
    "Pancham", "Pangoro", "Furfrou", "Espurr", "Meowstic", "Honedge",
    "Doublade", "Aegislash", "Spritzee", "Aromatisse", "Swirlix", "Slurpuff",
    "Inkay", "Malamar", "Binacle", "Barbaracle", "Skrelp", "Dragalge",
    "Clauncher", "Clawitzer", "Helioptile", "Heliolisk", "Tyrunt", "Tyrantrum",
    "Amaura", "Aurorus", "Sylveon", "Hawlucha", "Dedenne", "Carbink",
    "Goomy", "Sliggoo", "Goodra", "Klefki", "Phantump", "Trevenant",
    "Pumpkaboo", "Gourgeist", "Bergmite", "Avalugg", "Noibat", "Noivern",
    "Xerneas", "Yveltal", "Zygarde", "Diancie", "Hoopa", "Volcanion",
    # Generation 7
    "Rowlet", "Dartrix", "Decidueye", "Litten", "Torracat", "Incineroar",
    "Popplio", "Brionne", "Primarina", "Pikipek", "Trumbeak", "Toucannon",
    "Yungoos", "Gumshoos", "Grubbin", "Charjabug", "Vikavolt", "Crabrawler",
    "Crabominable", "Oricorio", "Cutiefly", "Ribombee", "Rockruff", "Lycanroc",
    "Wishiwashi", "Mareanie", "Toxapex", "Mudbray", "Mudsdale", "Dewpider",
    "Araquanid", "Fomantis", "Lurantis", "Morelull", "Shiinotic", "Salandit",
    "Salazzle", "Stufful", "Bewear", "Bounsweet", "Steenee", "Tsareena",
    "Comfey", "Oranguru", "Passimian", "Wimpod", "Golisopod", "Sandygast",
    "Palossand", "Pyukumuku", "Type: Null", "Silvally", "Minior", "Komala",
    "Turtonator", "Togedemaru", "Mimikyu", "Bruxish", "Drampa", "Dhelmise",
    "Jangmo-o", "Hakamo-o", "Kommo-o", "Tapu Koko", "Tapu Lele", "Tapu Bulu",
    "Tapu Fini", "Cosmog", "Cosmoem", "Solgaleo", "Lunala", "Nihilego",
    "Buzzwole", "Pheromosa", "Xurkitree", "Celesteela", "Kartana", "Guzzlord",
    "Necrozma", "Magearna", "Marshadow", "Poipole", "Naganadel", "Stakataka",
    "Blacephalon", "Zeraora", "Meltan", "Melmetal",
    # Generation 8
    "Grookey", "Thwackey", "Rillaboom", "Scorbunny", "Raboot", "Cinderace",
    "Sobble", "Drizzile", "Inteleon", "Skwovet", "Greedent", "Rookidee",
    "Corvisquire", "Corviknight", "Blipbug", "Dottler", "Orbeetle", "Nickit",
    "Thievul", "Gossifleur", "Eldegoss", "Wooloo", "Dubwool", "Chewtle",
    "Drednaw", "Yamper", "Boltund", "Rolycoly", "Carkol", "Coalossal",
    "Applin", "Flapple", "Appletun", "Silicobra", "Sandaconda", "Cramorant",
    "Arrokuda", "Barraskewda", "Toxel", "Toxtricity", "Sizzlipede", "Centiskorch",
    "Clobbopus", "Grapploct", "Sinistea", "Polteageist", "Hatenna", "Hattrem",
    "Hatterene", "Impidimp", "Morgrem", "Grimmsnarl", "Obstagoon", "Perrserker",
    "Cursola", "Sirfetch'd", "Mr. Rime", "Runerigus", "Milcery", "Alcremie",
    "Falinks", "Pincurchin", "Snom", "Frosmoth", "Stonjourner", "Eiscue",
    "Indeedee", "Morpeko", "Cufant", "Copperajah", "Dracozolt", "Arctozolt",
    "Dracovish", "Arctovish", "Duraludon", "Dreepy", "Drakloak", "Dragapult",
    "Zacian", "Zamazenta", "Eternatus", "Kubfu", "Urshifu", "Zarude",
    "Regieleki", "Regidrago", "Glastrier", "Spectrier", "Calyrex"], index=0)
    st.session_state.selected_pokemon = selected_pokemon

    container = st.empty()
    pokemon_data, generation_data = get_pokemon_info(selected_pokemon.lower())
    display_pokemon_info(pokemon_data, generation_data)
