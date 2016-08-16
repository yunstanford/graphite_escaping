class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''
     
    @staticmethod
    def green_print(content):
        return bcolors.OKGREEN + content + bcolors.ENDC

    @staticmethod
    def red_print(content):
        return bcolors.WARNING + content + bcolors.ENDC

    @staticmethod
    def color_print(content, color_code):
        return color_code + content + bcolors.ENDC