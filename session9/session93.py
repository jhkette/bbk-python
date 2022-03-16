def sentenceBuilder(subjects, verbs, objects):
  for subject in subjects:
    for verb in verbs:
      for object in objects:
        print(subject.capitalize(), verb, object)

subjects = ["Peppa Pig", "my neighbour", "the Major"]
verbs = ["kissed", "ate", "read"]
objects = ["a book", "a steak", "a dog"]
sentenceBuilder(subjects, verbs, objects)

"""
•Write a function sentenceBuilder() that takes

a list of subjects

a list of verbs

a list of objects

It prints out all the possible sentences it can build from the three lists.

Don't forget to capitalise the first letter and add a full stop at the end of each sentence.

Add a number in front of each sentence built.

For example,

subjects = ["Peppa Pig", "my neighbour", "the Major"]

verbs = ["kissed", "ate", "read"]

objects = ["a book", "a steak", "a dog"]
"""