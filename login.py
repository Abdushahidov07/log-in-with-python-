lict = []
task = []
cnt = 1
cnt1 = 1

while True:
    n = int(input("1. Register \n2. Log in \n3. Delete user \n4. Exit \n\nSelect an option: "))
    if n == 1:
        reg = {
            "id": cnt,
            "name": input("Name: "),
            "surname": input("Surname: "),
            "username": input("Username: "),
            "age": input("Write your age: "),
            "pass": input("Password: "),
            "tasks": []
        }
        lict.append(reg)
        print('Your profile: \n', reg['name'], "\n", reg['surname'], "\n", reg['username'], "\n", reg['age'], '\n',"Your id: ", cnt)
        cnt += 1
    elif n == 2:
        id = int(input("id="))
        for reg in lict:
            if id == reg['id']:
                ni = {
                    "username": input("Username: "),
                    "pass": input("Password: ")
                }
                if ni['pass'] == reg['pass'] and ni['username'] == reg['username']:
                    print('Your profile: \n', reg['name'], "\n", reg['surname'], "\n", reg['username'], "\n", reg['age'])
                    while True:
                        l = int(input("Menu: \n\n1. Search user \n2. Update account \n3. Log out \n4. Tasks \n\nSelect an option: "))
                        if l == 1:
                            id = int(input("id="))
                            for r in lict:
                                if id == r['id']:
                                    print(f"Profile {r['name']}: \nName: {r['name']}\nSurname: {r['surname']}\nNik: {r['username']}\nAge: {r['age']}")
                        elif l == 2:
                            password = input("Password: ")
                            if password == reg['pass']:
                                reg["name"] = input("Name: ")
                                reg['surname'] = input("Surname: ")
                                reg['username'] = input("Username: ")
                                reg['age'] = input("Write your age: ")
                                reg['pass'] = input("Password: ")
                            else:
                                print("Your password is incorrect")
                        elif l == 3:
                            break
                        elif l == 4:
                            q = int(input("Menu task:\n\n1. New Task\n2. Search Tasks\n3. Update Task \n4. Delete Task \n\nSelect an option: "))
                            if q == 1:
                                task1 = {
                                    "id": len(reg['tasks']) + 1,
                                    "task": input("Task: "),
                                    "vre": input("Time: "),
                                    "bol": False,
                                    "mesto": input('Location: ')
                                }
                                reg['tasks'].append(task1)
                                task.append(task1)
                            elif q == 2:
                                for t in reg['tasks']:
                                    print(t)
                            elif q == 3:
                                task_id = int(input("Task ID: "))
                                for t in reg['tasks']:
                                    if t['id'] == task_id:
                                        t['task'] = input("Task: ")
                                        t['vre'] = input("Time: ")
                                        t['mesto'] = input("Location: ")

                                        t['bol'] = bool(input("Completed (True/False): "))
                                        break
                            elif q == 4:
                                task_id = int(input("Task ID: "))
                                for i, t in enumerate(reg['tasks']):
                                    if t['id'] == task_id:
                                        del reg['tasks'][i]
                                        print("Task deleted")
                                        break
                                else:
                                    print("Task not found")
                else:
                    print("Your password or username is incorrect")
                    continue
        else:
            print("User not found")
    elif n == 3:
        id = int(input("id="))
        for i, reg in enumerate(lict):
            if id == reg['id']:
                password = input("Password: ")
                if password == reg['pass']:
                    del lict[i]
                    print("User deleted")
                    break
                else:
                    print("Your password is incorrect")
                    break
        else:
            print("User not found")
    elif n == 4:
        print("Exiting...")
        break
