color_name={"AliceBlue": "#f0f8ff", "AntiqueWhite3": "#8b8378", "azure1": "#f0ffff", "azure4": "#838b8b",
               "BlanchedAlmond": "#ffebcd", "brown1": "#ff4040", "CadetBlue3": "#7ac5cd", "chocolate3": "#cd661d", "CornflowerBlue": "#6495ed", "cornsilk2": "#eee8cd"}

color = input("Enter color: ")
while color != "":
    if color in color_name:
        print(color, "is", color_name[color])
    else:
        print("Invalid color")
    color = input("Enter color: ")