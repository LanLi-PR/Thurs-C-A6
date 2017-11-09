class Input_Output():
   # building_code = {493: 'ischool', 526: 'University of illinois Armory', 590: 'School of Art+Design' , 584: 'Huff Hall' ,718: 'English Building', 456: 'Lincoln Hall', 151: 'Davenport Hall', 162: 'Foreign Languages Building', 522: 'Undergraduate Library', 710: 'University of illinois Extension/Mumford Hall',631 :'Funk Agricultural Constitute/Funk ACES', 52: 'Freer Hall',37 :'School of Social Work', 39: 'Dance Studio', 36 : 'Institute of Government and public Affairs', 50: 'Allen Hall and Unit One', 26 : 'Mckinley Health Center', 525: 'UI Ice Arena', 195: 'Carl R. Woese Institute for Genomic Biology',65 :'Spurlock Museum'}

    building_code = {50: 'Allen Hall and Unit One', 195: 'Carl R. Woese Institute for Genomic Biology', 39 : 'Dance Studio',151 : 'Davenport Hall',718 : 'English Building',162 : 'Foreign Languages Building', 52 :'Freer Hall', 631 : 'Funk Agricultural Constitute/Funk ACES', 584 : 'Huff Hall',36 : 'Institute of Government and public Affairs', 456 : 'Lincoln Hall',26 : 'Mckinley Health Center',590 : 'School of Art+Design',37 : 'School of Social Work', 65 : 'Spurlock Museum',525 : 'UI Ice Arena', 522 : 'Undergraduate Library', 526 : 'University of illinois Armory', 710 : 'University of illinois Extension/Mumford Hall', 493 : 'ischool'}

    for i in building_code:
       print(i,building_code[i])

    str = int(input(" Enter the mailing code your starting point"))
    stp = int(input(" Enter the mailing code your starting point"))
    try:
        print("Showing the shortest route from", building_code[str],"to",  building_code[stp])
    except Exception as KeyError:
        print("Incorrect Mailing codes")
         
if __name__ == "__main__":
    Input_Output()
