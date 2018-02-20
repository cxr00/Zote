import datetime
import urllib.request
from zdn import *


def add_report(report: str):
    try:
        with open('data/reports.zote', 'a+') as f:
            f.write(report)
            f.write("\n")
    except UnicodeEncodeError as e:
        print("ERROR CODE 420. Unable to log command due to super dank name.")


def log(name, ctx):
    try:
        u_name = ctx.message.author.name
        server = ctx.message.server.name
        s_id = ctx.message.server.id
        ch_name = ctx.message.channel.name
        time_formatted = datetime.datetime.fromtimestamp(time.time()).strftime('%x %X')
        s = "{0}, {1}, {2}({3})-#{4}, {5}".format(u_name, name, server, s_id, ch_name, time_formatted)
        print(s)
        with open('data/log/cmd.zote', 'a') as f:
            f.write(s)
            f.write("\n")
    except UnicodeEncodeError:
        print("ERROR CODE 420. Unable to log command due to super dank name.")


def submit(name, id, meme):
    with open('data/memes.zote', 'a') as f:
        f.write("{0}\n".format(meme))
    print("Meme submitted by {0}({1}) at {2}".format(name, id, meme))


wiki_str = "http://hollowknight.wikia.com/wiki/"
base = wiki_str + "Special:Search"
search = base + "?query="
no_results = base.encode()


def wiki_search(query):
    try:
        query = query.replace(" ", "+")
        page = urllib.request.urlopen("{0}{1}".format(search, query)).readlines()
        flag = "class=\"result-link\"".encode()
        # print(page)
        for line in page:
            if flag in line:
                # print(line)
                out = line.split('\"'.encode())
                return out[1].decode("utf-8")
        return "None found"
    except Exception:
        return "None found"


def general_psa():
    s = "PSA: <#{0}> is a spoiler-free channel.\n\n"
    s += "This means no discussions past Crossroads.\n\n"
    s += "If it requires progressing past Crossroads to unlock inside Crossroads, don't talk about it here.\n\n"
    s += "If you need help with a specific portion of the game, ask in <#{1}> and someone will answer.\n\n"
    s += "If you wish to talk about the rest of the game or the lore or such, <#{2}>\n\n"
    s += "If you've drawn something or would like to talk about the art, <#{3}>.\n\n"
    return s.format(config["ch"]["general"], config["ch"]["help"], config["ch"]["discussion"], config["ch"]["art"])


def splr_lrt():
    s = "**Reminder**: Please avoid any discussion of content past the Forgotten Crossroads! Discuss details"
    s += " in <#{0}> or <#{1}>"
    return s.format(config["ch"]["help"], config["ch"]["discussion"])


def improve():
    s = "If you are stuck on a boss or don't know where to go, you can ask for tips in <#{0}> and <#{1}>! "
    s += "Members of the server can offer tips on charms, upgrades, and strategies for "
    s += "any part of the game.\n\n For *spoiler-lite* help, see <#{0}>.\n\n"
    s += "For spoiler-heavy details, see <#{1}> (you have been warned!)"
    return s.format(config["ch"]["help"], config["ch"]["discussion"])


def modtext():
    s = "**MOD-ONLY COMMANDS:**\n\n"
    s += "**ignore** [user id]: prevents the user from accessing Zote commands, or takes them off the ignore list.\n\n"
    s += "**ignorelist** shows all users being ignored and their ID.\n\n"
    s += "**silence** [#tag channel]: stops/starts Zote responding to commands in a channel\n\n"
    s += "**clear** [x] or **clear** [@tag user] [x]: deletes X messages from a channel (or a user in that channel)\n\n"
    s += "**clearzotes** [optional amount x]: deletes all _commands and posts from Zote, or the X most recent ones\n\n"
    s += "**helpchannel**: clears all messages in the help channel and reposts the opening help message.\n\n"
    s += "**ban**: reaction image of the False Knight's Banhammer (not an actual ban!)\n\n"
    return s


def helptext():
    help_text = "**Come one, come all! Come ask your game progression related questions here without fear of unnecessary or unrelated spoilers!**\n\n"
    help_text += "The channel is cleared every so often or upon request to further reduce any chance of unwanted spoilers. Tag @ Mods if the channel needs to be cleared.\n\n"
    help_text += "If you're interested in spoiler-free information about the final boss/ending or the Hidden Dreams update, check the Google Drive link in the channel description.\n\n"
    help_text += "If you just need more information about a particular enemy, boss, or charm, Zote has a built-in wiki search command. For example, try:\n\n"
    help_text += "{0}wiki Dirtmouth"
    return help_text.format(config["init"]["pre"])


def randomizer_taunt():
    possible = ["May you find Mantis Claw in King's Pass.",
                "If all else fails, just shade skip.",
                "If it takes more than 5 hours you should probably reset.",
                "You'll never find the Crystal Heart.",
                "It's impossible to softlock, just gitgud."
                ]
    return possible[random.randint(0, len(possible)-1)]
