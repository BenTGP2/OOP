Projects = {}

while True:
    print("1. Initialize project")
    print("2. Project closure")
    print("3. Project progress")
    print("4. Print a specific project")
    print("5. Print all projects")
    print("6. Close program")

    Input = input("Enter selection: ")

    if Input == "1":
        Managers = []
        Techs = []
        Team = []

        AddingTeam = True
        while AddingTeam:
            print("1. Add manager")
            print("2. Add member")
            print("3. Add technology")
            print("4. Finalize team assets")

            LoopInput = input("Enter selection")

            if LoopInput == "1":
                TeamManagers = input("Enter project manager: ")
                Managers.append(TeamManagers)
            elif LoopInput == "2":
                TeamMember = input("Enter team member: ")
                Team.append(TeamMember)
            elif LoopInput == "3":
                Technology = input("Enter technology: ")
                Techs.append(Technology)
            elif LoopInput == "4":
                print("Team assets finalized...")
                AddingTeam = False

        ProjectID = input("Enter project ID: ")
        StartDate = input("Enter project start date: ")
        EndDate = input("Enter project end date: ")
        Sponsor = input("Enter project sponsors: ")
        Budget = float(input("Enter project budget:"))

        Projects.update({ProjectID:{
                "TeamManagers":Managers,
                "TeamMembers":Team,
                "Technologies":Techs,
                "ProjectID":ProjectID,
                "StartDate":StartDate,
                "EndDate":EndDate,
                "Sponsor":Sponsor,
                "Budget":Budget
                         }})
    elif Input == "2":
        ProjectToKill = input("Enter the ID of the project you would like to close: ")
        del Projects[ProjectToKill]
    elif Input == "3":
        # This function is a work in progress!
        ProjectIDHook = input("Enter the ID of the project you would like to modify: ")
        ProjectToAccess = Projects[ProjectIDHook]

        QueryModify = input("Enter which value you would like to modify: ")
        ItemToModify = ProjectToAccess.items(QueryModify)

        UpdatedInformation = input("Enter the values you would like to update", ItemToModify, "with: ")
        ItemToModify.update(UpdatedInformation)
    elif Input == "4":
        ProjectToPrint = input("Enter the ID of the project you would like to print: ")
        print(Projects[ProjectToPrint])
    elif Input == "5":
        for Project in Projects.items():
            print(Project)
            print("---------------------------------------------------------------------------------------------------")
    elif Input == "6":
        print("Terminating program...")
        break
