class AnonymousSurvey():
    """收集匿名调查的答案"""

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        """Show question"""
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答案"""
        print("Survey results:")
        for response in self.responses:
            print("- " + response)