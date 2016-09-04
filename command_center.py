from commands import mmr_command
from commands import quit_command

class CommandCenter(object):

  def __init__(self, chatbot):
    self.chatbot = chatbot
    self.hon_account = 'Bubly'

  def _extract_username_from_line(self, line):
    """Extract the user who send the message from a line of chat.

    Messages are prefixed with the format of `:<username>!`.

    Args:
        line:  A line of text received from the Twitch irc server.

    Returns:
        Returns the username as a string. If the message is in an invalid
        format, then it returns an empty string.
    """
    if line:
      split_by_colon = line.split(':')
      if len(split_by_colon) > 1:
        username_segment = split_by_colon[1]
        split_by_exclamation = username_segment.split('!')
        if split_by_exclamation:
          return split_by_exclamation[0]
    return ''

  def _extract_message_from_line(self, line):
    """Extract the message from a line of chat.

    Messages are sufixed with the format of `:<message>`.

    Args:
        line:  A line of text received from the Twitch irc server.

    Returns:
        Returns the message as a string. If the message is in an invalid
        format, then it returns an empty string.
    """
    if line:
      split_by_colon = line.split(':')
      if len(split_by_colon) > 2:
        return split_by_colon[2]
    return ''

  def process(self, line):
    """Process a line of text and handle any commands that may occur.

    Args:
        line:  A line of text received from the Twitch irc server.
    """
    user = self._extract_username_from_line(line)
    message = self._extract_message_from_line(line)
    if not user or not message:
      return
    print 'COMMAND -> User: "' + user + '" Message: "' + message + '"'

    message_args = message.split()
    msg = message_args[0]
    if msg == '!mmr':
      mmr_command.MmrCommand(user, message_args, self.chatbot, self.hon_account)
    if msg == '!quit':
      quit_command.QuitCommand(user, message_args, self.chatbot)