#drinks.py
drink_list = [{
		'name': 'Vesper',
		'ingredients': {
			'gin': 60,
			'vodka': 15.0,
			'vermouth': 7.5
		},
		'prep': 'Shake and strain into a chilled cocktail glass.'
	},
	{
		'name': 'Bacardi',
		'ingredients': {
			'whiteRum': 45.0,
			'lij': 20,
			'grenadine': 10
		},
		'prep': 'Shake with ice cubes. Strain into chilled cocktail glass.'
	},
	{
		'name': 'Negroni',
		'ingredients': {
			'gin': 30,
			'campari': 30,
			'vermouth': 30
		},
		'prep': 'Build into old-fashioned glass filled with ice. Stir gently.'
	},
	{
		'name': 'Rose',
		'ingredients': {
			'cherryBrandy': 20,
			'vermouth': 40
		},
		'prep': 'Stir all ingredients with ice and strain into a cocktail glass.',
		'specials': ['3 dashes Strawberry syrup']
	},
	{
		'name': 'Old Fashioned',
		'ingredients': {
			'whiskey': 45.0
		},
		'prep': 'Place sugar cube in old-fashioned glass and saturate with bitters,add a dash of plain water. Muddle until dissolve. Fill the glass with ice cubes and add whisky.',
		'specials': ['2 dashes Angostura Bitters',
'1 sugar cube']
	},
	{
		'name': 'Tuxedo',
		'ingredients': {
			'gin': 30,
			'vermouth': 30
		},
		'prep': 'Stir all ingredients with ice and strain into cocktail glass.',
		'specials': ['1/2 bar spoon Maraschino',
'1/4 bar spoon Absinthe',
'3 dashes Orange Bitters']
	},
	{
		'name': 'Mojito',
		'ingredients': {
			'whiteRum': 40,
			'lij': 30
		},
		'prep': 'Muddle mint springs with sugar and lime juice. Add splash of soda water and fill glass with cracked ice. Pour rum and top with soda water. Serve with straw.',
		'specials': ['2 teaspoons white sugar',
'Soda water']
	},
	{
		'name': "Horse's Neck",
		'ingredients': {
			'brandy': 40,
			'gingerAle': 120
		},
		'prep': 'Build into highball glass with ice cubes. Stir gently. If required, add dashes of Angostura bitters.',
		'specials': ['Dash of Angostura bitters (optional)']
	},
	{
		'name': "Planter's Punch",
		'ingredients': {
			'darkRum': 45.0,
			'oj': 35.0,
			'pj': 35.0,
			'lej': 20,
			'grenadine': 10
		},
		'prep': 'Pour all ingredients, except the bitters, into shaker filled with ice. Shake. Pour into large glass, filled with ice. Add Angostura bitters, on top.',
		'specials': ['3 to 4 dashes Angostura bitters']
	},
	{
		'name': 'Sea Breeze',
		'ingredients': {
			'vodka': 40,
			'cj': 120,
			'gj': 30
		},
		'prep': 'Build all ingredients in a rock glass filled with ice.'
	},
	{
		'name': 'Pisco Sour',
		'ingredients': {
			'brandy': 45.0,
			'lej': 30,
			'grenadine': 20
		},
		'prep': 'Shake and strain into a chilled champagne flute. Dash some Angostura bitters on top.',
		'specials': ['1 raw egg white (small egg)']
	},
	{
		'name': 'Long Island Iced Tea',
		'ingredients': {
			'tequila': 15.0,
			'vodka': 15.0,
			'whiteRum': 15.0,
			'tripSec': 15.0,
			'gin': 15.0,
			'lej': 25.0,
			'grenadine': 30.0
		},
		'prep': 'Add all ingredients into highball glass filled with ice. Stir gently. Serve with straw.',
		'specials': ['1 dash of Cola']
	},
	{
		'name': 'Clover Club',
		'ingredients': {
			'gin': 45.0,
			'grenadine': 15.0,
			'lej': 15.0
		},
		'prep': 'Shake with ice cubes. Strain into cocktail glass.'
	},
	{
		'name': 'Angel Face',
		'ingredients': {
			'gin': 30,
			'apricotBrandy': 30,
			'appleBrandy': 30
		},
		'prep': 'Shake with ice cubes. Strain into a cocktail glass.'
	},
	{
		'name': 'Mimosa',
		'ingredients': {
			'champagne': 75.0,
			'oj': 75.0
		},
		'prep': 'Pour orange juice into flute and gently pour Champagne. Stir gently. Note: a Buck\'s Fizz and a Mimosa are the same drink.'
	},
	{
		'name': 'Whiskey Sour',
		'ingredients': {
			'whiskey': 45.0,
			'lej': 30.0,
			'grenadine': 15.0
		},
		'prep': 'Dash egg white (Optional: if used shake little harder to foam up the egg white). Pour all ingredients into cocktail shaker filled with ice. Shake. Strain into cocktail glass. If served \'On the rocks\',strain ingredients into old-fashioned glass filled with ice.'
	},
	{
		'name': 'Screwdriver',
		'ingredients': {
			'vodka': 50,
			'oj': 100
		},
		'prep': 'Build into a highball glass filled with ice. Stir gently.'
	},
	{
		'name': 'Cuba Libre',
		'ingredients': {
			'whiteRum': 50,
			'cola': 120,
			'lij': 10
		},
		'prep': 'Build all ingredients in a highball glass filled with ice.'
	},
	{
		'name': 'Manhattan',
		'ingredients': {
			'whiskey': 50,
			'vermouth': 20
		},
		'prep': 'Stir in mixing glass with ice cubes. Strain into chilled cocktail glass.',
		'specials': ['1 dash Angostura Bitters']
	},
	{
		'name': 'Porto Flip',
		'ingredients': {
			'brandy': 15.0,
			'port': 45.0,
			'eggYolk': 10
		},
		'prep': 'Shake with ice cubes. Strain into cocktail glass. Sprinkle with fresh ground nutmeg.'
	},
	{
		'name': 'Gin Fizz',
		'ingredients': {
			'gin': 45.0,
			'lej': 30,
			'grenadine': 10,
			'soda': 80
		},
		'prep': 'Shake all ingredients with ice cubes, except soda water. Pour into tumbler. Top with soda water.'
	},
	{
		'name': 'Espresso Martini',
		'ingredients': {
			'vodka': 50,
			'coffeeLiqueur': 10
		},
		'prep': 'Shake and strain into a chilled cocktail glass.',
		'specials': ['Sugar syrup (according to individual preference of sweetness)',
'1 short strong Espresso']
	},
	{
		'name': 'Margarita',
		'ingredients': {
			'tequila': 35.0,
			'tripSec': 20,
			'lij': 15.0
		},
		'prep': 'Shake with ice cubes. Strain into cocktail glass rimmed with salt (note:Fruit Margarita - blend selected fruit with the above recipe).'
	},
	{
		'name': 'French 75',
		'ingredients': {
			'gin': 30,
			'lej': 15.0,
			'champagne': 60
		},
		'prep': 'Shake with ice cubes, except for champagne. Strain into a champagne flute. Top up with champagne. Stir gently.',
		'specials': ['2 dashes Sugar syrup']
	},
	{
		'name': 'Yellow Bird',
		'ingredients': {
			'whiteRum': 30,
			'galliano': 15.0,
			'tripSec': 15.0,
			'lij': 15.0
		},
		'prep': 'Shake and strain into a chilled cocktail glass.'
	},
	{
		'name': 'Pina Colada',
		'ingredients': {
			'whiteRum': 30,
			'pj': 90,
			'coconutMilk': 30
		},
		'prep': 'Blend all the ingredients with ice in a electric blender, pour into a large goblet or Hurricane glass and serve with straws.'
	},
	{
		'name': 'Aviation',
		'ingredients': {
			'gin': 45.0,
			'cherryLiqueur': 15.0,
			'lej': 15.0
		},
		'prep': 'Shake and strain into a chilled cocktail glass.'
	},
	{
		'name': 'Bellini',
		'ingredients': {
			'prosecco': 100,
			'peachPuree': 50
		},
		'prep': 'Pour peach puree into chilled glass and add sparkling wine. Stir gently. Variations: Puccini (fresh mandarin juice), Rossini (fresh strawberry puree), Tintoretto (fresh pomegranate juice)'
	},
	{
		'name': 'Grasshopper',
		'ingredients': {
			'cremeCacao': 30,
			'cream': 30
		},
		'prep': 'Shake with ice cubes. Strain into chilled cocktail glass.'
	},
	{
		'name': 'Tequila Sunrise',
		'ingredients': {
			'tequila': 45.0,
			'oj': 90,
			'grenadine': 15.0
		},
		'prep': 'Build tequila and orange juice into highball with ice cubes. Add a splash of grenadine to create sunrise effect. Do not stir.'
	},
	{
		'name': 'Daiquiri',
		'ingredients': {
			'whiteRum': 45.0,
			'lij': 25.0,
			'grenadine': 15.0
		},
		'prep': 'Shake and strain into a cocktail glass.'
	},
	{
		'name': 'Rusty Nail',
		'ingredients': {
			'whiskey': 25.0
		},
		'prep': 'Build into old-fashioned glass filled with ice. Stir gently.'
	},
	{
		'name': 'B52',
		'ingredients': {
			'coffeeLiqueur': 20,
			'baileys': 20,
			'tripSec': 20
		},
		'prep': 'Layer ingredients one at a time starting with Kahlua, followed by Baileys Irish Cream and top with Grand Marnier. Flame the Grand Marnier, serve while the flame is still on, accompanied with a straw on side plate.'
	},
	{
		'name': 'Stinger',
		'ingredients': {
			'brandy': 50,
			'cremeCacao': 20
		},
		'prep': 'Stir in mixing glass with ice cubes. Strain into a cocktail glass.'
	},
	{
		'name': 'Golden Dream',
		'ingredients': {
			'galliano': 20,
			'tripSec': 20,
			'oj': 20,
			'cream': 10
		},
		'prep': 'Shake with ice cubes. Strain into chilled cocktail glass.'
	},
	{
		'name': 'God Mother',
		'ingredients': {
			'vodka': 35.0,
			'amaretto': 35.0
		},
		'prep': 'Build into old fashioned glass filled with ice cubes. Stir gently.'
	},
	{
		'name': 'Spritz Veneziano',
		'ingredients': {
			'prosecco': 60,
			'aperol': 40
		},
		'prep': 'Build into an old-fashioned glass filled with ice. Top with a splash of soda water.',
		'specials': ['Splash of Soda water']
	},
	{
		'name': 'Bramble',
		'ingredients': {
			'gin': 40,
			'lej': 15.0,
			'grenadine': 10,
			'blackberryLiqueur': 15.0
		},
		'prep': 'Build over crushed ice, in a rock glass. Stir, then pour the blackberry liqueur over the top of the drink in a circular fashion.'
	},
	{
		'name': 'Alexander',
		'ingredients': {
			'brandy': 30,
			'cremeCacao': 30,
			'cream': 30
		},
		'prep': 'Shake and strain into a chilled cocktail glass. Sprinkle with fresh ground nutmeg.'
	},
	{
		'name': 'Lemon Drop Martini',
		'ingredients': {
			'vodka': 25.0,
			'tripSec': 20,
			'lej': 15.0
		},
		'prep': 'Shake and strain into a chilled cocktail glass rimmed with sugar.'
	},
	{
		'name': 'French Martini',
		'ingredients': {
			'vodka': 45.0,
			'raspberryLiqueur': 15.0,
			'pj': 15.0
		},
		'prep': 'Stir in mixing glass with ice cubes. Strain into chilled cocktail glass. Squeeze oil from lemon peel onto the drink.'
	},
	{
		'name': 'Black Russian',
		'ingredients': {
			'vodka': 50,
			'coffeeLiqueur': 20
		},
		'prep': 'Build into old fashioned glass filled with ice cubes. Stir gently. Note: for White Russian, float fresh cream on the top and stir gently.'
	},
	{
		'name': 'Bloody Mary',
		'ingredients': {
			'vodka': 45.0,
			'tj': 90,
			'lej': 15.0
		},
		'prep': 'Stir gently, pour all ingredients into highball glass.',
		'specials': ['2 to 3 dashes of Worcestershire Sauce','Tabasco','Celery salt','Pepper']
	},
	{
		'name': 'Mai-tai',
		'ingredients': {
			'whiteRum': 40,
			'darkRum': 20,
			'tripSec': 15.0,
			'grenadine': 15.0,
			'lij': 10
		},
		'prep': 'Shake and strain into highball glass. Serve with straw.'
	}, {

		"name": "Madras",
		"ingredients": {

			"vodka": 45,
			"cj": 90,
			"oj": 30
		}
	}, {

		"name": "Lemon Drop",
		"ingredients": {

			"vodka": 40,
			"lej": 40,
			"grenadine": 15
		}
	}, {

		"name": "Cape Cod",
		"ingredients": {

			"vodka": 35,
			"cj": 135
		}
	}, {

		"name": "Bourbon Squash",
		"ingredients": {

			"whisky": 45,
			"oj": 50,
			"lej": 30,
			"grenadine": 20
		}
	}]

