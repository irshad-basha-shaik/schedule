import pyautogui as gui, time
gui.FAILSAFE= False
import schedule
import time
import requests

base="http://localhost:8080"
vintedPath="/api/Vinted/getVintedListing/71527462-excelstuff?status=not sent"
listingPath="/api/Vinted/vintedListingStatus"
Header={'Cookie':'csrftoken=bD0kdBbkK2ufeX55O4XtK4AF6v2k6QD0; JSESSIONID=53A97CBE2161972C9D5DBA53670836DD'}
'''
Cookie: csrftoken=bD0kdBbkK2ufeX55O4XtK4AF6v2k6QD0; JSESSIONID=53A97CBE2161972C9D5DBA53670836DD

'''
k = ["/women/clothes/other-clothing","/women/accessories/belts","/women/accessories/watches","/women/accessories/sunglasses","/men/clothes/other-mens-clothing","/men/clothes/swimwear","/women/accessories/gloves","/men/accessories/gloves","/men/clothes/costumes-and-special-outfits","/men/accessories/ties-and-pocket-squares","/men/accessories/belts","/men/accessories/watches","/men/accessories/sunglasses","/men/accessories/other","/women/clothes/lingerie-and-nightwear/bras","/women/clothes/lingerie-and-nightwear/panties","/women/clothes/lingerie-and-nightwear/nightwear","/women/clothes/lingerie-and-nightwear/other","/men/grooming/hair-care","/men/grooming/body-care","/men/grooming/hand-and-nail-care","/men/grooming/face-care","/men/grooming/make-up","/men/grooming/aftershave-and-cologne","/women/beauty/perfume","/women/beauty/other-beauty-items","/women/bags/other-bags","/women/bags/handbags","/women/bags/backpacks","/women/bags/shoulder-bags","/women/bags/clutches","/women/bags/purses-and-wallets","/women/bags/make-up-bags","/women/accessories/jewellery/other-jewellery","/women/accessories/jewellery/earrings","/women/accessories/jewellery/necklaces-beads-and-pendants","/women/accessories/jewellery/bracelets","/women/accessories/jewellery/jewellry-sets","/women/accessories/jewellery/brooches","/women/clothes/dresses/other-dresses"]#,"/women/clothes/dresses/mini-dresses",42,"/women/clothes/dresses/denim-dresses",43,"/women/clothes/trousers-and-leggings/leather-trousers",44,"/women/clothes/trousers-and-leggings/skinny-trousers",45,"/women/clothes/trousers-and-leggings/tailored-trousers",46,"/women/clothes/trousers-and-leggings/other-trousers",47,"/women/clothes/jumpers-and-sweaters/sweaters/v-neck-sweaters",48,"/women/clothes/jumpers-and-sweaters/sweaters/turtleneck-sweaters",49,"/women/clothes/jumpers-and-sweaters/sweaters/long-jumpers",50,"/women/clothes/jumpers-and-sweaters/sweaters/three-fourths-sleeve-jumpers",51,"/women/clothes/jumpers-and-sweaters/cardigans",52,"/women/clothes/jumpers-and-sweaters/boleros",53,"/women/clothes/jumpers-and-sweaters/hoodies-and-sweatshirts",54,"/women/clothes/jumpers-and-sweaters/other-jumpers-and-sweaters",55,"/women/clothes/skirts/mini-skirts",56,"/women/clothes/skirts/midi-skirts",57,"/women/clothes/skirts/maxi-skirts",58,"/women/clothes/skirts/other-skirts",59,"/women/clothes/shorts-and-cropped-trousers/knee-length-shorts",60,"/women/clothes/shorts-and-cropped-trousers/cropped-trousers",61,"/women/clothes/shorts-and-cropped-trousers/other-shorts-and-cropped-trousers",62,"/women/shoes/boots/knee-high-boots",63,"/women/shoes/boots/wellington-boots",64,"/women/shoes/slippers",65,"/women/clothes/swimwear/one-pieces",66,"/women/clothes/swimwear/bikinis-and-tankinis",67,"/women/clothes/swimwear/other-swimwear-and-beachwear",68,"/women/clothes/tops-and-t-shirts/t-shirts",69,"/women/clothes/tops-and-t-shirts/shirts",70,"/women/clothes/tops-and-t-shirts/short-sleeved-tops",71,"/women/clothes/tops-and-t-shirts/long-sleeved-tops",72,"/women/clothes/tops-and-t-shirts/three-fourths-sleeve-tops",73,"/women/clothes/tops-and-t-shirts/tunics",74,"/women/clothes/tops-and-t-shirts/other-tops-and-t-shirts",75,"/women/clothes/lingerie-and-nightwear/sets",76,"/women/accessories/hats-and-caps/caps",77,"/women/accessories/hats-and-caps-231",78,"/women/accessories/hats-and-caps/warm-hats",79,"/women/accessories/hats-and-caps/berets",80,"/women/accessories/hats-and-caps/headbands",81,"/women/accessories/hats-and-caps/other",82,"/women/accessories/scarves-and-shawls/knit-scarves",83,"/women/accessories/scarves-and-shawls/head-scarfs",84,"/women/accessories/scarves-and-shawls/oversized-scarves-and-shawls",85,"/women/accessories/scarves-and-shawls/shawls",86,"/women/accessories/scarves-and-shawls/other",87,"/men/accessories/jewellery/necklaces-and-pendants",88,"/men/accessories/jewellery/rings",89,"/men/accessories/jewellery/bracelets",90,"/men/accessories/jewellery/other",91,"/men/accessories/bags-and-backpacks/handbags",92,"/men/accessories/bags-and-backpacks/backpacks",93,"/men/accessories/bags-and-backpacks/shoulder-bags",94,"/men/accessories/bags-and-backpacks/wallets",95,"/men/accessories/bags-and-backpacks/other",96,"/men/clothes/trousers/skinny-trousers",97,"/men/clothes/trousers/wide-legged-trousers",98,"/men/clothes/trousers/tailored-trousers",99,"/men/clothes/trousers/other",,100,"/men/clothes/jumpers-and-sweaters/v-neck-jumpers",101,"/men/clothes/jumpers-and-sweaters/turtle-neck-jumpers",102,"/men/clothes/jumpers-and-sweaters/cardigans",103,"/men/clothes/jumpers-and-sweaters/hoodies-and-sweatshirts",104,"/men/clothes/jumpers-and-sweaters/other",105,"/men/clothes/trousers/cropped-trousers",106,"/men/clothes/shorts/other-shorts",107,"/men/accessories/scarves-and-shawls/knitted-scarves",108,"/men/accessories/scarves-and-shawls/head-scarves",109,"/men/accessories/scarves-and-shawls/large-scarves-and-shawls",110,"/men/accessories/scarves-and-shawls/other","/men/accessories/hats-and-caps/caps",112,"/men/accessories/hats-and-caps-288",113,"/men/accessories/hats-and-caps/winter-hats",114,"/men/accessories/hats-and-caps/berets",115,"/men/accessories/hats-and-caps/other",116,"/women/clothes/trousers-and-leggings/leggings",117,"/women/clothes/trousers-and-leggings/harem-pants",118,"/women/clothes/jumpers-and-sweaters/sweaters/knitted-jumpers",119,"/women/clothes/suits-and-blazers/blazers",120,"/women/clothes/tops-and-t-shirts/vest-tops",121,"/women/clothes/shorts-and-cropped-trousers/denim-shorts",122,"/women/clothes/skirts/high-waisted-skirts",123,"/women/clothes/skirts/denim-skirts",124,"/women/clothes/skirts/tulip-skirts",125,"/women/clothes/skirts/pencil-skirts",126,"/women/shoes/flats/ballerinas",127,"/women/bags/tote-bags",128,"/women/accessories/jewellery/rings",129,"/men/clothes/tops-and-t-shirts/vests-and-sleeveless-t-shirts",130,"/women/clothes/activewear/outerwear",131,"/women/clothes/activewear/tracksuits",132,"/women/clothes/activewear/trousers",133,"/women/clothes/activewear/dresses",134,"/women/clothes/activewear/skirts",135,"/women/clothes/activewear/tops-and-t-shirts",136,"/women/clothes/activewear/hoodies-and-sweatshirts",137,"/women/clothes/activewear/shorts",138,"/women/clothes/activewear/other-activewear",139,"/men/clothes/activewear/outerwear",140,"/men/clothes/activewear/tracksuits",141,"/men/clothes/activewear/trousers",142,"/men/clothes/activewear/tops-and-t-shirts",143,"/men/clothes/activewear/pullovers-and-sweaters",144,"/men/clothes/activewear/shorts",145,"/men/clothes/activewear/other-activewear",146,"/women/beauty/face-care",147,"/women/beauty/beauty-tools/face-care-tools",148,"/women/beauty/body-care",149,"/women/beauty/beauty-tools/body-care-tools",150,"/women/beauty/nail-care",151,"/women/beauty/beauty-tools/nail-care-tools",152,"/women/beauty/make-up",153,"/women/beauty/beauty-tools/make-up-tools",154,"/men/grooming/other-grooming-items",155,"/men/grooming/tools-and-accessories/other-tools",156,"/women/clothes/lingerie-and-nightwear/dressing-gowns",157,"/women/clothes/tops-and-t-shirts/crop-tops",158,"/women/clothes/tops-and-t-shirts/off-the-shoulder-tops",159,"/women/clothes/tops-and-t-shirts/blouses",160,"/women/clothes/tops-and-t-shirts/halterneck-tops",161,"/women/clothes/tops-and-t-shirts/turtlenecks",162,"/women/clothes/dresses/long-dresses",163,"/women/clothes/dresses/midi-dresses",164,"/women/clothes/dresses/formal-and-work-dresses",165,"/women/clothes/dresses/little-black-dresses",166,"/women/clothes/dresses/casual-dresses",167,"/women/clothes/dresses/special-occasion-dresses/backless-dresses",168,"/women/clothes/dresses/strapless-dresses",169,"/women/clothes/dresses/summer-dresses",170,"/women/clothes/jumpers-and-sweaters/sweaters/other-sweaters",171,"/women/clothes/jumpers-and-sweaters/kimonos",172,"/women/clothes/trousers-and-leggings/cropped-trousers-and-chinos",173,"/women/clothes/trousers-and-leggings/wide-leg-trousers",174,"/women/clothes/outerwear/coats/peacoats",175,"/women/clothes/coats-and-jackets/jackets/bomber-jackets",176,"/women/clothes/coats-and-jackets/jackets/denim-jackets",177,"/women/clothes/coats-and-jackets/raincoats",178,"/women/clothes/coats-and-jackets/jackets/fleece-jackets",179,"/women/clothes/coats-and-jackets/parkas",180,"/women/clothes/coats-and-jackets/faux-fur-coats",181,"/women/clothes/skirts/a-line-skirts",182,"/women/clothes/skirts/bodycon-skirts",183,"/women/clothes/skirts/skater-skirts",184,"/women/clothes/skirts/pleated-skirts",185,"/women/clothes/shorts-and-cropped-trousers/high-waisted-shorts",186,"/women/clothes/shorts-and-cropped-trousers/leather-shorts",187,"/women/clothes/shorts-and-cropped-trousers/lace-shorts",188,"/women/clothes/shorts-and-cropped-trousers/cargo-shorts",189,"/other-bags",190,"/women/accessories/hair-accessories",191,"/women/clothes/suits-and-blazers/trouser-suits",192,"/women/clothes/suits-and-blazers/skirt-suits",193,"/women/clothes/suits-and-blazers/suit-separates",194,"/women/clothes/suits-and-blazers/other-suits-and-blazers",195,"/women/clothes/jumpsuits-and-playsuits-1131",196,"/women/clothes/jumpsuits-and-playsuits/playsuits",197,"/women/clothes/jumpsuits-and-playsuits/other-jumpsuits-and-playsuits",198,"/women/accessories/other-accessories",199,"/women/clothes/maternity-clothes/maternity-trousers",200,"/women/clothes/maternity-clothes/maternity-skirts",201,"/women/clothes/maternity-clothes/maternity-tops",202,"/women/clothes/maternity-clothes/maternity-jumpsuits-and-playsuits",203,"/women/clothes/maternity-clothes/maternity-dresses",204,"/women/clothes/maternity-clothes/maternity-coats-and-jackets",205,"/women/clothes/maternity-clothes/maternity-jumpers-and-sweaters",206,"/women/clothes/maternity-clothes/maternity-shorts",207,"/women/clothes/maternity-clothes/maternity-swimwear-and-beachwear",208,"/kids/boys-clothing/trousers-and-dungarees/shorts-and-cropped-trousers",209,"/kids/boys-clothing/activewear",210,"/kids/boys-clothing/other-boys-clothing",211,"/women/accessories/tech-accessories",212,"/men/clothes/coats-and-jackets/jackets/bomber-jackets",213,"/men/clothes/coats-and-jackets/jackets/denim-jackets",214,"/men/clothes/coats-and-jackets/duffle-coats",215,"/men/clothes/coats-and-jackets/jackets/harrington-jackets",216,"/men/clothes/coats-and-jackets/parkas",217,"/men/clothes/coats-and-jackets/trench-coats",218,"/men/shoes/trainers",219,"/kids/girls-clothing/skirts",220,"/kids/girls-clothing/trousers-and-shorts/shorts-and-cropped-trousers",221,"/kids/girls-clothing/activewear",222,"/kids/girls-clothing/other-girls-clothing",223,"/kids/boys-clothing/bags-and-backpacks",224,"/kids/girls-clothing/bags-and-backpacks",225,"/women/clothes/lingerie-and-nightwear/socks",226,"/women/clothes/lingerie-and-nightwear/tights-and-stockings",227,"/women/beauty/hand-care",228,"/women/clothes/activewear/sports-bras",229,"/women/clothes/activewear/sports-accessories/scarves",230,"/women/clothes/activewear/sports-accessories/glasses",231,"/women/clothes/activewear/sports-accessories/watches-and-wristbands",232,"/women/clothes/activewear/sports-accessories/hats",233,"/women/clothes/activewear/sports-accessories/gloves",234,"/women/clothes/activewear/sports-accessories/protection-slash-padding",235,"/women/clothes/activewear/sports-accessories/other-accessories",236,"/men/shoes/sport-shoes/running-shoes",237,"/men/shoes/sport-shoes/indoor-training-shoes",238,"/men/clothes/activewear/sports-accessories/scarves",239,"/men/clothes/activewear/sports-accessories/glasses",240,"/men/clothes/activewear/sports-accessories/watches-and-wristbands",241,"/men/clothes/activewear/sports-accessories/hats",242,"/men/clothes/activewear/sports-accessories/gloves",243,"/men/clothes/activewear/sports-accessories/protective-items",244,"/men/clothes/activewear/sports-accessories/other-accessories",245,"/women/bags/patterned-and-embroidered-bags",246,"/kids/other-kids-items",247,"/kids/car-seats-and-chairs/car-chairs",248,"/kids/car-seats-and-chairs/feeding-chairs",249,"/kids/school-supplies/school-bags",250,"/kids/school-supplies-1509",251,"/kids/girls-clothing/clothing-bundles",252,"/kids/buggies/buggy-accessories",253,"/kids/buggies/umbrella-buggies",254,"/kids/girls-clothing/baby-clothing/rompers",255,"/kids/girls-clothing/baby-clothing/bodysuits",256,"/kids/girls-clothing/baby-clothing/dungarees",257,"/kids/girls-clothing/baby-clothing/sets",258,"/kids/girls-clothing/outerwear/gilets-and-body-warmers",259,"/kids/girls-clothing/shoes/baby-shoes",260,"/kids/girls-clothing/shoes/formal-and-special-occasion-shoes",261,"/kids/girls-clothing/shoes/slippers",262,"/kids/girls-clothing/tops-and-t-shirts/t-shirts",263,"/kids/girls-clothing/tops-and-t-shirts/polo-shirts",264,"/kids/girls-clothing/tops-and-t-shirts/shirts",265,"/kids/girls-clothing/tops-and-t-shirts/short-sleeved-tops",266,"/kids/girls-clothing/tops-and-t-shirts/long-sleeved-tops",267,"/kids/girls-clothing/tops-and-t-shirts/sleeveless-tops",268,"/kids/girls-clothing/tops-and-t-shirts/tunics",269,"/kids/girls-clothing/jumpers-and-hoodies-1542",270,"/kids/girls-clothing/jumpers-and-hoodies/v-neck-jumpers",271,"/kids/girls-clothing/jumpers-and-hoodies/turtleneck-jumpers",272,"/kids/girls-clothing/jumpers-and-hoodies/zip-up-jumpers",273,"/kids/girls-clothing/jumpers-and-hoodies/boleros",274,"/kids/girls-clothing/jumpers-and-hoodies/hoodies-and-sweatshirts",275,"/kids/girls-clothing/jumpers-and-hoodies/sleeveless-jumpers",276,"/kids/girls-clothing/dresses/long-dresses",277,"/kids/girls-clothing/dresses/short-dresses",278,"/kids/girls-clothing/trousers-and-shorts/jeans",279,"/kids/girls-clothing/trousers-and-shorts/skinny-trousers",280,"/kids/kids-furniture/cribs-and-cradles",281,"/kids/girls-clothing/trousers-and-shorts/wide-leg-trousers",282,"/kids/kids-furniture/cots",283,"/kids/girls-clothing/trousers-and-shorts/leggings",284,"/kids/kids-furniture/toddler-beds",285,"/kids/girls-clothing/trousers-and-shorts/jumpsuits-and-dungarees",286,"/kids/kids-furniture/mattresses/cot-mattresses",287,"/kids/kids-furniture/mattresses/crib-and-cradle-mattresses",288,"/kids/kids-furniture/mattresses/kid-bed-mattresses",289,"/kids/kids-furniture/playmats",290,"/kids/kids-furniture/playpens",291,"/kids/kids-furniture/changing-pads-and-tables",292,"/kids/girls-clothing/accessories/caps-and-hats",293,"/kids/girls-clothing/accessories/gloves",294,"/kids/kids-furniture/other-kids-furniture/chairs",295,"/kids/girls-clothing/accessories/scarves-and-shawls",296,"/kids/girls-clothing/accessories/belts",297,"/kids/girls-clothing/accessories/hairbands-and-hairclips",298,"/kids/girls-clothing/accessories/wallets-and-purses",299,"/kids/kids-furniture/other-kids-furniture/tables",300,"/kids/girls-clothing/accessories/jewellery",301,"/kids/kids-furniture/other-kids-furniture/carpets",302,"/kids/kids-furniture/other-kids-furniture/wardrobes",303,"/kids/kids-furniture/other-kids-furniture/shelves",304,"/kids/girls-clothing/swimwear/one-piece-swimsuits",305,"/kids/kids-furniture/other-kids-furniture/play-furniture",306,"/kids/girls-clothing/swimwear/bikinis-and-tankinis",307,"/kids/girls-clothing/swimwear/bathrobes",308,"/kids/ride-on-toys/bicycle-seats-and-trailers",309,"/kids/girls-clothing/sleepwear/one-piece-pyjamas",310,"/kids/girls-clothing/sleepwear/two-piece-pyjamas",311,"/kids/girls-clothing/sleepwear/nighties",312,"/kids/ride-on-toys/baby-walkers",313,"/kids/girls-clothing/underwear-and-socks/socks",314,"/kids/girls-clothing/underwear-and-socks/tights-and-leggings",315,"/kids/girls-clothing/underwear-and-socks/underwear",316,"/kids/ride-on-toys/push-and-pull-toys",317,"/kids/girls-clothing/clothing-for-twins",318,"/kids/ride-on-toys/scooters",319,"/kids/girls-clothing/fancy-dress-and-costumes",320,"/kids/ride-on-toys/tricycles",321,"/kids/ride-on-toys/bicycles",322,"/kids/ride-on-toys/outdoor-vehicles",323,"/kids/ride-on-toys/sledges-skis-and-snowboards",324,"/kids/buggies/running-and-sport-buggies",325,"/kids/buggies/universal-buggies",326,"/kids/buggies/buggies-for-twins",327,"/women/clothes/maternity-clothes/maternity-underwear-1615",328,"/women/clothes/maternity-clothes/maternity-underwear/sleep-wear",329,"/women/clothes/maternity-clothes/maternity-underwear/pregnancy-and-postpartum-belts",330,"/women/clothes/maternity-clothes/maternity-underwear/pregnancy-and-breastfeeding-bras",331,"/kids/baby-care/sleep-accessories/blankets",332,"/kids/baby-care/sleep-accessories/pillows",333,"/kids/baby-care/sleep-accessories/plaids",334,"/kids/baby-care/sleep-accessories/sleeping-bags",335,"/kids/baby-care/sleep-accessories/bedding",336,"/kids/baby-care/sleep-accessories/heating-pads-and-electric-blankets",337,"/kids/baby-care/nursing-and-feeding/cutlery",338,"/kids/baby-care/nursing-and-feeding/baby-bottles",339,"/kids/baby-care/nursing-and-feeding/pacifiers-dummies-and-soothers","/kids/baby-care/nursing-and-feeding/dishes",341,"/kids/baby-care/nursing-and-feeding/flasks-and-bottle-warmers",342,"/kids/baby-care/nursing-and-feeding/other-nursing-and-feeding-items",343,"/kids/boys-clothing/baby-clothing/rompers",344,"/kids/boys-clothing/baby-clothing/bodysuits",345,"/kids/boys-clothing/baby-clothing/dungarees",346,"/kids/boys-clothing/baby-clothing/sets",347,"/kids/boys-clothing/outerwear/gilets-and-body-warmers",348,"/kids/boys-clothing/shoes/baby-shoes",349,"/kids/boys-clothing/shoes/formal-and-special-occasion-shoes",350,"/kids/boys-clothing/shoes/slippers",351,"/kids/boys-clothing/tops-and-t-shirts/t-shirts",352,"/kids/boys-clothing/tops-and-t-shirts/polo-shirts",353,"/kids/boys-clothing/tops-and-t-shirts/shirts",354,"/kids/boys-clothing/tops-and-t-shirts/short-sleeved-tops",355,"/kids/boys-clothing/tops-and-t-shirts/long-sleeved-tops",356,"/kids/boys-clothing/tops-and-t-shirts/sleeveless-tops",357,"/kids/boys-clothing/jumpers-and-hoodies-1668",358,"/kids/boys-clothing/jumpers-and-hoodies/v-neck-jumpers",359,"/kids/boys-clothing/jumpers-and-hoodies/turtleneck-jumpers",360,"/kids/boys-clothing/jumpers-and-hoodies/zip-up-jumpers",361,"/kids/boys-clothing/jumpers-and-hoodies/hoodies-and-sweatshirts",362,"/kids/boys-clothing/jumpers-and-hoodies/sleeveless-jumpers",363,"/kids/baby-care/baby-carriers-and-wraps",364,"/kids/baby-care/swimming-equipment",365,"/kids/baby-care/nappies-and-skincare-1678",366,"/kids/baby-care/nappies-and-skincare/baby-hygiene",367,"/kids/baby-care/nappies-and-skincare/baby-changing-bags",368,"/kids/baby-care/childcare-accessories-and-tech/baby-monitors",369,"/kids/baby-care/childcare-accessories-and-tech/food-heaters",370,"/kids/baby-care/childcare-accessories-and-tech/breast-pumps-and-accessories",371,"/kids/baby-care/childcare-accessories-and-tech/sterilisers",372,"/kids/baby-care/childcare-accessories-and-tech/thermometers-and-scales",373,"/kids/baby-care/bouncers-and-swings-1688",374,"/kids/baby-care/bouncers-and-swings/swings",375,"/kids/baby-care/bibs",376,"/kids/baby-care/potties",377,"/kids/baby-care/childproofing-and-safety/childproofing-gates-and-guards",378,"/kids/boys-clothing/trousers-and-dungarees/jeans",379,"/kids/boys-clothing/trousers-and-dungarees/skinny-trousers",380,"/kids/boys-clothing/trousers-and-dungarees/wide-leg-trousers",381,"/kids/baby-care/childproofing-and-safety-equipment/car-sun-shades-and-screens",382,"/kids/boys-clothing/trousers-and-dungarees/leggings",383,"/kids/boys-clothing/trousers-and-dungarees/jumpsuits-and-dungarees",384,"/kids/baby-care/childproofing-and-safety-equipment/cycling-and-roller-skating-safety-equipment",385,"/kids/toys-and-games/electronic-games",386,"/kids/toys-and-games/action-figures",387,"/kids/toys-and-games/dolls",388,"/kids/boys-clothing/accessories/gloves",389,"/kids/boys-clothing/accessories/scarves-and-shawls",390,"/kids/boys-clothing/accessories/belts",391,"/kids/boys-clothing/accessories/wallets",392,"/kids/boys-clothing/accessories/ties-and-bow-ties",393,"/kids/boys-clothing/accessories/other-accessories",394,"/kids/boys-clothing/accessories/caps-and-hats",395,"/kids/boys-clothing/swimwear/swimming-trunks",396,"/kids/boys-clothing/swimwear/bathrobes",397,"/kids/boys-clothing/sleepwear/one-piece-pyjamas",398,"/kids/boys-clothing/sleepwear/two-piece-pyjamas",399,"/kids/boys-clothing/underwear-and-socks/socks",400,"/kids/boys-clothing/underwear-and-socks/tights-and-leggings",401,"/kids/boys-clothing/underwear-and-socks/underwear",402,"/kids/boys-clothing/clothing-bundles",403,"/kids/boys-clothing/clothing-for-twins",404,"/kids/boys-clothing/fancy-dress-and-costumes",405,"/kids/toys-and-games/educational-toys-and-games",406,"/kids/toys-and-games/soft-toys-and-stuffed-animals",407,"/kids/toys-and-games/rattles-and-chew-toys",408,"/kids/toys-and-games/musical-toys",409,"/kids/toys-and-games/construction-toys",410,"/kids/toys-and-games/wooden-toys",411,"/kids/toys-and-games/hanging-mobiles",412,"/kids/toys-and-games/water-toys-and-games",413,"/kids/toys-and-games/outdoor-toys-and-games",414,"/kids/baby-care/childproofing-and-safety-equipment/other-childproofing-and-safety-equipment",415,"/women/clothes/coats-and-jackets/capes-and-ponchos",416,"/women/clothes/dresses/special-occasion-dresses/party-and-cocktail-dresses",417,"/women/clothes/dresses/special-occasion-dresses/wedding-dresses",418,"/women/clothes/dresses/special-occasion-dresses/prom-dresses",419,"/women/clothes/dresses/special-occasion-dresses/evening-dresses",420,"/women/clothes/dresses/winter-dresses",421,"/women/clothes/swimwear/cover-ups-and-sarongs",422,"/women/clothes/lingerie-and-nightwear/shapewear",423,"/women/clothes/costumes-and-special-outfits",424,"/women/bags/satchels",425,"/women/accessories/jewellery/anklets",426,"/men/clothes/suits-and-blazers/suit-jackets-and-blazers",427,"/men/clothes/suits-and-blazers/suit-trousers",428,"/men/clothes/suits-and-blazers/waistcoats",429,"/men/clothes/suits-and-blazers/suit-sets",430,"/men/clothes/suits-and-blazers/wedding-suits",431,"/men/shoes/boots/wellington-boots",432,"/men/accessories/bags-and-backpacks/satchels",433,"/men/accessories/bags-and-backpacks/holdalls",434,"/men/accessories/bags-and-backpacks/bum-bags",435,"/men/accessories/jewellery/cufflinks",436,"/men/clothes/tops-and-t-shirts/shirts/checked-shirts",437,"/men/clothes/tops-and-t-shirts/shirts/denim-shirts",438,"/men/clothes/tops-and-t-shirts/shirts/plain-shirts",439,"/men/clothes/tops-and-t-shirts/shirts/print-shirts",440,"/men/clothes/tops-and-t-shirts/shirts/striped-shirts",441,"/men/clothes/tops-and-t-shirts/t-shirts/plain-t-shirts",442,"/men/clothes/tops-and-t-shirts/t-shirts/print-t-shirts",443,"/men/clothes/tops-and-t-shirts/t-shirts/striped-t-shirts",444,"/men/clothes/tops-and-t-shirts/t-shirts/polo-shirts",445,"/men/clothes/tops-and-t-shirts/t-shirts/long-sleeved-t-shirts",446,"/men/clothes/jumpers-and-sweaters-1811",447,"/men/clothes/jumpers-and-sweaters/zip-through-hoodies",448,"/men/clothes/jumpers-and-sweaters/crew-neck-jumpers",449,"/men/clothes/jumpers-and-sweaters/long-jumpers",450,"/men/clothes/jumpers-and-sweaters/chunky-knit-jumpers",451,"/men/clothes/jeans/ripped-jeans",452,"/men/clothes/jeans/skinny-jeans",453,"/men/clothes/jeans/slim-fit-jeans",454,"/men/clothes/jeans/straight-fit-jeans",455,"/men/clothes/trousers/chinos",456,"/men/clothes/trousers/joggers",457,"/men/clothes/shorts/cargo-shorts",458,"/men/clothes/shorts/chino-shorts",459,"/men/clothes/shorts/denim-shorts",460,"/men/clothes/jumpers-and-sweaters/sleeveless-jumpers",461,"/men/grooming/tools-and-accessories/shaving-tools",462,"/men/grooming/tools-and-accessories/grooming-tools",463,"/men/clothes/socks-and-underwear-1828",464,"/men/clothes/socks-and-underwear/pants-and-boxers",465,"/men/clothes/socks-and-underwear/dressing-gowns",466,"/women/clothes/coats-and-jackets/trench-coats",467,"/women/clothes/tops-and-t-shirts/bodysuits",468,"/women/clothes/tops-and-t-shirts/peplum-tops",469,"/women/clothes/shorts-and-cropped-trousers/low-waisted-shorts",470,"/women/clothes/jeans/boyfriend-jeans",471,"/women/clothes/jeans/cropped-jeans",472,"/women/clothes/jeans/flared-jeans",473,"/women/clothes/jeans/high-waisted-jeans",474,"/women/clothes/jeans/ripped-jeans",475,"/women/clothes/jeans/skinny-jeans",476,"/women/clothes/jeans/straight-jeans",477,"/women/clothes/trousers-and-leggings/straight-leg-trousers",478,"/women/clothes/lingerie-and-nightwear/lingerie-accessories",479,"/women/bags/bum-bags",480,"/women/bags/holdalls",481,"/women/bags/luggage-and-suitcases",482,"/women/accessories/umbrellas",483,"/women/accessories/keyrings",484,"/men/clothes/coats-and-jackets/jackets/fleece-jackets",485,"/men/clothes/coats-and-jackets/raincoats",486,"/men/clothes/coats-and-jackets/peacoats",487,"/men/accessories/bags-and-backpacks/luggage",488,"/men/grooming/grooming-kits",489,"/women/clothes/jeans/other",490,"/men/clothes/tops-and-t-shirts/shirts/other-shirts",491,"/men/clothes/suits-and-blazers/other-suits-and-blazers",492,"/men/clothes/socks-and-underwear/other-socks-and-underwear",493,"/men/clothes/tops-and-t-shirts/t-shirts/other-t-shirts",494,"/kids/boys-clothing/trousers-shorts-and-dungarees/other-trousers-shorts-and-dungarees",495,"/kids/boys-clothing/underwear-and-socks/other-underwear-and-socks",496,"/kids/girls-clothing/underwear-and-socks/other-underwear-and-socks",497,"/women/clothes/jumpers-and-sweaters/waistcoats",498,"/kids/girls-clothing/baby-clothing/others",499,"/kids/girls-clothing/jumpers-and-hoodies/other-jumpers-and-hoodies",500,"/kids/girls-clothing/tops-and-t-shirts/other-tops-and-t-shirts",501,"/kids/girls-clothing/trousers-shorts-and-dungarees/other-trousers-shorts-and-dungarees",502,"/kids/girls-clothing/accessories/other-accessories",503,"/kids/boys-clothing/baby-clothing/other-baby-clothing",504,"/kids/boys-clothing/tops-and-t-shirts/other-tops-and-t-shirts",505,"/kids/boys-clothing/jumpers-and-hoodies/other-jumpers-and-hoodies",506,"/women/beauty/hair-care",507,"/women/beauty/beauty-tools/hair-styling-tools",508,"/home/textiles/blankets",509,"/home/textiles/table-linen",510,"/home/textiles/tapestries-and-wall-hangings",511,"/home/home-accessories/picture-and-photo-frames",512,"/home/home-accessories/vases",513,"/home/home-accessories/display-shelves",514,"/home/textiles/bedding/bedding-sets",515,"/home/textiles/bedding/duvet-covers",516,"/home/textiles/bedding/pillowcases",517,"/home/textiles/bedding/sheets",518,"/home/textiles/curtains-and-drapes/opaque-curtains-and-drapes",519,"/home/textiles/towels/bath-towels",520,"/home/textiles/towels/beach-towels",521,"/home/textiles/towels/hand-towels",522,"/home/tableware/cutlery/cutlery-sets",523,"/home/tableware/cutlery/forks",524,"/home/tableware/cutlery/spoons",525,"/home/textiles/rugs-and-mats/doormats-and-floor-mats",526,"/home/textiles/rugs-and-mats-1954",527,"/home/textiles/curtains-and-drapes/sheer-curtains-and-drapes",528,"/home/home-accessories/candles-and-candle-holders-1956",529,"/home/home-accessories/candles-and-candle-holders/candle-holders",530,"/home/tableware/dinnerware/dinner-sets",531,"/home/tableware/dinnerware/bowls",532,"/home/tableware/dinnerware/plates",533,"/home/tableware/dinnerware/trays",534,"/home/home-accessories/storage/baskets",535,"/home/home-accessories/storage/boxes",536,"/home/home-accessories/storage/jewellery-organisers",537,"/home/home-accessories/storage/make-up-organisers",538,"/home/home-accessories/clocks/table-clocks",539,"/home/home-accessories/clocks/wall-clocks",540,"/home/home-accessories/mirrors/wall-mirrors",541,"/home/home-accessories/mirrors/table-mirrors",542,"/home/tableware/cutlery/table-knives",543,"/home/textiles/cushions",544,"/home/tableware/drinkware/cups-and-mugs",545,"/home/tableware/drinkware/coffeepots-and-teapots-2007",546,"/home/tableware/drinkware/jugs",547,"/home/tableware/drinkware/stemmed-glasses",548,"/home/tableware/drinkware/tumblers",549,"/home/tableware/drinkware/drinkware-sets",550,"/home/home-accessories/storage/clothes-bags-and-hangers",551,"/kids/girls-clothing/trousers-and-shorts/harem-trousers",552,"/kids/girls-clothing/formal-wear-and-special-occasion-clothing",553,"/kids/boys-clothing/trousers-and-dungarees/harem-trousers",554,"/kids/boys-clothing/formal-wear-and-special-occasion-clothing",555,"/women/clothes/maternity-clothes/sport-clothes",556,"/kids/toys-and-games/kitchen-toys",557,"/kids/toys-and-games/sleeping-toys",558,"/kids/baby-care/nappies-and-skincare/nappy-waste-containers",559,"/kids/baby-care/nursing-and-feeding/feeding-pillows-2088",560,"/pet-care/cats/beds",561,"/pet-care/cats/bowls-and-feeders-2099",562,"/pet-care/dogs/bowls-and-feeders-2117",563,"/pet-care/dogs/bowls-and-feeders/feeders",564,"/pet-care/dogs/clothing-and-accessories/coats-and-jackets",565,"/pet-care/dogs/clothing-and-accessories/shoes-and-boots",566,"/pet-care/dogs/clothing-and-accessories/accessories",567,"/pet-care/dogs/collars-and-leads-2122",568,"/pet-care/dogs/collars-and-leads/leads",569,"/pet-care/dogs/collars-and-leads/harnesses",570,"/pet-care/cats/bowls-and-feeders/feeders",571,"/pet-care/cats/clothing-and-accessories-2128",572,"/pet-care/cats/clothing-and-accessories/costumes",573,"/pet-care/cats/clothing-and-accessories/accessories",574,"/pet-care/cats/collars-and-leads-2133",575,"/pet-care/cats/collars-and-leads/harnesses-and-leads",576,"/pet-care/small-pets/habitats-and-accessories",577,"/pet-care/small-pets/toys",578,"/entertainment/games-and-puzzles/board-games",579,"/entertainment/games-and-puzzles/card-games",580,"/entertainment/music-and-video/cds",581,"/entertainment/music-and-video/cassettes",582,"/entertainment/music-and-video/vinyl",583,"/entertainment/music-and-video/older-audio-formats",584,"/entertainment/music-and-video/video/dvd",585,"/entertainment/music-and-video/video/vhs",586,"/entertainment/books/literature-and-fiction/classical-literature",587,"/entertainment/books/literature-and-fiction/comics-and-graphic-novels",588,"/entertainment/books/literature-and-fiction/contemporary-fiction",589,"/entertainment/books/literature-and-fiction/crime-and-thrillers",590,"/entertainment/books/literature-and-fiction/humour",591,"/entertainment/books/literature-and-fiction/poetry-and-drama",592,"/entertainment/books/literature-and-fiction/romance",593,"/entertainment/books/literature-and-fiction/science-fiction-and-fantasy",594,"/entertainment/books/literature-and-fiction/other-literature-and-fiction",595,"/entertainment/books/non-fiction/arts-and-entertainment",596,"/entertainment/books/non-fiction/biography",597,"/entertainment/books/non-fiction/business-and-finance",598,"/entertainment/books/non-fiction/computers-and-tech",599,"/entertainment/books/non-fiction/food-and-drink",600,"/entertainment/books/non-fiction/health-and-wellbeing",601,"/entertainment/books/non-fiction/history",602,"/entertainment/books/non-fiction/hobbies-crafts-and-diy",603,"/entertainment/books/non-fiction/parenting-and-family",604,"/entertainment/books/non-fiction/politics-and-society",605,"/entertainment/books/non-fiction/professional-and-technical",606,"/entertainment/books/non-fiction/reference",607,"/entertainment/books/non-fiction/religion-and-spirituality",608,"/entertainment/books/non-fiction/science-and-nature",609,"/entertainment/books/non-fiction/sports",610,"/entertainment/books/non-fiction/study-materials-and-textbooks",611,"/entertainment/books/non-fiction/travel",612,"/entertainment/books/non-fiction/other-non-fiction",613,"/entertainment/books/kids-and-young-adults/young-adults",614,"/entertainment/books/kids-and-young-adults-2364",615,"/entertainment/books/kids-and-young-adults/babies-and-toddlers",616,"/entertainment/video-games-and-consoles/pc-games-2368",617,"/entertainment/video-games-and-consoles/xbox-series-x-and-s/games",618,"/entertainment/video-games-and-consoles/xbox-series-x-and-s/consoles",619,"/entertainment/video-games-and-consoles/xbox-series-x-and-s/accessories",620,"/entertainment/video-games-and-consoles/xbox-one/games",621,"/entertainment/video-games-and-consoles/xbox-one/consoles",622,"/entertainment/video-games-and-consoles/xbox-one/accessories",623,"/entertainment/video-games-and-consoles/older-xbox/games",624,"/entertainment/video-games-and-consoles/older-xbox/consoles",625,"/entertainment/video-games-and-consoles/older-xbox/accessories",626,"/entertainment/video-games-and-consoles/playstation-5/games",627,"/entertainment/video-games-and-consoles/playstation-5/consoles",628,"/entertainment/video-games-and-consoles/playstation-5/accessories",629,"/entertainment/video-games-and-consoles/playstation-4/games",630,"/entertainment/video-games-and-consoles/playstation-4/consoles",631,"/entertainment/video-games-and-consoles/playstation-4/accessories",632,"/entertainment/video-games-and-consoles/older-playstation/games",633,"/entertainment/video-games-and-consoles/older-playstation/consoles",634,"/entertainment/video-games-and-consoles/older-playstation/accessories",635,"/entertainment/video-games-and-consoles/nintendo-switch/games",636,"/entertainment/video-games-and-consoles/nintendo-switch/consoles",637,"/entertainment/video-games-and-consoles/nintendo-switch/accessories",638,"/entertainment/video-games-and-consoles/nintendo-wii-and-wii-u/games",639,"/entertainment/video-games-and-consoles/nintendo-wii-and-wii-u/consoles",640,"/entertainment/video-games-and-consoles/nintendo-wii-and-wii-u/accessories",641,"/entertainment/video-games-and-consoles/nintendo-3ds-and-2ds/games",642,"/entertainment/video-games-and-consoles/nintendo-3ds-and-2ds/consoles",643,"/entertainment/video-games-and-consoles/nintendo-3ds-and-2ds/accessories",644,"/entertainment/video-games-and-consoles/nintendo-game-boy/games",645,"/entertainment/video-games-and-consoles/nintendo-game-boy/consoles",646,"/entertainment/video-games-and-consoles/nintendo-game-boy/accessories",647,"/entertainment/video-games-and-consoles/older-nintendo/games",648,"/entertainment/video-games-and-consoles/older-nintendo/consoles",649,"/entertainment/video-games-and-consoles/older-nintendo/accessories",650,"/entertainment/video-games-and-consoles/retro-gaming/steam",651,"/entertainment/video-games-and-consoles/retro-gaming/intellivision",652,"/entertainment/video-games-and-consoles/retro-gaming/atari",653,"/entertainment/video-games-and-consoles/retro-gaming/colecovision",654,"/entertainment/video-games-and-consoles/retro-gaming/commodore",655,"/entertainment/video-games-and-consoles/retro-gaming/-3do",656,"/entertainment/video-games-and-consoles/virtual-reality/games",657,"/entertainment/video-games-and-consoles/virtual-reality/consoles",658,"/entertainment/video-games-and-consoles/virtual-reality/accessories",659,"/entertainment/video-games-and-consoles/sega/games",660,"/entertainment/video-games-and-consoles/sega/consoles",661,"/entertainment/video-games-and-consoles/sega/accessories",662,"/entertainment/games-and-puzzles/tile-based-games",663,"/entertainment/games-and-puzzles/jigsaw-puzzles",664,"/entertainment/games-and-puzzles/brain-teasers-and-puzzles",665,"/entertainment/games-and-puzzles/travel-and-pocket-games",666,"/entertainment/games-and-puzzles/tabletop-and-miniature-gaming",667,"/entertainment/games-and-puzzles/stacking-and-balancing-games",668,"/entertainment/games-and-puzzles/floor-games",669,"/pet-care/dogs/clothing-and-accessories/jumpers",670,"/pet-care/cats/litter-boxes",671,"/pet-care/fish/decorations-and-accessories",672,"/pet-care/fish/aquarium-equipment",673,"/pet-care/birds/toys",674,"/pet-care/birds/cages-and-accessories",675,"/pet-care/reptiles/decorations-and-accessories",676,"/pet-care/reptiles/terrarium-equipment",677,"/pet-care/cats/grooming/brushes-and-combs",678,"/pet-care/cats/grooming/claw-care",679,"/pet-care/cats/travel-carriers/hard-carriers",680,"/pet-care/cats/travel-carriers/soft-carriers-and-backpacks",681,"/pet-care/cats/toys/teasers-and-wands",682,"/pet-care/cats/toys/balls",683,"/pet-care/cats/toys/soft-toys",684,"/pet-care/cats/toys/scratchers",685,"/pet-care/cats/toys/interactive-toys",686,"/pet-care/dogs/grooming/claw-care",687,"/pet-care/dogs/grooming/brushes-and-combs",688,"/pet-care/dogs/carriers-and-crates/crates",689,"/pet-care/dogs/carriers-and-crates/travel-carriers",690,"/pet-care/dogs/training-accessories/bags",691,"/pet-care/dogs/training-accessories/whistles",692,"/pet-care/dogs/beds-and-blankets/blankets",693,"/pet-care/dogs/beds-and-blankets-2512",694,"/pet-care/dogs/toys/tough-and-durable-toys",695,"/pet-care/dogs/toys/soft-toys",696,"/pet-care/dogs/toys/balls-and-fetch-toys",697,"/pet-care/dogs/collars-and-leads/muzzles",698,"/pet-care/dogs/clothing-and-accessories/t-shirts",699,"/pet-care/dogs/clothing-and-accessories/costumes",700,"/entertainment/music-and-video/video/blu-ray",701,"/women/clothes/outerwear/gilets-and-body-warmers",702,"/women/clothes/outerwear/coats/duffle-coats",703,"/women/clothes/outerwear/coats/overcoats-and-long-coats",704,"/women/clothes/outerwear/jackets/biker-and-racer-jackets",705,"/women/clothes/outerwear/jackets/field-and-utility-jackets",706,"/women/clothes/outerwear/jackets/shackets",707,"/women/clothes/outerwear/jackets/ski-and-snowboard-jackets",708,"/women/clothes/outerwear/jackets/varsity-jackets",709,"/women/clothes/outerwear/jackets/windbreakers",710,"/men/clothes/outerwear/coats/overcoats-and-long-coats",711,"/men/clothes/outerwear/jackets/biker-and-racer-jackets",712,"/men/clothes/outerwear/jackets/field-and-utility-jackets",713,"/men/clothes/outerwear/jackets/puffer-jackets",714,"/men/clothes/outerwear/jackets/quilted-jackets",715,"/men/clothes/outerwear/jackets/shackets",716,"/men/clothes/outerwear/jackets/ski-and-snowboard-jackets",717,"/kids/girls-clothing/outerwear/coats/duffle-coats",718,"/kids/girls-clothing/outerwear/coats/parkas",719,"/kids/girls-clothing/outerwear/coats/peacoats",720,"/kids/girls-clothing/outerwear/coats/trench-coats",721,"/kids/girls-clothing/outerwear/jackets/blazers",722,"/kids/girls-clothing/outerwear/jackets/bomber-jackets",723,"/kids/girls-clothing/outerwear/jackets/denim-jackets",724,"/kids/girls-clothing/outerwear/jackets/fleece-jackets",725,"/kids/girls-clothing/outerwear/jackets/puffer-jackets",726,"/kids/girls-clothing/outerwear/jackets/windbreakers",727,"/men/clothes/outerwear/jackets/varsity-jackets",728,"/men/clothes/outerwear/jackets/windbreakers",729,"/men/clothes/outerwear/ponchos",730,"/men/clothes/outerwear/gilets-and-body-warmers",731,"/kids/girls-clothing/outerwear/rain-gear/rain-trousers",732,"/kids/girls-clothing/outerwear/rain-gear/ponchos",733,"/kids/girls-clothing/outerwear/rain-gear/rain-suits-and-sets",734,"/kids/girls-clothing/outerwear/rain-gear/raincoats",735,"/kids/girls-clothing/outerwear/snow-gear/snow-jackets-and-coats",736,"/kids/boys-clothing/outerwear/coats/duffle-coats",737,"/kids/boys-clothing/outerwear/coats/parkas",738,"/kids/boys-clothing/outerwear/coats/peacoats",739,"/kids/boys-clothing/outerwear/coats/trench-coats",740,"/kids/girls-clothing/outerwear/snow-gear/snow-suits-and-sets",741,"/kids/boys-clothing/outerwear/jackets/blazers",742,"/kids/boys-clothing/outerwear/jackets/bomber-jackets",743,"/kids/boys-clothing/outerwear/jackets/denim-jackets",744,"/kids/boys-clothing/outerwear/jackets/fleece-jackets",745,"/kids/boys-clothing/outerwear/jackets/puffer-jackets",746,"/kids/boys-clothing/outerwear/jackets/windbreakers",747,"/kids/girls-clothing/outerwear/snow-gear/snow-trousers",748,"/women/clothes/outerwear/jackets/quilted-jackets",749,"/kids/boys-clothing/outerwear/rain-gear/rain-trousers",750,"/kids/boys-clothing/outerwear/rain-gear/ponchos",751,"/kids/boys-clothing/outerwear/rain-gear/raincoats",752,"/kids/boys-clothing/outerwear/rain-gear/rain-suits-and-sets",753,"/kids/boys-clothing/outerwear/snow-gear/snow-jackets-and-coats",754,"/kids/boys-clothing/outerwear/snow-gear/snow-trousers",755,"/kids/boys-clothing/outerwear/snow-gear/snow-suits-and-sets",756,"/women/clothes/outerwear/jackets/puffer-jackets",757,"/women/shoes/boots/ankle-boots",758,"/women/shoes/boots/mid-calf-boots",759,"/women/shoes/boots/over-the-knee-boots",760,"/women/shoes/boots/snow-boots",761,"/women/shoes/boots/work-boots",762,"/women/shoes/clogs-and-mules",763,"/women/shoes/trainers",764,"/women/shoes/flat-shoes/boat-shoes-loafers-and-moccasins",765,"/women/shoes/flat-shoes/espadrilles",766,"/women/shoes/flat-shoes/lace-up-shoes",767,"/women/shoes/flip-flops-flat-sandals-and-slides/flip-flops",768,"/women/shoes/flip-flops-flat-sandals-and-slides/flat-sandals",769,"/women/shoes/flip-flops-flat-sandals-and-slides/slides",770,"/women/shoes/sports-shoes/basketball-shoes",771,"/women/shoes/sports-shoes/climbing-and-bouldering-shoes",772,"/women/shoes/sports-shoes/cycling-shoes",773,"/women/shoes/sports-shoes/dance-shoes",774,"/women/shoes/sports-shoes/football-boots",775,"/women/shoes/sports-shoes/golf-shoes",776,"/women/shoes/sports-shoes/hiking-boots-and-shoes",777,"/women/shoes/sports-shoes/ice-skates",778,"/women/shoes/sports-shoes/indoor-football-shoes",779,"/women/shoes/sports-shoes/indoor-training-shoes-2648",780,"/women/shoes/sports-shoes/motorcycle-boots",781,"/women/shoes/sports-shoes/roller-skates-and-inline-skates",782,"/women/shoes/sports-shoes/running-shoes-2651",783,"/women/shoes/sports-shoes/ski-boots",784,"/women/shoes/sports-shoes/snowboard-boots",785,"/women/shoes/sports-shoes/swimming-and-water-shoes",786,"/women/shoes/sports-shoes/tennis-shoes",787,"/men/shoes/boat-shoes-loafers-and-moccasins",788,"/men/shoes/espadrilles",789,"/men/shoes/slippers",790,"/men/shoes/boots/chelsea-and-slip-on-boots",791,"/men/shoes/boots/desert-and-lace-up-boots",792,"/men/shoes/boots/snow-boots",793,"/men/shoes/boots/work-boots",794,"/men/shoes/flip-flops-sandals-and-slides/clogs-and-mules",795,"/men/shoes/flip-flops-sandals-and-slides/flip-flops",796,"/men/shoes/flip-flops-sandals-and-slides/sandals",797,"/men/shoes/flip-flops-sandals-and-slides/slides",798,"/men/shoes/formal-shoes/lace-up-shoes",799,"/men/shoes/formal-shoes/slip-on-shoes",800,"/men/shoes/formal-shoes/monk-strap-shoes",801,"/men/shoes/sports-shoes/basketball-shoes",802,"/men/shoes/sports-shoes/climbing-and-bouldering-shoes",803,"/men/shoes/sports-shoes/cycling-shoes",804,"/men/shoes/sports-shoes/dance-shoes",805,"/men/shoes/sports-shoes/football-boots",806,"/men/shoes/sports-shoes/golf-shoes",807,"/men/shoes/sports-shoes/hiking-boots-and-shoes",808,"/men/shoes/sports-shoes/ice-skates",809,"/men/shoes/sports-shoes/indoor-football-shoes",810,"/men/shoes/sports-shoes/motorcycle-boots",811,"/men/shoes/sports-shoes/roller-skates-and-inline-skates",812,"/men/shoes/sports-shoes/ski-boots",813,"/men/shoes/sports-shoes/snowboard-boots",814,"/men/shoes/sports-shoes/swimming-and-water-shoes",815,"/men/shoes/sports-shoes/tennis-shoes",816,"/women/shoes/heels/court-shoes",817,"/women/shoes/heels/high-heeled-sandals",818,"/women/shoes/flat-shoes/mary-janes",819,"/kids/girls-clothing/shoes/clogs-and-mules",820,"/kids/girls-clothing/shoes/heels",821,"/kids/girls-clothing/shoes/boots/ankle-boots",822,"/kids/girls-clothing/shoes/boots/mid-calf-boots",823,"/kids/girls-clothing/shoes/boots/snow-boots",824,"/kids/girls-clothing/shoes/boots/wellington-boots",825,"/kids/girls-clothing/shoes/flat-shoes/espadrilles",826,"/kids/girls-clothing/shoes/flat-shoes/lace-up-shoes",827,"/kids/girls-clothing/shoes/flip-flops-sandals-and-slides/flip-flops",828,"/kids/girls-clothing/shoes/flip-flops-sandals-and-slides/sandals",829,"/kids/girls-clothing/shoes/flip-flops-sandals-and-slides/slides",830,"/kids/girls-clothing/shoes/sports-shoes/basketball-shoes",831,"/kids/girls-clothing/shoes/sports-shoes/dance-shoes",832,"/kids/girls-clothing/shoes/sports-shoes/football-boots",833,"/kids/girls-clothing/shoes/sports-shoes/hiking-boots-and-shoes",834,"/kids/girls-clothing/shoes/sports-shoes/ice-skates",835,"/kids/girls-clothing/shoes/sports-shoes/roller-skates-and-inline-skates",836,"/kids/girls-clothing/shoes/sports-shoes/running-shoes",837,"/kids/girls-clothing/shoes/sports-shoes/ski-boots",838,"/kids/girls-clothing/shoes/sports-shoes/snowboard-boots",839,"/kids/girls-clothing/shoes/sports-shoes/swimming-and-water-shoes",840,"/kids/girls-clothing/shoes/trainers/hook-and-loop-trainers",841,"/kids/girls-clothing/shoes/trainers/lace-up-trainers",842,"/kids/girls-clothing/shoes/trainers/slip-on-trainers",843,"/kids/boys-clothing/shoes/boat-shoes-loafers-and-moccasins",844,"/kids/boys-clothing/shoes/espadrilles",845,"/kids/boys-clothing/shoes/boots/ankle-boots",846,"/kids/boys-clothing/shoes/boots/mid-calf-boots",847,"/kids/boys-clothing/shoes/boots/snow-boots",848,"/kids/boys-clothing/shoes/boots/wellington-boots",849,"/kids/boys-clothing/shoes/flip-flops-sandals-and-slides/clogs-and-mules",850,"/kids/boys-clothing/shoes/flip-flops-sandals-and-slides/flip-flops",851,"/kids/boys-clothing/shoes/flip-flops-sandals-and-slides/sandals",852,"/kids/boys-clothing/shoes/flip-flops-sandals-and-slides/slides",853,"/kids/boys-clothing/shoes/sports-shoes/basketball-shoes",854,"/kids/boys-clothing/shoes/sports-shoes/dance-shoes",855,"/kids/boys-clothing/shoes/sports-shoes/football-boots",856,"/kids/boys-clothing/shoes/sports-shoes/hiking-boots-and-shoes",857,"/kids/boys-clothing/shoes/sports-shoes/ice-skates",858,"/kids/boys-clothing/shoes/sports-shoes/roller-skates-and-inline-skates",859,"/kids/boys-clothing/shoes/sports-shoes/running-shoes",860,"/kids/boys-clothing/shoes/sports-shoes/ski-boots",861,"/kids/boys-clothing/shoes/sports-shoes/snowboard-boots",862,"/kids/boys-clothing/shoes/sports-shoes/swimming-and-water-shoes",863,"/kids/boys-clothing/shoes/trainers/hook-and-loop-trainers",864,"/kids/boys-clothing/shoes/trainers/lace-up-trainers",865,"/kids/boys-clothing/shoes/trainers/slip-on-trainers","/kids/girls-clothing/shoes/flat-shoes/ballerinas-mary-janes-and-t-bar-shoes"]#"/women/clothes/tops-and-t-shirts/camis",
def findImage():
    start = gui.locateCenterOnScreen("imageUpload.PNG")
    gui.moveTo(start)
    gui.click()
    time.sleep(2)
    start1 = gui.locateCenterOnScreen("imagePath.PNG")
    gui.moveTo(start1)
    gui.click()
    gui.typewrite('D:\listing images', interval=0.25)
    gui.press('enter')
    time.sleep(3)
    start2 = gui.locateCenterOnScreen("fileName.PNG")
    #gui.displayMousePosition()
    gui.moveTo(start2)
    gui.click()
    gui.typewrite('Game Party Nintendo Wii', interval=0.25)
    time.sleep(3)
    start3 = gui.locateCenterOnScreen("open.PNG")
    gui.moveTo(start3)
    gui.click()
    time.sleep(5)
    #gui.hotkey("ctrl","f")
    return None
