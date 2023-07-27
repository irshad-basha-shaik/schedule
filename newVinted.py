import pyautogui as gui, time
import pyperclip

gui.FAILSAFE= False
import schedule
import time
import requests

base="http://localhost:8080"
vintedPath="/api/Vinted/getVintedListing/71527462-excelstuff?status=not sent"
listingPath="/api/Vinted/vintedListingStatus"
Header={'Cookie':'csrftoken=bD0kdBbkK2ufeX55O4XtK4AF6v2k6QD0; JSESSIONID=B425D43584747956FCC39E67EB4AEC8C'}
#kk = ["/women/clothes/tops-and-t-shirts/camis","/women/clothes/other-clothing","/women/accessories/belts","/women/accessories/watches","/women/accessories/sunglasses","/men/clothes/other-mens-clothing","/men/clothes/swimwear","/women/accessories/gloves","/men/accessories/gloves","/men/clothes/costumes-and-special-outfits","/men/accessories/ties-and-pocket-squares","/men/accessories/belts","/men/accessories/watches","/men/accessories/sunglasses","/men/accessories/other","/women/clothes/lingerie-and-nightwear/bras","/women/clothes/lingerie-and-nightwear/panties","/women/clothes/lingerie-and-nightwear/nightwear","/women/clothes/lingerie-and-nightwear/other","/men/grooming/hair-care","/men/grooming/body-care","/men/grooming/hand-and-nail-care","/men/grooming/face-care","/men/grooming/make-up","/men/grooming/aftershave-and-cologne","/women/beauty/perfume","/women/beauty/other-beauty-items","/women/bags/other-bags","/women/bags/handbags","/women/bags/backpacks","/women/bags/shoulder-bags","/women/bags/clutches","/women/bags/purses-and-wallets","/women/bags/make-up-bags","/women/accessories/jewellery/other-jewellery","/women/accessories/jewellery/earrings","/women/accessories/jewellery/necklaces-beads-and-pendants","/women/accessories/jewellery/bracelets","/women/accessories/jewellery/jewellry-sets","/women/accessories/jewellery/brooches","/women/clothes/dresses/other-dresses","/women/clothes/dresses/mini-dresses","/women/clothes/dresses/denim-dresses","/women/clothes/trousers-and-leggings/leather-trousers","/women/clothes/trousers-and-leggings/skinny-trousers","/women/clothes/trousers-and-leggings/tailored-trousers","/women/clothes/trousers-and-leggings/other-trousers","/women/clothes/jumpers-and-sweaters/sweaters/v-neck-sweaters","/women/clothes/jumpers-and-sweaters/sweaters/turtleneck-sweaters","/women/clothes/jumpers-and-sweaters/sweaters/long-jumpers","/women/clothes/jumpers-and-sweaters/sweaters/three-fourths-sleeve-jumpers","/women/clothes/jumpers-and-sweaters/cardigans","/women/clothes/jumpers-and-sweaters/boleros","/women/clothes/jumpers-and-sweaters/hoodies-and-sweatshirts","/women/clothes/jumpers-and-sweaters/other-jumpers-and-sweaters","/women/clothes/skirts/mini-skirts","/women/clothes/skirts/midi-skirts","/women/clothes/skirts/maxi-skirts","/women/clothes/skirts/other-skirts","/women/clothes/shorts-and-cropped-trousers/knee-length-shorts","/women/clothes/shorts-and-cropped-trousers/cropped-trousers","/women/clothes/shorts-and-cropped-trousers/other-shorts-and-cropped-trousers","/women/shoes/boots/knee-high-boots","/women/shoes/boots/wellington-boots","/women/shoes/slippers","/women/clothes/swimwear/one-pieces","/women/clothes/swimwear/bikinis-and-tankinis","/women/clothes/swimwear/other-swimwear-and-beachwear","/women/clothes/tops-and-t-shirts/t-shirts","/women/clothes/tops-and-t-shirts/shirts","/women/clothes/tops-and-t-shirts/short-sleeved-tops","/women/clothes/tops-and-t-shirts/long-sleeved-tops","/women/clothes/tops-and-t-shirts/three-fourths-sleeve-tops","/women/clothes/tops-and-t-shirts/tunics","/women/clothes/tops-and-t-shirts/other-tops-and-t-shirts","/women/clothes/lingerie-and-nightwear/sets","/women/accessories/hats-and-caps/caps","/women/accessories/hats-and-caps-231","/women/accessories/hats-and-caps/warm-hats","/women/accessories/hats-and-caps/berets","/women/accessories/hats-and-caps/headbands","/women/accessories/hats-and-caps/other","/women/accessories/scarves-and-shawls/knit-scarves","/women/accessories/scarves-and-shawls/head-scarfs","/women/accessories/scarves-and-shawls/oversized-scarves-and-shawls","/women/accessories/scarves-and-shawls/shawls","/women/accessories/scarves-and-shawls/other","/men/accessories/jewellery/necklaces-and-pendants","/men/accessories/jewellery/rings","/men/accessories/jewellery/bracelets","/men/accessories/jewellery/other","/men/accessories/bags-and-backpacks/handbags","/men/accessories/bags-and-backpacks/backpacks","/men/accessories/bags-and-backpacks/shoulder-bags","/men/accessories/bags-and-backpacks/wallets","/men/accessories/bags-and-backpacks/other","/men/clothes/trousers/skinny-trousers","/men/clothes/trousers/wide-legged-trousers","/men/clothes/trousers/tailored-trousers","/men/clothes/trousers/other","/men/clothes/jumpers-and-sweaters/v-neck-jumpers","/men/clothes/jumpers-and-sweaters/turtle-neck-jumpers","/men/clothes/jumpers-and-sweaters/cardigans","/men/clothes/jumpers-and-sweaters/hoodies-and-sweatshirts","/men/clothes/jumpers-and-sweaters/other","/men/clothes/trousers/cropped-trousers","/men/clothes/shorts/other-shorts","/men/accessories/scarves-and-shawls/knitted-scarves","/men/accessories/scarves-and-shawls/head-scarves","/men/accessories/scarves-and-shawls/large-scarves-and-shawls","/men/accessories/scarves-and-shawls/other","/men/accessories/hats-and-caps/caps","/men/accessories/hats-and-caps-288","/men/accessories/hats-and-caps/winter-hats","/men/accessories/hats-and-caps/berets","/men/accessories/hats-and-caps/other","/women/clothes/trousers-and-leggings/leggings","/women/clothes/trousers-and-leggings/harem-pants","/women/clothes/jumpers-and-sweaters/sweaters/knitted-jumpers","/women/clothes/suits-and-blazers/blazers","/women/clothes/tops-and-t-shirts/vest-tops","/women/clothes/shorts-and-cropped-trousers/denim-shorts","/women/clothes/skirts/high-waisted-skirts","/women/clothes/skirts/denim-skirts","/women/clothes/skirts/tulip-skirts","/women/clothes/skirts/pencil-skirts","/women/shoes/flats/ballerinas","/women/bags/tote-bags","/women/accessories/jewellery/rings","/men/clothes/tops-and-t-shirts/vests-and-sleeveless-t-shirts","/women/clothes/activewear/outerwear","/women/clothes/activewear/tracksuits","/women/clothes/activewear/trousers","/women/clothes/activewear/dresses","/women/clothes/activewear/skirts","/women/clothes/activewear/tops-and-t-shirts","/women/clothes/activewear/hoodies-and-sweatshirts","/women/clothes/activewear/shorts","/women/clothes/activewear/other-activewear","/men/clothes/activewear/outerwear","/men/clothes/activewear/tracksuits","/men/clothes/activewear/trousers","/men/clothes/activewear/tops-and-t-shirts","/men/clothes/activewear/pullovers-and-sweaters","/men/clothes/activewear/shorts","/men/clothes/activewear/other-activewear","/women/beauty/face-care","/women/beauty/beauty-tools/face-care-tools","/women/beauty/body-care","/women/beauty/beauty-tools/body-care-tools","/women/beauty/nail-care","/women/beauty/beauty-tools/nail-care-tools","/women/beauty/make-up","/women/beauty/beauty-tools/make-up-tools","/men/grooming/other-grooming-items","/men/grooming/tools-and-accessories/other-tools","/women/clothes/lingerie-and-nightwear/dressing-gowns","/women/clothes/tops-and-t-shirts/crop-tops","/women/clothes/tops-and-t-shirts/off-the-shoulder-tops","/women/clothes/tops-and-t-shirts/blouses","/women/clothes/tops-and-t-shirts/halterneck-tops","/women/clothes/tops-and-t-shirts/turtlenecks","/women/clothes/dresses/long-dresses","/women/clothes/dresses/midi-dresses","/women/clothes/dresses/formal-and-work-dresses","/women/clothes/dresses/little-black-dresses","/women/clothes/dresses/casual-dresses","/women/clothes/dresses/special-occasion-dresses/backless-dresses","/women/clothes/dresses/strapless-dresses","/women/clothes/dresses/summer-dresses","/women/clothes/jumpers-and-sweaters/sweaters/other-sweaters","/women/clothes/jumpers-and-sweaters/kimonos","/women/clothes/trousers-and-leggings/cropped-trousers-and-chinos","/women/clothes/trousers-and-leggings/wide-leg-trousers","/women/clothes/outerwear/coats/peacoats","/women/clothes/coats-and-jackets/jackets/bomber-jackets","/women/clothes/coats-and-jackets/jackets/denim-jackets","/women/clothes/coats-and-jackets/raincoats","/women/clothes/coats-and-jackets/jackets/fleece-jackets","/women/clothes/coats-and-jackets/parkas","/women/clothes/coats-and-jackets/faux-fur-coats","/women/clothes/skirts/a-line-skirts","/women/clothes/skirts/bodycon-skirts","/women/clothes/skirts/skater-skirts","/women/clothes/skirts/pleated-skirts","/women/clothes/shorts-and-cropped-trousers/high-waisted-shorts","/women/clothes/shorts-and-cropped-trousers/leather-shorts","/women/clothes/shorts-and-cropped-trousers/lace-shorts","/women/clothes/shorts-and-cropped-trousers/cargo-shorts","/other-bags","/women/accessories/hair-accessories","/women/clothes/suits-and-blazers/trouser-suits","/women/clothes/suits-and-blazers/skirt-suits","/women/clothes/suits-and-blazers/suit-separates","/women/clothes/suits-and-blazers/other-suits-and-blazers","/women/clothes/jumpsuits-and-playsuits-1131","/women/clothes/jumpsuits-and-playsuits/playsuits","/women/clothes/jumpsuits-and-playsuits/other-jumpsuits-and-playsuits","/women/accessories/other-accessories","/women/clothes/maternity-clothes/maternity-trousers","/women/clothes/maternity-clothes/maternity-skirts","/women/clothes/maternity-clothes/maternity-tops","/women/clothes/maternity-clothes/maternity-jumpsuits-and-playsuits","/women/clothes/maternity-clothes/maternity-dresses","/women/clothes/maternity-clothes/maternity-coats-and-jackets","/women/clothes/maternity-clothes/maternity-jumpers-and-sweaters","/women/clothes/maternity-clothes/maternity-shorts","/women/clothes/maternity-clothes/maternity-swimwear-and-beachwear","/kids/boys-clothing/trousers-and-dungarees/shorts-and-cropped-trousers","/kids/boys-clothing/activewear","/kids/boys-clothing/other-boys-clothing","/women/accessories/tech-accessories","/men/clothes/coats-and-jackets/jackets/bomber-jackets","/men/clothes/coats-and-jackets/jackets/denim-jackets","/men/clothes/coats-and-jackets/duffle-coats","/men/clothes/coats-and-jackets/jackets/harrington-jackets","/men/clothes/coats-and-jackets/parkas","/men/clothes/coats-and-jackets/trench-coats","/men/shoes/trainers","/kids/girls-clothing/skirts","/kids/girls-clothing/trousers-and-shorts/shorts-and-cropped-trousers","/kids/girls-clothing/activewear","/kids/girls-clothing/other-girls-clothing","/kids/boys-clothing/bags-and-backpacks","/kids/girls-clothing/bags-and-backpacks","/women/clothes/lingerie-and-nightwear/socks","/women/clothes/lingerie-and-nightwear/tights-and-stockings","/women/beauty/hand-care","/women/clothes/activewear/sports-bras","/women/clothes/activewear/sports-accessories/scarves","/women/clothes/activewear/sports-accessories/glasses","/women/clothes/activewear/sports-accessories/watches-and-wristbands","/women/clothes/activewear/sports-accessories/hats","/women/clothes/activewear/sports-accessories/gloves","/women/clothes/activewear/sports-accessories/protection-slash-padding","/women/clothes/activewear/sports-accessories/other-accessories","/men/shoes/sport-shoes/running-shoes","/men/shoes/sport-shoes/indoor-training-shoes","/men/clothes/activewear/sports-accessories/scarves","/men/clothes/activewear/sports-accessories/glasses","/men/clothes/activewear/sports-accessories/watches-and-wristbands","/men/clothes/activewear/sports-accessories/hats","/men/clothes/activewear/sports-accessories/gloves","/men/clothes/activewear/sports-accessories/protective-items","/men/clothes/activewear/sports-accessories/other-accessories","/women/bags/patterned-and-embroidered-bags","/kids/other-kids-items","/kids/car-seats-and-chairs/car-chairs","/kids/car-seats-and-chairs/feeding-chairs","/kids/school-supplies/school-bags","/kids/school-supplies-1509","/kids/girls-clothing/clothing-bundles","/kids/buggies/buggy-accessories","/kids/buggies/umbrella-buggies","/kids/girls-clothing/baby-clothing/rompers","/kids/girls-clothing/baby-clothing/bodysuits","/kids/girls-clothing/baby-clothing/dungarees","/kids/girls-clothing/baby-clothing/sets","/kids/girls-clothing/outerwear/gilets-and-body-warmers","/kids/girls-clothing/shoes/baby-shoes","/kids/girls-clothing/shoes/formal-and-special-occasion-shoes","/kids/girls-clothing/shoes/slippers","/kids/girls-clothing/tops-and-t-shirts/t-shirts","/kids/girls-clothing/tops-and-t-shirts/polo-shirts","/kids/girls-clothing/tops-and-t-shirts/shirts","/kids/girls-clothing/tops-and-t-shirts/short-sleeved-tops","/kids/girls-clothing/tops-and-t-shirts/long-sleeved-tops","/kids/girls-clothing/tops-and-t-shirts/sleeveless-tops","/kids/girls-clothing/tops-and-t-shirts/tunics","/kids/girls-clothing/jumpers-and-hoodies-1542","/kids/girls-clothing/jumpers-and-hoodies/v-neck-jumpers","/kids/girls-clothing/jumpers-and-hoodies/turtleneck-jumpers","/kids/girls-clothing/jumpers-and-hoodies/zip-up-jumpers","/kids/girls-clothing/jumpers-and-hoodies/boleros","/kids/girls-clothing/jumpers-and-hoodies/hoodies-and-sweatshirts","/kids/girls-clothing/jumpers-and-hoodies/sleeveless-jumpers","/kids/girls-clothing/dresses/long-dresses","/kids/girls-clothing/dresses/short-dresses","/kids/girls-clothing/trousers-and-shorts/jeans","/kids/girls-clothing/trousers-and-shorts/skinny-trousers","/kids/kids-furniture/cribs-and-cradles","/kids/girls-clothing/trousers-and-shorts/wide-leg-trousers","/kids/kids-furniture/cots","/kids/girls-clothing/trousers-and-shorts/leggings","/kids/kids-furniture/toddler-beds","/kids/girls-clothing/trousers-and-shorts/jumpsuits-and-dungarees","/kids/kids-furniture/mattresses/cot-mattresses","/kids/kids-furniture/mattresses/crib-and-cradle-mattresses","/kids/kids-furniture/mattresses/kid-bed-mattresses","/kids/kids-furniture/playmats","/kids/kids-furniture/playpens","/kids/kids-furniture/changing-pads-and-tables","/kids/girls-clothing/accessories/caps-and-hats","/kids/girls-clothing/accessories/gloves","/kids/kids-furniture/other-kids-furniture/chairs","/kids/girls-clothing/accessories/scarves-and-shawls","/kids/girls-clothing/accessories/belts","/kids/girls-clothing/accessories/hairbands-and-hairclips","/kids/girls-clothing/accessories/wallets-and-purses","/kids/kids-furniture/other-kids-furniture/tables","/kids/girls-clothing/accessories/jewellery","/kids/kids-furniture/other-kids-furniture/carpets","/kids/kids-furniture/other-kids-furniture/wardrobes","/kids/kids-furniture/other-kids-furniture/shelves","/kids/girls-clothing/swimwear/one-piece-swimsuits","/kids/kids-furniture/other-kids-furniture/play-furniture","/kids/girls-clothing/swimwear/bikinis-and-tankinis","/kids/girls-clothing/swimwear/bathrobes","/kids/ride-on-toys/bicycle-seats-and-trailers","/kids/girls-clothing/sleepwear/one-piece-pyjamas","/kids/girls-clothing/sleepwear/two-piece-pyjamas","/kids/girls-clothing/sleepwear/nighties","/kids/ride-on-toys/baby-walkers","/kids/girls-clothing/underwear-and-socks/socks","/kids/girls-clothing/underwear-and-socks/tights-and-leggings","/kids/girls-clothing/underwear-and-socks/underwear","/kids/ride-on-toys/push-and-pull-toys","/kids/girls-clothing/clothing-for-twins","/kids/ride-on-toys/scooters","/kids/girls-clothing/fancy-dress-and-costumes","/kids/ride-on-toys/tricycles","/kids/ride-on-toys/bicycles","/kids/ride-on-toys/outdoor-vehicles","/kids/ride-on-toys/sledges-skis-and-snowboards","/kids/buggies/running-and-sport-buggies","/kids/buggies/universal-buggies","/kids/buggies/buggies-for-twins","/women/clothes/maternity-clothes/maternity-underwear-1615","/women/clothes/maternity-clothes/maternity-underwear/sleep-wear","/women/clothes/maternity-clothes/maternity-underwear/pregnancy-and-postpartum-belts","/women/clothes/maternity-clothes/maternity-underwear/pregnancy-and-breastfeeding-bras","/kids/baby-care/sleep-accessories/blankets","/kids/baby-care/sleep-accessories/pillows","/kids/baby-care/sleep-accessories/plaids","/kids/baby-care/sleep-accessories/sleeping-bags","/kids/baby-care/sleep-accessories/bedding","/kids/baby-care/sleep-accessories/heating-pads-and-electric-blankets","/kids/baby-care/nursing-and-feeding/cutlery","/kids/baby-care/nursing-and-feeding/baby-bottles","/kids/baby-care/nursing-and-feeding/pacifiers-dummies-and-soothers","/kids/baby-care/nursing-and-feeding/dishes","/kids/baby-care/nursing-and-feeding/flasks-and-bottle-warmers","/kids/baby-care/nursing-and-feeding/other-nursing-and-feeding-items","/kids/boys-clothing/baby-clothing/rompers","/kids/boys-clothing/baby-clothing/bodysuits","/kids/boys-clothing/baby-clothing/dungarees","/kids/boys-clothing/baby-clothing/sets","/kids/boys-clothing/outerwear/gilets-and-body-warmers","/kids/boys-clothing/shoes/baby-shoes","/kids/boys-clothing/shoes/formal-and-special-occasion-shoes","/kids/boys-clothing/shoes/slippers","/kids/boys-clothing/tops-and-t-shirts/t-shirts","/kids/boys-clothing/tops-and-t-shirts/polo-shirts","/kids/boys-clothing/tops-and-t-shirts/shirts","/kids/boys-clothing/tops-and-t-shirts/short-sleeved-tops","/kids/boys-clothing/tops-and-t-shirts/long-sleeved-tops","/kids/boys-clothing/tops-and-t-shirts/sleeveless-tops","/kids/boys-clothing/jumpers-and-hoodies-1668","/kids/boys-clothing/jumpers-and-hoodies/v-neck-jumpers","/kids/boys-clothing/jumpers-and-hoodies/turtleneck-jumpers","/kids/boys-clothing/jumpers-and-hoodies/zip-up-jumpers","/kids/boys-clothing/jumpers-and-hoodies/hoodies-and-sweatshirts","/kids/boys-clothing/jumpers-and-hoodies/sleeveless-jumpers","/kids/baby-care/baby-carriers-and-wraps","/kids/baby-care/swimming-equipment","/kids/baby-care/nappies-and-skincare-1678","/kids/baby-care/nappies-and-skincare/baby-hygiene","/kids/baby-care/nappies-and-skincare/baby-changing-bags","/kids/baby-care/childcare-accessories-and-tech/baby-monitors","/kids/baby-care/childcare-accessories-and-tech/food-heaters","/kids/baby-care/childcare-accessories-and-tech/breast-pumps-and-accessories","/kids/baby-care/childcare-accessories-and-tech/sterilisers","/kids/baby-care/childcare-accessories-and-tech/thermometers-and-scales","/kids/baby-care/bouncers-and-swings-1688","/kids/baby-care/bouncers-and-swings/swings","/kids/baby-care/bibs","/kids/baby-care/potties","/kids/baby-care/childproofing-and-safety/childproofing-gates-and-guards","/kids/boys-clothing/trousers-and-dungarees/jeans","/kids/boys-clothing/trousers-and-dungarees/skinny-trousers","/kids/boys-clothing/trousers-and-dungarees/wide-leg-trousers","/kids/baby-care/childproofing-and-safety-equipment/car-sun-shades-and-screens","/kids/boys-clothing/trousers-and-dungarees/leggings","/kids/boys-clothing/trousers-and-dungarees/jumpsuits-and-dungarees","/kids/baby-care/childproofing-and-safety-equipment/cycling-and-roller-skating-safety-equipment","/kids/toys-and-games/electronic-games","/kids/toys-and-games/action-figures","/kids/toys-and-games/dolls","/kids/boys-clothing/accessories/gloves","/kids/boys-clothing/accessories/scarves-and-shawls","/kids/boys-clothing/accessories/belts","/kids/boys-clothing/accessories/wallets","/kids/boys-clothing/accessories/ties-and-bow-ties","/kids/boys-clothing/accessories/other-accessories","/kids/boys-clothing/accessories/caps-and-hats","/kids/boys-clothing/swimwear/swimming-trunks","/kids/boys-clothing/swimwear/bathrobes","/kids/boys-clothing/sleepwear/one-piece-pyjamas","/kids/boys-clothing/sleepwear/two-piece-pyjamas","/kids/boys-clothing/underwear-and-socks/socks","/kids/boys-clothing/underwear-and-socks/tights-and-leggings","/kids/boys-clothing/underwear-and-socks/underwear","/kids/boys-clothing/clothing-bundles","/kids/boys-clothing/clothing-for-twins","/kids/boys-clothing/fancy-dress-and-costumes","/kids/toys-and-games/educational-toys-and-games","/kids/toys-and-games/soft-toys-and-stuffed-animals","/kids/toys-and-games/rattles-and-chew-toys","/kids/toys-and-games/musical-toys","/kids/toys-and-games/construction-toys","/kids/toys-and-games/wooden-toys","/kids/toys-and-games/hanging-mobiles","/kids/toys-and-games/water-toys-and-games","/kids/toys-and-games/outdoor-toys-and-games","/kids/baby-care/childproofing-and-safety-equipment/other-childproofing-and-safety-equipment","/women/clothes/coats-and-jackets/capes-and-ponchos","/women/clothes/dresses/special-occasion-dresses/party-and-cocktail-dresses","/women/clothes/dresses/special-occasion-dresses/wedding-dresses","/women/clothes/dresses/special-occasion-dresses/prom-dresses","/women/clothes/dresses/special-occasion-dresses/evening-dresses","/women/clothes/dresses/winter-dresses","/women/clothes/swimwear/cover-ups-and-sarongs","/women/clothes/lingerie-and-nightwear/shapewear","/women/clothes/costumes-and-special-outfits","/women/bags/satchels","/women/accessories/jewellery/anklets","/men/clothes/suits-and-blazers/suit-jackets-and-blazers","/men/clothes/suits-and-blazers/suit-trousers","/men/clothes/suits-and-blazers/waistcoats","/men/clothes/suits-and-blazers/suit-sets","/men/clothes/suits-and-blazers/wedding-suits","/men/shoes/boots/wellington-boots","/men/accessories/bags-and-backpacks/satchels","/men/accessories/bags-and-backpacks/holdalls","/men/accessories/bags-and-backpacks/bum-bags","/men/accessories/jewellery/cufflinks","/men/clothes/tops-and-t-shirts/shirts/checked-shirts","/men/clothes/tops-and-t-shirts/shirts/denim-shirts","/men/clothes/tops-and-t-shirts/shirts/plain-shirts","/men/clothes/tops-and-t-shirts/shirts/print-shirts","/men/clothes/tops-and-t-shirts/shirts/striped-shirts","/men/clothes/tops-and-t-shirts/t-shirts/plain-t-shirts","/men/clothes/tops-and-t-shirts/t-shirts/print-t-shirts","/men/clothes/tops-and-t-shirts/t-shirts/striped-t-shirts","/men/clothes/tops-and-t-shirts/t-shirts/polo-shirts","/men/clothes/tops-and-t-shirts/t-shirts/long-sleeved-t-shirts","/men/clothes/jumpers-and-sweaters-1811","/men/clothes/jumpers-and-sweaters/zip-through-hoodies","/men/clothes/jumpers-and-sweaters/crew-neck-jumpers","/men/clothes/jumpers-and-sweaters/long-jumpers","/men/clothes/jumpers-and-sweaters/chunky-knit-jumpers","/men/clothes/jeans/ripped-jeans","/men/clothes/jeans/skinny-jeans","/men/clothes/jeans/slim-fit-jeans","/men/clothes/jeans/straight-fit-jeans","/men/clothes/trousers/chinos","/men/clothes/trousers/joggers","/men/clothes/shorts/cargo-shorts","/men/clothes/shorts/chino-shorts","/men/clothes/shorts/denim-shorts","/men/clothes/jumpers-and-sweaters/sleeveless-jumpers","/men/grooming/tools-and-accessories/shaving-tools","/men/grooming/tools-and-accessories/grooming-tools","/men/clothes/socks-and-underwear-1828","/men/clothes/socks-and-underwear/pants-and-boxers","/men/clothes/socks-and-underwear/dressing-gowns","/women/clothes/coats-and-jackets/trench-coats","/women/clothes/tops-and-t-shirts/bodysuits","/women/clothes/tops-and-t-shirts/peplum-tops","/women/clothes/shorts-and-cropped-trousers/low-waisted-shorts","/women/clothes/jeans/boyfriend-jeans","/women/clothes/jeans/cropped-jeans","/women/clothes/jeans/flared-jeans","/women/clothes/jeans/high-waisted-jeans","/women/clothes/jeans/ripped-jeans","/women/clothes/jeans/skinny-jeans","/women/clothes/jeans/straight-jeans","/women/clothes/trousers-and-leggings/straight-leg-trousers","/women/clothes/lingerie-and-nightwear/lingerie-accessories","/women/bags/bum-bags","/women/bags/holdalls","/women/bags/luggage-and-suitcases","/women/accessories/umbrellas","/women/accessories/keyrings","/men/clothes/coats-and-jackets/jackets/fleece-jackets","/men/clothes/coats-and-jackets/raincoats","/men/clothes/coats-and-jackets/peacoats","/men/accessories/bags-and-backpacks/luggage","/men/grooming/grooming-kits","/women/clothes/jeans/other","/men/clothes/tops-and-t-shirts/shirts/other-shirts","/men/clothes/suits-and-blazers/other-suits-and-blazers","/men/clothes/socks-and-underwear/other-socks-and-underwear","/men/clothes/tops-and-t-shirts/t-shirts/other-t-shirts","/kids/boys-clothing/trousers-shorts-and-dungarees/other-trousers-shorts-and-dungarees","/kids/boys-clothing/underwear-and-socks/other-underwear-and-socks","/kids/girls-clothing/underwear-and-socks/other-underwear-and-socks","/women/clothes/jumpers-and-sweaters/waistcoats","/kids/girls-clothing/baby-clothing/others","/kids/girls-clothing/jumpers-and-hoodies/other-jumpers-and-hoodies","/kids/girls-clothing/tops-and-t-shirts/other-tops-and-t-shirts","/kids/girls-clothing/trousers-shorts-and-dungarees/other-trousers-shorts-and-dungarees","/kids/girls-clothing/accessories/other-accessories","/kids/boys-clothing/baby-clothing/other-baby-clothing","/kids/boys-clothing/tops-and-t-shirts/other-tops-and-t-shirts","/kids/boys-clothing/jumpers-and-hoodies/other-jumpers-and-hoodies","/women/beauty/hair-care","/women/beauty/beauty-tools/hair-styling-tools","/home/textiles/blankets","/home/textiles/table-linen","/home/textiles/tapestries-and-wall-hangings","/home/home-accessories/picture-and-photo-frames","/home/home-accessories/vases","/home/home-accessories/display-shelves","/home/textiles/bedding/bedding-sets","/home/textiles/bedding/duvet-covers","/home/textiles/bedding/pillowcases","/home/textiles/bedding/sheets","/home/textiles/curtains-and-drapes/opaque-curtains-and-drapes","/home/textiles/towels/bath-towels","/home/textiles/towels/beach-towels","/home/textiles/towels/hand-towels","/home/tableware/cutlery/cutlery-sets","/home/tableware/cutlery/forks","/home/tableware/cutlery/spoons","/home/textiles/rugs-and-mats/doormats-and-floor-mats","/home/textiles/rugs-and-mats-1954","/home/textiles/curtains-and-drapes/sheer-curtains-and-drapes","/home/home-accessories/candles-and-candle-holders-1956","/home/home-accessories/candles-and-candle-holders/candle-holders","/home/tableware/dinnerware/dinner-sets","/home/tableware/dinnerware/bowls","/home/tableware/dinnerware/plates","/home/tableware/dinnerware/trays","/home/home-accessories/storage/baskets","/home/home-accessories/storage/boxes","/home/home-accessories/storage/jewellery-organisers","/home/home-accessories/storage/make-up-organisers","/home/home-accessories/clocks/table-clocks","/home/home-accessories/clocks/wall-clocks","/home/home-accessories/mirrors/wall-mirrors","/home/home-accessories/mirrors/table-mirrors","/home/tableware/cutlery/table-knives","/home/textiles/cushions","/home/tableware/drinkware/cups-and-mugs","/home/tableware/drinkware/coffeepots-and-teapots-2007","/home/tableware/drinkware/jugs","/home/tableware/drinkware/stemmed-glasses","/home/tableware/drinkware/tumblers","/home/tableware/drinkware/drinkware-sets","/home/home-accessories/storage/clothes-bags-and-hangers","/kids/girls-clothing/trousers-and-shorts/harem-trousers","/kids/girls-clothing/formal-wear-and-special-occasion-clothing","/kids/boys-clothing/trousers-and-dungarees/harem-trousers","/kids/boys-clothing/formal-wear-and-special-occasion-clothing","/women/clothes/maternity-clothes/sport-clothes","/kids/toys-and-games/kitchen-toys","/kids/toys-and-games/sleeping-toys","/kids/baby-care/nappies-and-skincare/nappy-waste-containers","/kids/baby-care/nursing-and-feeding/feeding-pillows-2088","/pet-care/cats/beds","/pet-care/cats/bowls-and-feeders-2099","/pet-care/dogs/bowls-and-feeders-2117","/pet-care/dogs/bowls-and-feeders/feeders","/pet-care/dogs/clothing-and-accessories/coats-and-jackets","/pet-care/dogs/clothing-and-accessories/shoes-and-boots","/pet-care/dogs/clothing-and-accessories/accessories","/pet-care/dogs/collars-and-leads-2122","/pet-care/dogs/collars-and-leads/leads","/pet-care/dogs/collars-and-leads/harnesses","/pet-care/cats/bowls-and-feeders/feeders","/pet-care/cats/clothing-and-accessories-2128","/pet-care/cats/clothing-and-accessories/costumes","/pet-care/cats/clothing-and-accessories/accessories","/pet-care/cats/collars-and-leads-2133","/pet-care/cats/collars-and-leads/harnesses-and-leads","/pet-care/small-pets/habitats-and-accessories","/pet-care/small-pets/toys","/entertainment/games-and-puzzles/board-games","/entertainment/games-and-puzzles/card-games","/entertainment/music-and-video/cds","/entertainment/music-and-video/cassettes","/entertainment/music-and-video/vinyl","/entertainment/music-and-video/older-audio-formats","/entertainment/music-and-video/video/dvd","/entertainment/music-and-video/video/vhs","/entertainment/books/literature-and-fiction/classical-literature","/entertainment/books/literature-and-fiction/comics-and-graphic-novels","/entertainment/books/literature-and-fiction/contemporary-fiction","/entertainment/books/literature-and-fiction/crime-and-thrillers","/entertainment/books/literature-and-fiction/humour","/entertainment/books/literature-and-fiction/poetry-and-drama","/entertainment/books/literature-and-fiction/romance","/entertainment/books/literature-and-fiction/science-fiction-and-fantasy","/entertainment/books/literature-and-fiction/other-literature-and-fiction","/entertainment/books/non-fiction/arts-and-entertainment","/entertainment/books/non-fiction/biography","/entertainment/books/non-fiction/business-and-finance","/entertainment/books/non-fiction/computers-and-tech","/entertainment/books/non-fiction/food-and-drink","/entertainment/books/non-fiction/health-and-wellbeing","/entertainment/books/non-fiction/history","/entertainment/books/non-fiction/hobbies-crafts-and-diy","/entertainment/books/non-fiction/parenting-and-family","/entertainment/books/non-fiction/politics-and-society","/entertainment/books/non-fiction/professional-and-technical","/entertainment/books/non-fiction/reference","/entertainment/books/non-fiction/religion-and-spirituality","/entertainment/books/non-fiction/science-and-nature","/entertainment/books/non-fiction/sports","/entertainment/books/non-fiction/study-materials-and-textbooks","/entertainment/books/non-fiction/travel","/entertainment/books/non-fiction/other-non-fiction","/entertainment/books/kids-and-young-adults/young-adults","/entertainment/books/kids-and-young-adults","/entertainment/books/kids-and-young-adults/babies-and-toddlers","/entertainment/video-games-and-consoles/pc-games","/entertainment/video-games-and-consoles/xbox-series-x-and-s/games","/entertainment/video-games-and-consoles/xbox-series-x-and-s/consoles","/entertainment/video-games-and-consoles/xbox-series-x-and-s/accessories","/entertainment/video-games-and-consoles/xbox-one/games","/entertainment/video-games-and-consoles/xbox-one/consoles","/entertainment/video-games-and-consoles/xbox-one/accessories","/entertainment/video-games-and-consoles/older-xbox/games","/entertainment/video-games-and-consoles/older-xbox/consoles","/entertainment/video-games-and-consoles/older-xbox/accessories","/entertainment/video-games-and-consoles/playstation-5/games","/entertainment/video-games-and-consoles/playstation-5/consoles","/entertainment/video-games-and-consoles/playstation-5/accessories","/entertainment/video-games-and-consoles/playstation-4/games","/entertainment/video-games-and-consoles/playstation-4/consoles","/entertainment/video-games-and-consoles/playstation-4/accessories","/entertainment/video-games-and-consoles/older-playstation/games","/entertainment/video-games-and-consoles/older-playstation/consoles","/entertainment/video-games-and-consoles/older-playstation/accessories","/entertainment/video-games-and-consoles/nintendo-switch/games","/entertainment/video-games-and-consoles/nintendo-switch/consoles","/entertainment/video-games-and-consoles/nintendo-switch/accessories","/entertainment/video-games-and-consoles/nintendo-wii-and-wii-u/games","/entertainment/video-games-and-consoles/nintendo-wii-and-wii-u/consoles","/entertainment/video-games-and-consoles/nintendo-wii-and-wii-u/accessories","/entertainment/video-games-and-consoles/nintendo-3ds-and-2ds/games","/entertainment/video-games-and-consoles/nintendo-3ds-and-2ds/consoles","/entertainment/video-games-and-consoles/nintendo-3ds-and-2ds/accessories","/entertainment/video-games-and-consoles/nintendo-game-boy/games","/entertainment/video-games-and-consoles/nintendo-game-boy/consoles","/entertainment/video-games-and-consoles/nintendo-game-boy/accessories","/entertainment/video-games-and-consoles/older-nintendo/games","/entertainment/video-games-and-consoles/older-nintendo/consoles","/entertainment/video-games-and-consoles/older-nintendo/accessories","/entertainment/video-games-and-consoles/retro-gaming/steam","/entertainment/video-games-and-consoles/retro-gaming/intellivision","/entertainment/video-games-and-consoles/retro-gaming/atari","/entertainment/video-games-and-consoles/retro-gaming/colecovision","/entertainment/video-games-and-consoles/retro-gaming/commodore","/entertainment/video-games-and-consoles/retro-gaming/-3do","/entertainment/video-games-and-consoles/virtual-reality/games","/entertainment/video-games-and-consoles/virtual-reality/consoles","/entertainment/video-games-and-consoles/virtual-reality/accessories","/entertainment/video-games-and-consoles/sega/games","/entertainment/video-games-and-consoles/sega/consoles","/entertainment/video-games-and-consoles/sega/accessories","/entertainment/games-and-puzzles/tile-based-games","/entertainment/games-and-puzzles/jigsaw-puzzles","/entertainment/games-and-puzzles/brain-teasers-and-puzzles","/entertainment/games-and-puzzles/travel-and-pocket-games","/entertainment/games-and-puzzles/tabletop-and-miniature-gaming","/entertainment/games-and-puzzles/stacking-and-balancing-games","/entertainment/games-and-puzzles/floor-games","/pet-care/dogs/clothing-and-accessories/jumpers","/pet-care/cats/litter-boxes","/pet-care/fish/decorations-and-accessories","/pet-care/fish/aquarium-equipment","/pet-care/birds/toys","/pet-care/birds/cages-and-accessories","/pet-care/reptiles/decorations-and-accessories","/pet-care/reptiles/terrarium-equipment","/pet-care/cats/grooming/brushes-and-combs","/pet-care/cats/grooming/claw-care","/pet-care/cats/travel-carriers/hard-carriers","/pet-care/cats/travel-carriers/soft-carriers-and-backpacks","/pet-care/cats/toys/teasers-and-wands","/pet-care/cats/toys/balls","/pet-care/cats/toys/soft-toys","/pet-care/cats/toys/scratchers","/pet-care/cats/toys/interactive-toys","/pet-care/dogs/grooming/claw-care","/pet-care/dogs/grooming/brushes-and-combs","/pet-care/dogs/carriers-and-crates/crates","/pet-care/dogs/carriers-and-crates/travel-carriers","/pet-care/dogs/training-accessories/bags","/pet-care/dogs/training-accessories/whistles","/pet-care/dogs/beds-and-blankets/blankets","/pet-care/dogs/beds-and-blankets-2512","/pet-care/dogs/toys/tough-and-durable-toys","/pet-care/dogs/toys/soft-toys","/pet-care/dogs/toys/balls-and-fetch-toys","/pet-care/dogs/collars-and-leads/muzzles","/pet-care/dogs/clothing-and-accessories/t-shirts","/pet-care/dogs/clothing-and-accessories/costumes","/entertainment/music-and-video/video/blu-ray","/women/clothes/outerwear/gilets-and-body-warmers","/women/clothes/outerwear/coats/duffle-coats","/women/clothes/outerwear/coats/overcoats-and-long-coats","/women/clothes/outerwear/jackets/biker-and-racer-jackets","/women/clothes/outerwear/jackets/field-and-utility-jackets","/women/clothes/outerwear/jackets/shackets","/women/clothes/outerwear/jackets/ski-and-snowboard-jackets","/women/clothes/outerwear/jackets/varsity-jackets","/women/clothes/outerwear/jackets/windbreakers","/men/clothes/outerwear/coats/overcoats-and-long-coats","/men/clothes/outerwear/jackets/biker-and-racer-jackets","/men/clothes/outerwear/jackets/field-and-utility-jackets","/men/clothes/outerwear/jackets/puffer-jackets","/men/clothes/outerwear/jackets/quilted-jackets","/men/clothes/outerwear/jackets/shackets","/men/clothes/outerwear/jackets/ski-and-snowboard-jackets","/kids/girls-clothing/outerwear/coats/duffle-coats","/kids/girls-clothing/outerwear/coats/parkas","/kids/girls-clothing/outerwear/coats/peacoats","/kids/girls-clothing/outerwear/coats/trench-coats","/kids/girls-clothing/outerwear/jackets/blazers","/kids/girls-clothing/outerwear/jackets/bomber-jackets","/kids/girls-clothing/outerwear/jackets/denim-jackets","/kids/girls-clothing/outerwear/jackets/fleece-jackets","/kids/girls-clothing/outerwear/jackets/puffer-jackets","/kids/girls-clothing/outerwear/jackets/windbreakers","/men/clothes/outerwear/jackets/varsity-jackets","/men/clothes/outerwear/jackets/windbreakers","/men/clothes/outerwear/ponchos","/men/clothes/outerwear/gilets-and-body-warmers","/kids/girls-clothing/outerwear/rain-gear/rain-trousers","/kids/girls-clothing/outerwear/rain-gear/ponchos","/kids/girls-clothing/outerwear/rain-gear/rain-suits-and-sets","/kids/girls-clothing/outerwear/rain-gear/raincoats","/kids/girls-clothing/outerwear/snow-gear/snow-jackets-and-coats","/kids/boys-clothing/outerwear/coats/duffle-coats","/kids/boys-clothing/outerwear/coats/parkas","/kids/boys-clothing/outerwear/coats/peacoats","/kids/boys-clothing/outerwear/coats/trench-coats","/kids/girls-clothing/outerwear/snow-gear/snow-suits-and-sets","/kids/boys-clothing/outerwear/jackets/blazers","/kids/boys-clothing/outerwear/jackets/bomber-jackets","/kids/boys-clothing/outerwear/jackets/denim-jackets","/kids/boys-clothing/outerwear/jackets/fleece-jackets","/kids/boys-clothing/outerwear/jackets/puffer-jackets","/kids/boys-clothing/outerwear/jackets/windbreakers","/kids/girls-clothing/outerwear/snow-gear/snow-trousers","/women/clothes/outerwear/jackets/quilted-jackets","/kids/boys-clothing/outerwear/rain-gear/rain-trousers","/kids/boys-clothing/outerwear/rain-gear/ponchos","/kids/boys-clothing/outerwear/rain-gear/raincoats","/kids/boys-clothing/outerwear/rain-gear/rain-suits-and-sets","/kids/boys-clothing/outerwear/snow-gear/snow-jackets-and-coats","/kids/boys-clothing/outerwear/snow-gear/snow-trousers","/kids/boys-clothing/outerwear/snow-gear/snow-suits-and-sets","/women/clothes/outerwear/jackets/puffer-jackets","/women/shoes/boots/ankle-boots","/women/shoes/boots/mid-calf-boots","/women/shoes/boots/over-the-knee-boots","/women/shoes/boots/snow-boots","/women/shoes/boots/work-boots","/women/shoes/clogs-and-mules","/women/shoes/trainers","/women/shoes/flat-shoes/boat-shoes-loafers-and-moccasins","/women/shoes/flat-shoes/espadrilles","/women/shoes/flat-shoes/lace-up-shoes","/women/shoes/flip-flops-flat-sandals-and-slides/flip-flops","/women/shoes/flip-flops-flat-sandals-and-slides/flat-sandals","/women/shoes/flip-flops-flat-sandals-and-slides/slides","/women/shoes/sports-shoes/basketball-shoes","/women/shoes/sports-shoes/climbing-and-bouldering-shoes","/women/shoes/sports-shoes/cycling-shoes","/women/shoes/sports-shoes/dance-shoes","/women/shoes/sports-shoes/football-boots","/women/shoes/sports-shoes/golf-shoes","/women/shoes/sports-shoes/hiking-boots-and-shoes","/women/shoes/sports-shoes/ice-skates","/women/shoes/sports-shoes/indoor-football-shoes","/women/shoes/sports-shoes/indoor-training-shoes-2648","/women/shoes/sports-shoes/motorcycle-boots","/women/shoes/sports-shoes/roller-skates-and-inline-skates","/women/shoes/sports-shoes/running-shoes-2651","/women/shoes/sports-shoes/ski-boots","/women/shoes/sports-shoes/snowboard-boots","/women/shoes/sports-shoes/swimming-and-water-shoes","/women/shoes/sports-shoes/tennis-shoes","/men/shoes/boat-shoes-loafers-and-moccasins","/men/shoes/espadrilles","/men/shoes/slippers","/men/shoes/boots/chelsea-and-slip-on-boots","/men/shoes/boots/desert-and-lace-up-boots","/men/shoes/boots/snow-boots","/men/shoes/boots/work-boots","/men/shoes/flip-flops-sandals-and-slides/clogs-and-mules","/men/shoes/flip-flops-sandals-and-slides/flip-flops","/men/shoes/flip-flops-sandals-and-slides/sandals","/men/shoes/flip-flops-sandals-and-slides/slides","/men/shoes/formal-shoes/lace-up-shoes","/men/shoes/formal-shoes/slip-on-shoes","/men/shoes/formal-shoes/monk-strap-shoes","/men/shoes/sports-shoes/basketball-shoes","/men/shoes/sports-shoes/climbing-and-bouldering-shoes","/men/shoes/sports-shoes/cycling-shoes","/men/shoes/sports-shoes/dance-shoes","/men/shoes/sports-shoes/football-boots","/men/shoes/sports-shoes/golf-shoes","/men/shoes/sports-shoes/hiking-boots-and-shoes","/men/shoes/sports-shoes/ice-skates","/men/shoes/sports-shoes/indoor-football-shoes","/men/shoes/sports-shoes/motorcycle-boots","/men/shoes/sports-shoes/roller-skates-and-inline-skates","/men/shoes/sports-shoes/ski-boots","/men/shoes/sports-shoes/snowboard-boots","/men/shoes/sports-shoes/swimming-and-water-shoes","/men/shoes/sports-shoes/tennis-shoes","/women/shoes/heels/court-shoes","/women/shoes/heels/high-heeled-sandals","/women/shoes/flat-shoes/mary-janes","/kids/girls-clothing/shoes/clogs-and-mules","/kids/girls-clothing/shoes/heels","/kids/girls-clothing/shoes/boots/ankle-boots","/kids/girls-clothing/shoes/boots/mid-calf-boots","/kids/girls-clothing/shoes/boots/snow-boots","/kids/girls-clothing/shoes/boots/wellington-boots","/kids/girls-clothing/shoes/flat-shoes/espadrilles","/kids/girls-clothing/shoes/flat-shoes/lace-up-shoes","/kids/girls-clothing/shoes/flip-flops-sandals-and-slides/flip-flops","/kids/girls-clothing/shoes/flip-flops-sandals-and-slides/sandals","/kids/girls-clothing/shoes/flip-flops-sandals-and-slides/slides","/kids/girls-clothing/shoes/sports-shoes/basketball-shoes","/kids/girls-clothing/shoes/sports-shoes/dance-shoes","/kids/girls-clothing/shoes/sports-shoes/football-boots","/kids/girls-clothing/shoes/sports-shoes/hiking-boots-and-shoes","/kids/girls-clothing/shoes/sports-shoes/ice-skates","/kids/girls-clothing/shoes/sports-shoes/roller-skates-and-inline-skates","/kids/girls-clothing/shoes/sports-shoes/running-shoes","/kids/girls-clothing/shoes/sports-shoes/ski-boots","/kids/girls-clothing/shoes/sports-shoes/snowboard-boots","/kids/girls-clothing/shoes/sports-shoes/swimming-and-water-shoes","/kids/girls-clothing/shoes/trainers/hook-and-loop-trainers","/kids/girls-clothing/shoes/trainers/lace-up-trainers","/kids/girls-clothing/shoes/trainers/slip-on-trainers","/kids/boys-clothing/shoes/boat-shoes-loafers-and-moccasins","/kids/boys-clothing/shoes/espadrilles","/kids/boys-clothing/shoes/boots/ankle-boots","/kids/boys-clothing/shoes/boots/mid-calf-boots","/kids/boys-clothing/shoes/boots/snow-boots","/kids/boys-clothing/shoes/boots/wellington-boots","/kids/boys-clothing/shoes/flip-flops-sandals-and-slides/clogs-and-mules","/kids/boys-clothing/shoes/flip-flops-sandals-and-slides/flip-flops","/kids/boys-clothing/shoes/flip-flops-sandals-and-slides/sandals","/kids/boys-clothing/shoes/flip-flops-sandals-and-slides/slides","/kids/boys-clothing/shoes/sports-shoes/basketball-shoes","/kids/boys-clothing/shoes/sports-shoes/dance-shoes","/kids/boys-clothing/shoes/sports-shoes/football-boots","/kids/boys-clothing/shoes/sports-shoes/hiking-boots-and-shoes","/kids/boys-clothing/shoes/sports-shoes/ice-skates","/kids/boys-clothing/shoes/sports-shoes/roller-skates-and-inline-skates","/kids/boys-clothing/shoes/sports-shoes/running-shoes","/kids/boys-clothing/shoes/sports-shoes/ski-boots","/kids/boys-clothing/shoes/sports-shoes/snowboard-boots","/kids/boys-clothing/shoes/sports-shoes/swimming-and-water-shoes","/kids/boys-clothing/shoes/trainers/hook-and-loop-trainers","/kids/boys-clothing/shoes/trainers/lace-up-trainers","/kids/boys-clothing/shoes/trainers/slip-on-trainers","/kids/girls-clothing/shoes/flat-shoes/ballerinas-mary-janes-and-t-bar-shoes"]
'''
Cookie: csrftoken=bD0kdBbkK2ufeX55O4XtK4AF6v2k6QD0; JSESSIONID=B425D43584747956FCC39E67EB4AEC8C
'''
k = ["/Entertainment/Video-games-and-consoles/Virtual-reality/Consoles","/Entertainment/Video-games-and-consoles/Virtual-reality/Accessories","/Entertainment/Video-games-and-consoles/Sega/Games","/Entertainment/Video-games-and-consoles/Sega/Consoles","/Entertainment/Video-games-and-consoles/Sega/Accessories","/Entertainment/Games-and-puzzles/Tile-based-games","/Entertainment/Games-and-puzzles/Jigsaw-puzzles","/Entertainment/Games-and-puzzles/Brain-teasers-and-puzzles","/Entertainment/Games-and-puzzles/Travel-and-pocket-games","/Entertainment/Games-and-puzzles/Tabletop-and-miniature-gaming","/Entertainment/Games-and-puzzles/Stacking-and-balancing-games","/Entertainment/Games-and-puzzles/Floor-games","/Entertainment/Music-and-video/Video/Blu-ray","/Women/Clothes/Dresses/Denim-dresses","/Women/Clothes/Trousers-and-leggings/Leather-trousers"]#,"/Women/Clothes/Trousers-and-leggings/Skinny-trousers","/Women/Clothes/Trousers-and-leggings/Tailored-trousers"]#,,"/Women/Clothes/Jumpers-and-sweaters/Sweaters/Turtleneck-sweaters",,"/Women/Clothes/Jumpers-and-sweaters/Sweaters/Long-jumpers",0,"/Women/Clothes/Jumpers-and-sweaters/Sweaters/Three-fourths-sleeve-jumpers",1,"/Women/Clothes/Jumpers-and-sweaters/Cardigans",2,"/Women/Clothes/Jumpers-and-sweaters/Boleros",3,"/Women/Clothes/Jumpers-and-sweaters/Hoodies-and-sweatshirts",4,"/Women/Clothes/Jumpers-and-sweaters/Other-jumpers-and-sweaters"]#,5,"/Women/Clothes/Skirts/Mini-skirts",,"/Women/Clothes/Skirts/Midi-skirts",,"/Women/Clothes/Skirts/Maxi-skirts",,"/Women/Clothes/Skirts/Other-skirts",,"/Women/Clothes/Shorts-and-cropped-trousers/Knee-length-shorts",0,"/Women/Clothes/Shorts-and-cropped-trousers/Cropped-trousers",1,"/Women/Clothes/Shorts-and-cropped-trousers/Other-shorts-and-cropped-trousers",2,"/Women/Shoes/Boots/Knee-high-boots",3,"/Women/Shoes/Boots/Wellington-boots",4,"/Women/Shoes/Slippers",5,"/Women/Clothes/Swimwear/One-pieces",6,"/Women/Clothes/Swimwear/Bikinis-and-tankinis",,"/Women/Clothes/Swimwear/Other-swimwear-and-beachwear",,"/Women/Clothes/Tops-and-t-shirts/T-shirts",,"/Women/Clothes/Tops-and-t-shirts/Shirts",0,"/Women/Clothes/Tops-and-t-shirts/Short-sleeved-tops",1,"/Women/Clothes/Tops-and-t-shirts/Long-sleeved-tops",2,"/Women/Clothes/Tops-and-t-shirts/Three-fourths-sleeve-tops",3,"/Women/Clothes/Tops-and-t-shirts/Tunics",4,"/Women/Clothes/Tops-and-t-shirts/Other-tops-and-t-shirts",5,"/Women/Clothes/Lingerie-and-nightwear/Sets",6,"/Women/Accessories/Hats-and-caps/Caps",7,"/Women/Accessories/Hats-and-caps-231",,"/Women/Accessories/Hats-and-caps/Warm-hats",,"/Women/Accessories/Hats-and-caps/Berets",0,"/Women/Accessories/Hats-and-caps/Headbands",1,"/Women/Accessories/Hats-and-caps/Other",2,"/Women/Accessories/Scarves-and-shawls/Knit-scarves",3,"/Women/Accessories/Scarves-and-shawls/Head-scarfs",4,"/Women/Accessories/Scarves-and-shawls/Oversized-scarves-and-shawls",5,"/Women/Accessories/Scarves-and-shawls/Shawls",6,"/Women/Accessories/Scarves-and-shawls/Other",7,"/Men/Accessories/Jewellery/Necklaces-and-pendants",8,"/Men/Accessories/Jewellery/Rings",,"/Men/Accessories/Jewellery/Bracelets",0,"/Men/Accessories/Jewellery/Other",1,"/Men/Accessories/Bags-and-backpacks/Handbags",2,"/Men/Accessories/Bags-and-backpacks/Backpacks",3,"/Men/Accessories/Bags-and-backpacks/Shoulder-bags",4,"/Men/Accessories/Bags-and-backpacks/Wallets",5,"/Men/Accessories/Bags-and-backpacks/Other",6,"/Men/Clothes/Trousers/Skinny-trousers",7,"/Men/Clothes/Trousers/Wide-legged-trousers",8,"/Men/Clothes/Trousers/Tailored-trousers",,"/Men/Clothes/Trousers/Other",,00,"/Men/Clothes/Jumpers-and-sweaters/V-neck-jumpers",01,"/Men/Clothes/Jumpers-and-sweaters/Turtle-neck-jumpers",02,"/Men/Clothes/Jumpers-and-sweaters/Cardigans",03,"/Men/Clothes/Jumpers-and-sweaters/Hoodies-and-sweatshirts",04,"/Men/Clothes/Jumpers-and-sweaters/Other",05,"/Men/Clothes/Trousers/Cropped-trousers",06,"/Men/Clothes/Shorts/Other-shorts",07,"/Men/Accessories/Scarves-and-shawls/Knitted-scarves",08,"/Men/Accessories/Scarves-and-shawls/Head-scarves",09,"/Men/Accessories/Scarves-and-shawls/Large-scarves-and-shawls",10,"/Men/Accessories/Scarves-and-shawls/Other","/Men/Accessories/Hats-and-caps/Caps",12,"/Men/Accessories/Hats-and-caps-288",13,"/Men/Accessories/Hats-and-caps/Winter-hats",14,"/Men/Accessories/Hats-and-caps/Berets",15,"/Men/Accessories/Hats-and-caps/Other",16,"/Women/Clothes/Trousers-and-leggings/Leggings",17,"/Women/Clothes/Trousers-and-leggings/Harem-pants",18,"/Women/Clothes/Jumpers-and-sweaters/Sweaters/Knitted-jumpers",19,"/Women/Clothes/Suits-and-blazers/Blazers",0,"/Women/Clothes/Tops-and-t-shirts/Vest-tops",1,"/Women/Clothes/Shorts-and-cropped-trousers/Denim-shorts",2,"/Women/Clothes/Skirts/High-waisted-skirts",,"/Women/Clothes/Skirts/Denim-skirts",,"/Women/Clothes/Skirts/Tulip-skirts",,"/Women/Clothes/Skirts/Pencil-skirts",,"/Women/Shoes/Flats/Ballerinas",,"/Women/Bags/Tote-bags",,"/Women/Accessories/Jewellery/Rings",,"/Men/Clothes/Tops-and-t-shirts/Vests-and-sleeveless-t-shirts",0,"/Women/Clothes/Activewear/Outerwear",1,"/Women/Clothes/Activewear/Tracksuits",2,"/Women/Clothes/Activewear/Trousers",3,"/Women/Clothes/Activewear/Dresses",,"/Women/Clothes/Activewear/Skirts",,"/Women/Clothes/Activewear/Tops-and-t-shirts",,"/Women/Clothes/Activewear/Hoodies-and-sweatshirts",,"/Women/Clothes/Activewear/Shorts",,"/Women/Clothes/Activewear/Other-activewear",,"/Men/Clothes/Activewear/Outerwear",0,"/Men/Clothes/Activewear/Tracksuits",1,"/Men/Clothes/Activewear/Trousers",2,"/Men/Clothes/Activewear/Tops-and-t-shirts",3,"/Men/Clothes/Activewear/Pullovers-and-sweaters",4,"/Men/Clothes/Activewear/Shorts",,"/Men/Clothes/Activewear/Other-activewear",,"/Women/Beauty/Face-care",,"/Women/Beauty/Beauty-tools/Face-care-tools",,"/Women/Beauty/Body-care",,"/Women/Beauty/Beauty-tools/Body-care-tools","/Women/Beauty/Nail-care","/Women/Beauty/Beauty-tools/Nail-care-tools","/Women/Beauty/Make-up","/Women/Beauty/Beauty-tools/Make-up-tools","/Men/Grooming/Other-grooming-items","/Men/Grooming/Tools-and-accessories/Other-tools","/Women/Clothes/Lingerie-and-nightwear/Dressing-gowns"]#"/Women/Clothes/Tops-and-t-shirts/Crop-tops",,"/Women/Clothes/Tops-and-t-shirts/Off-the-shoulder-tops",,"/Women/Clothes/Tops-and-t-shirts/Blouses",0,"/Women/Clothes/Tops-and-t-shirts/Halterneck-tops",1,"/Women/Clothes/Tops-and-t-shirts/Turtlenecks",2,"/Women/Clothes/Dresses/Long-dresses",3,"/Women/Clothes/Dresses/Midi-dresses",4,"/Women/Clothes/Dresses/Formal-and-work-dresses",5,"/Women/Clothes/Dresses/Little-black-dresses",6,"/Women/Clothes/Dresses/Casual-dresses",,"/Women/Clothes/Dresses/Special-occasion-dresses/Backless-dresses",,"/Women/Clothes/Dresses/Strapless-dresses",,"/Women/Clothes/Dresses/Summer-dresses",0,"/Women/Clothes/Jumpers-and-sweaters/Sweaters/Other-sweaters",1,"/Women/Clothes/Jumpers-and-sweaters/Kimonos",2,"/Women/Clothes/Trousers-and-leggings/Cropped-trousers-and-chinos",3,"/Women/Clothes/Trousers-and-leggings/Wide-leg-trousers",4,"/Women/Clothes/Outerwear/Coats/Peacoats",5,"/Women/Clothes/Coats-and-jackets/Jackets/Bomber-jackets",6,"/Women/Clothes/Coats-and-jackets/Jackets/Denim-jackets",7,"/Women/Clothes/Coats-and-jackets/Raincoats",,"/Women/Clothes/Coats-and-jackets/Jackets/Fleece-jackets",,"/Women/Clothes/Coats-and-jackets/Parkas",0,"/Women/Clothes/Coats-and-jackets/Faux-fur-coats",1,"/Women/Clothes/Skirts/A-line-skirts",2,"/Women/Clothes/Skirts/Bodycon-skirts",3,"/Women/Clothes/Skirts/Skater-skirts",4,"/Women/Clothes/Skirts/Pleated-skirts",5,"/Women/Clothes/Shorts-and-cropped-trousers/High-waisted-shorts",6,"/Women/Clothes/Shorts-and-cropped-trousers/Leather-shorts",7,"/Women/Clothes/Shorts-and-cropped-trousers/Lace-shorts",8,"/Women/Clothes/Shorts-and-cropped-trousers/Cargo-shorts",,"/Other-bags",0,"/Women/Accessories/Hair-accessories",1,"/Women/Clothes/Suits-and-blazers/Trouser-suits",2,"/Women/Clothes/Suits-and-blazers/Skirt-suits",3,"/Women/Clothes/Suits-and-blazers/Suit-separates",4,"/Women/Clothes/Suits-and-blazers/Other-suits-and-blazers",5,"/Women/Clothes/Jumpsuits-and-playsuits-1131",6,"/Women/Clothes/Jumpsuits-and-playsuits/Playsuits",7,"/Women/Clothes/Jumpsuits-and-playsuits/Other-jumpsuits-and-playsuits",8,"/Women/Accessories/Other-accessories",,"/Women/Clothes/Maternity-clothes/Maternity-trousers",00,"/Women/Clothes/Maternity-clothes/Maternity-skirts",01,"/Women/Clothes/Maternity-clothes/Maternity-tops",02,"/Women/Clothes/Maternity-clothes/Maternity-jumpsuits-and-playsuits",03,"/Women/Clothes/Maternity-clothes/Maternity-dresses",04,"/Women/Clothes/Maternity-clothes/Maternity-coats-and-jackets",05,"/Women/Clothes/Maternity-clothes/Maternity-jumpers-and-sweaters",06,"/Women/Clothes/Maternity-clothes/Maternity-shorts",07,"/Women/Clothes/Maternity-clothes/Maternity-swimwear-and-beachwear",08,"/Kids/Boys-clothing/Trousers-and-dungarees/Shorts-and-cropped-trousers",09,"/Kids/Boys-clothing/Activewear",10,"/Kids/Boys-clothing/Other-boys-clothing",11,"/Women/Accessories/Tech-accessories",12,"/Men/Clothes/Coats-and-jackets/Jackets/Bomber-jackets",13,"/Men/Clothes/Coats-and-jackets/Jackets/Denim-jackets",14,"/Men/Clothes/Coats-and-jackets/Duffle-coats",15,"/Men/Clothes/Coats-and-jackets/Jackets/Harrington-jackets",16,"/Men/Clothes/Coats-and-jackets/Parkas",17,"/Men/Clothes/Coats-and-jackets/Trench-coats",18,"/Men/Shoes/Trainers",19,"/Kids/Girls-clothing/Skirts",20,"/Kids/Girls-clothing/Trousers-and-shorts/Shorts-and-cropped-trousers",21,"/Kids/Girls-clothing/Activewear",22,"/Kids/Girls-clothing/Other-girls-clothing",23,"/Kids/Boys-clothing/Bags-and-backpacks",24,"/Kids/Girls-clothing/Bags-and-backpacks",25,"/Women/Clothes/Lingerie-and-nightwear/Socks",26,"/Women/Clothes/Lingerie-and-nightwear/Tights-and-stockings",27,"/Women/Beauty/Hand-care",28,"/Women/Clothes/Activewear/Sports-bras",29,"/Women/Clothes/Activewear/Sports-accessories/Scarves",0,"/Women/Clothes/Activewear/Sports-accessories/Glasses",1,"/Women/Clothes/Activewear/Sports-accessories/Watches-and-wristbands",2,"/Women/Clothes/Activewear/Sports-accessories/Hats",3,"/Women/Clothes/Activewear/Sports-accessories/Gloves",,"/Women/Clothes/Activewear/Sports-accessories/Protection-slash-padding",,"/Women/Clothes/Activewear/Sports-accessories/Other-accessories",,"/Men/Shoes/Sport-shoes/Running-shoes",,"/Men/Shoes/Sport-shoes/Indoor-training-shoes",,"/Men/Clothes/Activewear/Sports-accessories/Scarves",,"/Men/Clothes/Activewear/Sports-accessories/Glasses",0,"/Men/Clothes/Activewear/Sports-accessories/Watches-and-wristbands",1,"/Men/Clothes/Activewear/Sports-accessories/Hats",2,"/Men/Clothes/Activewear/Sports-accessories/Gloves",3,"/Men/Clothes/Activewear/Sports-accessories/Protective-items",4,"/Men/Clothes/Activewear/Sports-accessories/Other-accessories",,"/Women/Bags/Patterned-and-embroidered-bags",,"/Kids/Other-kids-items",,"/Kids/Car-seats-and-chairs/Car-chairs",,"/Kids/Car-seats-and-chairs/Feeding-chairs",,"/Kids/School-supplies/School-bags",0,"/Kids/School-supplies-1509",1,"/Kids/Girls-clothing/Clothing-bundles",2,"/Kids/Buggies/Buggy-accessories",3,"/Kids/Buggies/Umbrella-buggies",4,"/Kids/Girls-clothing/Baby-clothing/Rompers",5,"/Kids/Girls-clothing/Baby-clothing/Bodysuits",,"/Kids/Girls-clothing/Baby-clothing/Dungarees",,"/Kids/Girls-clothing/Baby-clothing/Sets",,"/Kids/Girls-clothing/Outerwear/Gilets-and-body-warmers",,"/Kids/Girls-clothing/Shoes/Baby-shoes",0,"/Kids/Girls-clothing/Shoes/Formal-and-special-occasion-shoes",1,"/Kids/Girls-clothing/Shoes/Slippers",2,"/Kids/Girls-clothing/Tops-and-t-shirts/T-shirts",3,"/Kids/Girls-clothing/Tops-and-t-shirts/Polo-shirts",4,"/Kids/Girls-clothing/Tops-and-t-shirts/Shirts",5,"/Kids/Girls-clothing/Tops-and-t-shirts/Short-sleeved-tops",6,"/Kids/Girls-clothing/Tops-and-t-shirts/Long-sleeved-tops",,"/Kids/Girls-clothing/Tops-and-t-shirts/Sleeveless-tops",,"/Kids/Girls-clothing/Tops-and-t-shirts/Tunics",,"/Kids/Girls-clothing/Jumpers-and-hoodies-1542",0,"/Kids/Girls-clothing/Jumpers-and-hoodies/V-neck-jumpers",1,"/Kids/Girls-clothing/Jumpers-and-hoodies/Turtleneck-jumpers",2,"/Kids/Girls-clothing/Jumpers-and-hoodies/Zip-up-jumpers",3,"/Kids/Girls-clothing/Jumpers-and-hoodies/Boleros",4,"/Kids/Girls-clothing/Jumpers-and-hoodies/Hoodies-and-sweatshirts",5,"/Kids/Girls-clothing/Jumpers-and-hoodies/Sleeveless-jumpers",6,"/Kids/Girls-clothing/Dresses/Long-dresses",7,"/Kids/Girls-clothing/Dresses/Short-dresses",,"/Kids/Girls-clothing/Trousers-and-shorts/Jeans",,"/Kids/Girls-clothing/Trousers-and-shorts/Skinny-trousers",0,"/Kids/Kids-furniture/Cribs-and-cradles",1,"/Kids/Girls-clothing/Trousers-and-shorts/Wide-leg-trousers",2,"/Kids/Kids-furniture/Cots",3,"/Kids/Girls-clothing/Trousers-and-shorts/Leggings",4,"/Kids/Kids-furniture/Toddler-beds",5,"/Kids/Girls-clothing/Trousers-and-shorts/Jumpsuits-and-dungarees",6,"/Kids/Kids-furniture/Mattresses/Cot-mattresses",7,"/Kids/Kids-furniture/Mattresses/Crib-and-cradle-mattresses",8,"/Kids/Kids-furniture/Mattresses/Kid-bed-mattresses",,"/Kids/Kids-furniture/Playmats",0,"/Kids/Kids-furniture/Playpens",1,"/Kids/Kids-furniture/Changing-pads-and-tables",2,"/Kids/Girls-clothing/Accessories/Caps-and-hats",3,"/Kids/Girls-clothing/Accessories/Gloves",4,"/Kids/Kids-furniture/Other-kids-furniture/Chairs",5,"/Kids/Girls-clothing/Accessories/Scarves-and-shawls",6,"/Kids/Girls-clothing/Accessories/Belts",7,"/Kids/Girls-clothing/Accessories/Hairbands-and-hairclips",8,"/Kids/Girls-clothing/Accessories/Wallets-and-purses",,"/Kids/Kids-furniture/Other-kids-furniture/Tables",00,"/Kids/Girls-clothing/Accessories/Jewellery",01,"/Kids/Kids-furniture/Other-kids-furniture/Carpets",02,"/Kids/Kids-furniture/Other-kids-furniture/Wardrobes",03,"/Kids/Kids-furniture/Other-kids-furniture/Shelves",04,"/Kids/Girls-clothing/Swimwear/One-piece-swimsuits",05,"/Kids/Kids-furniture/Other-kids-furniture/Play-furniture",06,"/Kids/Girls-clothing/Swimwear/Bikinis-and-tankinis",07,"/Kids/Girls-clothing/Swimwear/Bathrobes",08,"/Kids/Ride-on-toys/Bicycle-seats-and-trailers",09,"/Kids/Girls-clothing/Sleepwear/One-piece-pyjamas",10,"/Kids/Girls-clothing/Sleepwear/Two-piece-pyjamas",11,"/Kids/Girls-clothing/Sleepwear/Nighties",12,"/Kids/Ride-on-toys/Baby-walkers",13,"/Kids/Girls-clothing/Underwear-and-socks/Socks",14,"/Kids/Girls-clothing/Underwear-and-socks/Tights-and-leggings",15,"/Kids/Girls-clothing/Underwear-and-socks/Underwear",16,"/Kids/Ride-on-toys/Push-and-pull-toys",17,"/Kids/Girls-clothing/Clothing-for-twins",18,"/Kids/Ride-on-toys/Scooters",19,"/Kids/Girls-clothing/Fancy-dress-and-costumes",20,"/Kids/Ride-on-toys/Tricycles",21,"/Kids/Ride-on-toys/Bicycles",22,"/Kids/Ride-on-toys/Outdoor-vehicles",23,"/Kids/Ride-on-toys/Sledges-skis-and-snowboards",24,"/Kids/Buggies/Running-and-sport-buggies",25,"/Kids/Buggies/Universal-buggies",26,"/Kids/Buggies/Buggies-for-twins",27,"/Women/Clothes/Maternity-clothes/Maternity-underwear-1615",28,"/Women/Clothes/Maternity-clothes/Maternity-underwear/Sleep-wear",29,"/Women/Clothes/Maternity-clothes/Maternity-underwear/Pregnancy-and-postpartum-belts","/Women/Clothes/Maternity-clothes/Maternity-underwear/Pregnancy-and-breastfeeding-bras","/Kids/Baby-care/Sleep-accessories/Blankets","/Kids/Baby-care/Sleep-accessories/Pillows","/Kids/Baby-care/Sleep-accessories/Plaids","/Kids/Baby-care/Sleep-accessories/Sleeping-bags","/Kids/Baby-care/Sleep-accessories/Bedding","/Kids/Baby-care/Sleep-accessories/Heating-pads-and-electric-blankets","/Kids/Baby-care/Nursing-and-feeding/Cutlery","/Kids/Baby-care/Nursing-and-feeding/Baby-bottles","/Kids/Baby-care/Nursing-and-feeding/Pacifiers-dummies-and-soothers","/Kids/Baby-care/Nursing-and-feeding/Dishes",1,"/Kids/Baby-care/Nursing-and-feeding/Flasks-and-bottle-warmers",2,"/Kids/Baby-care/Nursing-and-feeding/Other-nursing-and-feeding-items",3,"/Kids/Boys-clothing/Baby-clothing/Rompers",4,"/Kids/Boys-clothing/Baby-clothing/Bodysuits",,"/Kids/Boys-clothing/Baby-clothing/Dungarees",,"/Kids/Boys-clothing/Baby-clothing/Sets",,"/Kids/Boys-clothing/Outerwear/Gilets-and-body-warmers",,"/Kids/Boys-clothing/Shoes/Baby-shoes",,"/Kids/Boys-clothing/Shoes/Formal-and-special-occasion-shoes",0,"/Kids/Boys-clothing/Shoes/Slippers",1,"/Kids/Boys-clothing/Tops-and-t-shirts/T-shirts",2,"/Kids/Boys-clothing/Tops-and-t-shirts/Polo-shirts",3,"/Kids/Boys-clothing/Tops-and-t-shirts/Shirts",4,"/Kids/Boys-clothing/Tops-and-t-shirts/Short-sleeved-tops",5,"/Kids/Boys-clothing/Tops-and-t-shirts/Long-sleeved-tops",,"/Kids/Boys-clothing/Tops-and-t-shirts/Sleeveless-tops",,"/Kids/Boys-clothing/Jumpers-and-hoodies-1668",,"/Kids/Boys-clothing/Jumpers-and-hoodies/V-neck-jumpers",,"/Kids/Boys-clothing/Jumpers-and-hoodies/Turtleneck-jumpers",0,"/Kids/Boys-clothing/Jumpers-and-hoodies/Zip-up-jumpers",1,"/Kids/Boys-clothing/Jumpers-and-hoodies/Hoodies-and-sweatshirts",2,"/Kids/Boys-clothing/Jumpers-and-hoodies/Sleeveless-jumpers",3,"/Kids/Baby-care/Baby-carriers-and-wraps",4,"/Kids/Baby-care/Swimming-equipment",5,"/Kids/Baby-care/Nappies-and-skincare-1678",6,"/Kids/Baby-care/Nappies-and-skincare/Baby-hygiene",,"/Kids/Baby-care/Nappies-and-skincare/Baby-changing-bags",,"/Kids/Baby-care/Childcare-accessories-and-tech/Baby-monitors",,"/Kids/Baby-care/Childcare-accessories-and-tech/Food-heaters",0,"/Kids/Baby-care/Childcare-accessories-and-tech/Breast-pumps-and-accessories",1,"/Kids/Baby-care/Childcare-accessories-and-tech/Sterilisers",2,"/Kids/Baby-care/Childcare-accessories-and-tech/Thermometers-and-scales",3,"/Kids/Baby-care/Bouncers-and-swings-1688",4,"/Kids/Baby-care/Bouncers-and-swings/Swings",5,"/Kids/Baby-care/Bibs",6,"/Kids/Baby-care/Potties",7,"/Kids/Baby-care/Childproofing-and-safety/Childproofing-gates-and-guards",,"/Kids/Boys-clothing/Trousers-and-dungarees/Jeans",,"/Kids/Boys-clothing/Trousers-and-dungarees/Skinny-trousers",0,"/Kids/Boys-clothing/Trousers-and-dungarees/Wide-leg-trousers",1,"/Kids/Baby-care/Childproofing-and-safety-equipment/Car-sun-shades-and-screens",2,"/Kids/Boys-clothing/Trousers-and-dungarees/Leggings",3,"/Kids/Boys-clothing/Trousers-and-dungarees/Jumpsuits-and-dungarees",4,"/Kids/Baby-care/Childproofing-and-safety-equipment/Cycling-and-roller-skating-safety-equipment",5,"/Kids/Toys-and-games/Electronic-games",6,"/Kids/Toys-and-games/Action-figures",7,"/Kids/Toys-and-games/Dolls",8,"/Kids/Boys-clothing/Accessories/Gloves",,"/Kids/Boys-clothing/Accessories/Scarves-and-shawls",0,"/Kids/Boys-clothing/Accessories/Belts",1,"/Kids/Boys-clothing/Accessories/Wallets",2,"/Kids/Boys-clothing/Accessories/Ties-and-bow-ties",3,"/Kids/Boys-clothing/Accessories/Other-accessories",4,"/Kids/Boys-clothing/Accessories/Caps-and-hats",5,"/Kids/Boys-clothing/Swimwear/Swimming-trunks",6,"/Kids/Boys-clothing/Swimwear/Bathrobes",7,"/Kids/Boys-clothing/Sleepwear/One-piece-pyjamas",8,"/Kids/Boys-clothing/Sleepwear/Two-piece-pyjamas",,"/Kids/Boys-clothing/Underwear-and-socks/Socks",00,"/Kids/Boys-clothing/Underwear-and-socks/Tights-and-leggings",01,"/Kids/Boys-clothing/Underwear-and-socks/Underwear",02,"/Kids/Boys-clothing/Clothing-bundles",03,"/Kids/Boys-clothing/Clothing-for-twins",04,"/Kids/Boys-clothing/Fancy-dress-and-costumes",05,"/Kids/Toys-and-games/Educational-toys-and-games",06,"/Kids/Toys-and-games/Soft-toys-and-stuffed-animals",07,"/Kids/Toys-and-games/Rattles-and-chew-toys",08,"/Kids/Toys-and-games/Musical-toys",09,"/Kids/Toys-and-games/Construction-toys",10,"/Kids/Toys-and-games/Wooden-toys",11,"/Kids/Toys-and-games/Hanging-mobiles",12,"/Kids/Toys-and-games/Water-toys-and-games",13,"/Kids/Toys-and-games/Outdoor-toys-and-games",14,"/Kids/Baby-care/Childproofing-and-safety-equipment/Other-childproofing-and-safety-equipment",15,"/Women/Clothes/Coats-and-jackets/Capes-and-ponchos",16,"/Women/Clothes/Dresses/Special-occasion-dresses/Party-and-cocktail-dresses",17,"/Women/Clothes/Dresses/Special-occasion-dresses/Wedding-dresses",18,"/Women/Clothes/Dresses/Special-occasion-dresses/Prom-dresses",19,"/Women/Clothes/Dresses/Special-occasion-dresses/Evening-dresses",20,"/Women/Clothes/Dresses/Winter-dresses",21,"/Women/Clothes/Swimwear/Cover-ups-and-sarongs",22,"/Women/Clothes/Lingerie-and-nightwear/Shapewear",23,"/Women/Clothes/Costumes-and-special-outfits",24,"/Women/Bags/Satchels",25,"/Women/Accessories/Jewellery/Anklets",26,"/Men/Clothes/Suits-and-blazers/Suit-jackets-and-blazers",27,"/Men/Clothes/Suits-and-blazers/Suit-trousers",28,"/Men/Clothes/Suits-and-blazers/Waistcoats",29,"/Men/Clothes/Suits-and-blazers/Suit-sets","/Men/Clothes/Suits-and-blazers/Wedding-suits","/Men/Shoes/Boots/Wellington-boots","/Men/Accessories/Bags-and-backpacks/Satchels","/Men/Accessories/Bags-and-backpacks/Holdalls","/Men/Accessories/Bags-and-backpacks/Bum-bags","/Men/Accessories/Jewellery/Cufflinks","/Men/Clothes/Tops-and-t-shirts/Shirts/Checked-shirts","/Men/Clothes/Tops-and-t-shirts/Shirts/Denim-shirts","/Men/Clothes/Tops-and-t-shirts/Shirts/Plain-shirts","/Men/Clothes/Tops-and-t-shirts/Shirts/Print-shirts","/Men/Clothes/Tops-and-t-shirts/Shirts/Striped-shirts","/Men/Clothes/Tops-and-t-shirts/T-shirts/Plain-t-shirts","/Men/Clothes/Tops-and-t-shirts/T-shirts/Print-t-shirts","/Men/Clothes/Tops-and-t-shirts/T-shirts/Striped-t-shirts","/Men/Clothes/Tops-and-t-shirts/T-shirts/Polo-shirts","/Men/Clothes/Tops-and-t-shirts/T-shirts/Long-sleeved-t-shirts","/Men/Clothes/Jumpers-and-sweaters-1811","/Men/Clothes/Jumpers-and-sweaters/Zip-through-hoodies","/Men/Clothes/Jumpers-and-sweaters/Crew-neck-jumpers","/Men/Clothes/Jumpers-and-sweaters/Long-jumpers",0,"/Men/Clothes/Jumpers-and-sweaters/Chunky-knit-jumpers",1,"/Men/Clothes/Jeans/Ripped-jeans",2,"/Men/Clothes/Jeans/Skinny-jeans",3,"/Men/Clothes/Jeans/Slim-fit-jeans",4,"/Men/Clothes/Jeans/Straight-fit-jeans",5,"/Men/Clothes/Trousers/Chinos",,"/Men/Clothes/Trousers/Joggers",,"/Men/Clothes/Shorts/Cargo-shorts",,"/Men/Clothes/Shorts/Chino-shorts",,"/Men/Clothes/Shorts/Denim-shorts",0,"/Men/Clothes/Jumpers-and-sweaters/Sleeveless-jumpers",1,"/Men/Grooming/Tools-and-accessories/Shaving-tools",2,"/Men/Grooming/Tools-and-accessories/Grooming-tools",3,"/Men/Clothes/Socks-and-underwear-1828",4,"/Men/Clothes/Socks-and-underwear/Pants-and-boxers",5,"/Men/Clothes/Socks-and-underwear/Dressing-gowns",6,"/Women/Clothes/Coats-and-jackets/Trench-coats",,"/Women/Clothes/Tops-and-t-shirts/Bodysuits",,"/Women/Clothes/Tops-and-t-shirts/Peplum-tops",,"/Women/Clothes/Shorts-and-cropped-trousers/Low-waisted-shorts",0,"/Women/Clothes/Jeans/Boyfriend-jeans",1,"/Women/Clothes/Jeans/Cropped-jeans",2,"/Women/Clothes/Jeans/Flared-jeans",3,"/Women/Clothes/Jeans/High-waisted-jeans",4,"/Women/Clothes/Jeans/Ripped-jeans",5,"/Women/Clothes/Jeans/Skinny-jeans",6,"/Women/Clothes/Jeans/Straight-jeans",7,"/Women/Clothes/Trousers-and-leggings/Straight-leg-trousers",,"/Women/Clothes/Lingerie-and-nightwear/Lingerie-accessories",,"/Women/Bags/Bum-bags",0,"/Women/Bags/Holdalls",1,"/Women/Bags/Luggage-and-suitcases",2,"/Women/Accessories/Umbrellas",3,"/Women/Accessories/Keyrings",4,"/Men/Clothes/Coats-and-jackets/Jackets/Fleece-jackets",5,"/Men/Clothes/Coats-and-jackets/Raincoats",6,"/Men/Clothes/Coats-and-jackets/Peacoats",7,"/Men/Accessories/Bags-and-backpacks/Luggage",8,"/Men/Grooming/Grooming-kits",,"/Women/Clothes/Jeans/Other",0,"/Men/Clothes/Tops-and-t-shirts/Shirts/Other-shirts",1,"/Men/Clothes/Suits-and-blazers/Other-suits-and-blazers",2,"/Men/Clothes/Socks-and-underwear/Other-socks-and-underwear",3,"/Men/Clothes/Tops-and-t-shirts/T-shirts/Other-t-shirts",4,"/Kids/Boys-clothing/Trousers-shorts-and-dungarees/Other-trousers-shorts-and-dungarees",5,"/Kids/Boys-clothing/Underwear-and-socks/Other-underwear-and-socks",6,"/Kids/Girls-clothing/Underwear-and-socks/Other-underwear-and-socks",7,"/Women/Clothes/Jumpers-and-sweaters/Waistcoats",8,"/Kids/Girls-clothing/Baby-clothing/Others",,"/Kids/Girls-clothing/Jumpers-and-hoodies/Other-jumpers-and-hoodies",00,"/Kids/Girls-clothing/Tops-and-t-shirts/Other-tops-and-t-shirts",01,"/Kids/Girls-clothing/Trousers-shorts-and-dungarees/Other-trousers-shorts-and-dungarees",02,"/Kids/Girls-clothing/Accessories/Other-accessories",03,"/Kids/Boys-clothing/Baby-clothing/Other-baby-clothing",04,"/Kids/Boys-clothing/Tops-and-t-shirts/Other-tops-and-t-shirts",05,"/Kids/Boys-clothing/Jumpers-and-hoodies/Other-jumpers-and-hoodies",06,"/Women/Beauty/Hair-care",07,"/Women/Beauty/Beauty-tools/Hair-styling-tools",08,"/Home/Textiles/Blankets",09,"/Home/Textiles/Table-linen",10,"/Home/Textiles/Tapestries-and-wall-hangings",11,"/Home/Home-accessories/Picture-and-photo-frames",12,"/Home/Home-accessories/Vases",13,"/Home/Home-accessories/Display-shelves",14,"/Home/Textiles/Bedding/Bedding-sets",15,"/Home/Textiles/Bedding/Duvet-covers",16,"/Home/Textiles/Bedding/Pillowcases",17,"/Home/Textiles/Bedding/Sheets",18,"/Home/Textiles/Curtains-and-drapes/Opaque-curtains-and-drapes",19,"/Home/Textiles/Towels/Bath-towels",20,"/Home/Textiles/Towels/Beach-towels",21,"/Home/Textiles/Towels/Hand-towels",22,"/Home/Tableware/Cutlery/Cutlery-sets",23,"/Home/Tableware/Cutlery/Forks",24,"/Home/Tableware/Cutlery/Spoons",25,"/Home/Textiles/Rugs-and-mats/Doormats-and-floor-mats",26,"/Home/Textiles/Rugs-and-mats-1954",27,"/Home/Textiles/Curtains-and-drapes/Sheer-curtains-and-drapes",28,"/Home/Home-accessories/Candles-and-candle-holders-1956",29,"/Home/Home-accessories/Candles-and-candle-holders/Candle-holders","/Home/Tableware/Dinnerware/Dinner-sets","/Home/Tableware/Dinnerware/Bowls","/Home/Tableware/Dinnerware/Plates","/Home/Tableware/Dinnerware/Trays","/Home/Home-accessories/Storage/Baskets","/Home/Home-accessories/Storage/Boxes","/Home/Home-accessories/Storage/Jewellery-organisers","/Home/Home-accessories/Storage/Make-up-organisers","/Home/Home-accessories/Clocks/Table-clocks","/Home/Home-accessories/Clocks/Wall-clocks","/Home/Home-accessories/Mirrors/Wall-mirrors","/Home/Home-accessories/Mirrors/Table-mirrors","/Home/Tableware/Cutlery/Table-knives","/Home/Textiles/Cushions","/Home/Tableware/Drinkware/Cups-and-mugs","/Home/Tableware/Drinkware/Coffeepots-and-teapots-2007","/Home/Tableware/Drinkware/Jugs","/Home/Tableware/Drinkware/Stemmed-glasses","/Home/Tableware/Drinkware/Tumblers","/Home/Tableware/Drinkware/Drinkware-sets","/Home/Home-accessories/Storage/Clothes-bags-and-hangers","/Kids/Girls-clothing/Trousers-and-shorts/Harem-trousers","/Kids/Girls-clothing/Formal-wear-and-special-occasion-clothing","/Kids/Boys-clothing/Trousers-and-dungarees/Harem-trousers","/Kids/Boys-clothing/Formal-wear-and-special-occasion-clothing","/Women/Clothes/Maternity-clothes/Sport-clothes","/Kids/Toys-and-games/Kitchen-toys","/Kids/Toys-and-games/Sleeping-toys",58,"/Kids/Baby-care/Nappies-and-skincare/Nappy-waste-containers","/Kids/Baby-care/Nursing-and-feeding/Feeding-pillows-2088",0,"/Pet-care/Cats/Beds",1,"/Pet-care/Cats/Bowls-and-feeders-2099",2,"/Pet-care/Dogs/Bowls-and-feeders-2117",3,"/Pet-care/Dogs/Bowls-and-feeders/Feeders",4,"/Pet-care/Dogs/Clothing-and-accessories/Coats-and-jackets",5,"/Pet-care/Dogs/Clothing-and-accessories/Shoes-and-boots",6,"/Pet-care/Dogs/Clothing-and-accessories/Accessories",,"/Pet-care/Dogs/Collars-and-leads-2122",,"/Pet-care/Dogs/Collars-and-leads/Leads",,"/Pet-care/Dogs/Collars-and-leads/Harnesses",0,"/Pet-care/Cats/Bowls-and-feeders/Feeders",1,"/Pet-care/Cats/Clothing-and-accessories-2128",2,"/Pet-care/Cats/Clothing-and-accessories/Costumes",3,"/Pet-care/Cats/Clothing-and-accessories/Accessories",4,"/Pet-care/Cats/Collars-and-leads-2133",5,"/Pet-care/Cats/Collars-and-leads/Harnesses-and-leads",6,"/Pet-care/Small-pets/Habitats-and-accessories",7,"/Pet-care/Small-pets/Toys","/Pet-care/Dogs/Clothing-and-accessories/Jumpers",0,"/Pet-care/Cats/Litter-boxes",1,"/Pet-care/Fish/Decorations-and-accessories",2,"/Pet-care/Fish/Aquarium-equipment",3,"/Pet-care/Birds/Toys",4,"/Pet-care/Birds/Cages-and-accessories",5,"/Pet-care/Reptiles/Decorations-and-accessories",6,"/Pet-care/Reptiles/Terrarium-equipment",7,"/Pet-care/Cats/Grooming/Brushes-and-combs",,"/Pet-care/Cats/Grooming/Claw-care",,"/Pet-care/Cats/Travel-carriers/Hard-carriers",0,"/Pet-care/Cats/Travel-carriers/Soft-carriers-and-backpacks",1,"/Pet-care/Cats/Toys/Teasers-and-wands",2,"/Pet-care/Cats/Toys/Balls",3,"/Pet-care/Cats/Toys/Soft-toys",4,"/Pet-care/Cats/Toys/Scratchers",5,"/Pet-care/Cats/Toys/Interactive-toys",6,"/Pet-care/Dogs/Grooming/Claw-care",7,"/Pet-care/Dogs/Grooming/Brushes-and-combs",8,"/Pet-care/Dogs/Carriers-and-crates/Crates",,"/Pet-care/Dogs/Carriers-and-crates/Travel-carriers",0,"/Pet-care/Dogs/Training-accessories/Bags",1,"/Pet-care/Dogs/Training-accessories/Whistles",2,"/Pet-care/Dogs/Beds-and-blankets/Blankets",3,"/Pet-care/Dogs/Beds-and-blankets-2512",4,"/Pet-care/Dogs/Toys/Tough-and-durable-toys",5,"/Pet-care/Dogs/Toys/Soft-toys",6,"/Pet-care/Dogs/Toys/Balls-and-fetch-toys",7,"/Pet-care/Dogs/Collars-and-leads/Muzzles",8,"/Pet-care/Dogs/Clothing-and-accessories/T-shirts",,"/Pet-care/Dogs/Clothing-and-accessories/Costumes",01,"/Women/Clothes/Outerwear/Gilets-and-body-warmers",02,"/Women/Clothes/Outerwear/Coats/Duffle-coats",03,"/Women/Clothes/Outerwear/Coats/Overcoats-and-long-coats",04,"/Women/Clothes/Outerwear/Jackets/Biker-and-racer-jackets",05,"/Women/Clothes/Outerwear/Jackets/Field-and-utility-jackets",06,"/Women/Clothes/Outerwear/Jackets/Shackets",07,"/Women/Clothes/Outerwear/Jackets/Ski-and-snowboard-jackets",08,"/Women/Clothes/Outerwear/Jackets/Varsity-jackets",09,"/Women/Clothes/Outerwear/Jackets/Windbreakers",10,"/Men/Clothes/Outerwear/Coats/Overcoats-and-long-coats",11,"/Men/Clothes/Outerwear/Jackets/Biker-and-racer-jackets",12,"/Men/Clothes/Outerwear/Jackets/Field-and-utility-jackets",13,"/Men/Clothes/Outerwear/Jackets/Puffer-jackets",14,"/Men/Clothes/Outerwear/Jackets/Quilted-jackets",15,"/Men/Clothes/Outerwear/Jackets/Shackets",16,"/Men/Clothes/Outerwear/Jackets/Ski-and-snowboard-jackets",17,"/Kids/Girls-clothing/Outerwear/Coats/Duffle-coats",18,"/Kids/Girls-clothing/Outerwear/Coats/Parkas",19,"/Kids/Girls-clothing/Outerwear/Coats/Peacoats",20,"/Kids/Girls-clothing/Outerwear/Coats/Trench-coats",21,"/Kids/Girls-clothing/Outerwear/Jackets/Blazers",22,"/Kids/Girls-clothing/Outerwear/Jackets/Bomber-jackets",23,"/Kids/Girls-clothing/Outerwear/Jackets/Denim-jackets",24,"/Kids/Girls-clothing/Outerwear/Jackets/Fleece-jackets",25,"/Kids/Girls-clothing/Outerwear/Jackets/Puffer-jackets",26,"/Kids/Girls-clothing/Outerwear/Jackets/Windbreakers",27,"/Men/Clothes/Outerwear/Jackets/Varsity-jackets",28,"/Men/Clothes/Outerwear/Jackets/Windbreakers",29,"/Men/Clothes/Outerwear/Ponchos","/Men/Clothes/Outerwear/Gilets-and-body-warmers","/Kids/Girls-clothing/Outerwear/Rain-gear/Rain-trousers","/Kids/Girls-clothing/Outerwear/Rain-gear/Ponchos","/Kids/Girls-clothing/Outerwear/Rain-gear/Rain-suits-and-sets","/Kids/Girls-clothing/Outerwear/Rain-gear/Raincoats","/Kids/Girls-clothing/Outerwear/Snow-gear/Snow-jackets-and-coats","/Kids/Boys-clothing/Outerwear/Coats/Duffle-coats","/Kids/Boys-clothing/Outerwear/Coats/Parkas","/Kids/Boys-clothing/Outerwear/Coats/Peacoats","/Kids/Boys-clothing/Outerwear/Coats/Trench-coats","/Kids/Girls-clothing/Outerwear/Snow-gear/Snow-suits-and-sets","/Kids/Boys-clothing/Outerwear/Jackets/Blazers","/Kids/Boys-clothing/Outerwear/Jackets/Bomber-jackets","/Kids/Boys-clothing/Outerwear/Jackets/Denim-jackets","/Kids/Boys-clothing/Outerwear/Jackets/Fleece-jackets","/Kids/Boys-clothing/Outerwear/Jackets/Puffer-jackets","/Kids/Boys-clothing/Outerwear/Jackets/Windbreakers","/Kids/Girls-clothing/Outerwear/Snow-gear/Snow-trousers","/Women/Clothes/Outerwear/Jackets/Quilted-jackets","/Kids/Boys-clothing/Outerwear/Rain-gear/Rain-trousers","/Kids/Boys-clothing/Outerwear/Rain-gear/Ponchos","/Kids/Boys-clothing/Outerwear/Rain-gear/Raincoats","/Kids/Boys-clothing/Outerwear/Rain-gear/Rain-suits-and-sets","/Kids/Boys-clothing/Outerwear/Snow-gear/Snow-jackets-and-coats","/Kids/Boys-clothing/Outerwear/Snow-gear/Snow-trousers","/Kids/Boys-clothing/Outerwear/Snow-gear/Snow-suits-and-sets","/Women/Clothes/Outerwear/Jackets/Puffer-jackets","/Women/Shoes/Boots/Ankle-boots",58,"/Women/Shoes/Boots/Mid-calf-boots","/Women/Shoes/Boots/Over-the-knee-boots","/Women/Shoes/Boots/Snow-boots","/Women/Shoes/Boots/Work-boots",62,"/Women/Shoes/Clogs-and-mules",63,"/Women/Shoes/Trainers",64,"/Women/Shoes/Flat-shoes/Boat-shoes-loafers-and-moccasins",65,"/Women/Shoes/Flat-shoes/Espadrilles",66,"/Women/Shoes/Flat-shoes/Lace-up-shoes",67,"/Women/Shoes/Flip-flops-flat-sandals-and-slides/Flip-flops",68,"/Women/Shoes/Flip-flops-flat-sandals-and-slides/Flat-sandals",69,"/Women/Shoes/Flip-flops-flat-sandals-and-slides/Slides",70,"/Women/Shoes/Sports-shoes/Basketball-shoes",71,"/Women/Shoes/Sports-shoes/Climbing-and-bouldering-shoes",72,"/Women/Shoes/Sports-shoes/Cycling-shoes",73,"/Women/Shoes/Sports-shoes/Dance-shoes",74,"/Women/Shoes/Sports-shoes/Football-boots",75,"/Women/Shoes/Sports-shoes/Golf-shoes",76,"/Women/Shoes/Sports-shoes/Hiking-boots-and-shoes",77,"/Women/Shoes/Sports-shoes/Ice-skates",78,"/Women/Shoes/Sports-shoes/Indoor-football-shoes",79,"/Women/Shoes/Sports-shoes/Indoor-training-shoes-2648",0,"/Women/Shoes/Sports-shoes/Motorcycle-boots",1,"/Women/Shoes/Sports-shoes/Roller-skates-and-inline-skates",2,"/Women/Shoes/Sports-shoes/Running-shoes-2651",3,"/Women/Shoes/Sports-shoes/Ski-boots",4,"/Women/Shoes/Sports-shoes/Snowboard-boots",5,"/Women/Shoes/Sports-shoes/Swimming-and-water-shoes",6,"/Women/Shoes/Sports-shoes/Tennis-shoes",7,"/Men/Shoes/Boat-shoes-loafers-and-moccasins",8,"/Men/Shoes/Espadrilles",,"/Men/Shoes/Slippers",0,"/Men/Shoes/Boots/Chelsea-and-slip-on-boots",1,"/Men/Shoes/Boots/Desert-and-lace-up-boots",2,"/Men/Shoes/Boots/Snow-boots",3,"/Men/Shoes/Boots/Work-boots",4,"/Men/Shoes/Flip-flops-sandals-and-slides/Clogs-and-mules",5,"/Men/Shoes/Flip-flops-sandals-and-slides/Flip-flops",6,"/Men/Shoes/Flip-flops-sandals-and-slides/Sandals",7,"/Men/Shoes/Flip-flops-sandals-and-slides/Slides",8,"/Men/Shoes/Formal-shoes/Lace-up-shoes",,"/Men/Shoes/Formal-shoes/Slip-on-shoes",00,"/Men/Shoes/Formal-shoes/Monk-strap-shoes",01,"/Men/Shoes/Sports-shoes/Basketball-shoes",02,"/Men/Shoes/Sports-shoes/Climbing-and-bouldering-shoes",03,"/Men/Shoes/Sports-shoes/Cycling-shoes",04,"/Men/Shoes/Sports-shoes/Dance-shoes",05,"/Men/Shoes/Sports-shoes/Football-boots",06,"/Men/Shoes/Sports-shoes/Golf-shoes",07,"/Men/Shoes/Sports-shoes/Hiking-boots-and-shoes",08,"/Men/Shoes/Sports-shoes/Ice-skates",09,"/Men/Shoes/Sports-shoes/Indoor-football-shoes",10,"/Men/Shoes/Sports-shoes/Motorcycle-boots",11,"/Men/Shoes/Sports-shoes/Roller-skates-and-inline-skates",12,"/Men/Shoes/Sports-shoes/Ski-boots",13,"/Men/Shoes/Sports-shoes/Snowboard-boots",14,"/Men/Shoes/Sports-shoes/Swimming-and-water-shoes",15,"/Men/Shoes/Sports-shoes/Tennis-shoes",16,"/Women/Shoes/Heels/Court-shoes",17,"/Women/Shoes/Heels/High-heeled-sandals",18,"/Women/Shoes/Flat-shoes/Mary-janes",19,"/Kids/Girls-clothing/Shoes/Clogs-and-mules",20,"/Kids/Girls-clothing/Shoes/Heels",21,"/Kids/Girls-clothing/Shoes/Boots/Ankle-boots",22,"/Kids/Girls-clothing/Shoes/Boots/Mid-calf-boots",23,"/Kids/Girls-clothing/Shoes/Boots/Snow-boots",24,"/Kids/Girls-clothing/Shoes/Boots/Wellington-boots",25,"/Kids/Girls-clothing/Shoes/Flat-shoes/Espadrilles",26,"/Kids/Girls-clothing/Shoes/Flat-shoes/Lace-up-shoes",27,"/Kids/Girls-clothing/Shoes/Flip-flops-sandals-and-slides/Flip-flops",28,"/Kids/Girls-clothing/Shoes/Flip-flops-sandals-and-slides/Sandals",29,"/Kids/Girls-clothing/Shoes/Flip-flops-sandals-and-slides/Slides","/Kids/Girls-clothing/Shoes/Sports-shoes/Basketball-shoes","/Kids/Girls-clothing/Shoes/Sports-shoes/Dance-shoes","/Kids/Girls-clothing/Shoes/Sports-shoes/Football-boots","/Kids/Girls-clothing/Shoes/Sports-shoes/Hiking-boots-and-shoes","/Kids/Girls-clothing/Shoes/Sports-shoes/Ice-skates","/Kids/Girls-clothing/Shoes/Sports-shoes/Roller-skates-and-inline-skates","/Kids/Girls-clothing/Shoes/Sports-shoes/Running-shoes","/Kids/Girls-clothing/Shoes/Sports-shoes/Ski-boots","/Kids/Girls-clothing/Shoes/Sports-shoes/Snowboard-boots","/Kids/Girls-clothing/Shoes/Sports-shoes/Swimming-and-water-shoes","/Kids/Girls-clothing/Shoes/Trainers/Hook-and-loop-trainers","/Kids/Girls-clothing/Shoes/Trainers/Lace-up-trainers","/Kids/Girls-clothing/Shoes/Trainers/Slip-on-trainers","/Kids/Boys-clothing/Shoes/Boat-shoes-loafers-and-moccasins","/Kids/Boys-clothing/Shoes/Espadrilles","/Kids/Boys-clothing/Shoes/Boots/Ankle-boots","/Kids/Boys-clothing/Shoes/Boots/Mid-calf-boots","/Kids/Boys-clothing/Shoes/Boots/Snow-boots","/Kids/Boys-clothing/Shoes/Boots/Wellington-boots","/Kids/Boys-clothing/Shoes/Flip-flops-sandals-and-slides/Clogs-and-mules","/Kids/Boys-clothing/Shoes/Flip-flops-sandals-and-slides/Flip-flops","/Kids/Boys-clothing/Shoes/Flip-flops-sandals-and-slides/Sandals","/Kids/Boys-clothing/Shoes/Flip-flops-sandals-and-slides/Slides","/Kids/Boys-clothing/Shoes/Sports-shoes/Basketball-shoes","/Kids/Boys-clothing/Shoes/Sports-shoes/Dance-shoes","/Kids/Boys-clothing/Shoes/Sports-shoes/Football-boots","/Kids/Boys-clothing/Shoes/Sports-shoes/Hiking-boots-and-shoes","/Kids/Boys-clothing/Shoes/Sports-shoes/Ice-skates",58,"/Kids/Boys-clothing/Shoes/Sports-shoes/Roller-skates-and-inline-skates","/Kids/Boys-clothing/Shoes/Sports-shoes/Running-shoes","/Kids/Boys-clothing/Shoes/Sports-shoes/Ski-boots","/Kids/Boys-clothing/Shoes/Sports-shoes/Snowboard-boots",62,"/Kids/Boys-clothing/Shoes/Sports-shoes/Swimming-and-water-shoes",63,"/Kids/Boys-clothing/Shoes/Trainers/Hook-and-loop-trainers",64,"/Kids/Boys-clothing/Shoes/Trainers/Lace-up-trainers",65,"/Kids/Boys-clothing/Shoes/Trainers/Slip-on-trainers","/Kids/Girls-clothing/Shoes/Flat-shoes/Ballerinas-mary-janes-and-t-bar-shoes"]#"/Women/Clothes/Tops-and-t-shirts/Camis","/Women/Clothes/Other-clothing","/Women/Accessories/Belts","/Women/Accessories/Watches","/Women/Accessories/Sunglasses","/Women/Clothes/Dresses/Other-dresses","/Women/Accessories/Jewellery/Jewellry-sets","/Women/Accessories/Jewellery/Brooches","/Women/Accessories/Jewellery/Bracelets","/Women/Accessories/Jewellery/Necklaces-beads-and-pendants","/Women/Accessories/Jewellery/Earrings","/Women/Accessories/Jewellery/Other-jewellery","/Women/Bags/Make-up-bags","/Women/Bags/Purses-and-wallets","/Women/Bags/Clutches","/Women/Bags/Shoulder-bags","/Women/Bags/Backpacks","/Women/Bags/Handbags","/Women/Bags/Other-bags","/Women/Beauty/Other-beauty-items","/Women/Beauty/Perfume","/Men/Grooming/Aftershave-and-cologne","/Men/Grooming/Make-up","/Men/Grooming/Face-care","/Men/Grooming/Hand-and-nail-care","/Men/Grooming/Body-care","/Men/Grooming/Hair-care","/Men/Accessories/Other","/Women/Clothes/Lingerie-and-nightwear/Other","/Women/Clothes/Lingerie-and-nightwear/Nightwear","/Women/Clothes/Lingerie-and-nightwear/Panties","/Women/Clothes/Lingerie-and-nightwear/Bras","/Men/Accessories/Sunglasses","/Men/Accessories/Belts","/Men/Accessories/Watches","/Men/Accessories/Ties-and-pocket-squares","/Men/Clothes/Swimwear","/Women/Accessories/Gloves","/Men/Accessories/Gloves","/Men/Clothes/Costumes-and-special-outfits","/Women/Clothes/Trousers-and-leggings/Other-trousers","/Entertainment/Music-and-video/Video/Vhs","/Entertainment/Music-and-video/Video/Dvd","/Entertainment/Music-and-video/Music/Older-audio-formats","/Entertainment/Music-and-video/Music/Vinyl","/Entertainment/Music-and-video/Music/Cassettes","/Entertainment/Music-and-video/Music/Cds","/Entertainment/Games-and-puzzles/Card-games","/Entertainment/Games-and-puzzles/Board-games","/Entertainment/Books/Literature-and-fiction/Poetry-and-drama","/Entertainment/Books/Literature-and-fiction/Humour","/Entertainment/Books/Literature-and-fiction/Crime-and-thrillers","/Entertainment/Books/Literature-and-fiction/Contemporary-fiction","/Entertainment/Books/Literature-and-fiction/Comics-and-graphic-novels","/Entertainment/Books/Literature-and-fiction/Classical-literature","/Women/Clothes/Dresses/Mini-dresses","/Entertainment/Books/Non-fiction/Food-and-drink","/Entertainment/Books/Non-fiction/Computers-and-tech","/Entertainment/Books/Non-fiction/Biography","/Entertainment/Books/Non-fiction/Business-and-finance","/Entertainment/Books/Non-fiction/Arts-and-entertainment","/Entertainment/Books/Literature-and-fiction/Romance","/Entertainment/Books/Literature-and-fiction/Science-fiction-and-fantasy","/Entertainment/Books/Literature-and-fiction/Other-literature-and-fiction","/Entertainment/Video-games-and-consoles/Playstation-5/Accessories","/Entertainment/Video-games-and-consoles/Playstation-5/Games","/Entertainment/Video-games-and-consoles/Playstation-5/Consoles","/Entertainment/Video-games-and-consoles/Older-xbox/Accessories","/Entertainment/Video-games-and-consoles/Older-xbox/Consoles","/Entertainment/Video-games-and-consoles/Older-xbox/Games","/Entertainment/Video-games-and-consoles/Xbox-one/Games","/Entertainment/Video-games-and-consoles/Xbox-one/Consoles","/Entertainment/Video-games-and-consoles/Xbox-one/Accessories","/Entertainment/Video-games-and-consoles/Xbox-series-x-and-s/Accessories","/Entertainment/Video-games-and-consoles/Xbox-series-x-and-s/Consoles","/Entertainment/Video-games-and-consoles/Xbox-series-x-and-s/Games","/Entertainment/Video-games-and-consoles/Pc-games","/Entertainment/Books/Kids-and-young-adults/Babies-and-toddlers","/Entertainment/Books/Kids-and-young-adults","/Entertainment/Books/Kids-and-young-adults/Young-adults","/Entertainment/Books/Non-fiction/Professional-and-technical","/Entertainment/Books/Non-fiction/Reference","/Entertainment/Books/Non-fiction/Religion-and-spirituality","/Entertainment/Books/Non-fiction/Science-and-nature","/Entertainment/Books/Non-fiction/Sports","/Entertainment/Books/Non-fiction/Study-materials-and-textbooks","/Entertainment/Books/Non-fiction/Travel","/Entertainment/Books/Non-fiction/Other-non-fiction","/Entertainment/Books/Non-fiction/Health-and-wellbeing","/Entertainment/Books/Non-fiction/History","/Entertainment/Books/Non-fiction/Hobbies-crafts-and-diy","/Entertainment/Books/Non-fiction/Parenting-and-family","/Entertainment/Books/Non-fiction/Politics-and-society","/Entertainment/Video-games-and-consoles/Virtual-reality/Games","/Entertainment/Video-games-and-consoles/Retro-gaming/Steam","/Entertainment/Video-games-and-consoles/Retro-gaming/Intellivision","/Entertainment/Video-games-and-consoles/Retro-gaming/Atari","/Entertainment/Video-games-and-consoles/Retro-gaming/Colecovision","/Entertainment/Video-games-and-consoles/Retro-gaming/Commodore","/Entertainment/Video-games-and-consoles/Retro-gaming/-3do","/Entertainment/Video-games-and-consoles/Older-nintendo/Games","/Entertainment/Video-games-and-consoles/Older-nintendo/Consoles","/Entertainment/Video-games-and-consoles/Older-nintendo/Accessories","/Entertainment/Video-games-and-consoles/Nintendo-game-boy/Games","/Entertainment/Video-games-and-consoles/Nintendo-game-boy/Consoles","/Entertainment/Video-games-and-consoles/Nintendo-game-boy/Accessories","/Entertainment/Video-games-and-consoles/Nintendo-3ds-and-2ds/Games","/Entertainment/Video-games-and-consoles/Nintendo-3ds-and-2ds/Consoles","/Entertainment/Video-games-and-consoles/Nintendo-3ds-and-2ds/Accessories","/Entertainment/Video-games-and-consoles/Nintendo-wii-and-wii-u/Games","/Entertainment/Video-games-and-consoles/Nintendo-wii-and-wii-u/Consoles","/Entertainment/Video-games-and-consoles/Nintendo-wii-and-wii-u/Accessories","/Entertainment/Video-games-and-consoles/Nintendo-switch/Games","/Entertainment/Video-games-and-consoles/Nintendo-switch/Consoles","/Entertainment/Video-games-and-consoles/Nintendo-switch/Accessories","/Entertainment/Video-games-and-consoles/Older-playstation/Games","/Entertainment/Video-games-and-consoles/Older-playstation/Consoles","/Entertainment/Video-games-and-consoles/Older-playstation/Accessories","/Entertainment/Video-games-and-consoles/Playstation-4/Games","/Entertainment/Video-games-and-consoles/Playstation-4/Consoles","/Entertainment/Video-games-and-consoles/Playstation-4/Accessories"
def findImagePath():
    start1 = gui.locateCenterOnScreen("imagePath.PNG")
    if (start1 != None):
        gui.moveTo(start1)
        gui.click()
        return None
    else:
        findImagePath()

