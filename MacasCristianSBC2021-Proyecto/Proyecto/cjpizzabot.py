import telegram
from telegram.ext import *
import logging
import connectionOWL as con
import TeleToken as keys
import connectionDBP as dbp
from telegram import ReplyKeyboardMarkup
import spacytry as spy


# Set up the logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')

# Message error


def error(update, context):
    logging.error(f'Update {update} caused error {context.error}')

# COMMANDS

reply_keyboard = [
    ['/listNamedPizza', '/listIngredientscommands'],
    ['/listAllIngredients', '/listDrinks'],
]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

reply_keyboard2 = [
    ['/ingredientsAmericanaHot', '/ingredientsAmericana','/ingredientsHawaiana'],
    [ '/ingredientsMargherita', '/ingredientsSoho', '/back'],
]
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=True)

reply_keyboard3 = [
    ['/CheeseTopping', '/MeatTopping','/SeafoodTopping'],
    [ '/PepperTopping', '/VegetablesTopping', '/back'],
]
markup3 = ReplyKeyboardMarkup(reply_keyboard3, one_time_keyboard=True)

def start_command(update, context):  
        
    update.message.reply_text(
        'Bienvenido a CJ Pizza :',
        reply_markup=markup)
    
    update.message.reply_text('https://media.istockphoto.com/vectors/glowing-neon-effect-pizza-icon-outline-symbol-collection-vector-id1196247115?k=6&m=1196247115&s=170667a&w=0&h=a5GK1aOpZjx98V-JdxaPOemJEEtjUSzqJHR3No87jDI='),

    update.message.reply_text(
        "Lista de comandos :"
        "\n/listNamedPizza "
        "\n/listIngredientscommands"
        "\n/listAllIngredients"
        "\n/listDrinks")


def types_command_namedPizza(update, context):
    qres = con.get_response_pizzas()
    update.message.reply_text('Lista de pizzas : ', reply_markup=markup)
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        update.message.reply_text(name)

def types_command_ingredientsAmericana (update, context):    
    update.message.reply_text('Lista de ingredientes : ', reply_markup=markup2)
    qres = con.get_response_ingredients("AmericanaPizza")
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        ingredients = result['ingredients']['value']
        update.message.reply_text(ingredients)
        update.message.reply_text(dbp.obtener_ingredientes(ingredients))
        update.message.reply_text(dbp.obtener_photoIngredientes(ingredients))

def types_command_ingredientsAmericanaHot (update, context):    
    update.message.reply_text('Lista de ingredientes : ', reply_markup=markup2)
    qres = con.get_response_ingredients("AmericanaHotPizza")
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        ingredients = result['ingredients']['value']
        update.message.reply_text(ingredients)
        update.message.reply_text(dbp.obtener_ingredientes(ingredients))
        update.message.reply_text(dbp.obtener_photoIngredientes(ingredients))

def types_command_ingredientsHawaiana (update, context):    
    update.message.reply_text('Lista de ingredientes : ', reply_markup=markup2)
    qres = con.get_response_ingredients("HawaianaPizza")
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        ingredients = result['ingredients']['value']
        update.message.reply_text(ingredients)
        update.message.reply_text(dbp.obtener_ingredientes(ingredients))
        update.message.reply_text(dbp.obtener_photoIngredientes(ingredients))

def types_command_ingredientsMargherita (update, context):    
    update.message.reply_text('Lista de ingredientes : ', reply_markup=markup2)
    qres = con.get_response_ingredients("MargheritaPizza")
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        ingredients = result['ingredients']['value']
        update.message.reply_text(ingredients)
        update.message.reply_text(dbp.obtener_ingredientes(ingredients))
        update.message.reply_text(dbp.obtener_photoIngredientes(ingredients))

def types_command_ingredientsSoho (update, context):    
    update.message.reply_text('Lista de ingredientes : ', reply_markup=markup2)
    qres = con.get_response_ingredients("SohoPizza")
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        ingredients = result['ingredients']['value']        
        update.message.reply_text(ingredients)
        update.message.reply_text(dbp.obtener_ingredientes(ingredients))
        update.message.reply_text(dbp.obtener_photoIngredientes(ingredients))
        

def simple_spacy_try(update, context):
    mytxt = update.message.text  # obtener el texto que envio el usuario
    print(mytxt)
    doc = spy.spacy_info(mytxt)
    for w in doc:
        a = w.text, w.pos_
        update.message.reply_text(a)

def types_command_getCheeseTopping (update, context):    
    update.message.reply_text('Lista de ingredientes : ', reply_markup=markup3)
    qres = con.get_response_getToppings("CheeseTopping")
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        ingredients = result['ingredients']['value']        
        update.message.reply_text(ingredients)
        update.message.reply_text(dbp.obtener_ingredientes(ingredients))
        update.message.reply_text(dbp.obtener_photoIngredientes(ingredients))

