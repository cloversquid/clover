# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

headers = True # switch to True if you want to enable section headers in output
def disp_header(header, num):
    if headers:
        if num == 1:
            print(f"\n=== {header} ===\n")
        else: 
            print(f"\n{header}")

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    },
    "Altair": {
        "RA": "19h 50m 47s",
        "Dec": "+08° 52′ 06″",
        "Magnitude": 0.76,
        "Spectral Type": "A7Vn"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
disp_header("1) Write a function that uses a loop to print the name of each star.", 2)

def print_names(lst):
    for name in lst:
        print(f"    {name}")

print_names(targets)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.
disp_header("2) Write a function that uses a loop to print the name of each star with its spectral type.", 2)

def print_names_sptype(lst):
    for name,info in lst.items():
        print(f" ~\n Name: {name}\n Spectral Type: {info["Spectral Type"]}")
    print(" ~")
        

print_names_sptype(targets)

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
disp_header("3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.", 2)

def mag_over_tenth(lst):
    mag_list = []
    for name, info in lst.items():
        if info["Magnitude"] > 0.1:
            mag_list.append(name)
    return mag_list

print(f"  {mag_over_tenth(targets)}")
            
# 4) Look up another target, add all the necessary information to the targets list. 
disp_header("4) Look up another target, add all the necessary information to the targets list. ", 2)

print(f"  Altair\n  {targets["Altair"]}")

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
disp_header("5) Write a function that finds the brightest star whose Declination is closest to 20°.", 2)

def find_bright_dec20(lst):
    best_name = None
    best_mag =  None
    best_dec = None
    best_distance = None 

    for name, info in lst.items():
        deg = int(info["Dec"].split()[0].replace("−", "-").replace("°", ""))
        mag = info["Magnitude"]
        distance = abs(deg - 20)

        if best_distance is None or distance < best_distance or (distance == best_distance and mag < best_mag):
            best_name = name
            best_mag = mag
            best_dec = deg
            best_distance = distance
    return best_name, best_mag, best_dec

print(find_bright_dec20(targets))

# 6) What is your favorite constellation?

print(f"Orion, because I can always find it, and I have freckles on my arm that I have always thought looked like his belt. \nAnd Betelguise is so red! It also orients me so I can find other constellations or objects.")