def findImageUpload():
    start = gui.locateCenterOnScreen("imageUpload.PNG")
    if (start != None):
        gui.moveTo(start)
        gui.click()
        return None
    else:
        findImageUpload()

def locateImage():
    start1 = gui.locateCenterOnScreen("imageName.PNG")
    if (start1 != None):
        gui.moveTo(start1)
        gui.click()
        return None
    else:
        locateImage()

def findImage(a,obj):
    findImageUpload()
    findImagePath()
    gui.hotkey("ctrl","a")
    gui.hotkey("del")
    gui.typewrite('C:\\Users\\yaseen\\Desktop\\irshad\\schedule', interval=0.05)
    gui.press('enter')
    time.sleep(1)
    locateImage()
    gui.typewrite(a+".png", interval=0.05)
    start1 = gui.locateCenterOnScreen("save.PNG")
    gui.moveTo(start1)
    gui.click()
    #gui.hotkey("ctrl","f")
    return None
def resetConsole():
    x, y = gui.locateCenterOnScreen("resetConsole.PNG")
    if(x!=None):
        gui.moveTo(x, y)
        gui.click()
        gui.moveTo(x, y + 50)
        gui.click()
    else:
        resetConsole()
def findTitle(obj):
    start = gui.locateCenterOnScreen("title.PNG")
    if(start==None):
        start1 = gui.locateCenterOnScreen("title2.PNG")
        if(start1==None):
            findTitle(obj)
        else:
            gui.moveTo(start1)
            gui.click()
            gui.typewrite(obj, interval=0.05)
            return None
    else:
        gui.moveTo(start)
        gui.click()
        gui.typewrite(obj, interval=0.05)
        return None
