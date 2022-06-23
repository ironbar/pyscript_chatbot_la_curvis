import random
from js import setTimeout
from pyodide import create_proxy, create_once_callable


def update_chat_with_user_message(event):
    conversation = Element('conversation')
    initial_content = conversation.element.innerHTML
    new_text = Element('text_input').value
    updated_content = initial_content + format_user_message(new_text)
    conversation.write(updated_content)
    # this is used to create the ilusion of the bot taking some time to reply
    setTimeout(create_once_callable(update_chat_with_bot_reply), 500)
    auto_scroll_down()


def update_chat_with_bot_reply():
    conversation = Element('conversation')
    initial_content = conversation.element.innerHTML
    updated_content = initial_content + format_bot_message(get_bot_reply())
    conversation.write(updated_content)
    auto_scroll_down()


def format_user_message(text):
    html_message = """
    <div class="user_message">
        <b>You: </b>%s<br>
    </div>
    """ % text
    return html_message


def format_bot_message(text):
    html_message = """
    <div class="bot_message">
        <b>la_curvis: </b>%s<br>
    </div>
    """ % text
    return html_message


def get_bot_reply():
    replies = [
        'IMBÉCIL',
        'IDIOTA',
        'CAPULLO',
        'DE VERDAD...',
        'STOP!',
    ]
    return random.choice(replies)


def auto_scroll_down():
    conversation = Element('conversation')
    conversation.element.scrollTop = conversation.element.scrollHeight


button = document.querySelector("button")
button.addEventListener("click", create_proxy(update_chat_with_user_message))