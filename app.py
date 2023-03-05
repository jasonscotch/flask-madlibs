from flask import Flask, render_template, request
# from random import choice, sample
from stories import story1, story2, story3

from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY'] = 'password123'

debug = DebugToolbarExtension(app)

stories = {s.code: s for s in [story1, story2, story3]}


@app.route("/", methods=['GET'])
def dropdown():

    return render_template('home.html', stories=stories.values())


@app.route('/prompts', methods=['GET'])
def show_prompts():

    story_name = request.args.get('story_name')
    story = stories[story_name]
    prompts = story.prompts
    # print(story, prompts)
    return render_template('prompts.html', prompts=prompts, story_name=story_name)


@app.route("/story", methods=['GET'])
def show_story():
    
    story_name = request.args.get('story_name')
    story = stories[story_name]
    text = story.generate(request.args)
    return render_template('story.html', text=text, story_name=story_name)
