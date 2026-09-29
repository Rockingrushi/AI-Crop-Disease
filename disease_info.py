"""
Comprehensive disease treatment, precautions, and pesticide recommendations
for all 38 plant disease classes in the PlantVillage dataset.
"""

DISEASE_DATA = {
    "Apple___Apple_scab": {
        "display_name": "Apple - Apple Scab",
        "status": "Infected",
        "precautions": [
            "Rake and destroy fallen leaves in autumn to eliminate overwintering fungal spores.",
            "Prune trees annually to open the canopy and promote rapid leaf drying.",
            "Avoid overhead irrigation; water the soil base directly.",
            "Plant resistant apple varieties (e.g., Liberty, Prima, Freedom)."
        ],
        "medicines_pesticides": [
            "Fungicides: Captan 50 WP, Mancozeb 75 WG, or Myclobutanil.",
            "Organic: Copper-based fungicides (Bordeaux mixture) or Liquid Sulfur sprays.",
            "Systemic option: Difenoconazole or Trifloxystrobin during early bud break."
        ],
        "cure_steps": "Apply fungicides in early spring when green leaf tips appear. Repeat every 7-10 days during wet periods until petal fall."
    },
    "Apple___Black_rot": {
        "display_name": "Apple - Black Rot (Frogeye Leaf Spot)",
        "status": "Infected",
        "precautions": [
            "Prune out dead wood, cankers, and mummified apples hanging from trees.",
            "Disinfect pruning tools with 70% alcohol or 10% bleach solution between cuts.",
            "Ensure good air circulation within the tree canopy.",
            "Prevent insect damage on fruits, as wounds invite fungal entry."
        ],
        "medicines_pesticides": [
            "Chemical Fungicides: Captan, Thiophanate-methyl, or Mancozeb.",
            "Organic: Copper fungicides sprayed before bloom.",
            "Bio-control: Bacillus subtilis formulations."
        ],
        "cure_steps": "Prune infected branches 6-8 inches below visible cankers. Spray protective fungicides from silver tip stage through harvest."
    },
    "Apple___Cedar_apple_rust": {
        "display_name": "Apple - Cedar Apple Rust",
        "status": "Infected",
        "precautions": [
            "Remove nearby Eastern red cedar or juniper trees within a 1-mile radius if possible.",
            "Inspect nearby junipers in winter and prune out reddish gall swellings before spring.",
            "Choose rust-resistant cultivars (e.g., Redfree, Enterprise, William's Pride)."
        ],
        "medicines_pesticides": [
            "Fungicides: Myclobutanil (Immunox), Mancozeb, Propiconazole, or Tebuconazole.",
            "Organic: Sulfur sprays or Copper soap applied at pink bud stage."
        ],
        "cure_steps": "Begin fungicide sprays when apple blossom buds show pink and repeat at 7 to 10-day intervals until cedar galls stop sporulating."
    },
    "Apple___healthy": {
        "display_name": "Apple - Healthy Plant",
        "status": "Healthy",
        "precautions": [
            "Continue regular monitoring for early signs of pests or lesions.",
            "Maintain balanced fertilization; avoid excess nitrogen which spurs soft growth.",
            "Provide consistent deep watering at the drip line."
        ],
        "medicines_pesticides": [
            "No chemical pesticides required.",
            "Preventative Neem oil spray (optional) to deter sucking pests."
        ],
        "cure_steps": "Your apple leaves look healthy! Keep up standard orchard sanitation, annual winter pruning, and proper watering."
    },
    "Blueberry___healthy": {
        "display_name": "Blueberry - Healthy Plant",
        "status": "Healthy",
        "precautions": [
            "Maintain acidic soil pH between 4.5 and 5.2 using elemental sulfur.",
            "Apply 2-3 inches of pine bark or needle mulch to retain moisture.",
            "Avoid overhead watering to keep foliage dry."
        ],
        "medicines_pesticides": [
            "No pesticides needed.",
            "Use acid-forming organic fertilizers like ammonium sulfate if needed."
        ],
        "cure_steps": "Plant is thriving! Maintain soil acidity, mulch root zones, and inspect periodically for scale or aphids."
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "display_name": "Cherry - Powdery Mildew",
        "status": "Infected",
        "precautions": [
            "Prune suckers and interior dense branches to improve airflow and sunlight.",
            "Avoid excessive nitrogen fertilization, which generates susceptible young tissue.",
            "Avoid late afternoon or evening overhead irrigation."
        ],
        "medicines_pesticides": [
            "Fungicides: Myclobutanil, Fenbuconazole, or Boscalid + Pyraclostrobin.",
            "Organic: Wettable sulfur, Potassium bicarbonate (MilStop), or Horticultural oils.",
            "Bio-fungicides: Bacillus amyloliquefaciens."
        ],
        "cure_steps": "Apply sulfur or potassium bicarbonate sprays upon first leaf emergence and repeat every 10-14 days until harvest."
    },
    "Cherry_(including_sour)___healthy": {
        "display_name": "Cherry - Healthy Plant",
        "status": "Healthy",
        "precautions": [
            "Prune during dry winter weather to prevent bacterial canker.",
            "Apply dormant horticultural oil in late winter to suppress overwintering mite and aphid eggs.",
            "Ensure well-drained soil."
        ],
        "medicines_pesticides": [
            "No treatment needed.",
            "Preventative organic dormant copper spray before bud swell."
        ],
        "cure_steps": "Leaves are healthy. Keep the canopy well-aerated and practice routine orchard hygiene."
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "display_name": "Corn (Maize) - Gray Leaf Spot",
        "status": "Infected",
        "precautions": [
            "Practice 2-year crop rotation with non-host crops like soybeans or alfalfa.",
            "Till crop residue under after harvest to accelerate decomposition of fungal matter.",
            "Select resistant or tolerant corn hybrids.",
            "Maintain optimal plant spacing to avoid dense canopy moisture."
        ],
        "medicines_pesticides": [
            "Fungicides: Azoxystrobin + Difenoconazole, Pyraclostrobin, or Propiconazole.",
            "Foliar spray: Mancozeb or Chlorothalonil (in early stages)."
        ],
        "cure_steps": "Apply foliar fungicides at tassel stage (VT to R1) if lesions appear on the third leaf below the ear leaf or higher."
    },
    "Corn_(maize)___Common_rust_": {
        "display_name": "Corn (Maize) - Common Rust",
        "status": "Infected",
        "precautions": [
            "Plant rust-resistant certified hybrid seeds.",
            "Plant early in the season to avoid peak summer spore arrival from southern winds.",
            "Monitor lower leaves regularly during cool, humid periods (60-75°F)."
        ],
        "medicines_pesticides": [
            "Fungicides: Triazole fungicides (Propiconazole, Tebuconazole) or Strobilurin (Azoxystrobin).",
            "Broad-spectrum: Mancozeb 75 WP."
        ],
        "cure_steps": "Fungicide treatment is economical if pustules cover >5% of the upper canopy before silking stage."
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "display_name": "Corn (Maize) - Northern Corn Leaf Blight",
        "status": "Infected",
        "precautions": [
            "Rotate crops annually away from corn.",
            "Incorporate crop stubble into soil thoroughly to destroy fungal overwintering sites.",
            "Choose hybrids with Ht-gene resistance."
        ],
        "medicines_pesticides": [
            "Fungicides: Pyraclostrobin + Fluxapyroxad, Azoxystrobin + Propiconazole.",
            "Alternative: Chlorothalonil or Mancozeb."
        ],
        "cure_steps": "Spray systemic fungicides between V14 and early silking if cigar-shaped lesions are observed on middle leaves."
    },
    "Corn_(maize)___healthy": {
        "display_name": "Corn (Maize) - Healthy Plant",
        "status": "Healthy",
        "precautions": [
            "Maintain balanced soil nutrition (NPK with adequate zinc and sulfur).",
            "Monitor fields regularly during warm, humid conditions.",
            "Keep field borders clear of wild grassy weed hosts."
        ],
        "medicines_pesticides": [
            "No chemical intervention needed."
        ],
        "cure_steps": "The maize crop looks vibrant and disease-free. Maintain balanced nitrogen application and steady irrigation."
    },
    "Grape___Black_rot": {
        "display_name": "Grape - Black Rot",
        "status": "Infected",
        "precautions": [
            "Prune out and destroy all mummified berries from vines and ground in winter.",
            "Canopy management: Trellis shoots upward to maximize sunlight and wind penetration.",
            "Remove sucker growth around the vine base."
        ],
        "medicines_pesticides": [
            "Fungicides: Myclobutanil (Rally), Mancozeb, Captan, or Kresoxim-methyl.",
            "Organic: Copper octanoate or Copper sulfate with hydrated lime (Bordeaux)."
        ],
        "cure_steps": "Apply protective sprays starting at early shoot growth (3-5 inches) and continue at 10-14 day intervals until 4-5 weeks post-bloom."
    },
    "Grape___Esca_(Black_Measles)": {
        "display_name": "Grape - Esca (Black Measles)",
        "status": "Infected",
        "precautions": [
            "Delay pruning until late winter to reduce wound susceptibility.",
            "Apply pruning wound sealants or paste containing copper or Trichoderma to large cuts.",
            "Remove and incinerate severely infected vines with trunk dieback."
        ],
        "medicines_pesticides": [
            "Wound protectants: Thiophanate-methyl paste or Trichoderma atroviride bio-fungicide.",
            "Foliar: Fosetyl-Al or Phosphorous acid sprays can slow internal progression."
        ],
        "cure_steps": "There is no complete cure once trunk wood is decayed. Sanitize pruning tools and protect vine wounds immediately after cutting."
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "display_name": "Grape - Leaf Blight (Isariopsis Spot)",
        "status": "Infected",
        "precautions": [
            "Prune and burn infected shoots and fallen foliage after harvest.",
            "Thin leaves around grape bunches to lower microclimate humidity.",
            "Avoid sprinklers that wet the vineyard canopy."
        ],
        "medicines_pesticides": [
            "Fungicides: Mancozeb 75 WP, Copper oxychloride 50 WP, or Carbendazim 50 WP.",
            "Organic: Bordeaux mixture (1%) or Copper hydroxide."
        ],
        "cure_steps": "Spray Copper oxychloride or Mancozeb immediately upon observing brown angular spots; repeat every 12-15 days during rainy spells."
    },
    "Grape___healthy": {
        "display_name": "Grape - Healthy Plant",
        "status": "Healthy",
        "precautions": [
            "Maintain open canopy architecture with regular summer shoot positioning.",
            "Ensure good soil drainage and balanced potassium levels.",
            "Scout weekly for berry moths and leafhoppers."
        ],
        "medicines_pesticides": [
            "No pesticides needed.",
            "Apply organic compost around root dripline in spring."
        ],
        "cure_steps": "Vines are healthy! Continue proper trellising, weed control around trunks, and balanced watering."
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "display_name": "Citrus - Huanglongbing (Citrus Greening)",
        "status": "Infected",
        "precautions": [
            "Control Asian Citrus Psyllid (ACP) vectors aggressively, as they spread the bacterium.",
            "Use certified disease-free nursery stock from protected screen houses.",
            "Remove and destroy symptomatic, declining trees to protect adjacent healthy trees."
        ],
        "medicines_pesticides": [
            "Vector Insecticides: Imidacloprid, Thiamethoxam, Bifenthrin, or Spinetoram to kill psyllids.",
            "Organic vector control: Horticultural mineral oil (1-2%) or Neem oil sprays.",
            "Nutritional therapy: Enhanced foliar micronutrients (Zinc, Iron, Manganese) to prolong tree vigor."
        ],
        "cure_steps": "No known botanical cure exists for the bacteria inside phloem. Focus strictly on aggressive psyllid vector eradication and foliar nutritional support."
    },
    "Peach___Bacterial_spot": {
        "display_name": "Peach - Bacterial Spot",
        "status": "Infected",
        "precautions": [
            "Plant resistant peach varieties (e.g., Candor, Dixired, Clayton, Sentinel).",
            "Avoid high nitrogen fertilizer that promotes lush, tender bacterial targets.",
            "Establish windbreaks to reduce blowing sand and wind-borne lesions."
        ],
        "medicines_pesticides": [
            "Bactericides: Copper hydroxide or Copper sulfate during dormant and delayed-dormant stages.",
            "Growing season: Oxytetracycline (Mycoshield) or low-rate Copper with hydrated lime."
        ],
        "cure_steps": "Spray copper formulations at leaf fall and bud swell. In growing season, apply oxytetracycline starting from shuck split at 7-day intervals."
    },
    "Peach___healthy": {
        "display_name": "Peach - Healthy Plant",
        "status": "Healthy",
        "precautions": [
            "Perform open-center pruning to allow full sun penetration.",
            "Apply dormant copper-oil spray before pink bud stage to prevent peach leaf curl.",
            "Mulch around trunk base, keeping mulch 4 inches away from bark."
        ],
        "medicines_pesticides": [
            "No chemical pesticides needed."
        ],
        "cure_steps": "Your peach foliage is healthy! Ensure adequate irrigation during fruit sizing and maintain winter orchard sanitation."
    },
    "Pepper,_bell___Bacterial_spot": {
        "display_name": "Bell Pepper - Bacterial Spot",
        "status": "Infected",
        "precautions": [
            "Use certified pathogen-free seeds treated with hot water or hydrochloric acid.",
            "Rotate crops with non-solanaceous species (corn, beans, brassicas) for 2-3 years.",
            "Avoid overhead irrigation; use drip lines beneath plastic mulch.",
            "Never cultivate, weed, or harvest plants while foliage is wet."
        ],
        "medicines_pesticides": [
            "Bactericides: Fixed Copper (Copper Hydroxide) combined with Mancozeb (acts synergistically).",
            "Biologicals: Bacillus subtilis or bacteriophage products (OmniLytics AgriPhage).",
            "Plant activator: Acibenzolar-S-methyl (Actigard)."
        ],
        "cure_steps": "Remove heavily spotted seedlings immediately. Spray copper-mancozeb tank mix preventatively every 7 days during warm, rainy weather."
    },
    "Pepper,_bell___healthy": {
        "display_name": "Bell Pepper - Healthy Plant",
        "status": "Healthy",
        "precautions": [
            "Maintain consistent soil moisture to prevent blossom end rot.",
            "Apply organic mulch to stabilize soil temperatures.",
            "Stake or cage pepper plants to keep fruit and leaves elevated above soil."
        ],
        "medicines_pesticides": [
            "No treatment needed."
        ],
        "cure_steps": "Plants look excellent! Provide 6-8 hours of direct sunlight and regular calcium/potassium-rich feeding."
    },
    "Potato___Early_blight": {
        "display_name": "Potato - Early Blight (Alternaria solani)",
        "status": "Infected",
        "precautions": [
            "Rotate fields with non-host crops for at least 2-3 years.",
            "Ensure adequate nitrogen and potassium fertility; stressed plants are far more susceptible.",
            "Hill soil well over tubers and kill vines 2 weeks before harvest to avoid skin infection."
        ],
        "medicines_pesticides": [
            "Protectant Fungicides: Mancozeb 75 WP, Chlorothalonil, or Copper Hydroxide.",
            "Systemic Fungicides: Azoxystrobin, Difenoconazole, or Boscalid.",
            "Organic: Copper sulfate / Bordeaux mixture or Bacillus amyloliquefaciens."
        ],
        "cure_steps": "Begin fungicide applications as soon as bottom leaves show characteristic concentric target-ring spots. Repeat every 7-10 days."
    },
    "Potato___Late_blight": {
        "display_name": "Potato - Late Blight (Phytophthora infestans)",
        "status": "Infected",
        "precautions": [
            "Plant only certified disease-free seed tubers.",
            "Eliminate cull piles and volunteer potato sprouts near the garden or field.",
            "Avoid overhead watering; irrigate during early morning so leaves dry quickly.",
            "Destroy and bag infected foliage immediately if outbreak is detected."
        ],
        "medicines_pesticides": [
            "Fungicides: Metalaxyl / Mefenoxam (Ridomil Gold), Cymoxanil (Curzate), Dimethomorph, or Fluopicolide.",
            "Protectants: Mancozeb, Chlorothalonil, or Copper Hydroxide.",
            "Organic: Fixed copper sprays applied before rain events."
        ],
        "cure_steps": "Late blight spreads rapidly! Apply systemic fungicides immediately upon spotting water-soaked dark lesions. Destroy heavily infected plants."
    },
    "Potato___healthy": {
        "display_name": "Potato - Healthy Plant",
        "status": "Healthy",
        "precautions": [
            "Hill plants when they reach 6-8 inches tall to protect growing tubers from greening and pests.",
            "Maintain uniform soil moisture without waterlogging.",
            "Scout undersides of leaves weekly for Colorado potato beetle eggs."
        ],
        "medicines_pesticides": [
            "No pesticides needed."
        ],
        "cure_steps": "Potato vines are healthy and clean! Continue regular hilling, steady watering, and scout after warm rainfall."
    },
    "Raspberry___healthy": {
        "display_name": "Raspberry - Healthy Plant",
        "status": "Healthy",
        "precautions": [
            "Prune out old floricanes after fruiting to promote vigorous primocane growth.",
            "Trellis canes to ensure good airflow and sunshine.",
            "Plant in raised beds or well-drained loamy soil to prevent Phytophthora root rot."
        ],
        "medicines_pesticides": [
            "No treatment needed."
        ],
        "cure_steps": "Raspberry leaves are in great condition. Keep soil mulched and ensure annual pruning of spent fruiting canes."
    },
    "Soybean___healthy": {
        "display_name": "Soybean - Healthy Plant",
        "status": "Healthy",
        "precautions": [
            "Maintain optimal row spacing to balance yield and airflow.",
            "Scout for soybean aphid, stink bugs, and bean leaf beetles during pod-filling stages.",
            "Ensure proper Bradyrhizobium inoculation during planting."
        ],
        "medicines_pesticides": [
            "No chemical intervention required."
        ],
        "cure_steps": "The crop is healthy and vegetative. Monitor canopy regularly through flowering (R1) to pod development (R3)."
    },
    "Squash___Powdery_mildew": {
        "display_name": "Squash - Powdery Mildew",
        "status": "Infected",
        "precautions": [
            "Choose powdery mildew resistant squash/pumpkin hybrids.",
            "Space plants generously (at least 3-4 feet apart) to facilitate air circulation.",
            "Plant in full sun; shade fosters powdery mildew spore germination.",
            "Clear away all spent squash vines and leaves at the end of the season."
        ],
        "medicines_pesticides": [
            "Fungicides: Myclobutanil, Triflumizole, or Pyraclostrobin.",
            "Organic/Home Remedy: Potassium bicarbonate (1 tbsp per gallon) + liquid castile soap.",
            "Bio-remedies: Neem oil (1%) or diluted milk spray (40% milk, 60% water)."
        ],
        "cure_steps": "Spray potassium bicarbonate or neem oil on both upper and lower leaf surfaces at the very first sight of white powdery talc patches."
    },
    "Strawberry___Leaf_scorch": {
        "display_name": "Strawberry - Leaf Scorch (Diplocarpon earlianum)",
        "status": "Infected",
        "precautions": [
            "Mow and renovate June-bearing strawberry beds immediately after harvest.",
            "Rake and remove dead or scorched leaves to eliminate fungal fruiting bodies.",
            "Use drip tape instead of sprinklers to keep crowns and foliage dry.",
            "Do not overcrowd runners; thin runner plants to 4-6 inches apart."
        ],
        "medicines_pesticides": [
            "Fungicides: Captan 50 WP, Thiophanate-methyl, or Pyraclostrobin (Cabrio).",
            "Organic: Copper octanoate (soap) or Liquid Sulfur.",
            "Bio-fungicide: Bacillus subtilis."
        ],
        "cure_steps": "Apply protective fungicides in spring as new growth starts, especially if wet weather is forecasted. Remove severely scorched leaves."
    },
    "Strawberry___healthy": {
        "display_name": "Strawberry - Healthy Plant",
        "status": "Healthy",
        "precautions": [
            "Mulch beds with clean straw to keep ripening berries off damp soil.",
            "Avoid overhead irrigation during evening hours.",
            "Renovate beds annually to prevent disease buildup in older crowns."
        ],
        "medicines_pesticides": [
            "No pesticides needed."
        ],
        "cure_steps": "Strawberry leaves look healthy and green! Maintain clean straw mulching and balanced fruit fertilization."
    },
    "Tomato___Bacterial_spot": {
        "display_name": "Tomato - Bacterial Spot (Xanthomonas)",
        "status": "Infected",
        "precautions": [
            "Never save seed from infected plants; purchase certified disease-free seeds.",
            "Rotate solanaceous crops (tomatoes, peppers, potatoes, eggplants) for 3 years.",
            "Water with soaker hoses or drip lines; never spray water directly onto leaves.",
            "Sterilize pruning shears and tomato stakes between seasons."
        ],
        "medicines_pesticides": [
            "Bactericides: Copper Hydroxide (Kocide) tank-mixed with Mancozeb (enhances copper efficacy).",
            "Biologicals: AgriPhage (bacteriophages) or Serenade Garden (Bacillus subtilis).",
            "Plant defense stimulator: Regalia (Reynoutria sachalinensis extract)."
        ],
        "cure_steps": "Prune out lower infected leaves when foliage is completely dry. Spray copper-mancozeb mix every 5-7 days during rainy, hot periods."
    },
    "Tomato___Early_blight": {
        "display_name": "Tomato - Early Blight (Alternaria solani)",
        "status": "Infected",
        "precautions": [
            "Prune off the bottom 12 inches of tomato branches once the plant reaches 2-3 feet tall.",
            "Lay down thick straw or plastic mulch to stop soil-borne fungal spores from splashing onto lower leaves.",
            "Space tomato plants 24-36 inches apart with sturdy cages or stakes.",
            "Rotate crops annually."
        ],
        "medicines_pesticides": [
            "Chemical Fungicides: Chlorothalonil (Daconil), Mancozeb, or Difenoconazole.",
            "Organic: Copper fungicides (Liquid Copper / Bordeaux mixture) or Sulfur dust.",
            "Bio-fungicide: Bacillus amyloliquefaciens (Double Nickel)."
        ],
        "cure_steps": "Snip off and trash all yellowing leaves with dark target-board concentric rings. Spray Chlorothalonil or Copper thoroughly, coating both leaf sides."
    },
    "Tomato___Late_blight": {
        "display_name": "Tomato - Late Blight (Phytophthora infestans)",
        "status": "Infected",
        "precautions": [
            "Grow resistant tomato cultivars (e.g., Mountain Magic, Defiant PhR, Plum Regal).",
            "Ensure wide spacing in sunny, wind-exposed locations.",
            "Destroy self-sown volunteer tomatoes and nearby potato culls.",
            "Water early in the morning so sun quickly evaporates any dampness."
        ],
        "medicines_pesticides": [
            "Fungicides: Metalaxyl / Mefenoxam, Cymoxanil, Propamocarb, or Fluopicolide.",
            "Protectants: Chlorothalonil, Mancozeb, or Copper Hydroxide.",
            "Organic: Fixed Copper spray applied proactively before wet storm fronts."
        ],
        "cure_steps": "Act immediately! Prune and bag infected dark, water-soaked foliage. Apply systemic fungicides to protect remaining healthy vines and fruit."
    },
    "Tomato___Leaf_Mold": {
        "display_name": "Tomato - Leaf Mold (Passalora fulva)",
        "status": "Infected",
        "precautions": [
            "Common in high tunnels and greenhouses; keep relative humidity below 85% with fans and venting.",
            "Water directly at the base using drip irrigation.",
            "Prune lower suckers to maximize cross-ventilation."
        ],
        "medicines_pesticides": [
            "Fungicides: Chlorothalonil, Mancozeb, or Boscalid.",
            "Organic: Copper hydroxide or potassium bicarbonate.",
            "Bio-control: Bacillus subtilis."
        ],
        "cure_steps": "Increase greenhouse ventilation immediately. Remove yellow-spotted foliage with olive-green mold undersides and spray copper fungicide."
    },
    "Tomato___Septoria_leaf_spot": {
        "display_name": "Tomato - Septoria Leaf Spot",
        "status": "Infected",
        "precautions": [
            "Mulch soil heavily to prevent spores from splashing upward during rainfall.",
            "Prune off lower leaves that touch or sit near the ground.",
            "Sanitize tomato stakes with a 10% bleach solution before reusing.",
            "Clean up all tomato vine debris after the final harvest."
        ],
        "medicines_pesticides": [
            "Fungicides: Chlorothalonil (Daconil), Mancozeb, or Pyraclostrobin.",
            "Organic: Liquid Copper fungicide or Copper soap.",
            "Bio-spray: Serenade (Bacillus subtilis)."
        ],
        "cure_steps": "Prune out infected lower leaves showing tiny circular spots with dark margins and gray centers. Spray Chlorothalonil every 7-10 days."
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "display_name": "Tomato - Two-Spotted Spider Mites",
        "status": "Infected (Pest)",
        "precautions": [
            "Avoid dusty conditions around plants; mist foliage lightly during hot, dry spells.",
            "Avoid overusing broad-spectrum synthetic insecticides which destroy beneficial predatory mites.",
            "Keep weeds like bindweed and nightshade cleared from surrounding perimeter."
        ],
        "medicines_pesticides": [
            "Miticide / Acaricide: Abamectin, Bifenazate (Floramite), or Spiromesifen.",
            "Organic: Cold-pressed Neem oil (1%), Insecticidal soap, or Horticultural spray oil.",
            "Biological: Release predatory mites (Phytoseiulus persimilis or Neoseiulus californicus)."
        ],
        "cure_steps": "Spray undersides of leaves where mites congregate with insecticidal soap or neem oil every 3-5 days to break egg-hatching cycles."
    },
    "Tomato___Target_Spot": {
        "display_name": "Tomato - Target Spot (Corynespora cassiicola)",
        "status": "Infected",
        "precautions": [
            "Discard crop residues promptly after harvest.",
            "Improve plant spacing to allow fast canopy drying.",
            "Avoid overhead irrigation; use drip lines."
        ],
        "medicines_pesticides": [
            "Fungicides: Azoxystrobin + Difenoconazole, Chlorothalonil, or Famoxadone + Cymoxanil.",
            "Organic: Copper-based fungicides."
        ],
        "cure_steps": "Prune infected leaves exhibiting brown circular lesions with pale centers and yellow halos. Spray protective fungicides weekly."
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "display_name": "Tomato - Yellow Leaf Curl Virus (TYLCV)",
        "status": "Infected (Viral)",
        "precautions": [
            "Plant virus-resistant tomato hybrids (e.g., Tycoon, Charger, Invictus).",
            "Install 50-mesh fine insect exclusion netting in nursery beds to block whiteflies.",
            "Place yellow sticky traps around the garden to catch and monitor adult whiteflies.",
            "Uproot and immediately bag symptomatic plants with curled, stunted yellowing leaves."
        ],
        "medicines_pesticides": [
            "Vector Insecticides: Dinotefuran, Acetamiprid, Imidacloprid, or Spirotetramat to control whiteflies.",
            "Organic Vector Control: Insecticidal soaps, Azadirachtin (Neem extract), or Pyrethrins.",
            "Physical: Reflective silver mulches to repel whitefly landings."
        ],
        "cure_steps": "Viruses cannot be cured once the plant is infected. Rogue out infected plants to protect neighbors and treat whitefly vectors immediately."
    },
    "Tomato___Tomato_mosaic_virus": {
        "display_name": "Tomato - Tomato Mosaic Virus (ToMV)",
        "status": "Infected (Viral)",
        "precautions": [
            "Select ToMV-resistant varieties (labeled with 'T' or 'ToMV').",
            "Wash hands thoroughly with soap and water after handling tobacco products before touching tomato plants.",
            "Soak pruning shears in 20% non-fat dry milk or 10% trisodium phosphate solution.",
            "Rogue out and destroy infected plants immediately; do NOT compost them."
        ],
        "medicines_pesticides": [
            "No chemical cure exists for viral plant infections.",
            "Dip tools in non-fat dry milk solution (skim milk inactivates virus particles during pruning)."
        ],
        "cure_steps": "Carefully remove and bag the entire infected plant and its root system. Disinfect hands, stakes, and tools before touching healthy plants."
    },
    "Tomato___healthy": {
        "display_name": "Tomato - Healthy Plant",
        "status": "Healthy",
        "precautions": [
            "Maintain consistent watering schedule to avoid blossom end rot and fruit cracking.",
            "Mulch generously around base to maintain moisture and deter splash-borne pathogens.",
            "Support with sturdy cages or trellis and prune suckers for optimal sunlight."
        ],
        "medicines_pesticides": [
            "No pesticides needed.",
            "Apply balanced tomato fertilizer (high in phosphorus, potassium, and calcium)."
        ],
        "cure_steps": "Your tomato plant looks strong and vibrant! Keep soil evenly moist and maintain pruning hygiene."
    }
}


