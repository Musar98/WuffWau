from dog_data import get_dog_data


# Your tool finds and prints various interesting aspects about the given data. Those are:
# Which is the longest dog name? (if there is a tie, it's okay to print only one, or all of them, whatever you prefer -- also note that the names are cut off unfortunately, you can ignore that)
# Which is the shortest one? (same as above; also, ? in the data should not count as the shortest name)
# Which are the top 10 most common names...
# ...overall?
# ...for male dogs?
# ...for female dogs?
# Hint: a collections.Counter makes this easier.
# You don't need to preprocess names or e.g. merge similar names, i.e. "Luna" and "Luna-Verena (Mona Lisa)" are two different dogs.
# How many dogs are male vs. female?
# Your tool should print all this information in a single run. How the output looks exactly is up to you, as long as all this information is visible.
# Sample output (your invocation and output may vary):
# $ wuff stats
# Shortest Name: Bo
# Longest Name:  Zar-Lorcan vom Franzosenkeller
# ... more output omitted ...


def wuff_stats():
    dog_data = get_dog_data()

    longest_name = "",
    shortest_name = "",
    top_ten_most_common_names_overall = ""
    top_ten_most_common_names_male = ""
    top_ten_most_common_names_female = ""

    pass
