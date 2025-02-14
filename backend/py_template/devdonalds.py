from dataclasses import dataclass
from typing import List, Dict, Union
from flask import Flask, request, jsonify
import re
import json
import dacite

# ==== Type Definitions, feel free to add or modify ===========================
@dataclass
class CookbookEntry:
	name: str

@dataclass
class RequiredItem():
	name: str
	quantity: int

@dataclass
class Recipe(CookbookEntry):
	requiredItems: List[RequiredItem]

@dataclass
class Ingredient(CookbookEntry):
	cookTime: int

@dataclass
class RequiredIngredient(RequiredItem):
	cookTime: int

@dataclass
class Response:
	name: str
	cookTime: int
	ingredients: List[RequiredItem]

# =============================================================================
# ==== HTTP Endpoint Stubs ====================================================
# =============================================================================
app = Flask(__name__)

# Store your recipes here!
cookbook = {key: value for key, value in []}

# Task 1 helper (don't touch)
@app.route("/parse", methods=['POST'])
def parse():
	data = request.get_json()
	recipe_name = data.get('input', '')
	parsed_name = parse_handwriting(recipe_name)
	if parsed_name is None:
		return 'Invalid recipe name', 400
	return jsonify({'msg': parsed_name}), 200

# [TASK 1] ====================================================================
# Takes in a recipeName and returns it in a form that 
def parse_handwriting(recipeName: str) -> Union[str | None]:
	# Replace - and _ with white space
	recipeName = recipeName.replace('_', ' ')
	recipeName = recipeName.replace('-', ' ')

	# remove non character or non whitespace
	recipeName = ''.join([c for c in recipeName if (c.isalpha() or c == ' ')])


	# Remove more than one white space
	tokens = recipeName.split()
	recipeName = ' '.join(tokens)

	# Capitalise first char
	recipeName = recipeName.title()

	if not len(recipeName) > 0:
		return None

	return recipeName


# [TASK 2] ====================================================================
# Endpoint that adds a CookbookEntry to your magical cookbook
@app.route('/entry', methods=['POST'])
def create_entry():
	data = request.get_json()
	name = data.get('name')
	type = data.get('type')

	if name is None:
		return 'No name given', 400
	if type is None:
		return 'No type given', 400
	
	# Check name does not exist
	if name in cookbook:
		return 'Entry already exists', 400
	# match on entry type
	match type:
		case "recipe":
			# try deserialise data
			try:	
				recp = dacite.from_dict(Recipe, data)
			except dacite.exceptions.DaciteError as e:
				
				return jsonify({"error": str(e)}), 400  # Return error if deserialisation fails
			
			# Check Recipe requiredItems can only have one element per name.
			item_names = [item.name for item in recp.requiredItems]

			if len(item_names) != len(set(item_names)):
				return 'Repeated Items in requiredItems of recepie', 400

			cookbook[name] = recp
			
		case "ingredient":
			# Get cook time and run checks
			cook_time = data.get('cookTime')
			if cook_time is None:
				return 'No cooktime given', 400
			elif not (isinstance(cook_time, int)) or cook_time < 0:
				return 'Negative or non integer cooktime given', 400
			
			try:	
				ingredients = dacite.from_dict(Ingredient, data)
			except dacite.exceptions.DaciteError as e:
				return jsonify({"error": str(e)}), 400  # Return error if deserialisation fails
			
			cookbook[name] = ingredients
			
		case _:
			return 'Invalid type given', 400
		
	

	return '', 200


# [TASK 3] ====================================================================
# Endpoint that returns a summary of a recipe that corresponds to a query name
@app.route('/summary', methods=['GET'])
def summary():
	name = request.args.get('name')
	if name == None:
		return 'missing query param', 400
	
	try:
		raw_recipe = cookbook[name]
	except:
		return 'No such Recipe found', 400
	
	if isinstance(raw_recipe, Ingredient):
		return 'Not a Recipe', 400

	# Finalised flattened ingredient List
	try:
		ingredient_list = sum([unpack_recipe_items(i) for i in raw_recipe.requiredItems], [])
	except Exception as e:
		return str(e), 400

	# Accumulate cookTime and ingredients
	cookTime = 0
	ingredients_dict = {key: value for key, value in []}

	for i in ingredient_list:
		cookTime += i.quantity * i.cookTime

		if i.name in ingredients_dict:
			ingredients_dict[i.name] += i.quantity
		else:
			ingredients_dict[i.name] = i.quantity

	# Turn dictonary into list
	ingredients = [ RequiredItem(k,r) for k,r in ingredients_dict.items()]

	return jsonify(Response(name, cookTime, ingredients)), 200


# Take in an RequiredItem, flatten it, meaning that if the Item is a Recipe it will return all Ingredient it contains
def unpack_recipe_items(item):
	try:
		raw_recipe = cookbook[item.name]
	except:
		raise Exception(f"Cannot find recipe item with name {item.name}.")
	
	if isinstance(raw_recipe, Recipe):
		# Collect items needed, if Item is a recipe, unpack using recursions
		return sum([unpack_recipe_items(i) for i in raw_recipe.requiredItems], [])
	elif isinstance(raw_recipe, Ingredient):
		# We have found a base ingredient, returnn
		return [RequiredIngredient(item.name, item.quantity, raw_recipe.cookTime)]

# =============================================================================
# ==== DO NOT TOUCH ===========================================================
# =============================================================================

if __name__ == '__main__':
	app.run(debug=True, port=8080)
