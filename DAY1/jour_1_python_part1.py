###################################################################################################
###				ADVENT 			OF			 CODE :			 DAY 1 			PART 1				###
###################################################################################################

# Objectif du Jour 1  :
# Vos valeurs données par le site est un fichier texte de 1000 lignes contenant des mots fait de lettres et de chiffes. Votre objectif est de
# créer une fonction qui sélectionne tous les chiffres du mot, assemble le premier et le dernier de chaque mot pour former un nouveau nombre, puis
# renvoir la somme de tous les nombres.

# Bonne chance ! 

# Evidemment, si votre objectif est de vous améliorer, pensez a regarder mon programme de manière inspirative, sans le copier. Essayez de le faire à votre manière !


with open("input_day_1.txt", "r") as f: # Permet d'importer le fichier .txt contenant votre input du jour
    user_input = [line for line in f.readlines()] # Contient dans la variable 'user_input' le contenu du fichier entier


def trebuchet(words_list):
    """Assemble le premier et le dernier chiffre d'un mot afin de constituer un nombre, puis fait la somme de tous les nouveaux nombres.

    Entrées:
        words_list (str): La liste des mots fournis pas Advent Of Code
    """

  # Crée un tableau qui servira à stocker les nouveaux nombres pour en faire la somme ensuite
    list_values = []
  
    for selected_word in words_list: # A chaque passage de boucle, sélectionne un mot du fichier et le stocke dans la variable selected_word
        
        # print(selected_word) -- Ce genre de lignes vous permet si vous souhaitez d'observer
		#							si votre programme fonctionne bien
         
        # Crée un tableau pou rstocker les chiffres du mot dans l'ordre ou ils apparaissent.
		# Le tableau sera réinitialisé a chaque changement de mot
        list_numbers = []

        for caracter in selected_word: # Selectionne un caractère du mot un par un
          try : 
            # Change le caractère en integer ( etait un chiffre mais en str )
            int(caracter)
            # Ajoute le caractère au tableau 'list_numbers'
            list_numbers.append(caracter)

          # Si le programme renvoie une ValueError, c'est que le caractère est une lettre et non un chiffre on le passe donc.
          except ValueError: 
            pass # Passe la ligne de code ( remplit le vide d'actions )
            
        # print(list_numbers) 

      # Si le mot contient seulement un seul nombre
        if len(list_numbers) == 1: 

          # Ajout le nombre deux fois au tableau
          number_1 = str(list_numbers[0]) # Change le chiffre d'un int à un str pour pouvoir le concaténer avec l'autre
          number_2 = str(list_numbers[0])
          
          # print("Premier nombre = " + number_1) 
          # print("Dernier nombre = " + number_2) 

          value = number_1 + number_2 # Concatène les deux chiffres pour créer le nouveau nombre
          # print("Ajoute " + value + " au tableau) 


          list_values.append(int(value)) # Ajoute le nouveau nombre au tableau 'list_numbers'

        elif len(list_numbers) > 1: # S'il y à plus d'un chiffre dans le mot
          
          number_1 = str(list_numbers[0]) # Change le premier chiffre d'un int à un str pour pouvoir le concaténer avec l'autre
          number_2 = str(list_numbers[len(list_numbers)-1]) # Change le dernier chiffre d'un int à un str pour pouvoir le concaténer avec l'autre
          # print("Premier nombre = " + number_1) 
          # print("Dernier nombre = " + number_2)    
          
          value = number_1 + number_2 # Concatène les deux chiffres pour créer le nouveau nombre
          #print("Adding " + value)

          list_values.append(int(value)) # Ajoute le nouveau nombre au tableau 'list_numbers'
    
    return(sum(list_values)) # Renvoie la somme de toutes les valeurs du tableau



print(trebuchet(user_input))