def findTitle(obj):
    start = gui.locateCenterOnScreen("title.PNG")
    gui.moveTo(start)
    gui.click()
    gui.typewrite(obj, interval=0.25)
    time.sleep(3)
    return None
def findDescription(obj):
    start = gui.locateCenterOnScreen("describe.PNG")
    gui.moveTo(start)
    gui.click()
    gui.typewrite(obj, interval=0.25)
    time.sleep(3)
    return None
def inspect():
    # gui.hotkey("ctrl", "shift", "I")
    # time.sleep(2)
    # start1 = gui.locateCenterOnScreen("console1.PNG")
    # gui.moveTo(start1)
    # gui.click()
    # time.sleep(3)
    # x, y = gui.locateCenterOnScreen("resetConsole.PNG")
    # gui.moveTo(x, y)
    # gui.click()
    # time.sleep(2)
    return None
def findWomenCategory(obj):
    """women-(700,332)"""
    for u in range(len(obj)):
        gui.click(700, 310)
        time.sleep(2)
        v = u + 1
        if (obj[v] == 'clothes'):
            gui.click(700, 345)
            time.sleep(2)
            w = v + 1
            # gui.mouseInfo()
            if (obj[w] == 'tops-and-t-shirts'):
                gui.hotkey("ctrl", "f")
                gui.click(700, 565)
                time.sleep(2)
                x = w + 1
                # gui.mouseInfo()
                if (obj[x] == 'camis'):  # chelsea & slip on boots=700,350,desert & laseup boots:700,400wellington boots:700,500,work boots:700,540
                    gui.click(700, 440)
                    time.sleep(2)
                    y = x + 1
            if (obj[w] == 'other-clothing'):
                #gui.mouseInfo()
                gui.hotkey("ctrl","f")
                gui.typewrite("other clothing", interval=0.25)
                gui.click(700, 555)
                time.sleep(2)
                x = w + 1
