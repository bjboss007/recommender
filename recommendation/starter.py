from  recommendation.user.question import questions
from  recommendation.models import * 
from  recommendation import create_app
import os

app = create_app()
app.test_request_context().push()
 
def starter():
    db.drop_all()
    db.create_all()
    
    for quest in questions:
        question = Question(name = quest["question"], answer = quest['answer'])
        options = []
        for opt in quest["options"]:
            option = Option(name = opt)
            options.append(option)
        question.options = options
        db.session.add(question)

    normal = Category(name = "Normal")
    mild = Category(name = "Mild")
    moderate = Category(name = "Moderate")
    severe = Category(name = "Severe")
    file_name = os.path.join('http://localhost:8082/static/images','aaaa.png')
    normal_1 = """
        <ul>
            <li> Three minute Breathing </li>
            <li>Mindfulness stretching</li>
            <li>Mindful showering</li>
            <li>Mindful Brushing your teeth</li>
            <li>Mindful eating</li>
            <li>Mindful making your bed.</li>
        </ul>
    """
    mild_1 = """
        <ol>
            <li>
                <span> Life style changes </span>:
                <ul>
                    <li>Get enough sleep (8 hoours daily)</li>
                    <li> Eat a healthy diet </li>
                    <li> Take regualar breaks from work </li>
                    <li> Find a relaxing hobby i.e gardening or woodworking. </li>
                    <li> Stay away from alcohol or caffeine</li>
                    <li> Surround yourself with supportive and posiive friends & Family.</li>
                </ul>
            </li>
        </ol>
    """

    mild_2 = """
        <ol>
            <li>
                <span> Regular Exercise </span>
                <ul>
                    <li>Do breathing exercise; Breathe in and out (5 mins)</li>
                    <li> Have a short stoll </li>
                    <li> Practise a gentle yoga exercise </li>
                </ul>
            </li>
        </ol>
    """

    moderate_1 = """
        <ul>
            <li> Replace negative beliefs with positive, healthy ones.</li>
            <li> Improve your communication skills</li>
            <li> Increase your self-esteem</li>
            <li> Regain a sense of satisfaction & control in your life</li>
            <li> Eat right</li>
            <li> Avoid alcohol </li>
        </ul>
    """

    moderate_2 = """
    <ul style = "list-style:none">
            <li>
                <span> Get plenty of exercise </span>
            </li>
        </ul>
    """

    severe_1 = """
        <ul>
            <li> Replace negative beliefs with positive, healthy ones.</li>
            <li> Improve your communication skills</li>
            <li> Increase your self-esteem</li>
            <li> Regain a sense of satisfaction & control in your life</li>
            <li> Eat right</li>
            <li> Avoid alcohol </li>
        </ul>
    """

    severe_2 = """
        <ul>
            <li>
                Get plenty of exercise </a> 
            </li>
            <li>
                You can talk to your Doctor or visit the nearest Health care for further help.
            </li>
        </ul>
    """

    r_normal = Remedy(name = normal_1, title = "normal")
    r_mild1 = Remedy(name = mild_1, title = "mild_1")
    r_mild2 = Remedy(name = mild_2, title = "mild_2", image_file = file_name)
    r_mod1 = Remedy(name = moderate_1, title = "moderate_1")
    r_mod2 = Remedy(name = moderate_2, title = "moderate_2", image_file = file_name)
    r_sev = Remedy(name = severe_1, title = "severe_1")
    r_sev2 = Remedy(name = severe_2, title = "severe_2", image_file = file_name)

    normal.remedies = [r_normal]
    mild.remedies = [r_mild1, r_mild2]
    moderate.remedies = [r_mod1, r_mod2]
    severe.remedies = [r_sev, r_sev2]

    db.session.add_all([normal, mild, moderate, severe])
    db.session.commit()