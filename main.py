#import my functions and set up my variables and lists that i will utalise later
import time
items = 1
total_money = 0 
order = []
comboorcombno = []
superitemcost = []

#menu for user to see what they want to order
print("Welcome to the South High Deli, what would you like to order?")
print(" ")
print("Combos include a drink and fries")
print("Bacon and Eggs (Solo $5 / Combo $10 )")
print("Tuna Melt (Solo $3 / Combo $8 )")
print("Cold Cut Sub (Solo $5 / Combo $10 )")
print("Meat Lovers Pizza (Solo $13 / Combo $18 )")
print("Loaded Ham and Cheese (Solo $4 / Combo $9 )")
print("Chicken Sandwich (Solo $4 / Combo $9 )")
print("Spicy Jalopeno Chicken Sandwich (Solo $5 / Combo $10 )")
print(" ")

#gives the user a little time to go over the menu before ordering no rush
print("Alright ill give you a second to decide what you'd like to order")
time.sleep(5)
print(" ")
print("Ok looks like you're ready to order tell me what you would like type 'done' when you're done with your order")
food = input(": ")
order.append(food)

#loop for the user to order food and stops when the user says to stop
while food != 'done':
  print(" ")
  print("Alright what else")
  food = input(": ")

#if statement to put the users input into a list for the recipt
  if food != 'done' and food == 'Bacon and Eggs' or food == 'Tuna Melt' or food == 'Cold Cut Sub' or food == 'Meat Lovers Pizza' or food == 'Loaded Ham and Cheese' or food == 'Chicken Sandwich' or food == 'Spicy Jalopeno Chicken Sandwich': 
    order.append(food)

#if statement that counts up every time an item is ordered for recipt
  if food != 'done' and food == 'Bacon and Eggs' or food == 'Tuna Melt' or food == 'Cold Cut Sub' or food == 'Meat Lovers Pizza' or food == 'Loaded Ham and Cheese' or food == 'Chicken Sandwich' or food == 'Spicy Jalopeno Chicken Sandwich':
    items = items + 1

#input error that comes up whenever the user writes a response that isnt recognised
  while food != 'Bacon and Eggs' and  food != 'Tuna Melt' and food != 'Cold Cut Sub' and food != 'Meat Lovers Pizza' and food != 'Loaded Ham and Cheese' and food != 'Chicken Sandwich' and food != 'Spicy Jalopeno Chicken Sandwich' and food != 'done':
      print("Im sorry i didnt get that can you repeat that?")
      food = input(": ")

#if statement that counts up every time an item is ordered for recipt is needed again since this is for the input after the user writes something that isnt recognised
      if food != 'done' and food == 'Bacon and Eggs' or food == 'Tuna Melt' or food == 'Cold Cut Sub' or food == 'Meat Lovers Pizza' or food == 'Loaded Ham and Cheese' or food == 'Chicken Sandwich' or food == 'Spicy Jalopeno Chicken Sandwich':
        items = items + 1

#if statement to put the users input into a list for the recipt is needed again since this is for the input after the user writes something that isnt recognised
      if food != 'done' and food == 'Bacon and Eggs' or food == 'Tuna Melt' or food == 'Cold Cut Sub' or food == 'Meat Lovers Pizza' or food == 'Loaded Ham and Cheese' or food == 'Chicken Sandwich' or food == 'Spicy Jalopeno Chicken Sandwich': 
        order.append(food)

#function for when the recipt is ready for the user
def recipt():

#input for the user to tip the waiter whatever percenatege they feel like giving
  print(" ")
  tip_cent = int(input("What percentage do you want to tip your waiter?: % "))

#math to calculate taxes and tip percentage
  int_cent = tip_cent / 100
  yucky_tax = total_money * 0.10
  tip_cost = total_money * int_cent

#without floating the value there could be decimals that go past that 100ths place which i thought didnt look nice so i looked up online how i can just limit it to 2 decimal places
  floated_tax = "{:.2f}".format(yucky_tax)
  floated_tip = "{:.2f}".format(tip_cost)

#displayes text that says printing recipt and the program waits for a little bit to make the user feel like if a recipt is actually being generated like in a resturant
  print(" ")
  print('Printing recipt please wait...')
  time.sleep(5)
  print(" ")
  print("Here is your Recipt!")

#math to calculate the total for the bill
  totesywotesy = total_money + tip_cost + yucky_tax
  floated_totey = "{:.2f}".format(totesywotesy)

#for i in range that lists every item orderd and its price as well as if it was ordered as a combo or not
  for x in range(len(order)):
    print(order[x], "$",superitemcost[x])
    print("Combo?:", comboorcombno[x],)
    print(" ")

#prints all the information for the recipt like the ammount of food items orderd price before tax how much the tax is how much the user payed in tips and lastly the final total all added up
  print('Total Items Ordered', items)
  print("Subtotal: $",total_money)
  print("Taxes: $", floated_tax)
  print("Tip: $", floated_tip)
  print("Final Total: $",floated_totey)
  print(" ")
  print("Goodbye thank you for eating at south high deli!")

#for i in range that lists every single item that the user has ordered asking if they want to order the item as a combo or not and if they say yes then the price of the item is put into a list so then in the recipt it can display the individual cost of every item
for item in order:
  print(" ")
  if item == 'Bacon and Eggs':
    print("Would you like your Bacon and Eggs as a combo?")
    combno = input(": ")
    if combno == 'yes':
      total_money = total_money + 10
      superitemcost.append(10)
    else:
      total_money = total_money + 5
      superitemcost.append(5)
    comboorcombno.append(combno)
  
  if item == 'Tuna Melt':
    print("Would you like your Tuna Melt as a combo?")
    combno = input(": ")
    if combno == 'yes':
      total_money = total_money + 8
      superitemcost.append(8)
    else:
      total_money = total_money + 3
      superitemcost.append(3)
    comboorcombno.append(combno)
  
  if item == 'Cold Cut Sub':
    print("Would you like your Cold Cut Sub as a combo?")
    combno = input(": ")
    if combno == 'yes':
      total_money = total_money + 10
      superitemcost.append(10)
    else:
      total_money = total_money + 5
      superitemcost.append(5)
    comboorcombno.append(combno)
  
  if item == 'Meat Lovers Pizza':
    print("Would you like your Meat Lovers Pizza as a combo?")
    combno = input(": ")
    if combno == 'yes':
      total_money = total_money + 18
      superitemcost.append(18)
    else:
      total_money = total_money + 13
      superitemcost.append(13)
    comboorcombno.append(combno)
  
  if item == 'Loaded Ham and Cheese':
    print("Would you like your Loaded Ham and Cheese as a combo?")
    combno = input(": ")
    if combno == 'yes':
      total_money = total_money + 9
      superitemcost.append(9)
    else:
      total_money = total_money + 4
      superitemcost.append(4)
    comboorcombno.append(combno)
  
  if item == 'Chicken Sandwich':
    print("Would you like your Chicken Sandwich as a combo?")
    combno = input(": ")
    if combno == 'yes':
      total_money = total_money + 9
      superitemcost.append(9)
    else:
      total_money = total_money + 4
      superitemcost.append(4)
    comboorcombno.append(combno)
  
  if item == 'Spicy Jalopeno Chicken Sandwich':
    print("Would you like your Spicy Jalopeno Chicken Sandwich as a combo?")
    combno = input(": ")
    if combno == 'yes':
      total_money = total_money + 10
      superitemcost.append(10)
    else:
      total_money = total_money + 5
      superitemcost.append(5)
    comboorcombno.append(combno)

#lastly the function so then after the user is done ordering they get their recipt
recipt()