def types_command_getMeatTopping (update, context):    
    update.message.reply_text('Lista de ingredientes : ', reply_markup=markup3)
    qres = con.get_response_getToppings("MeatTopping")
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        ingredients = result['ingredients']['value']        
        update.message.reply_text(ingredients)
        update.message.reply_text(dbp.obtener_ingredientes(ingredients))
        update.message.reply_text(dbp.obtener_photoIngredientes(ingredients))

def types_command_getSeafoodTopping (update, context):    
    update.message.reply_text('Lista de ingredientes : ', reply_markup=markup3)
    qres = con.get_response_getToppings("SeafoodTopping")
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        ingredients = result['ingredients']['value']        
        update.message.reply_text(ingredients)
        update.message.reply_text(dbp.obtener_ingredientes(ingredients))
        update.message.reply_text(dbp.obtener_photoIngredientes(ingredients))

def types_command_getPepperTopping (update, context):    
    update.message.reply_text('Lista de ingredientes : ', reply_markup=markup3)
    qres = con.get_response_getToppings("PepperTopping")
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        ingredients = result['ingredients']['value']        
        update.message.reply_text(ingredients)
        update.message.reply_text(dbp.obtener_ingredientes(ingredients))
        update.message.reply_text(dbp.obtener_photoIngredientes(ingredients))

def types_command_getVegetablesTopping (update, context):    
    update.message.reply_text('Lista de ingredientes : ', reply_markup=markup3)
    qres = con.get_response_getToppings("VegetablesTopping")
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        ingredients = result['ingredients']['value']        
        update.message.reply_text(ingredients)
        update.message.reply_text(dbp.obtener_ingredientes(ingredients))
        update.message.reply_text(dbp.obtener_photoIngredientes(ingredients))

def types_command_listIngredientscommands(update, context):
       update.message.reply_text(
        "Lista de Comandos de ingredientes :"
        "\n/ingredientsAmericanaHot"
        "\n/ingredientsAmericana"
        "\n/ingredientsHawaiana"
        "\n/ingredientsMargherita"
        "\n/ingredientsSoho", reply_markup=markup2)

def types_command_listAllIngredients(update, context):
    update.message.reply_text(
        "PizzaTopping :"
        "\n/CheeseTopping "
        "\n/MeatTopping"
        "\n/SeafoodTopping"
        "\n/PepperTopping"
        "\n/VegetablesTopping", reply_markup=markup3)

def types_command_listDrinks(update, context):
    qres = con.get_response_drinks()
    update.message.reply_text('Lista de bebidas : ', reply_markup=markup)
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        update.message.reply_text(name)
        update.message.reply_text(dbp.obtener_ingredientes(name))
        update.message.reply_text(dbp.obtener_photoIngredientes(name))

def command_back(update, context):
    update.message.reply_text(
        "Lista de comandos :"
        "\n/listNamedPizza "
        "\n/listIngredientscommands"
        "\n/listAllIngredients", reply_markup=markup)



if __name__ == '__main__':
    updater = Updater(token=keys.API_KEY, use_context=True)
    bot = telegram.Bot(token=keys.API_KEY)
    

    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('listNamedPizza', types_command_namedPizza))
    dp.add_handler(CommandHandler('listIngredientscommands', types_command_listIngredientscommands))
    dp.add_handler(CommandHandler('listAllIngredients', types_command_listAllIngredients))
    dp.add_handler(CommandHandler('listDrinks', types_command_listDrinks))
    dp.add_handler(CommandHandler('ingredientsAmericana', types_command_ingredientsAmericana))
    dp.add_handler(CommandHandler('ingredientsAmericanaHot', types_command_ingredientsAmericanaHot))
    dp.add_handler(CommandHandler('ingredientsHawaiana', types_command_ingredientsHawaiana))
    dp.add_handler(CommandHandler('ingredientsMargherita', types_command_ingredientsMargherita))
    dp.add_handler(CommandHandler('ingredientsSoho', types_command_ingredientsSoho))
    dp.add_handler(CommandHandler('CheeseTopping', types_command_getCheeseTopping))
    dp.add_handler(CommandHandler('MeatTopping', types_command_getMeatTopping))
    dp.add_handler(CommandHandler('SeafoodTopping', types_command_getSeafoodTopping))
    dp.add_handler(CommandHandler('PepperTopping', types_command_getPepperTopping))
    dp.add_handler(CommandHandler('VegetablesTopping', types_command_getVegetablesTopping))
    dp.add_handler(CommandHandler('back', command_back))
    dp.add_handler(MessageHandler(Filters.text, simple_spacy_try)) 

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()
