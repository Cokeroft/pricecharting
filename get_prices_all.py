from get_prices_csv import get_prices_from_csv


def main():
    # Nintendo
    get_prices_from_csv("Virtual Boy")
    get_prices_from_csv("Gamecube")
    get_prices_from_csv("Wii")
    get_prices_from_csv("Wii U")
    get_prices_from_csv("NES")
    get_prices_from_csv("Super Nintendo")
    get_prices_from_csv("Nintendo 64")
    get_prices_from_csv("Nintendo Switch")
    get_prices_from_csv("GameBoy")
    get_prices_from_csv("GameBoy Color")
    get_prices_from_csv("GameBoy Advance")
    get_prices_from_csv("Nintendo DS")
    get_prices_from_csv("Nintendo 3DS")

    # Sega
    get_prices_from_csv("Sega Master System")
    get_prices_from_csv("Sega Genesis")
    get_prices_from_csv("Sega CD")
    get_prices_from_csv("Sega 32X")
    get_prices_from_csv("Sega Saturn")
    get_prices_from_csv("Sega Dreamcast")
    get_prices_from_csv("Sega Game Gear")

    # Sony
    get_prices_from_csv("Playstation")
    get_prices_from_csv("Playstation 2")
    get_prices_from_csv("Playstation 3")
    get_prices_from_csv("Playstation 4")
    get_prices_from_csv("Playstation Vita")
    get_prices_from_csv("PSP")

    # Microsoft
    get_prices_from_csv("Xbox")
    get_prices_from_csv("Xbox 360")
    get_prices_from_csv("Xbox One")

    # Other
    get_prices_from_csv("Amiibo")
    get_prices_from_csv("3DO")
    get_prices_from_csv("TurboGrafx-16")
    get_prices_from_csv("Nintendo Power")
    get_prices_from_csv("Neo Geo")

main()
