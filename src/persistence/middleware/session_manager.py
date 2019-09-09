from config import DB_AUTOCOMMIT
import sqlalchemy.orm.scoping as scoping
from sqlalchemy.exc import SQLAlchemyError
from persistence.exceptions import DataBaseException


class SQLAlchemySessionManager:
    def __init__(self, session):
        self._session_factory = session
        self._scoped = isinstance(session, scoping.ScopedSession)

    def process_request(self, req, res, resource=None):
        """
        Handle post-processing of the response (after routing).
        """
        req.context['session'] = self._session_factory

    def process_response(self, req, res, resource=None):
        """
        Handle post-processing of the response (after routing).
        """
        session = req.context['session']

        if DB_AUTOCOMMIT:
            try:
                session.commit()
            except SQLAlchemyError as ex:
                session.rollback()
                raise DataBaseException(
                    title='Database Rollback Error',
                    description=''.join(str(ex.__cause__).replace('\n', ' '))
                )

        if self._scoped:
            # remove any database-loaded state from all current objects
            # so that the next access of any attribute, or any query execution will retrieve new state
            session.remove()
        else:
            session.close()