def findMenCategory(obj):
    """men-700,371"""
    for u in range(len(obj)):
        gui.click(700, 350)
        time.sleep(2)
        v = u + 1
        # gui.mouseInfo()
        if (obj[v] == 'shoes'):
            gui.click(700, 400)
            time.sleep(2)
            w = v + 1
            # gui.mouseInfo()
            if (obj[w] == 'boots'):
                gui.click(700, 390)
                time.sleep(2)
                x = w + 1
                # gui.mouseInfo()
                if (obj[x] == 'snow-boots'):  # chelsea & slip on boots=700,350,desert & laseup boots:700,400wellington boots:700,500,work boots:700,540
                    gui.click(700, 445)
                    time.sleep(2)
                    y = x + 1
                    gui.mouseInfo()


def findHomeCategory(obj):
    # home - 700, 460

    return None
def findKidsCategory(obj):
    # kids - 700, 420

    return None
def findEntertainmentCategory(obj):
    #entertainment - 700, 500
    words = obj.split('/')
    start = gui.locateCenterOnScreen("entertainment.PNG")
    gui.moveTo(start)
    gui.click()
    time.sleep(2)
    for x in range(len(words)):
        if words[x] != '':
            print(x)
    return None
def findPetCareCategory(obj):
    # petcare - 700, 550
    words = obj.split('/')
    start = gui.locateCenterOnScreen("petCare.PNG")
    gui.moveTo(start)
    gui.click()
    time.sleep(2)
    for x in range(len(words)):
        if words[x] != '':
            print(x)
    return None

