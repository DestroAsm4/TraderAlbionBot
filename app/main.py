from app.detect.tool_detect.detect import Detect
from setting import Pathes, GameName
from app.active.cliker import Clicker
# from detect.tool_detect.vision import Vision

class Scenaries:

    def __init__(self):
        self.detecter_mail_ind = Detect(Pathes.mail_ind, options='mail_ind')
        self.detecter_new_mail = Detect(Pathes.not_read_mail, options='not_read_mail')
        Detect.focus_game(GameName.albion)

    def gen_scen(self):
        while True:
            points_mail_ind = self.detecter_mail_ind.detect()
            if points_mail_ind:
                Clicker.mail_ind()

                while True:
                    points_new_mail = self.detecter_new_mail.detect()
                    if points_new_mail:
                        for points in points_new_mail:
                            Clicker.active_click_mail(points[0], points[1])
                            #read
                            Clicker.active_click_close_mail()


if __name__ == '__main__':
    scenario = Scenaries()
    scenario.gen_scen()