def findDescription(obj):
    start = gui.locateCenterOnScreen("describe1.PNG")
    if (start == None):
        findDescription(obj)
    else:
        gui.moveTo(start)
        gui.click()
        gui.typewrite(obj, interval=0.05)
        return None
    start = gui.locateCenterOnScreen("outside1.PNG")
    gui.moveTo(start)
    gui.click()
    return None
def setObject(obj):
    #for obj in k:
    if "-" in obj:
        obj = obj.replace("-", " ")
    if "Pc " in obj:
        obj = obj.replace("Pc ", "PC ")
    if " xbox" in obj:
        obj = obj.replace(" xbox", " Xbox")
    if " s" in obj:
        obj = obj.replace(" s", " S")
    if " x " in obj:
        obj = obj.replace(" x ", " X ")
    if " one" in obj:
        obj = obj.replace(" one", " One")
    if "Playstation" in obj:
        obj = obj.replace("Playstation", "PlayStation")
    if "non fiction" in obj:
        obj = obj.replace("non fiction", "non-fiction")
    if "Non fiction" in obj:
        obj = obj.replace("Non fiction", "Non-fiction")
    if "Mini dresses" in obj:
        obj = obj.replace("Mini dresses", "Mini-dresses")
    if "Cds" in obj:
        obj = obj.replace("Cds", "CDs")
    if "Dvd" in obj:
        obj = obj.replace("Dvd", "DVD")
    if "Vhs" in obj:
        obj = obj.replace("Vhs", "VHS")
    if " and " in obj:
        obj = obj.replace(" and ", " & ")
    if "mens" in obj:
        obj = obj.replace("mens", "men's")
    if "Necklaces beads" in obj:
        obj = obj.replace("Necklaces beads", "Necklaces, beads")
    if "Make up" in obj:
        obj = obj.replace("Make up", "Make-up")
    if "nintendo" in obj:
        obj = obj.replace("nintendo", "Nintendo")
    if "wii" in obj:
        obj = obj.replace("wii", "Wii")
    if " u" in obj:
        obj = obj.replace(" u", " U")
    if "3ds" in obj:
        obj = obj.replace("3ds", "3DS")
    if "2ds" in obj:
        obj = obj.replace("2ds", "2DS")
    if "3do" in obj:
        obj = obj.replace("3do", "3DO")
    if "& Society" in obj:
        obj = obj.replace("& Society", "& society")
    if "Nintendo game boy" in obj:
        obj = obj.replace("Nintendo game boy", "Nintendo Game Boy")
    if " playstation" in obj:
        obj = obj.replace(" playstation", " PlayStation")
    if "Flip flops, flat Sandals & Slides" in obj:
        obj = obj.replace("Flip flops, flat Sandals & Slides", "Flip-flops, flat sandals & slides")
    return obj