def findCategories(obj):
    gui.hotkey("ctrl","end")
    time.sleep(2)
    start = gui.locateCenterOnScreen("category1.PNG")
    gui.moveTo(start)
    gui.click()
    time.sleep(2)
    for i in k:
        words = i.split('/')
        for u in range(len(words)):
            if words[u]!='':
                if (words[u] == 'women'):#
                    findWomenCategory(words)
                    #gui.mouseInfo()
                if (words[u] == 'men'):
                    findMenCategory(words)
                #gui.mouseInfo()
                elif (words[u] == 'Home'):
                    findHomeCategory(words)
                elif (words[u] == 'Kids'):
                    findKidsCategory(words)
                elif (words[u] == 'Entertainment'):
                    findEntertainmentCategory(words)
                elif (words[u] == 'Pet care'):
                    findPetCareCategory(words)

def postVinted(obj):
    screenWidth, screenHeight = gui.size()
    gui.moveTo(0, screenHeight)
    gui.click()
    gui.typewrite('Chrome', interval=0.25)
    gui.press('enter')
    time.sleep(2)
    gui.hotkey('win', 'up')
    gui.keyDown('alt')
    gui.press(' ')
    gui.press('x')
    gui.keyUp('alt')
    # gui.mouseInfo()
    gui.click(240, 440)
    time.sleep(3)
    gui.hotkey("ctrl", "t")
    time.sleep(1)
    gui.click(200, 51)
    time.sleep(1)
    # gui.hotkey("del")
    time.sleep(1)
    gui.typewrite("https://www.vinted.co.uk/items/new")
    time.sleep(1)
    gui.press('enter')
    time.sleep(3)
    #findImage(obj["imageUrl"])
    #findTitle(obj["title"])
    #findDescription(obj["description"])
    time.sleep(1)
    findCategories(obj["tooltip"])
    gui.hotkey("ctrl", "w")
    # #gui.mouseInfo()
    return None
