"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code,  words, text):
        """Create story with words and template text."""

        self.code = code
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    'Story 1',
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    'Story 2',
    ['adjective_1', 'adjective_2', 'adjective_3', 'adverb', 'noun_1', 'noun_2', 'noun_3', 'noun_4', 'noun_5', 'noun_6', 'plural_noun'],
    """Driving a car can be fun if you follow this {adjective_1} advice:
    When approaching a {noun_1} on the right, always blow your {noun_2}.
    Before making an {adjective_2} turn, always stick your {noun_3} out of the window.
    Every 2000 miles, have your {noun_4} inspected and your {noun_5} checked.
    When approaching a school, watch out for {adjective_3} {plural_noun}.
    Above all, drive {adverb} The {noun_6} you save may be your own!"""
)

story3 = Story(
    'Story 3',
    ['adjective_1', 'adjective_2', 'adjective_3', 'name_of_female_person', 'name_of_male_person', 'noun', 'occupation_1', 'occupation_2', 'part_of_body', 'verb_ending_in_ing'],
    """Thank You! Thank you from the bottom of my {part_of_body}. I don't know what to say. I'm speechless. I truly didn't expect to win this {noun}, certainly not with so many {adjective_1} actors competing in the same category. First and foremost, my thanks to {name_of_female_person} You couldn't work with a better {occupation_1} And I'm sure I wouldn't be {verb_ending_in_ing} here tonight if it weren't for my {adjective_2} director. I must also thank {name_of_male_person}, who wrote an {adjective_3} script for me. Of course, none of this would be happening if it
    weren't for my agent, who convinced the network that I could play a 75 year-old, retired {occupation_2}."""
)