def inspectOpen():
    gui.hotkey("ctrl", "shift", "j")
    time.sleep(1)
    start1 = gui.locateCenterOnScreen("console.PNG")
    if (start1!=None):
        gui.moveTo(start1)
        gui.click()
        resetConsole()
    else:
        start = gui.locateCenterOnScreen("console1.PNG")
        if (start != None):
            gui.moveTo(start)
            gui.click()
            resetConsole()
        else:
            inspectOpen()

def inspectClose():
    start1 = gui.locateCenterOnScreen("console1.PNG")
    if (start1==None):
        gui.hotkey("ctrl", "shift", "j")
        return None
    else:
        inspectClose()

def findCat():
    start = gui.locateCenterOnScreen("category1.PNG")
    if (start != None):
        gui.moveTo(start)
        gui.click()
    else:
        start = gui.locateCenterOnScreen("category1.PNG")
        if (start != None):
            gui.moveTo(start)
            gui.click()
        else:
            findCat()
def findCategories(obj):
    findOutside()
    gui.hotkey("ctrl", "end")
    obj = setObject(obj)
    findCat()
    inspectOpen()
    gui.typewrite("function doIt(obj1){a =document.getElementsByClassName('input-dropdown__content')[0].children[0].children[0].children; console.log(a); obj2 = obj1.split('/'); for(var j=0;j<obj2.length;j++){ obj=obj2[j]; for(var i=0;i<a.length;i++){ console.log(obj+'=='+a[i].textContent); if(obj==a[i].textContent){  a[i].children[0].click()}}}}function doItB(obj1) { var a = document.getElementsByClassName('input-dropdown__content')[0].children[0].children[1].children; console.log(a); if (a != null) { for (var i = 0; i < a.length; i++) { console.log(obj+'=='+a[i].textContent); if (obj1 == a[i].textContent) { a[i].children[0].click(); } } } else { var b = document.getElementsByClassName('input-dropdown__content')[0].children[0].children[4].children; if (b != null) {for (var i = 0; i < b.length; i++) { console.log(obj+'=='+b[i].textContent); if (obj1 == b[i].textContent) { b[i].children[0].click(); } }} else {var c = document.getElementsByClassName('input-dropdown__content')[0].children[0].children[2].children; if (c != null) {  for (var i = 0; i < c.length; i++) { console.log(obj+'=='+c[i].textContent); if (obj1 == c[i].textContent) { c[i].children[0].click(); } } } else {  var d = document.getElementsByClassName('input-dropdown__content')[0].children[0].children[0].children; if (d != null) {  for (var i = 0; i < d.length; i++) { console.log(obj + '==' + d[i].textContent); if (obj1 == d[i].textContent) { d[i].children[0].click(); }}}}",interval=0.03)
    #gui.typewrite("function doIt(obj1){a =document.getElementsByClassName('input-dropdown__content')[0].children[0].children[0].children;\n console.log(a);\n obj2 = obj1.split('/');\n for(var j=0;j<obj2.length;j++){\n obj=obj2[j];\n for(var i=0;i<a.length;i++){\n if(obj==a[i].textContent){ \n a[i].children[0].click()}}}}\n function doItB(obj1) { var a = document.getElementsByClassName('input-dropdown__content')[0].children[0].children[1].children;\n console.log(a);\n if (a != null) {\n for (var i = 0; i < a.length; i++) {\n if (obj1 == a[i].textContent) {\n a[i].children[0].click();\n }\n }\n } else {\n var b = document.getElementsByClassName('input-dropdown__content')[0].children[0].children[4].children;\n if (b != null) {for (var i = 0; i < b.length; i++) {\n if (obj1 == b[i].textContent) {\n b[i].children[0].click();\n }\n }} else {var c = document.getElementsByClassName('input-dropdown__content')[0].children[0].children[2].children; for (var i = 0; i < c.length; i++) {\n if (obj1 == c[i].textContent) {\n c[i].children[0].click();\n }\n }\n }\n }}",interval=0.02)
    #gui.typewrite("function doIt(obj1) { var a = document.getElementsByClassName('input-dropdown__content')[0].children[0].children[1].children;\n console.log(a);\n if (a != null) {\n for (var i = 0; i < a.length; i++) {\n if (obj1 == a[i].textContent) {\n a[i].children[0].click();\n }\n }\n } else if(a== null) {\n var b = document.getElementsByClassName('input-dropdown__content')[0].children[0].children[4].children;\n for (var i = 0; i < b.length; i++) {\n if (obj1 == b[i].textContent) {\n b[i].children[0].click();}\n }}else {\n for (var i = 0; i < c.length; i++) {\n if (obj1 == c[i].textContent) {\n c[i].children[0].click();}\n }}\n }",interval=0.02)
    #gui.typewrite("function doIt(obj1){a =document.getElementsByClassName('input-dropdown__content')[0].children[0].children[0].children;\n console.log(a);\n obj2 = obj1.split('/');\n for(var j=0;j<obj2.length;j++){\n obj=obj2[j];\n for(var i=0;i<a.length;i++){\n if(obj==a[i].textContent){ \n a[i].children[0].click()}}}}\n function doItB(obj1) {\n var a = document.getElementsByClassName('input-dropdown__content')[0].children[0].children[1].children;\n console.log(a);\n if (a != null) {\n for (var i = 0; i < a.length; i++) {\n if (obj1 == a[i].textContent) {\n a[i].children[0].click();\n  }\n}\n} else {\nvar b = document.getElementsByClassName('input-dropdown__content')[0].children[0].children[4].children;\nfor (var i = 0; i < b.length; i++) {\nif (obj1 == b[i].textContent) {\nb[i].children[0].click();\n}\n}\n}\n}",interval=0.02)
    #gui.typewrite("function doIt(obj1){a =document.getElementsByClassName('input-dropdown__content')[0].children[0].children[0].children;\n console.log(a);\n obj2 = obj1.split('/');\n for(var j=0;j<obj2.length;j++){\n obj=obj2[j];\n for(var i=0;i<a.length;i++){\n console.log(obj+'=='+a[i].textContent); \n if(obj==a[i].textContent){ \n a[i].children[0].click()}}}}", interval=0.02)
    time.sleep(10)
    gui.press('enter')
    gui.typewrite("doIt('"+obj+"')")
    gui.press('enter')
    #inspectClose()

