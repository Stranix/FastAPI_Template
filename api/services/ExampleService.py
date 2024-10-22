from fastapi import Depends

from sqlalchemy.orm import Session

from config.base import db_helper


class ExampleService:

    def __init__(self, session: Session = Depends(db_helper.session_getter)):
        self.session = session
