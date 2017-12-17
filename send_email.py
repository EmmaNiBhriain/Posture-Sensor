def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox258f624fe3bc4c60b8fa57f7ffce0a3e.mailgun.org/messages",
        auth=("api", "key-de741695d3ee0e12408db62a8b5851ff"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox258f624fe3bc4c60b8fa57f7ffce0a3e.mailgun.org>",
              "to": "Emma <obrienemma0@gmail.com>",
              "subject": "Hello Emma",
              "text": "Congratulations Emma, you just sent an email with Mailgun!  You are truly awesome!"})
