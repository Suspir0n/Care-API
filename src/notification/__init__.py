class BaseNotification:

    def __init__(self):
        message = ''
        self.notify = {'message': message}
        self.notifications = list()


    def add_notification(self, message):
        """
        This method add a notification receiving a message for add in list.
        :param message: receive a message with param.
        :return: null
        """
        self.notify['message'] = message
        self.notifications.append(self.notify)


    def is_true(self, value, message):
        """
        This method verify if the value is true for add message in list.
        :param value: receive a value string any
        :param message: receive a message with param.
        :return: null
        """
        if value is True:
            self.notify['message'] = message
            self.notifications.append(self.notify)


    def is_required(self, value, message):
        """
        This method verify if the value not is true or the size is less than
        or equal to zero for add message in list.
        :param value: receive a value string any
        :param message: receive a message with param.
        :return: null
        """
        if not value or len(value) <= 0:
            self.notify['message'] = message
            self.notifications.append(self.notify)


    def has_min_len(self, value, minimum, message):
        """
        This method verify if the value has the size minimum for add message in list.
        :param value: receive a value string any
        :param minimum: receive a value minimum
        :param message: receive a message with param.
        :return: null
        """
        if not value or len(value) < minimum:
            self.notify['message'] = message
            self.notifications.append(self.notify)


    def has_max_len(self, value, maximum, message):
        """
        This method verify if the value has the size maximum for add message in list.
        :param value: receive a value string any
        :param maximum: receive a value maximum
        :param message: receive a message with param.
        :return: null
        """
        if not value or len(value) > maximum:
            self.notify['message'] = message
            self.notifications.append(self.notify)


    def is_fixed_len(self, value, scale, message):
        """
        This method verify if the value is a size fixed for add message in list.
        :param value: receive a value string any
        :param scale: receive the size fixed
        :param message: receive a message with param.
        :return: null
        """
        if len(value) != scale:
            self.notify['message'] = message
            self.notifications.append(self.notify)


    def all_notifications(self):
        """
        This method return all notifications receives.
        :return: a list notifications
        """
        return self.notifications


    def valid(self):
        """
        This method return true or false if the size of list is valid.
        :return: true or false
        """
        return len(self.notifications) == 0

    pass