def findUnisex(obj):
    start = gui.locateCenterOnScreen("unisex.PNG")
    if (start != None):
        gui.moveTo(start)
        gui.click()
        return None
    else:
        findUnisex(obj)
def findWriteConsole():
    start = gui.locateCenterOnScreen("consoleWrite.PNG")
    if (start != None):
        gui.moveTo(start)
        gui.click()
        return None
    else:
        start = gui.locateCenterOnScreen("writeConsole.PNG")
        if (start != None):
            gui.moveTo(start)
            gui.click()
            return None
        else:
            findWriteConsole()


def findBrand(obj):
    start = gui.locateCenterOnScreen("brand.PNG")
    if (start != None):
        gui.moveTo(start)
        gui.click()
    else:
        start = gui.locateCenterOnScreen("brand1.PNG")
        if (start != None):
            gui.moveTo(start)
            gui.click()
        else:
            findBrand(obj)
    time.sleep(1)
    findWriteConsole()
    #gui.typewrite("function doIt(obj1)    {var    a = document.getElementsByClassName('input-dropdown__content')[0].children[0].children[1].children;    console.log(a);    if (            a != null) {for (var i = 0; i < a.length; i++) {if (obj1 == a[i].textContent) {a[i].children[0].click();}}} else {var b = document.getElementsByClassName('input-dropdown__content')[0].children[0].children[4].children; for (var i = 0; i < b.length; i++) {if (obj1 == b[i].textContent) {b[i].children[0].click();}}}}",interval=0.02)
    #gui.typewrite("function doItB(obj1) {\n var a = document.getElementsByClassName('input-dropdown__content')[0].children[0].children[1].children;\n console.log(a);\n if (a != null) {\n for (var i = 0; i < a.length; i++) {\n if (obj1 == a[i].textContent) {\n a[i].children[0].click();\n  }\n}\n} else {\nvar b = document.getElementsByClassName('input-dropdown__content')[0].children[0].children[4].children;\nfor (var i = 0; i < b.length; i++) {\nif (obj1 == b[i].textContent) {\nb[i].children[0].click();\n}\n}\n}\n}",interval=0.02)
    #gui.typewrite("function doIt(obj1){a =document.getElementsByClassName('input-dropdown__content')[0].children[0].children[1].children;\n b =document.getElementsByClassName('input-dropdown__content')[0].children[0].children[4].children;\n console.log(a);\n if(a!=None){ for(var i=0;i<a.length;i++){\n if(obj1==a[i].textContent){ \n a[i].children[0].click()}};if(b!=None){for(var i=0;i<b.length;i++){\n if(obj1==b[i].textContent){ \n b[i].children[0].click()}}}",interval=0.02)
    #gui.typewrite("function doIt(obj1){a =document.getElementsByClassName('input-dropdown__content')[0].children[0].children[1].children;\n console.log(a);\n obj2 = obj1.split('/');\n for(var j=0;j<obj2.length;j++){\n obj=obj2[j];\n for(var i=0;i<a.length;i++){\n console.log(obj+'=='+a[i].textContent); \n if(obj==a[i].textContent){ \n a[i].children[0].click()}}}}",interval=0.02)
    #gui.press('enter')
    gui.typewrite("doItB('" + obj + "')")
    gui.press('enter')
    #inspectClose()
    # gui.hotkey("ctrl", "shift", "j")
    return None