def get_disease_info(disease_key):
    """
    Returns disease metadata, precautions, and cure details.
    Falls back to a safe default if key is not found.
    """
    if disease_key in DISEASE_DATA:
        return DISEASE_DATA[disease_key]

    clean_name = disease_key.replace("___", " - ").replace("_", " ")
    is_healthy = "healthy" in disease_key.lower()

    if is_healthy:
        return {
            "display_name": clean_name,
            "status": "Healthy",
            "precautions": [
                "Continue regular scouting and monitoring.",
                "Ensure proper watering, balanced nutrition, and adequate sunlight.",
                "Keep planting area clean of weeds and debris."
            ],
            "medicines_pesticides": [
                "No chemical pesticides needed."
            ],
            "cure_steps": "The plant appears healthy. Maintain standard cultural practices and adequate spacing."
        }
    else:
        return {
            "display_name": clean_name,
            "status": "Infected",
            "precautions": [
                "Isolate or prune visibly infected leaves promptly.",
                "Avoid overhead watering; irrigate the root zone directly.",
                "Sanitize gardening tools before and after each use."
            ],
            "medicines_pesticides": [
                "Apply broad-spectrum organic fungicide like Neem oil or Copper fungicide.",
                "For bacterial infections: Copper-based bactericide.",
                "For fungal infections: Mancozeb or Chlorothalonil protectant sprays."
            ],
            "cure_steps": "Prune infected plant parts and dispose of them away from garden. Apply protective fungicide/bactericide spray according to label directions."
        }