drink_options = [
	{
		"name": "Gin",
		"value": "gin"
	},
	{
		"name": "White Rum",
		"value": "whiteRum"
	},
	{
		"name": "Dark Rum",
		"value": "darkRum"
	},
	{
		"name": "Coconut Rum",
		"value": "coconutRum"
	},
	{
		"name": "Vodka",
		"value": "vodka"
	},
	{
		"name": "Tequila",
		"value": "tequila"
	},
	{
		"name": "Tonic Water",
		"value": "tonic"
	},
	{
		"name": "Coke",
		"value": "coke"
	},
	{
		"name": "Orange Juice",
		"value": "oj"
	},
	{
		"name": "Margarita Mix",
		"value": "mmix"
	},
	{
		"name": "Cranberry Juice",
		"value": "cj"
	},
	{
		"name": "Pineapple Juice",
		"value": "pj"
	},
	{
		"name": "Apple Juice",
		"value": "aj"
	},
	{
		"name": "Grapefruit Juice",
		"value": "gj"
	},
	{
		"name": "Tomato Juice",
		"value": "tj"
	},
	{
		"name": "Lime Juice",
		"value": "lij"
	},
	{
		"name": "Lemon Juice",
		"value": "lej"
	},
	{
		"name": "Whiskey",
		"value": "whiskey"
	},
	{
		"name": "Triple Sec",
		"value": "tripSec"
	},
	{
		"name": "Grenadine",
		"value": "grenadine"
	},
	{
		"name": "Vermouth",
		"value": "vermouth"
	},
	{
		"name": "Soda",
		"value": "soda"
	},
	{
		"name": "Peach Schnapps",
		"value": "peachSchnapps"
	},
	{
		"name": "Midori",
		"value": "midori"
	},
	{
		"name": "Presecco",
		"value": "prosecco"
	},
	{
		"name": "Cherry Brandy",
		"value": "cherryBrandy"
	},
	{
		"name": "Apple Brandy",
		"value": "appleBrandy"
	},
	{
		"name": "Apricot Brandy",
		"value": "apricotBrandy"
	},
	{
		"name": "Brandy (generic)",
		"value": "brandy"
	},
	{
		"name": "Champagne",
		"value": "champagne"
	},
	{
		"name": "Cola",
		"value": "cola"
	},
	{
		"name": "Port",
		"value": "port"
	},
	{
		"name": "Coconut Milk",
		"value": "coconutMilk"
	},
	{
		"name": "Creme de Cacao",
		"value": "cremeCacao"
	},
	{
		"name": "Grenadine",
		"value": "grenadine"
	},
]


# Check for ingredients that we don 't have a record for
if __name__ == "__main__":
	found = []
	drinks = [x["value"] for x in drink_options]
	for D in drink_list:
		for I in D["ingredients"]:
			if I not in drinks and I not in found:
				found.append(I)
	print(I)