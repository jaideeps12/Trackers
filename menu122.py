def show_menu():
    running=True
    while running:
      print("Welcome to the Study tracker ")
      print("Menu")
      print("Please select an option from the below menu")
      print("1. Log a study session \n2. View study history\n3. Set study goals \n4. View progress report\n5. Exit")
      choice=int(input("Enter your choice :"))
      if choice==1:
         print("Log a study session")
      elif choice==2:
         print("View study history")
      elif choice==3:
         print("Set study goals")
      elif choice==4:
         print("View progress report")
      elif choice==5:
         print("Subject distribution chart")
      elif choice==6:
         print("Weekly study trend")
      else:
         print("Wrong choice")
show_menu()