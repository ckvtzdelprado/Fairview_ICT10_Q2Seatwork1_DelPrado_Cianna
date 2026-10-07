from pyscript import document

club_members = [
    "Laine Del Prado",
    "Jaeden Cajanding",
    "Jose Chiong",
    "Margareth Salacup"
]


def check_candidate(event):

    first_name = document.getElementById("first-name").value
    last_name = document.getElementById("last-name").value

    full_name = first_name + " " + last_name

    is_member = full_name in club_members

    messages = {
        True: "Congratulations " + full_name + "! You are now part of the ICT club.",
        False: "Sorry " + full_name + ", your name is not on the list."
    }

    result = messages[is_member]

    document.getElementById("result").innerText = result