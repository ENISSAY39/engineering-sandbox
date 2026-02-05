# Voici le code à réaliser pour le projet de suivi des dépenses personnelles en Python. Ce code permet de suivre les dépenses, de les catégoriser.
list_expenses_Food =[]
list_expenses_Divertissement =[]
list_expenses_Taxes =[]
user_choice_expenses = str(input("Dans quelle catégorie souhaitez-vous enregistrer votre dépense ? (F : Food | D : Divertissement | T : Taxes) : "))

if user_choice_expenses == "F":
    user_price_F = int(input("Combien d'€ est votre dépense ? :"))
    list_expenses_Food.append(user_price_F)
    print("Voici à présent vos dépenses actuelles: \n","Voici les dépenses de nourriture: ", list_expenses_Food, ".\n","Dépenses Divertissement :",list_expenses_Divertissement, ".\n", "Dépenses Taxes :", list_expenses_Taxes, ".\n")

elif user_choice_expenses == "D":
    user_price_D = int(input("Combien d'€ est votre dépense ? :"))
    list_expenses_Divertissement.append(user_price_D)
    print("Voici à présent vos dépenses actuelles: \n","Voici les dépenses de nourriture: ", list_expenses_Food, ".\n","Dépenses Divertissement :",list_expenses_Divertissement, ".\n", "Dépenses Taxes :", list_expenses_Taxes, ".\n")

elif user_choice_expenses == "T":
    user_price_T = int(input("Combien d'€ est votre dépense ? :"))
    list_expenses_Taxes.append(user_price_T)
    print("Voici à présent vos dépenses actuelles: \n","Voici les dépenses de nourriture: ", list_expenses_Food, ".\n","Dépenses Divertissement :",list_expenses_Divertissement, ".\n", "Dépenses Taxes :", list_expenses_Taxes, ".\n")

else:
    print("Error")