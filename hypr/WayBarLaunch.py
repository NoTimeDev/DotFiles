from os import system


with open("/home/devvy/.config/hypr/IsWay.txt", "r") as File:
    IsRead = File.read()

if IsRead == "False":
    IsRead = "True"
    with open("/home/devvy/.config/hypr/IsWay.txt", "w") as File:
        File.write(IsRead)

    system("waybar")

else: 
    IsRead = "False"
    
    with open("/home/devvy/.config/hypr/IsWay.txt", "w") as File:
        File.write(IsRead)


    system("pkill waybar")
   