def findIsbn(obj):
    start = gui.locateCenterOnScreen("isbn.PNG")
    gui.moveTo(start)
    gui.click()
    time.sleep(1)
    return None
def findSize(obj):
    start = gui.locateCenterOnScreen("size.PNG")
    if (start != None):
        gui.moveTo(start)
        gui.click()
    else:
        start = gui.locateCenterOnScreen("size1.PNG")
        if (start != None):
            gui.moveTo(start)
            gui.click()
        else:
            findSize(obj)
    findWriteConsole()
    #gui.typewrite("function doIt(obj1){a =document.getElementsByClassName('input-dropdown__content')[0].children[0].children[2].children;\n console.log(a);\n for(var i=0;i<a.length;i++){\n if(obj1==a[i].textContent){ \n a[i].children[0].click()}}}",interval=0.02)
    #gui.typewrite("function doIt(obj1){a =document.getElementsByClassName('input-dropdown__content')[0].children[0].children[1].children;\n console.log(a);\n obj2 = obj1.split('/');\n for(var j=0;j<obj2.length;j++){\n obj=obj2[j];\n for(var i=0;i<a.length;i++){\n console.log(obj+'=='+a[i].textContent); \n if(obj==a[i].textContent){ \n a[i].children[0].click()}}}}",interval=0.02)
    #gui.press('enter')
    gui.typewrite("doItB('" + obj + "')")
    gui.press('enter')
    #inspectClose()
    # gui.hotkey("ctrl", "shift", "j")
    return None
