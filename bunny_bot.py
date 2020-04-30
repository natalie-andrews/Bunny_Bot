import re
import random

class BunnyBot:
  # potential negative responses
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
  # keywords for exiting the conversation
  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later", "goodbye", "got to go")
  # random starter questions
  random_questions = (
        "How's your day going Mummy Bunny? ",
        "What do you do when you leave the house? ",
        "What did you have to eat today? I had some fresh weeds. ",
        "Are there other bunnies like me? ",
        "Do you want to come hang out with me in the garden? ",
        "Would you like to help me dig a hole? ",
        "Do you have any carrots today? "
    )

  def __init__(self):
    self.bunnybabble = {'hows_your_day_intent': '.*\s*your day.*','carrots_intent': '.\s*carrot.*', 'cubed_intent': '.*.*(\d+)'}

  # Define .greet() below:
  def greet(self):
    self.name = input("Hi there. Who I am talking to?")
    will_chat = input(f"Hey {self.name}! Do you want to chat with me? ")
    if will_chat in self.negative_responses:
      print ("No worries, see you later! xxx")
      return
    self.chat()

  # Define .make_exit() here:
  def make_exit(self, reply):
    for word in self.exit_commands:
      if word in reply:
        print ("Bye for now! I hope we can chat later xxx")
        return True

  # Define .chat() next:
  def chat(self):
    reply = input(random.choice(self.random_questions)).lower()
    while not self.make_exit(reply):
      reply = input(self.match_reply(reply))

  # Define .match_reply() below:
  def match_reply(self, reply):
    found = False
    for intent, regPattern in self.bunnybabble.items():
      found_match = re.findall(regPattern, reply)
      if found_match and intent == 'hows_your_day_intent':
        return self.hows_your_day_intent()
      elif found_match and intent == 'carrots_intent':
        return self.carrots_intent()
      elif found_match and intent == 'cubed_intent':
        return self.cubed_intent(found_match[0])
    if not found:
      return self.no_match_intent()

  def hows_your_day_intent(self):
    responses = ("Pretty relaxing, I've just been napping. ", "Great! I dug a tunnel, do you want to see? ", "Good, but I'm kind of hungry, do you have any snacks? ", "It's been alright, but I'm a bit lonely and would love a pat. ", "So good, just been eating some curtains! ")
    return random.choice(responses)

  def carrots_intent(self):
    responses = ("I love carrots! Can I have one now? ", "Unfortunately I never get a full carrots, only the peel. ", "Carrots are good but so is apple! Do you have a snack for me? ")
    return random.choice(responses)
       
  def cubed_intent(self, number):
    number = int(number)
    cubed_number = number * number * number
    return (f"The cube of {number} is {cubed_number}. Who knew bunnies were good at maths? ")

  def plans_for_today_intent(self):
    responses = ("I might see if my pigeon friends are around! ", "Maybe hang out with Mummy Bunny if she's doing some gardening. ", "Probably watch some TV with Mummy Bunny and Nicole. ", "I'm just going to hang around until some weeds appear for me to eat. ")
    return random.choice(responses)

  def love_me_intent(self):
    responses = ("Of course I do, you're the best Mummy Bunny ever! ", "I love you so much, no one else gets me weeds like you do. ", "Yes I do, you give the best pats and jaw rubs. ", "Absolutely, thanks for always looking after me. ")
    return random.choice(responses)

  def my_name_intent(self):
    responses = ("Honestly, I'm not sure. It's either Bunny, Fluffy Bun or Heather. It's a bit confusing. ", "Well, someone once mentioned Flat Bunny which got me a little worried. ", "Mummy Bunny calls me Bunny Bun a lot? ")
    return random.choice(responses)

  def favourite_intent(self):
    responses = ("Mummy Bunny obviously. She looks after me. ", "Nicole is pretty cool, after all, I am technically her rabbit. She can be pretty loud though. ", "Natalie is nice to me, but I never really see her anymore which is sad. ")
    return random.choice(responses)

  def no_match_intent(self):
    responses = ("Please tell me more. ", "Tell me more! ", "Why do you say that? ", "I see. Can you elaborate? ", "Interesting. Can you tell me more? ", "I see. How do you think? ", "Why? ", "How do you think I feel when you say that? ")
    return random.choice(responses)


my_bot = BunnyBot()
my_bot.greet()