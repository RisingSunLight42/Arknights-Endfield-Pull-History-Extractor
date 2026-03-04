import csv
import requests
from os import environ
from dotenv import load_dotenv


ASIA_SERVER=2
US_EU_SERVER=3
PULL_HISTORY_BASE_LINK="https://ef-webview.gryphline.com/api/record/char?lang={LANG}&seq_id={SEQ_ID}&pool_type={BANNER_TYPE}&token={TOKEN}&server_id={SERVER_ID}"
CHARTERED="E_CharacterGachaPoolType_Special"
STANDARD="E_CharacterGachaPoolType_Standard"
BEGINNER="E_CharacterGachaPoolType_Beginner"
BANNER_TYPES=[CHARTERED, STANDARD, BEGINNER]
BANNER_NAMES={
    CHARTERED: "Chartered Headhunting",
    STANDARD: "Basic Headhunting",
    BEGINNER: "Beginner Headhunting",
}
SEQ_ID=1_000_000
EXPORT_FOLDER="exports"


def print_without_token(element: str):
    sane_part, to_sanitize = element.split("&token=")
    print(sane_part + "&token=REDACTED&" + to_sanitize.split("&")[1])    


def get_lang() -> str:
    if environ.get("LANG_PULL") != None:
        return environ.get("LANG_PULL")
    return "en-us"


def ask_server() -> int:
    print("Please select your server (1=ASIA,2=US_EU,default is US_EU): ",end="")
    server = input()
    try:
        server = int(server)
    except ValueError:
        return US_EU_SERVER
    if server == 1:
        return ASIA_SERVER
    return US_EU_SERVER


def ask_banner() -> list:
    print("Which banner do you want to parse the pulls? (0=All,1=Chartered,2=Standard,3=Beginner,default is All) ",end="")
    banner = input()
    try:
        banner = int(banner)
    except ValueError:
        return BANNER_TYPES
    if banner == 0:
        return ASIA_SERVER
    elif banner == 1:
        return [CHARTERED]
    elif banner == 2:
        return [STANDARD]
    elif banner == 3:
        return [BEGINNER]
    return BANNER_TYPES


def get_banner_pulls(generated_link: str, banner_type: str) -> list:
    BANNER_LINK = generated_link.replace("{BANNER_TYPE}", banner_type)
    all_pulls = []
    previous_seq_id = SEQ_ID
    base_response = requests.get(BANNER_LINK).json()
    returned_character = base_response["data"]["list"]
    all_pulls = [*all_pulls, *returned_character]
    has_more = base_response["data"]["hasMore"]
    while has_more:
        BANNER_LINK = BANNER_LINK.replace(f"seq_id={previous_seq_id}", f"seq_id={returned_character[-1]["seqId"]}")
        previous_seq_id = returned_character[-1]["seqId"]
        base_response = requests.get(BANNER_LINK).json()
        try:
            returned_character = base_response["data"]["list"]
            all_pulls = [*all_pulls, *returned_character]
            has_more = base_response["data"]["hasMore"]
            print(f"{len(all_pulls)} pulls parsed for {BANNER_NAMES[banner_type]}")
        except:
            print("==ERROR ENCOUNTERED==")
            print_without_token(BANNER_LINK)
            print(base_response)
    return all_pulls


def get_all_pulls(generated_link: str, banner_list: list) -> dict:
    all_pulls_dict = {}
    for banner_type in banner_list:
        all_pulls_dict[banner_type] = get_banner_pulls(generated_link, banner_type)
        break
    return all_pulls_dict


def write_csv(chara_dict: dict) -> None:
    fieldnames = ["poolName", "charName", "rarity", "isFree", "isNew", "gachaTs"]
    for key, value in chara_dict.items():
        csv_filename = f"{BANNER_NAMES[key]}.csv".replace(" ", "_")
        with open(csv_filename, mode='w', newline='', encoding="UTF-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(value)


def script_run() -> None:
    print("==SCRIPT HAS STARTED==")
    load_dotenv()
    if environ.get("TOKEN") == None:
        raise Exception("You haven't put your auth token in your .env file. PLease refer to the README for more informations.")
    TOKEN = environ.get("TOKEN")
    LANG = get_lang()
    SERVER_ID = ask_server()
    GENERATED_LINK = PULL_HISTORY_BASE_LINK.replace("{LANG}", LANG).replace("{SEQ_ID}", str(SEQ_ID)).replace("{TOKEN}", TOKEN).replace("{SERVER_ID}", str(SERVER_ID))
    chara_dict = get_all_pulls(GENERATED_LINK, ask_banner())
    write_csv(chara_dict)
    print("==SCRIPT HAS FINISHED==")


if __name__ == "__main__":
    script_run()