def findCondition(obj):
    start = gui.locateCenterOnScreen("condition.PNG")
    if (start != None):
        gui.moveTo(start)
        gui.click()
    else:
        findCondition(obj)
    findWriteConsole()
    #gui.typewrite("function doIt(obj1){a =document.getElementsByClassName('input-dropdown__content')[0].children[0].children[0].children;\n console.log(a);\n for(var i=0;i<a.length;i++){\n if(obj1==a[i].textContent){ \n a[i].children[0].click()}}}",interval=0.02)
    #gui.typewrite("function doIt(obj1){a =document.getElementsByClassName('input-dropdown__content')[0].children[0].children[1].children;\n console.log(a);\n obj2 = obj1.split('/');\n for(var j=0;j<obj2.length;j++){\n obj=obj2[j];\n for(var i=0;i<a.length;i++){\n console.log(obj+'=='+a[i].textContent); \n if(obj==a[i].textContent){ \n a[i].children[0].click()}}}}",interval=0.02)
    #gui.press('enter')
    gui.typewrite("doItB('" + obj + "')")
    gui.press('enter')

def findOutside():
    start = gui.locateCenterOnScreen("outside.PNG")
    if (start != None):
        gui.moveTo(start)
        gui.click()
        return None
    else:
        start = gui.locateCenterOnScreen("outside1.PNG")
        if (start != None):
            gui.moveTo(start)
            gui.click()
            return None
        else:
            findOutside()
