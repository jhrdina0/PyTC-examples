from Teamcenter.Soa.Client.Model import ErrorStack, ErrorValue, PartialErrorListener

class AppXPartialErrorListener(PartialErrorListener):
    __namespace__ = "AppXPartialErrorListener"
    def __init__(self):
        self.ErrorsQueue: list[ErrorValue] = []

    def HandlePartialError(self, partialErrors: list[ErrorStack]):
        """
        Handle partial errors from the server and add them to the queue.
        :param partialErrors: A list of ErrorStack objects
        """
        for stack in partialErrors:
            errors = stack.ErrorValues
            self.ErrorsQueue.extend(errors)

    def GetLastError(self) -> ErrorValue | None:
        """
        Retrieve the last error from the queue and remove it from the list.
        :return: The last ErrorValue[] or None if the queue is empty.
        """
        if not self.ErrorsQueue:
            return None
        
        # Get the last error in the queue
        return_val = self.ErrorsQueue[-1]
        
        # Remove the last error after returning it
        self.ErrorsQueue.pop()
        
        return return_val
