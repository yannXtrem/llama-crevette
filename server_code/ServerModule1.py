import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
from gpt4all import GPT4All
@anvil.server.callable
def ask(question):
  model = GPT4All("Phi-3-mini-4k-instruct.Q4_0.gguf") # downloads / loads a 4.66GB LLM
  with model.chat_session():
    print(model.generate(question, max_tokens=1024))