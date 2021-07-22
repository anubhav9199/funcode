import pywhatkit as kit
from optparse import OptionParser


class Worker:
    def __init__(self):
        pass

    def search_phrase(self):
        text = input("Enter text you wnat to search ->: ")
        try:
            kit.search(text)
        except Exception as e:
            raise e

    def play_video_on_youtube(self):
        topic = input("Enter the video name ->: ")
        _use_api = input("Do you want to use API(Yes or Y/No or N) ->: ")
        use_api = True if _use_api.lower() in ['yes', 'y'] else False
        try:
            kit.playonyt(topic, use_api=use_api)
        except Exception as e:
            raise e

    def send_msg_on_whatsapp(self):
        phone_num = input("Enter the Phone Number of receiver ->: ")
        text = input("Enter the text you want to send ->: ")
        send_hour = int(input("Enter the hour at which you want to send msg ->: "))
        send_mins = int(input("Enter the minute at which you want to send msg ->: "))
        try:
            kit.sendwhatmsg(phone_num, text, send_hour, send_mins, tab_close=True)
        except Exception as e:
            raise e

    def text_to_handwritten(self):
        text = input("Enter some random text")
        try:
            kit.text_to_handwriting(text, rgb=(0, 0, 255))
        except Exception as e:
            raise e


def main(options):
    worker_obj = Worker()

    if options.function == "handwritten":
        worker_obj.text_to_handwritten()

    elif options.function == "wsappmsg":
        worker_obj.send_msg_on_whatsapp()

    elif options.function == "youtube":
        worker_obj.play_video_on_youtube()

    elif options.function == "google":
        worker_obj.search_phrase()

    else:
        print("You can use these options given below : \n1. -f --func write which function you want to use'")


if __name__ == "__main__":

    opt_parse = OptionParser()
    opt_parse.add_option("-f", "--func", dest="function",
                         help='write which function you want to use')
    # opt_parse.add_option("-h", "--help", dest="help", default=False,
    #                      help='Help with the options to use')

    options, _ = opt_parse.parse_args()

    main(options)
