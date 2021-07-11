import pywhatkit as kit
from optparse import OptionParser


def send_msg_on_whatsapp():
    phone_num = input("Enter the Phone Number of receiver ->: ")
    text = input("Enter the text you want to send ->: ")
    send_hour = input("Enter the hour at which you want to send msg ->: ")
    send_mins = input("Enter the minute at which you want to send msg ->: ")
    kit.sendwhatmsg(phone_num, text, send_hour, send_mins)


def text_to_handwritten():
    text = input("Enter some random text")
    kit.text_to_handwriting(text, rgb=(0, 0, 255))


def main(options):
    if options.function == "t-to-h":
        text_to_handwritten()

    elif options.function == "send-wsp-msg":
        send_msg_on_whatsapp()

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
