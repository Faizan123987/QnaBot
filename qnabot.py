from botbuilder.core import TurnContext,ActivityHandler,MessageFactory
from botbuilder.ai.qna import QnAMaker,QnAMakerEndpoint


class QnaBot(ActivityHandler):
    def __init__(self):
       qna_endpoint = QnAMakerEndpoint("28959c6f-f79e-4805-8ee6-21a73a948eaa","33063322-32b0-422c-ad2d-8f846f9831db","https://pocbot.azurewebsites.net/qnamaker")
       self.qna_maker = QnAMaker(qna_endpoint)

    async def on_message_activity(self,turn_context:TurnContext):
      response = await self.qna_maker.get_answers(turn_context)
      if response and len(response) > 0:
         await turn_context.send_activity(MessageFactory.text(response[0].answer))