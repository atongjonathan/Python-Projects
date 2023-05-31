with open(r"C:\Users\Administrator\PycharmProjects\emails\Input\Names\invited_names.txt") as file:
    names = file.readlines()
with open(r"C:\Users\Administrator\PycharmProjects\emails\Input\Letters\starting_letter.txt")as letter:
    text = letter.read()
    print(text)

for name in names:
    name = name.strip()
    with open(f"C:/Users/Administrator/PycharmProjects/emails/Output/ReadyToSend/letter for {name}.txt", mode='w')as new:
        letter_contents = text.replace("[name]", name.strip())
        new.write(letter_contents)