def job():
    response = requests.get(base+vintedPath,headers=Header)
    k = response.json()
    #print(response)
    for element in k["results"]:
        postVinted(element)
        #response = requests.post(base+listingPath, params={'id':element["id"]}, headers=Header)
        #kk = response.json()
        #,params={'address': location}
        #print("The pastebin URL is:%s" % kk)
        print(element)


def fetchCategories():
    screenWidth, screenHeight = gui.size()
    gui.moveTo(0,screenHeight)
    gui.click()
    gui.typewrite('Chrome', interval=0.25)
    gui.press('enter')
    time.sleep(2)
    gui.hotkey('win', 'up')
    gui.keyDown('alt')
    gui.press(' ')
    gui.press('x')
    gui.keyUp('alt')
    #gui.mouseInfo()
    gui.click(240,440)
    time.sleep(3)
    gui.hotkey("ctrl", "t")
    time.sleep(1)
    gui.click(200,51)
    time.sleep(1)
    #gui.hotkey("del")
    time.sleep(1)
    gui.typewrite("https://www.vinted.co.uk/entertainment/video-games-and-consoles/xbox-one/games/3227882508-battle-crashers-xbox-one-game")
    time.sleep(1)
    #gui.mouseInfo()
    gui.press('enter')
    time.sleep(3)
    gui.hotkey("ctrl","shift","c")
    time.sleep(3)
    image_path = r'C:\Users\yaseen\Downloads\Screenshot from 2023-07-15 11-03-04.png'
    found_images = list(gui.locateAllOnScreen(image_path))
    # Iterate through the found images
    for image_location in found_images:
        # Get the center coordinates of each found image
        image_center = gui.center(image_location)

        # Perform actions using the found image coordinates
        # Example: Move the mouse to the center of the image and click
        gui.moveTo(image_center)
        gui.click()
def identifyloc():
    while True:
        currentMouseX, currentMouseY = gui.position()
        print(currentMouseX,currentMouseY)
        time.sleep(3)
#testChrome()
schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


