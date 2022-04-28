class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


email_list = []

while True:
    command = input()
    if command == 'Stop':
        break

    new_command = command.split(" ")
    sender = new_command[0]
    receiver = new_command[1]
    content = new_command[2]
    info = Email(sender, receiver, content)
    email_list.append(info)

send_emails = [email_list[int(x)].send() for x in input().split(", ")]
for i in email_list:
    print(i.get_info())

