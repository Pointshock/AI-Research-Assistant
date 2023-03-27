# This imports the package we will use to make the API call to Wikipedia
import wikipedia
# This lets the user know what the program is doing
print("\n\nHello, my name is Agent Smith. I will be your guide to the world of research.\n")
# This gets the user's input to search for a topic
user_topic = input("\n\nWhat would you like me to research for you? \n")
# This displays a line for a better user experience
print("_" * 50)
print("\n\n")
# Wikipedia API call
wiki_page = wikipedia.page(user_topic)
print("\n\n" + wiki_page.title + "\n")
# This displays a line for a better user experience
print("_" * 50)
# This displays the summary of the topic the user wants to research
print("\n\n" + wiki_page.summary + "\n")
# This displays a line for a better user experience
print("_" * 50)
# Saves the users inputs
# Writes data to a text file
# If it does not exist it creates a file
file_obj = open("data_save.txt", "a")
# Write some stuff to the file
# Use the file object, not the file name to handle the file
file_obj.write(wiki_page.title + "\n")
file_obj.write("_" * 50)
file_obj.write("\n" + wiki_page.summary + "\n")
# Close the file right away
file_obj.close()