def findColors(obj):
    start = gui.locateCenterOnScreen("colours.PNG")
    if (start!=None):
        gui.moveTo(start)
        gui.click()
    else:
        start = gui.locateCenterOnScreen("colors.PNG")
        if (start != None):
            gui.moveTo(start)
            gui.click()
        else:
            findColors(obj)
    findWriteConsole()
    #gui.typewrite("function doIt(obj1){a =document.getElementsByClassName('input-dropdown__content')[0].children[0].children[4].children;\n console.log(a);\n for(var i=0;i<a.length;i++){\n if(obj1==a[i].textContent){ \n a[i].children[0].click()}}}",interval=0.02)
    # gui.typewrite("function doIt(obj1){a =document.getElementsByClassName('input-dropdown__content')[0].children[0].children[1].children;\n console.log(a);\n obj2 = obj1.split('/');\n for(var j=0;j<obj2.length;j++){\n obj=obj2[j];\n for(var i=0;i<a.length;i++){\n console.log(obj+'=='+a[i].textContent); \n if(obj==a[i].textContent){ \n a[i].children[0].click()}}}}",interval=0.02)
    #gui.press('enter')
    gui.typewrite("doIt('" + obj + "')")
    gui.press('enter')
    #inspectClose()
    findOutside()
    return None
def findMaterial(obj):
    start = gui.locateCenterOnScreen("material.PNG")
    if (start != None):
        gui.moveTo(start)
        gui.click()
    else:
        start = gui.locateCenterOnScreen("material1.PNG")
        if (start != None):
            gui.moveTo(start)
            gui.click()
        else:
            findMaterial(obj)
    findWriteConsole()
    #gui.typewrite("function doIt(obj1){a =document.getElementsByClassName('input-dropdown__content')[0].children[0].children[0].children;\n console.log(a);\n for(var i=0;i<a.length;i++){\n if(obj1==a[i].textContent){ \n a[i].children[0].click()}}}",interval=0.02)
    # gui.typewrite("function doIt(obj1){a =document.getElementsByClassName('input-dropdown__content')[0].children[0].children[1].children;\n console.log(a);\n obj2 = obj1.split('/');\n for(var j=0;j<obj2.length;j++){\n obj=obj2[j];\n for(var i=0;i<a.length;i++){\n console.log(obj+'=='+a[i].textContent); \n if(obj==a[i].textContent){ \n a[i].children[0].click()}}}}",interval=0.02)
    #gui.press('enter')
    gui.typewrite("doIt('" + obj + "')")
    gui.press('enter')
    #inspectClose()
    findOutside()
    #gui.hotkey("ctrl", "shift", "j")
    return None

def findPrice(obj):
    start = gui.locateCenterOnScreen("price.PNG")
    if (start != None):
        gui.moveTo(start)
        gui.click()
        gui.typewrite(obj)
        return None
    else:
        start = gui.locateCenterOnScreen("price1.PNG")
        if (start != None):
            gui.moveTo(start)
            gui.click()
            gui.typewrite(obj)
            return None
        else:
            findPrice(obj)

def findParcelSize(obj):
    findOutside()
    if(obj=='small'):
        start = gui.locateCenterOnScreen("smallParcelSize.PNG")
        gui.moveTo(start)
        gui.click()
        return None

    elif (obj == 'medium'):
        start = gui.locateCenterOnScreen("mediumParcelSize.PNG")
        gui.moveTo(start)
        gui.click()
        return None

    elif (obj == 'large'):
        start = gui.locateCenterOnScreen("largeParcelSize.PNG")
        gui.moveTo(start)
        gui.click()
        return None
    else:
        findParcelWeight(obj)

def findParcelWeight(obj):
    gui.hotkey("ctrl","f")
    gui.typewrite(obj)
    findOutside()
    if (obj == 'small'):
        start = gui.locateCenterOnScreen("smallWeight.PNG")
        gui.moveTo(start)
        gui.click()
        return None
    elif (obj == 'medium'):
        start = gui.locateCenterOnScreen("mediumWeight.PNG")
        gui.moveTo(start)
        gui.click()
        return None
    elif (obj == 'large'):
        start = gui.locateCenterOnScreen("largeWeight.PNG")
        gui.moveTo(start)
        gui.click()
        return None
    else:
        findParcelSize(obj)

def findSave():
    start = gui.locateCenterOnScreen("upload.PNG")
    if(start!=None):
        gui.moveTo(start)
        gui.click()
        return None
    else:
        start = gui.locateCenterOnScreen("upload1.PNG")
        if (start != None):
            gui.moveTo(start)
            gui.click()
            return None
        else:
            findSave()

def download_image(url, file_name, headers):
    # Send GET request
    response = requests.get(url, headers=headers)
    # Save the image
    if response.status_code == 200:
        file_name = file_name
        with open(file_name, "wb") as f:
            f.write(response.content)
    else:
        print(response.status_code)
def uploadImage(a,url):
    headers = {"User-Agent": "Chrome",}
    file_name = a+".png"
    download_image(url, file_name, headers)
    return None
def loginChrome():
    start = gui.locateCenterOnScreen("loginChrome.PNG")
    if (start != None):
        gui.moveTo(start)
        gui.click()
        return None
    else:
        start = gui.locateCenterOnScreen("irshadLogin.PNG")
        if (start != None):
            gui.moveTo(start)
            gui.click()
            return None
        else:
            loginChrome()
def loginChrome1():
    time.sleep(1)
    gui.click(243, 452)
    return None

def domainUrl():
    start = gui.locateCenterOnScreen("domainUrl.PNG")
    if (start != None):
        gui.moveTo(start)
        gui.click()
        gui.typewrite("https://www.vinted.co.uk/items/new")
        gui.press('enter')
        time.sleep(1)
        return None
    else:
        domainUrl()
def domainUrl1():
    time.sleep(1)
    gui.click(285,55)
    gui.typewrite("https://www.vinted.co.uk/items/new")
    gui.press('enter')
    time.sleep(1)
    return None

def startChrome():
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
    #gui.mouseInfo()
    loginChrome1()
    return None
def postVinted(obj):
    uploadImage(obj["title"],obj["imageUrl"])
    gui.hotkey("ctrl", "t")
    time.sleep(1)
    domainUrl1()
    # gui.hotkey("del")
    time.sleep(1)
    #findImage(obj["title"],obj["imageUrl"])
    #findTitle(obj["title"])
    #findDescription(obj["description"])
    findCategories(obj["tooltip"])#'/Men/Shoes/Boots/Snow-boots'
    if (obj["unisex"] == True):
        findUnisex(obj["unisex"])
    if (obj["isbn"] != None):
        findIsbn(obj["isbn"])
    if (obj["brand"] != None):
        time.sleep(1)
        findBrand(obj["brand"])
    if(obj["size"]!=None):
        time.sleep(1)
        findSize(obj["size"])
    if (obj["conditionId"]!= None):
        findCondition(obj["conditionId"])
    if (obj["color"] != None):
        findColors(obj["color"])
    if (obj["material"] != None):
        findMaterial(obj["material"])
    if(obj["price"]!=None):
        time.sleep(1)
        findPrice(str(obj["price"]))
    findOutside()
    gui.hotkey("ctrl", "f")
    gui.typewrite("parcel size")
    findParcelSize(obj["parcelSize"])
    #findParcelWeight(obj["parcelWeight"])
    gui.hotkey("ctrl", "end")
    #findSave()
    time.sleep(1)
    #gui.hotkey("ctrl", "w")
    #gui.press('enter')
    return None
def job():
    response = requests.get(base+vintedPath,headers=Header)
    k = response.json()
    startChrome()
    for element in k["results"]:
        postVinted(element)
        print(element)

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


