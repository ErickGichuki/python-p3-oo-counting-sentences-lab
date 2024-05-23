#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self._value = value

  @property
  def value(self):
      return self._value
  
  @value.setter
  def value(self, new_value):
     if isinstance(new_value, str):
        self._value = new_value

     else:
        print("The value must be a string.")

  def is_sentence(self):
     if self._value.endswith('.'):
        return True
     else:
        return False
  def is_question(self):
     if self._value.endswith("?"):
        return True
     else:
        return False
     
  def is_exclamation(self):
     if self._value.endswith("!"):
        return True
     else:
        return False
     
  def count_sentences(self):
     import re
     sentences = re.split(r'[.!?]', self._value)
     sentences = [s for s in sentences if s.strip()]
     return len(sentences)
