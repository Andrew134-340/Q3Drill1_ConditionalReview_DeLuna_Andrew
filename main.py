from pyscript import document

def compute_average(event):
    # Get raw input values
    s1 = document.getElementById("score1").value
    s2 = document.getElementById("score2").value

    # Check if any field is empty
    if s1 == "" or s2 == "":
        document.getElementById("average").innerText = "Invalid"
        document.getElementById("result").innerText = "N/A"
        return

    # Handle invalid input
    try:
        score1 = float(s1)
        score2 = float(s2)
    except:
        document.getElementById("average").innerText = "Invalid"
        document.getElementById("result").innerText = "Numbers only"
        return

    # Compute average
    average = (score1 + score2) / 2

    # Determine result using the big 3 conditional statements.
    if average >= 90:
        result = "Awesome! Passed with flying colors!"
    elif average >= 75:
        result = "Passed :D"
    else:
        result = "Failed :("

    # Display results accordingly.
    document.getElementById("average").innerText = str(round(average, 2))
    document.getElementById("result").innerText = result
