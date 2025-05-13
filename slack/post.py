import os
from slackclient import SlackClient

client = SlackClient(os.environ["SLACK_API_TOKEN"])

response = client.api_call(
    "chat.postMessage",
    channel = "#test",
    # text = "Hello world!!",
    # attachments = [
    #     {
    #         "fallback": "Required plain-text summary of the attachment.",
    #         "color": "#2eb886",
    #         "pretext": "Optional text that appears above the attachment block",
    #         "author_name": "Bobby Tables",
    #         "author_link": "http://flickr.com/bobby/",
    #         "author_icon": "http://flickr.com/icons/bobby.jpg",
    #         "title": "Slack API Documentation",
    #         "title_link": "https://api.slack.com/",
    #         "text": "Optional text that appears within the attachment",
    #         "fields": [
    #             {
    #                 "title": "Priority",
    #                 "value": "High",
    #                 "short": False
    #             }
    #         ],
    #         "image_url": "http://my-website.com/path/to/image.jpg",
    #         "thumb_url": "http://example.com/path/to/thumb.png",
    #         "footer": "Slack API",
    #         "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
    #         "ts": 123456789
    #     }
    # ],
    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ":monkey: Danny Torrence left the following review for your property:"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": 
                    ":monkey: Danny Torrence left the following review for your property:\n" +
                    ":monkey: Danny Torrence left the following review for your property:\n" +
                    ":monkey: Danny Torrence left the following review for your property:\n"
            }
        }
    ]
    #     {
    #         "type": "section",
    #         "text": {
    #             "type": "mrkdwn",
    #             "text": "<https://example.com|Overlook Hotel> \n :star: \n Doors had too many axe holes, guest in room " +
    #             "237 was far too rowdy, whole place felt stuck in the 1920s."
    #         },
    #         "accessory": {
    #             "type": "image",
    #             "image_url": "https://images.pexels.com/photos/750319/pexels-photo-750319.jpeg",
    #             "alt_text": "Haunted hotel image"
    #         }
    #     },
    #     {
    #         "type": "section",
    #         "fields": [
    #             {
    #                 "type": "mrkdwn",
    #                 "text": "*Average Rating*\n1.0"
    #             }
    #         ]
    #     }
    # ]
)

print str(response)