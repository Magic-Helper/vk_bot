from loguru import logger
from vkbottle import BaseMiddleware
from vkbottle.bot import Message


class CutReportMessageMiddleware(BaseMiddleware[Message]):
    REPORT_SIGN = 'жалоба от игрока'

    async def pre(self) -> None:
        if self.REPORT_SIGN in self.event.text.lower():
            splitted = self.event.text.split('\n')
            self.event.text = '\n'.join(splitted[:3])
            print(self.event.text)


class ClearSpaceBeforeLineMiddleware(BaseMiddleware[Message]):
    async def pre(self) -> None:
        self.event.text = self.event.text.replace(' \n', '\n')


class PostLogMiddleware(BaseMiddleware[Message]):
    async def post(self) -> None:
        if not self.handlers:
            return

        msg = ''
        for handler in self.handlers:
            msg += f'Отработал {handler}. \n. Эвент: {self.event.dict(exclude_none=True)}'
        logger.info(msg)
