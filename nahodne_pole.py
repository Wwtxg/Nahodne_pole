def calculate_sum(numbers): #funkce
   """
   Funkce, která přijímá pole čísel a vrací jejich součet.
   """
   total = 0
   for number in numbers:  # Cyklus s pevným počtem opakování
       total += number
   return total

def main():
   numbers = [] #pole
   # Vstup s přetypováním
   num_elements = int(input("Kolik čísel chcete zadat? ")) #Počet čísel
   # Cyklus s pevným počtem opakování
   for i in range(num_elements):
       num = float(input(f"Zadejte číslo {i+1}: ")) 
       numbers.append(num)  # Přidání do pole
   # Výstup a volání funkce s parametrem
   total_sum = calculate_sum(numbers)
   print(f"Součet zadaných čísel je: {total_sum}") #Součet
   # Cyklus s podmínkou
   while True:
       choice = input("Chcete odebrat číslo z pole? (ano/ne) ").strip().lower() #Možnost odebrat číslo z pole
       if choice == 'ne':
           break #Ukonči algoritmus
       elif choice == 'ano':
           if not numbers:  # Kontrola, zda pole není prázdné
               print("Pole je prázdné, nelze odebrat žádné číslo.")
               continue
           # Odebrání posledního prvku z pole
           removed_number = numbers.pop()
           print(f"Odebrané číslo: {removed_number}") #Ukaže odebrané číslo
       else:
           print("Neplatná volba, zkuste to znovu.")
   # Práce s podmínkou a logickými funkcemi
   if numbers and (total_sum > 0 or len(numbers) > 1) and not (total_sum < 0):
       print("Pole obsahuje kladný součet nebo více než jedno číslo a součet není záporný.")
   else:
       print("Pole nevyhovuje podmínkám.")

if __name__ == "__main__":
   main()